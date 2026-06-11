import streamlit as st
import pandas as pd

# Premium layout and design setup
st.set_page_config(page_title="Dream11 AI Live Engine Pro", layout="wide")

# Custom CSS for Cricbuzz style Premium Look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stAlert { border-radius: 8px; }
    h1 { color: #d71920; font-family: 'Arial Black', sans-serif; text-align: center; }
    h3 { color: #111111; font-weight: bold; }
    .stButton>button { background-color: #1d8815; color: white; width: 100%; border-radius: 8px; font-weight: bold; height: 45px; font-size: 16px; }
    .stButton>button:hover { background-color: #15660f; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🏏 Dream11 AI Live-to-Live Prediction Engine")
st.write("<p style='text-align: center; font-size: 16px;'>🔥 Ground Condition, Pitch Report aur Actual Match Lineup Intelligence Tool</p>", unsafe_allow_html=True)

st.markdown("---")

# Left Column for Inputs, Right Column for Live Analysis & Team Generation
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.subheader("📝 1. Match & Toss Details")
    match_name = st.text_input("Match Ka Naam Likho (e.g., WI vs SL, BAN vs AUS):", "WI vs SL (1st T20I)")
    
    toss_winner = st.text_input("Toss Kisne Jeeta?", "West Indies")
    decision = st.radio("Toss Jeet Kar Kya Chunna?", ["Batting Pehle", "Bowling Pehle"])
    
    st.subheader("🏟️ 2. Ground & Pitch Intelligence")
    pitch_condition = st.selectbox(
        "Real-Time Pitch Behavior Select Karo:",
        ["Flat & Batting Paradise (High Scoring)", "Slow & Spinning (Spinners Friendly)", "Green & Fast Bouncy (Fast Bowlers Friendly)", "Balanced Surface"]
    )
    
    # Auto logic builder base on pitch
    if "Spinning" in pitch_condition:
        st.warning("🎯 **AI Ground Note:** Pitch par cracks hain, ball ghumegi. 2nd innings mein spin track aur daldal ban jayega!")
    elif "Flat" in pitch_condition:
        st.success("🔥 **AI Ground Note:** Sapaat aur tez outfield wali pitch hai. Chowke-chakka ki baarish hogi, batsmen ko poori madad hai.")
    elif "Green" in pitch_condition:
        st.error("💨 **AI Ground Note:** Tez dhoop aur ghas ke karan shuruati overs mein ball swing hogi. Fast bowlers powerplay mein kahr machayenge.")
    else:
        st.info("⚖️ **AI Ground Note:** Yeh pitch batsman aur bowler dono ko barabar madad karegi. Core all-rounders sabse badi key honge.")

    st.subheader("👥 3. Actual Playing 11 (Toss Ke Baad)")
    st.write("Dream11 ya Cricbuzz se aane waale asli players ke naam comma (,) laga kar yahan dalo:")
    
    # Pre-filled actual stars based on match text
    default_t1 = "Shai Hope, Nicholas Pooran, Rovman Powell, Sherfane Rutherford, Andre Russell, Romario Shepherd, Roston Chase, Gudakesh Motie, Alzarri Joseph, Shamar Joseph, Akeal Hosein"
    default_t2 = "Pathum Nissanka, Kusal Mendis, Charith Asalanka, Sadeera Samarawickrama, Bhanuka Rajapaksa, Wanindu Hasaranga, Kamindu Mendis, Maheesh Theekshana, Matheesha Pathirana, Asitha Fernando, Dilshan Madushanka"
    
    team1_input = st.text_area("Team 1 Actual Players:", default_t1, height=100)
    team2_input = st.text_area("Team 2 Actual Players:", default_t2, height=100)

# Process Names Safely
t1_players = [p.strip() for p in team1_input.split(",") if p.strip()]
t2_players = [p.strip() for p in team2_input.split(",") if p.strip()]

with col_right:
    st.subheader("📊 Live Player Form & Tactical Fitment")
    
    processed_list = []
    
    # Smart Form and Fitment Logic
    def analyze_player_pro(name, team, pitch):
        base_f = 8.5 if any(k in name.lower() for k in ["pooran", "hasaranga", "russell", "pathirana", "hope", "nissanka", "asalanka"]) else 7.8
        fit_status = "⭐ Highly Stable"
        calculated_score = base_f
        
        if "Spinning" in pitch:
            if any(k in name.lower() for k in ["hasaranga", "theekshana", "kamindu", "motie", "hosein", "chase"]):
                calculated_score += 1.4
                fit_status = "🔥 Spin Master (Middle-overs Match Winner)"
            elif any(k in name.lower() for k in ["joseph", "pathirana", "fernando"]):
                calculated_score -= 0.6
                fit_status = "⚠️ Medium Fit (Pacer on Spin Track)"
                
        elif "Green" in pitch:
            if any(k in name.lower() for k in ["joseph", "pathirana", "fernando", "madushanka", "russell"]):
                calculated_score += 1.5
                fit_status = "⚡ Lethal (Powerplay Swing Specialist)"
            elif any(k in name.lower() for k in ["theekshana", "motie"]):
                calculated_score -= 1.0
                fit_status = "❌ Flop Threat (No assistance on Green track)"
                
        elif "Flat" in pitch:
            if any(k in name.lower() for k in ["pooran", "hope", "nissanka", "asalanka", "powell", "mendis"]):
                calculated_score += 1.2
                fit_status = "🚀 Run Machine (Dangerous on flat surface)"
                
        dt_probability = f"{min(int(calculated_score * 10), 99)}%"
        return {"Player Name": name, "Team": team, "Form Rating": f"⭐ {base_f:.1f}/10", "Tactical Timing / Fit": fit_status, "Expected DT %": dt_probability, "_score": calculated_score}

    for p in t1_players:
        processed_list.append(analyze_player_pro(p, "Team 1", pitch_condition))
    for p in t2_players:
        processed_list.append(analyze_player_pro(p, "Team 2", pitch_condition))

    if processed_list:
        df_players = pd.DataFrame(processed_list)
        df_sorted = df_players.sort_values(by="_score", ascending=False)
        
        # Displaying Clean Data Table
        st.dataframe(df_sorted[["Player Name", "Team", "Form Rating", "Tactical Timing / Fit", "Expected DT %"]], use_container_width=True, height=300)
        
        st.markdown("---")
        st.subheader("🏆 AI Dream Winning Team Combinations")
        st.success("✅ **LINEUP ALIGNED:** Teams built using official input parameters.")
        
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            st.markdown("#### 🥇 Small League / Head-to-Head")
            safe_lineup = df_sorted.head(11) if len(df_sorted) >= 11 else df_sorted
            st.table(safe_lineup[["Player Name", "Expected DT %"]])
            if len(safe_lineup) >= 2:
                st.caption(f"🔴 **C:** {safe_lineup.iloc[0]['Player Name']} | 🔵 **VC:** {safe_lineup.iloc[1]['Player Name']}")
                
        with col_t2:
            st.markdown("#### 💣 Mega Grand League (G.L.)")
            if len(df_sorted) >= 13:
                gl_lineup = pd.concat([df_sorted.head(6), df_sorted.iloc[8:11], df_sorted.tail(2)])
            else:
                gl_lineup = df_sorted
            st.table(gl_lineup[["Player Name", "Expected DT %"]])
            if len(gl_lineup) >= 5:
                st.caption(f"🔴 **C:** {gl_lineup.iloc[2]['Player Name']} | 🔵 **VC:** {gl_lineup.iloc[4]['Player Name']}")
    else:
        st.info("Kripya actual playing players ke naam enter karein.")
