import streamlit as st
import openai
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(
    page_title="J-Marketer OS | The Virtual Japan Team",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #FAFAFA; }
    h1, h2, h3 { color: #2C3E50; }
    .tool-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #D32F2F;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .highlight { color: #D32F2F; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAV ---
with st.sidebar:
    st.title("🇯🇵 J-Marketer OS")
    st.caption("Your In-House Japan Assistant")
    
    api_key = st.text_input("🔑 API Key", type="password")
    
    st.markdown("---")
    st.markdown("### 🧰 Toolkit")
    selected_tool = st.radio("Select Tool", 
        ["1. Brand Strategy (Base)", 
         "2. Campaign Planner (Seasonal)", 
         "3. Japan Calendar Alert"])
    
    st.markdown("---")
    st.info("Current Season in Japan: **Winter (Shogatsu Prep)**")

if not api_key:
    st.warning("Please enter API Key to start.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

# ==========================================
# TOOL 1: BRAND STRATEGY (The Foundation)
# ==========================================
if selected_tool == "1. Brand Strategy (Base)":
    st.header("1. Define Your Japan Brand Persona")
    st.markdown("This is your foundational strategy. Use this when you first enter the market.")
    
    # (Keep the inputs simple for this demo)
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Industry", ["Fashion", "Beauty", "SaaS", "Food", "Travel"])
    with col2:
        price = st.selectbox("Price", ["Budget", "Standard", "Premium", "Luxury"])
        
    if st.button("Generate Core Persona"):
        # (This is where the Persona Logic from the previous code goes)
        st.success("Persona Profile Saved! (Mockup)")
        st.markdown(f"<div class='tool-card'><b>Target Persona:</b> Yuko, the detailed-oriented office worker.<br><b>Core Value:</b> Reliability > Trend.</div>", unsafe_allow_html=True)


# ==========================================
# TOOL 2: CAMPAIGN PLANNER (The Recurring Feature)
# ==========================================
elif selected_tool == "2. Campaign Planner (Seasonal)":
    st.header("2. Seasonal Campaign Planner")
    st.markdown("Plan your next specific launch. The AI will adjust for **Japanese Weather, Holidays, and Buying Moods**.")
    
    # --- CAMPAIGN INPUTS ---
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            campaign_name = st.text_input("Campaign Item / Name", value="Summer Linen Collection")
            campaign_month = st.selectbox("Launch Month", 
                ["January (New Year)", "February (Valentine)", "March (New Life)", "April (Sakura)", 
                 "May (Golden Week)", "June (Rainy Season/Bonus)", "July (Summer Start)", "August (Obon/Heat)",
                 "September (Silver Week)", "October (Halloween)", "November (Winter Prep)", "December (Gift)"])
        with c2:
            budget = st.text_input("Campaign Budget (JPY)", value="¥1,000,000")
            goal = st.selectbox("Campaign Goal", ["Brand Awareness (Lookbook)", "Sales / Conversion", "Lead Generation"])

    st.markdown("---")
    
    if st.button("🚀 Draft Media Plan"):
        with st.spinner(f"Analyzing Japanese market conditions for {campaign_month}..."):
            
            # --- THE CAMPAIGN LOGIC ---
            system_prompt = """
            You are a Japanese Marketing Director. 
            Create a specific Campaign Media Plan.
            
            CRITICAL CONTEXT:
            - Adjust for specific Japanese Seasons (e.g., June is 'Rainy Season' so focus on 'Comfort/Indoor', July is 'Bonus Season' so people spend more).
            - Adjust for Japanese Holidays (Golden Week, Obon).
            
            Output Format:
            1. 🌦️ MARKET MOOD: What are Japanese people thinking/feeling in this specific month?
            2. 🗝️ KEYWORDS & COPY: 3 Japanese phrases that fit this specific item and season.
            3. 📅 TIMELINE ADVICE: When to start ads, when to stop (e.g., stop during Obon delivery pause).
            4. 💰 MEDIA MIX: Specific to this campaign goal.
            """
            
            user_prompt = f"Product: {campaign_name}. Month: {campaign_month}. Goal: {goal}. Budget: {budget}."
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}]
            )
            
            # --- OUTPUT ---
            st.markdown(f"<div class='tool-card'>{response.choices[0].message.content}</div>", unsafe_allow_html=True)


# ==========================================
# TOOL 3: JAPAN CALENDAR ALERT (The "News" Feature)
# ==========================================
elif selected_tool == "3. Japan Calendar Alert":
    st.header("3. Upcoming Japan Marketing Alerts")
    st.markdown("Don't miss key sales opportunities.")
    
    # In a real app, this data would come from your weekly updates
    st.info("💡 **Pro Tip:** In Japan, employees receive huge cash bonuses (Bonus) in **June** and **December**. This is the highest spending time for luxury and durables.")
    
    st.markdown("""
    ### 📅 Next 3 Months Outlook
    
    | Month | Event | Marketing Action |
    | :--- | :--- | :--- |
    | **March** | **New Life Season (Shin-Seikatsu)** | Moving, new jobs, school starts. Sell furniture, suits, stationery. |
    | **April** | **Sakura / Golden Week Prep** | Travel booking peaks. Outdoor goods. |
    | **May** | **Golden Week (GW)** | National Holiday week. Ad costs spike. Delivery delays. |
    """)
    
    st.button("📩 Subscribe to Weekly Intelligence ($49/mo)")