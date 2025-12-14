import streamlit as st
import time

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="J-Marketer OS | Japan Marketing Assistant",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS STYLING (The "Look") ---
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp { background-color: #FAFAFA; }
    h1, h2, h3 { color: #2C3E50; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Card/Box Styling */
    .tool-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #D32F2F; /* Japan Red */
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    
    /* Input Fields */
    .stSelectbox, .stTextInput { margin-bottom: 15px; }
    
    /* Buttons */
    .stButton>button {
        background-color: #2C3E50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover { background-color: #D32F2F; color: white; }
    
    /* Metrics/KPI Boxes */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #EEEEEE;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🇯🇵 J-Marketer OS")
    st.caption("v2.0 | Enterprise Edition")
    
    # --- DESIGN MODE TOGGLE ---
    st.markdown("---")
    st.markdown("### 🛠️ Developer Settings")
    design_mode = st.toggle("Design Mode (Preview UI)", value=True)
    
    if design_mode:
        st.info("✅ **Design Mode ON**\n\nNo API Key needed.\nAI responses are simulated.")
        api_key = "dummy_key"
    else:
        api_key = st.text_input("🔑 OpenAI API Key", type="password")
        if not api_key:
            st.warning("Enter API Key to run real AI.")
    
    st.markdown("---")
    
    # Navigation
    st.markdown("### 🧰 Tools")
    selected_tool = st.radio("Select Module", 
        ["1. Brand Strategy DNA", 
         "2. Seasonal Campaign Planner", 
         "3. Japan Market Calendar"])

# --- 4. MAIN LOGIC ---

# Check if we should stop (Only if NOT in design mode and NO key)
if not design_mode and not api_key:
    st.title("🇯🇵 J-Marketer OS")
    st.warning("Please enter your API Key in the sidebar or switch to 'Design Mode' to preview.")
    st.stop()

# ==========================================
# TOOL 1: BRAND STRATEGY DNA
# ==========================================
if selected_tool == "1. Brand Strategy DNA":
    st.header("1. Brand Strategy DNA")
    st.markdown("Define the core persona and positioning for the Japanese market.")
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            category = st.selectbox("Industry Category", ["Fashion & Apparel", "Beauty & Cosmetics", "SaaS B2B", "Travel/Inbound"])
        with col2:
            price = st.selectbox("Price Positioning", ["Budget (Petit-Price)", "Standard", "Premium (Gohoubi)", "Luxury"])
        with col3:
            vibe = st.selectbox("Visual Aesthetic", ["Kawaii (Cute)", "Minimalist (Natural)", "Mode (Edgy)", "Traditional"])

    st.markdown("### 📝 Brand Context")
    usage = st.text_area("What is the main usage context?", placeholder="e.g. A busy working mom using it for quick skincare in the morning.")

    if st.button("🧬 Generate Persona Profile"):
        with st.spinner("Analyzing Market Data..."):
            time.sleep(1.5) # Fake loading time for UI feel
            
            # MOCK OUTPUT (for Design Mode)
            output_html = """
            <div class='tool-card'>
                <h3>👺 Target Persona: "Yuko, The Efficiency-Seeking Mom"</h3>
                <p><b>Demographics:</b> 34 years old, lives in Tokyo suburbs, works full-time.</p>
                <p><b>Values:</b> She prioritizes <b>"Taipa" (Time Performance)</b> over luxury. She wants products that work in 60 seconds.</p>
                <hr>
                <h4>🎯 Localization Hook</h4>
                <p>Do not sell "Beauty". Sell <b>"Time"</b>. Use the phrase <b>「忙しい朝の救世主」 (Savior of busy mornings)</b>.</p>
            </div>
            """
            st.markdown(output_html, unsafe_allow_html=True)

# ==========================================
# TOOL 2: SEASONAL CAMPAIGN PLANNER
# ==========================================
elif selected_tool == "2. Seasonal Campaign Planner":
    st.header("2. Seasonal Campaign Planner")
    st.markdown("Plan marketing campaigns aligned with Japanese weather, holidays, and buying moods.")
    
    # KPIs Row
    k1, k2, k3 = st.columns(3)
    k1.metric("Current Season", "Winter", "Cold/Dry")
    k2.metric("Next Big Event", "New Year", "Jan 1")
    k3.metric("Ad Cost Trend", "High", "+20%")
    
    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        campaign_name = st.text_input("Campaign Name", value="Sakura Spring Collection")
        month = st.selectbox("Launch Month", ["March (New Life)", "April (Sakura)", "June (Rainy Season)", "December (Bonus)"])
    with c2:
        budget = st.selectbox("Budget Range", ["< ¥500k (Test)", "¥1M - ¥3M (Growth)", "¥5M+ (Scale)"])
        goal = st.multiselect("Campaign Goals", ["Brand Awareness", "Direct Sales", "Lead Gen", "Store Visits"], default=["Direct Sales"])

    if st.button("🚀 Draft Media Plan"):
        with st.spinner("Consulting J-Marketer Intelligence..."):
            time.sleep(2) # Fake loading
            
            # MOCK OUTPUT
            output_html = f"""
            <div class='tool-card'>
                <h3>📅 Campaign Strategy for: {month}</h3>
                <p><b>Market Mood:</b> {month} is a time of "New Beginnings" (Shin-Seikatsu). Consumers are looking to refresh their wardrobe/items.</p>
                <br>
                <h4>📢 Recommended Media Mix</h4>
                <ul>
                    <li><b>Instagram Reels (50%):</b> Focus on "Outfit Styling" videos.</li>
                    <li><b>SmartNews Ads (30%):</b> Target the "Spring Trends" channel.</li>
                    <li><b>Retargeting (20%):</b> Criteo or Google Display.</li>
                </ul>
                <div style='background-color:#FFF3CD; padding:10px; border-radius:5px; margin-top:10px;'>
                    <b>⚠️ Japan Trap Warning:</b> Do not start ads *during* Golden Week (May 1-5). Start 2 weeks before. Shipping is delayed during holidays.
                </div>
            </div>
            """
            st.markdown(output_html, unsafe_allow_html=True)

# ==========================================
# TOOL 3: JAPAN MARKET CALENDAR
# ==========================================
elif selected_tool == "3. Japan Market Calendar":
    st.header("3. Japan Market Calendar")
    
    tab1, tab2 = st.tabs(["Upcoming Events", "My Alerts"])
    
    with tab1:
        st.markdown("""
        <div class='tool-card'>
            <h4>🗓️ Q1 2025 Outlook</h4>
            <table style="width:100%">
              <tr>
                <th>Month</th>
                <th>Event</th>
                <th>Marketing Action</th>
              </tr>
              <tr>
                <td><b>January</b></td>
                <td>Oshogatsu (New Year)</td>
                <td>"Hatsu-uri" (First Sale). Focus on Lucky Bags (Fukubukuro).</td>
              </tr>
              <tr>
                <td><b>February</b></td>
                <td>Valentine's Day</td>
                <td>Women buy chocolate for Men (and themselves). Gift campaigns.</td>
              </tr>
               <tr>
                <td><b>March</b></td>
                <td>Shin-Seikatsu (New Life)</td>
                <td>Moving season. High demand for furniture, suits, appliances.</td>
              </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.info("You have no unread alerts.")
        st.button("Refresh Alerts")

# Footer
st.markdown("---")
st.caption("Powered by J-Marketer OS")
