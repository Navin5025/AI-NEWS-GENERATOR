import streamlit as st
import requests
from datetime import datetime

st.set_page_config(
    page_title="Cyfuture Assignment News Generator",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
   
    .stApp {
        background: linear-gradient(135deg, #1a1c1e 0%, #232529 100%);
    }
    
    [data-testid="stSidebar"] {
        display: none;
    }
    
    .header {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem auto;
        text-align: center;
        color: white;
        max-width: 1000px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    .input-section {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem auto;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .customize-options {
        display: flex;
        gap: 2rem;
        margin: 2rem 0;
        align-items: center;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-size: 1rem !important;
        color: white !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
    }
    
    .stButton {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        padding: 0.75rem 3rem !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        min-width: 200px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 16px rgba(16, 185, 129, 0.2);
    }
    
    .stDownloadButton > button {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        padding: 0.75rem 2rem !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        margin: 1rem auto !important;
        display: block !important;
    }
    
    .stDownloadButton > button:hover {
        background: rgba(255, 255, 255, 0.15) !important;
        transform: translateY(-2px);
    }
    
    .article-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem auto;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    .article-container h2 {
        color: white;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .article-container p {
        line-height: 1.7;
        color: rgba(255, 255, 255, 0.9);
    }
    
    h1, h2, h3 {
        color: white !important;
        font-weight: 600 !important;
    }
    
    .white-text {
        color: white !important;
    }
    
    /* Dropdown styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 0.75rem !important;
        color: white !important;
    }

    .stSelectbox > div > div:hover {
        border-color: #10b981 !important;
    }
    
    /* Label text color */
    .stSelectbox label, .stTextInput label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
    }
    
    /* Fix text colors */
    div[data-testid="stMarkdownContainer"] {
        color: white !important;
    }
    
    /* Spinner color */
    .stSpinner > div {
        border-top-color: #10b981 !important;
    }
    
    /* Error and warning messages */
    .stAlert {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    </style>
""", unsafe_allow_html=True)

def main():
    with st.container():
        st.markdown("""
            <div class="header">
                <h1 style="font-size: 3rem; margin-bottom: 1rem; color: #10b981; text-shadow: 0 0 20px rgba(16, 185, 129, 0.3);">Cyfuture Assignment News Generator</h1>
                <p style="margin: 0; font-size: 1.2rem; color: rgba(255, 255, 255, 0.9);">Made with ❤️ by Navin</p>
            </div>
        """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        
        headline = st.text_input(
            "",
            placeholder="✨ Enter a news topic (e.g., 'Technology', 'Sports', 'Business')",
            key="headline_input"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            tone = st.selectbox(
                "News Category 📰",
                options=["Breaking News", "Feature Story", "Investigative Report"],
                index=0
            )
        
        with col2:
            length = st.selectbox(
                "News Length 📝",
                options=[300, 500, 800],
                help="Short (300), Medium (500), or Long (800) words",
                index=1
            )
        
        if st.button("Generate Breaking News ⚡", key="generate_btn"):
            if headline:
                with st.spinner("Breaking News Alert! Generating latest updates... 🔄"):
                    try:
                        BACKEND_URL = "https://al-news-article-writer.onrender.com/generate-article"
                        
                        response = requests.post(
                            BACKEND_URL,
                            json={
                                "headline": headline,
                                "tone": tone.lower(),
                                "length": length
                            }
                        )
                        
                        if response.status_code == 200:
                            article_data = response.json()
                            current_date = datetime.now().strftime("%B %d, %Y")
                            
                            st.markdown(
                                f"""
                                <div class="article-container">
                                    <div style="border-bottom: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 1rem; padding-bottom: 0.5rem;">
                                        <p style="color: #10b981; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.5rem;">BREAKING NEWS</p>
                                        <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">{current_date}</p>
                                    </div>
                                    <h2 style="color: #ffffff; font-size: 1.8rem; margin-bottom: 1.5rem;">{article_data['headline']}</h2>
                                    <div style="color: rgba(255, 255, 255, 0.9); line-height: 1.8;">{article_data['article']}</div>
                                    <div style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid rgba(255, 255, 255, 0.1);">
                                        <p style="color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">
                                            <span style="color: #10b981;">📊 Word count:</span> {article_data['word_count']} words | 
                                            <span style="color: #10b981;">🕒 Published:</span> {current_date}
                                        </p>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                            
                            st.download_button(
                                "📥 Download Article",
                                article_data['article'],
                                file_name=f"article_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                                mime="text/plain"
                            )
                        else:
                            st.error("Unable to generate article. Please try again.")
                    except Exception as e:
                        st.error("Something went wrong. Please try again later.")
            else:
                st.warning("Please enter a headline to generate an article!")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
