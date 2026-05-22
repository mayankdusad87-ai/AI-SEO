import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# =========================================
# LOAD ENV VARIABLES
# =========================================

load_dotenv()

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Real Estate SEO Generator",
    page_icon="🏢",
    layout="wide"
)

# =========================================
# API CLIENT
# =========================================

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1",
)

# =========================================
# TITLE
# =========================================

st.title("🏢 AI Real Estate SEO Generator")
st.markdown("Generate SEO keywords & hashtags for real estate projects using AI.")

# =========================================
# SIDEBAR INPUTS
# =========================================

st.sidebar.header("Project Details")

project_name = st.sidebar.text_input("Project Name")

city = st.sidebar.selectbox(
    "City",
    [
        "Jaipur",
        "Mumbai",
        "Pune",
        "Bangalore",
        "Delhi",
        "Hyderabad",
        "Ahmedabad"
    ]
)

micro_market = st.sidebar.text_input("Micro Market")

project_type = st.sidebar.selectbox(
    "Project Type",
    [
        "Residential",
        "Commercial",
        "Mixed Use"
    ]
)

configuration = st.sidebar.multiselect(
    "Configuration",
    [
        "1BHK",
        "2BHK",
        "3BHK",
        "4BHK",
        "Villa",
        "Office Space",
        "Retail Shop"
    ]
)

landmarks = st.sidebar.text_area("Nearby Landmarks")

brand_positioning = st.sidebar.selectbox(
    "Brand Positioning",
    [
        "Luxury",
        "Affordable Luxury",
        "Smart Living",
        "Family-Centric",
        "Investment Focused"
    ]
)

usp = st.sidebar.text_area("USP (Unique Selling Proposition)")

# =========================================
# GENERATE BUTTON
# =========================================

generate = st.button("🚀 Generate SEO & Hashtags")

# =========================================
# AI GENERATION
# =========================================

if generate:

    # Validation
    if not project_name:
        st.warning("Please enter Project Name")
        st.stop()

    with st.spinner("Generating SEO keywords and hashtags..."):

        prompt = f"""
        You are an expert real estate SEO strategist.

        Generate the following for the project below:

        1. 20 SEO Keywords
        2. 15 Long Tail Keywords
        3. 30 Instagram Hashtags

        Project Details:
        -----------------
        Project Name: {project_name}
        City: {city}
        Micro Market: {micro_market}
        Project Type: {project_type}
        Configuration: {configuration}
        Nearby Landmarks: {landmarks}
        Brand Positioning: {brand_positioning}
        USP: {usp}

        Focus on:
        - High search intent
        - Local SEO
        - Real estate buyers
        - Premium branding
        - Social media discoverability

        Return ONLY valid JSON.

        Format:
        {{
            "seo_keywords": [],
            "long_tail_keywords": [],
            "hashtags": []
        }}
        """

        try:

            response = client.chat.completions.create(
                model="grok-beta",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a real estate SEO expert."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
            )

            result = response.choices[0].message.content

            # Parse JSON
            data = json.loads(result)

            seo_keywords = data.get("seo_keywords", [])
            long_tail_keywords = data.get("long_tail_keywords", [])
            hashtags = data.get("hashtags", [])

            # =========================================
            # DISPLAY OUTPUT
            # =========================================

            st.success("SEO Generated Successfully!")

            tab1, tab2, tab3 = st.tabs(
                [
                    "SEO Keywords",
                    "Long Tail Keywords",
                    "Hashtags"
                ]
            )

            # =========================================
            # SEO KEYWORDS TAB
            # =========================================

            with tab1:

                st.subheader("SEO Keywords")

                for keyword in seo_keywords:
                    st.markdown(f"- {keyword}")

            # =========================================
            # LONG TAIL KEYWORDS TAB
            # =========================================

            with tab2:

                st.subheader("Long Tail Keywords")

                for keyword in long_tail_keywords:
                    st.markdown(f"- {keyword}")

            # =========================================
            # HASHTAGS TAB
            # =========================================

            with tab3:

                st.subheader("Instagram Hashtags")

                hashtag_text = " ".join(hashtags)

                st.code(hashtag_text)

        except json.JSONDecodeError:
            st.error("AI returned invalid JSON. Try again.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
