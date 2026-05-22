def build_prompt(project_data):

    prompt = f"""
    You are an expert real estate SEO strategist.

    Generate:
    1. 20 SEO keywords
    2. 15 Long-tail keywords
    3. 30 Instagram hashtags

    Project Details:
    -------------------------
    Project Name: {project_data['project_name']}
    City: {project_data['city']}
    Micro Market: {project_data['micro_market']}
    Project Type: {project_data['project_type']}
    Configuration: {project_data['configuration']}
    Nearby Landmarks: {project_data['landmarks']}
    Brand Positioning: {project_data['brand_positioning']}
    USP: {project_data['usp']}

    Focus on:
    - High search intent
    - Local SEO
    - Real estate buyers
    - Social media discoverability
    - Luxury branding language

    Return ONLY valid JSON.

    JSON Format:
    {{
        "seo_keywords": [],
        "long_tail_keywords": [],
        "hashtags": []
    }}
    """

    return prompt
