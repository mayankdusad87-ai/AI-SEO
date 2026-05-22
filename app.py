import streamlit as st
from modules.ai_engine import generate_seo_data
from modules.seo_formatter import display_results

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Real Estate SEO Generator",
    page_icon="🏢",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton button {
    width: 100%;
    background-color: black;
    color: white;
    border-radius: 10px;
    height: 3rem;
    font-size: 18px;
    font-weight: 600;
}

.stButton button:hover {
    background-color: #333333;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITLE
# =========================================

st.title("🏢 AI Real Estate SEO Generator")
st.markdown(
    "Generate SEO keywords, long-tail keywords, and hashtags using AI."
)

# =========================================
# SIDEBAR
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

usp = st.sidebar.text_area("USP")

# =========================================
# GENERATE BUTTON
# =========================================

if st.button("🚀 Generate SEO & Hashtags"):

    if not project_name:
        st.warning("Please enter project name")
        st.stop()

    project_data = {
        "project_name": project_name,
        "city": city,
        "micro_market": micro_market,
        "project_type": project_type,
        "configuration": configuration,
        "landmarks": landmarks,
        "brand_positioning": brand_positioning,
        "usp": usp
    }

    with st.spinner("Generating SEO data..."):

        try:
            result = generate_seo_data(project_data)
            display_results(result)

        except Exception as e:
            st.error(f"Error: {str(e)}")
