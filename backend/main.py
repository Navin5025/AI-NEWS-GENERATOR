from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

app = FastAPI(
    title="News Article Generator API",
    description="API for generating news articles from headlines using Gemini",
    version="1.0.0"
)

class HeadlineRequest(BaseModel):
    headline: str
    tone: Optional[str] = "neutral"
    length: Optional[int] = 500

class ArticleResponse(BaseModel):
    headline: str
    article: str
    generated_at: str
    word_count: int

def create_prompt(headline: str, length: int) -> str:
    current_date = datetime.now().strftime("%B %d, %Y")
    return f"""Generate a breaking news report for today ({current_date}) about {headline}.
    The news report should be approximately {length} words long.
    
    Follow these news reporting guidelines:
    - Start with a strong news lead (who, what, when, where, why)
    - Include recent developments and breaking updates
    - Add quotes from relevant authorities or experts
    - Mention specific details, statistics, or data
    - Include reactions from affected parties
    - End with potential impacts or next steps
    
    Format the news as:
    - Location and Date
    - Breaking News Headline
    - Main News Content with Quotes
    - Additional Context and Background
    - Latest Updates
    - Future Implications
    
    Make it feel like a real news report from a professional news agency.
    """

@app.post("/generate-article", response_model=ArticleResponse)
async def generate_article(request: HeadlineRequest):
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = create_prompt(request.headline, request.length)
        
        # Calculate max tokens based on desired word count
        max_tokens = request.length * 5  # Approximate token-to-word ratio
        
        response = model.generate_content(
            prompt,
            generation_config={
                'temperature': 0.7,
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': max_tokens
            }
        )

        article = response.text.strip()
        
        # Adjust article length to match requested word count
        words = article.split()
        if len(words) > request.length:
            words = words[:request.length]
            article = ' '.join(words)
        
        return ArticleResponse(
            headline=request.headline,
            article=article,
            generated_at=datetime.now().isoformat(),
            word_count=len(article.split())
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating article: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model": "gemini-pro"
    }
