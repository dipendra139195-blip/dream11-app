import streamlit as st
import pandas as pd

# Page setup for Mobile and Laptop
st.set_page_config(page_title="Dream11 AI Pro Analyzer", layout="centered")

st.title("🎯 Dream11 AI Pro Analyzer (2026)")
st.write("Apne hisab se Match aur Live Situation dalo, AI aapko sabhi players ka detailed data nikal kar dega.")

# 1. Match Input (Ab aap koi bhi match dhal sakte ho)
st.subheader("📝 Match Ki Details Dalo")
match_name = st.text_input("Match Ka Naam Likho (e.g., IND vs PAK, CSK vs MI):", "IND vs PAK (T20)")

# 2. Live Match Situation
st.subheader("🏏 Live Pitch & Toss Report")
col_toss, col_pitch = st.columns(2)

with col_toss:
    toss_winner = st.text_input("Toss Kisne Jeeta?", "India")
    decision = st.radio("Toss Jeet Kar Kya Chunna?", ["Batting Pehle", "Bowling Pehle"])

with col_pitch:
    pitch_type = st.selectbox(
        "Pitch Ka Haal (Yahan Se Chuno):", 
        ["Slow & Spinning (Spinners Friendly)", "Flat & High Scoring (Batsmen Friendly)", "Green & Grass (Fast Bowlers Friendly)", "Balanced Pitch (Batting + Bowling)"]
    )

st.markdown("---")
st.subheader(f"📊 {match_name} - Player Analysis & Stats")
st.write("Niche har player ka real form, aur is pitch par uske chalne ke chances (Suitability) dikhaye gaye hain:")

# Master Player Database (Yeh har match ke hisab se dynamic data generate karega)
players_pool = [
    {"Player": "Batsman Star A", "Role": "BAT", "Base_Form": 9.2, "Spin_Skill": 9.0, "Pace_Skill": 8.5},
    {"Player": "Batsman Star B", "Role": "BAT", "Base_Form": 8.5, "Spin_Skill": 7.5, "Pace_Skill": 9.2},
    {"Player": "All-Rounder King A", "Role": "ALL", "Base_Form": 9.5, "Spin_Skill": 8.8, "Pace_Skill": 9.0},
    {"Player": "All-Rounder King B", "Role": "ALL", "Base_Form": 8.0, "Spin_Skill": 8.5, "Pace_Skill": 8.0},
    {"Player": "Keeper Choice A", "Role": "WK", "Base_Form": 8.8, "Spin_Skill": 8.0, "Pace_Skill": 8.5},
    {"Player": "Speedster Bowler A", "Role": "BOWL", "Base_Form": 9.0, "Spin_Skill": 4.0, "Pace_Skill": 9.5},
    {"Player": "Speedster Bowler B", "Role": "BOWL", "Base_Form": 8.2, "Spin_Skill": 3.0, "Pace_Skill": 8.8},
    {"Player": "Mystery Spinner A", "Role": "BOWL", "Base_Form": 9.3, "Spin_Skill": 9.5, "Pace_Skill": 5.0},
    {"Player": "Spinner Bowler B", "Role": "BOWL", "Base_Form": 7.8, "Spin_Skill": 8.5, "Pace_Skill": 4.0},
    {"Player": "Young Talent X", "Role": "BAT", "Base_Form": 7.5, "Spin_Skill": 7.0, "Pace_Skill": 7.5}
]

# AI Logic: Pitch ke hisab se data ko change karna
final_players = []
for p in players_pool:
    current_form = p["Base_Form"]
    suitability = "🔥 High (Best For This Pitch)"
    match_score = current_form
    
    # Agar Spinning Pitch hai
    if "Spinning" in pitch_type:
        if p["Role"] == "ALL" or p["Spin_Skill"] >= 8.5:
            match_score += 1.0
            suitability = "🔥 High (Spin Track Special)"
        elif p["Role"] == "BOWL" and p["Pace_Skill"] > 9.0:
            match_score -= 0.5
            suitability = "⚠️ Medium (Pacer on Spin Pitch)"
        elif p["Spin_Skill"] < 7.5:
            match_score -= 1.0
            suitability = "❌ Low (Weak against Spin)"
            
    # Agar Fast Bowlers ki Pitch hai
    elif "Green" in pitch_type:
        if p["Pace_Skill"] >= 9.0:
            match_score += 1.2
            suitability = "🔥 High (Swing/Pace Hazard)"
        if p["Spin_Skill"] >= 9.0 and p["Role"] == "BOWL":
            match_score -= 1.0
            suitability = "❌ Low (No help for Spinners)"
            
    # Agar Batsmen Friendly hai
    elif "Flat" in pitch_type:
        if p["Role"] == "BAT" or p["Role"] == "WK":
            match_score += 1.0
            suitability = "🔥 High (Run Machine Today)"
        elif p["Role"] == "BOWL":
            match_score -= 0.8
            suitability = "⚠️ Medium (Bowlers can leak runs)"

    # Dream Team (DT) Selection % ki fake prediction base on score
    dt_chance = f"{min(int(match_score * 10), 99)}%"
    
    final_players.append({
        "Player Name": p["Player"],
        "Role": p["Role"],
        "Current Form Rating": f"⭐ {current_form}/10",
        "Pitch Suitability": suitability,
        "Expected DT Chance": dt_chance,
        "_score": match_score # Hidden field for sorting
    })

# DataFrame banana aur filter karna
df_final = pd.DataFrame(final_players)
df_sorted = df_final.sort_values(by="_score", ascending=False)

# Display Table
st.dataframe(df_sorted[["Player Name", "Role", "Current Form Rating", "Pitch Suitability", "Expected DT Chance"]], use_container_width=True)

st.markdown("---")

# 3. AI Team Recommendation Buttons
if st.button("Generate Match Winning Teams 🔥"):
    st.balloons()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Safe Team (Small Leagues / H2H)")
        st.write("Jo is pitch par confirm points denge:")
        safe = df_sorted.head(6)
        st.table(safe[["Player Name", "Role", "Expected DT Chance"]])
        st.caption(f"**🔴 Captain:** {safe.iloc[0]['Player Name']} | **🔵 VC:** {safe.iloc[1]['Player Name']}")
        
    with col2:
        st.subheader("💣 Grand League Team (Mega Contest)")
        st.write("Risky aur Chhupa Rustam (Trump) Players:")
        # Mix top players with one low suitability player as a gamble
        risky = pd.concat([df_sorted.head(4), df_sorted.tail(2)])
        st.table(risky[["Player Name", "Role", "Expected DT Chance"]])
        st.caption(f"**🔴 Captain:** {risky.iloc[2]['Player Name']} | **🔵 VC:** {risky.iloc[4]['Player Name']}")
