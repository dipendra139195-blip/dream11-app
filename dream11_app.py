import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Premium Layout Design Like Cricbuzz Corporate App
st.set_page_config(page_title="Dream11 Live AI Engine (Original)", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    h1 { color: #d71920; font-family: 'Arial Black', sans-serif; text-align: center; }
    .match-box { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 6px solid #d71920; margin-bottom: 20px; }
    .green-p { color: #1d8815; font-weight: bold; font-size: 14px; }
    .red-p { color: #d71920; font-weight: bold; font-size: 14px; }
    .stButton>button { background-color: #d71920; color: white; border-radius: 8px; font-weight: bold; height: 45px; width: 100%; }
    .stButton>button:hover { background-color: #b51218; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Dream11 AI Live-to-Live Production Engine")
st.write("<p style='text-align: center; font-size: 16px; color:#666;'>⚠️ WARNING: 100% Original Data Stream Enabled. No Mock Data Allowed.</p>", unsafe_allow_html=True)
st.markdown("---")

# 🔑 AAPKI RAPIDAPI CRICBUZZ KEY CONFIGURATION
# (Niche hum ise activate karne ka tarika dekhenge)
RAPIDAPI_KEY = st.text_input("🔑 Enter Your RapidAPI Cricbuzz Key To Activate Live Server:", type="password")

if not RAPIDAPI_KEY:
    st.info("💡 **Original App Chalanay Ke Liye:** Niche diye gaye tarike se apni RapidAPI Key nikalein aur upar dalkar server connect karein!")
else:
    # Live Real-Time Connection Headers
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    # 1. FETCH LIVE MATCHES LIST DIRECT FROM CRICBUZZ SERVER
    @st.cache_data(ttl=30) # Har 30 seconds mein background mein automatic live refresh hoga
    def fetch_real_cricbuzz_matches():
        try:
            url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"
            response = requests.get(url, headers=headers)
            return response.json().get("typeMatches", [])
        except Exception as e:
            return []

    match_data_raw = fetch_real_cricbuzz_matches()
    
    match_list = []
    match_map = {}
    
    for match_type in match_data_raw:
        for m in match_type.get("seriesMatches", []):
            for detail in m.get("seriesAdWrapper", {}).get("matches", []):
                m_id = detail.get("matchInfo", {}).get("matchId")
                m_title = f"{detail.get('matchInfo', {}).get('team1', {}).get('teamName')} vs {detail.get('matchInfo', {}).get('team2', {}).get('teamName')} ({detail.get('matchInfo', {}).get('matchDesc')})"
                if m_id and m_title:
                    match_list.append(m_title)
                    match_map[m_title] = detail

    if not match_list:
        st.error("❌ Key sahi nahi hai ya API limit khatam ho gayi hai. Kripya correct Cricbuzz Live Feed Key daalein.")
    else:
        # Match Selector Box
        selected_match_title = st.selectbox("🎯 Select Real Internet Live Match:", match_list)
        selected_match = match_map[selected_match_title]
        
        m_info = selected_match.get("matchInfo", {})
        m_id = m_info.get("matchId")
        m_status = selected_match.get("matchScore", {}).get("matchScoreDetails", {}).get("customStatus", "Live Coverage Active")
        
        # Display Actual Live Card
        st.markdown(f"""
        <div class='match-box'>
            <h2>{selected_match_title}</h2>
            <p><strong>🏟️ Venue / Ground:</strong> {m_info.get('venueInfo', {}).get('name')}, {m_info.get('venueInfo', {}).get('city')}</p>
            <p><strong>📢 Live Cricbuzz Status:</strong> {m_status}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 2. FETCH REAL-TIME SQUADS & LINEUPS
        @st.cache_data(ttl=20)
        def fetch_real_squads(match_id):
            try:
                url = f"https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/{match_id}/squads"
                res = requests.get(url, headers=headers)
                return res.json()
            except:
                return {}

        squad_data = fetch_real_squads(m_id)
        
        # Pitch Selector for Strategic Fitment
        pitch_type = st.selectbox("🧠 Select Pitch/Ground Behavior (For AI Calculations):", ["Flat & High Scoring", "Slow & Turning (Spin Friendly)", "Green & Grass (Pace/Swing Friendly)", "Balanced Surface"])
        
        st.markdown("---")
        col_squads, col_ai_engine = st.columns([1, 1.2])
        
        team1_players = squad_data.get("team1", {}).get("player", [])
        team2_players = squad_data.get("team2", {}).get("player", [])
        
        active_roster = []
        
        with col_squads:
            st.subheader("👥 Live Lineups (🔴 Red / 🟢 Green Indicators)")
            
            # Team 1 Display
            t1_name = squad_data.get("team1", {}).get("name", "Team 1")
            st.markdown(f"#### **{t1_name}**")
            for p in team1_players:
                is_playing = p.get("played") # Original Boolean from cricbuzz server
                dot_text = "<span class='green-p'>🟢 Playing XI</span>" if is_playing else "<span class='red-p'>🔴 Substitute / Bench</span>"
                st.markdown(f"- {p.get('name')} ({p.get('role', 'PLAYER')}) — {dot_text}", unsafe_allow_html=True)
                if is_playing:
                    active_roster.append({"name": p.get('name'), "role": p.get('role'), "team": t1_name, "is_captain": p.get('captain', False)})
                    
            # Team 2 Display
            t2_name = squad_data.get("team2", {}).get("name", "Team 2")
            st.markdown(f"#### **{t2_name}**")
            for p in team2_players:
                is_playing = p.get("played")
                dot_text = "<span class='green-p'>🟢 Playing XI</span>" if is_playing else "<span class='red-p'>🔴 Substitute / Bench</span>"
                st.markdown(f"- {p.get('name')} ({p.get('role', 'PLAYER')}) — {dot_text}", unsafe_allow_html=True)
                if is_playing:
                    active_roster.append({"name": p.get('name'), "role": p.get('role'), "team": t2_name, "is_captain": p.get('captain', False)})

        with col_ai_engine:
            st.subheader("📊 Pitch-Based Performance Evaluation")
            
            if not active_roster:
                st.info("⏳ Waiting for Toss. Shuruati Squads upar dikh rahi hain, Toss hote hi Playing XI automatic filter ho jayegi!")
            else:
                ai_calculated_list = []
                for p_obj in active_roster:
                    base_rating = 8.5 if p_obj['is_captain'] or p_obj['role'] == "AllRounder" else 8.0
                    fitment = "⭐ Form Match"
                    
                    # Live Strategic Calculation Engine
                    if "Spin" in pitch_type:
                        if p_obj['role'] in ["Bowler", "AllRounder"]:
                            base_rating += 1.3
                            fitment = "🔥 Spin Hazard (Highly Effective in middle overs)"
                    elif "Green" in pitch_type:
                        if p_obj['role'] == "Bowler":
                            base_rating += 1.4
                            fitment = "⚡ Seam/Swing Threat (Lethal in Powerplay)"
                    elif "Flat" in pitch_type:
                        if p_obj['role'] == "Batsman":
                            base_rating += 1.2
                            fitment = "🚀 Boundary Machine (Flat Surface Aggressor)"
                            
                    ai_calculated_list.append({
                        "Player": p_obj['name'],
                        "Team": p_obj['team'],
                        "Role": p_obj['role'],
                        "Dynamic Rating": f"⭐ {base_rating:.1f}/10",
                        "Tactical Fit": fitment,
                        "_score": base_rating
                    })
                
                df_engine = pd.DataFrame(ai_calculated_list)
                df_sorted = df_engine.sort_values(by="_score", ascending=False)
                
                st.dataframe(df_sorted[["Player", "Team", "Role", "Dynamic Rating", "Tactical Fit"]], use_container_width=True, height=300)
                
                st.markdown("---")
                st.subheader("🏆 Live Generated Dream Winning Teams")
                
                col_h2h, col_gl = st.columns(2)
                with col_h2h:
                    st.markdown("#### 🥇 Safe Team (Head-to-Head / Small League)")
                    st.table(df_sorted.head(11)[["Player", "Role"]])
                    st.caption(f"🔴 **C:** {df_sorted.iloc[0]['Player']} | 🔵 **VC:** {df_sorted.iloc[1]['Player']}")
                    
                with col_gl:
                    st.markdown("#### 💣 Mega Grand League Team")
                    if len(df_sorted) >= 11:
                        gl_combination = pd.concat([df_sorted.head(7), df_sorted.tail(4)])
                    else:
                        gl_combination = df_sorted
                    st.table(gl_combination[["Player", "Role"]])
                    st.caption(f"🔴 **C:** {df_sorted.iloc[2]['Player']} | 🔵 **VC:** {df_sorted.iloc[4]['Player']}")
