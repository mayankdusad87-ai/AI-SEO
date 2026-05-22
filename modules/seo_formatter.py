import streamlit as st

# =========================================
# DISPLAY RESULTS
# =========================================

def display_results(data):

    seo_keywords = data.get("seo_keywords", [])
    long_tail_keywords = data.get("long_tail_keywords", [])
    hashtags = data.get("hashtags", [])

    st.success("SEO Generated Successfully!")

    tab1, tab2, tab3 = st.tabs(
        [
            "SEO Keywords",
            "Long Tail Keywords",
            "Hashtags"
        ]
    )

    # =========================================
    # SEO KEYWORDS
    # =========================================

    with tab1:

        st.subheader("SEO Keywords")

        for keyword in seo_keywords:
            st.markdown(f"- {keyword}")

    # =========================================
    # LONG TAIL KEYWORDS
    # =========================================

    with tab2:

        st.subheader("Long Tail Keywords")

        for keyword in long_tail_keywords:
            st.markdown(f"- {keyword}")

    # =========================================
    # HASHTAGS
    # =========================================

    with tab3:

        st.subheader("Instagram Hashtags")

        hashtag_text = " ".join(hashtags)

        st.code(hashtag_text)
