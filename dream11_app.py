import streamlit as st
import pandas as pd

# Mobile aur Laptop dono ke liye screen ko adjust karna
st.set_page_config(page_title="Dream11 AI Team Generator", layout="centered")

st.title("🎯 Real-Time Dream11 Team Generator (2026)")
st.write("Match, Pitch aur Real-time data ke hisab se apni best team chuno.")

# 1. Match Selection
match = st.selectbox("Match Chuno:", ["BAN vs AUS - 2nd ODI (Dhaka)"])

# 2. Real-Time Toss aur Pitch Condition Input
st.subheader("🏏 Live Match Situation")
toss_winner = st.radio("Toss Kisne Jeeta?", ["Bangladesh", "Australia"])
decision = st.radio("Toss Jeet Kar Kya Chunna?", ["Batting Pehle", "Bowling Pehle"])

pitch_type = st.selectbox("Pitch Ka Haal (Real-Time):", ["Slow & Spinning (Dhaka Type)", "Flat & Batting Friendly", "Green & Pace Friendly"])

# Mock Data (Real app mein yeh data API se auto-update hoga)
players_data = {
    "Player": ["Mosaddek Hossain", "Najmul Shanto", "Tanzid Hasan", "Nahid Rana", "Mustafizur Rahman", 
               "Cameron Green", "Alex Carey", "Nathan Ellis", "Matt Renshaw", "Adam Zampa"],
    "Team": ["BAN", "BAN", "BAN", "BAN", "BAN", "AUS", "AUS", "AUS", "AUS", "AUS"],
    "Role": ["ALL", "BAT", "BAT", "BOWL", "BOWL", "ALL", "WK", "BOWL", "ALL", "BOWL"],
    "Form_Rating": [9.5, 8.8, 8.0, 9.2, 8.5, 9.0, 7.8, 8.7, 7.5, 8.2]
}
df = pd.DataFrame(players_data)

# 3. Team Generation Logic (Algorithm)
if st.button("Generate Dream11 Teams 🔥"):
    st.success(f"Analyzing data for {match}... Pitch is {pitch_type}!")
    
    # Simple logic base on pitch
    if "Spinning" in pitch_type:
        st.info("💡 Tip: Is pitch par spinners aur all-rounders zyada points denge.")
        # Filter spinners/all-rounders higher
        df.loc[df['Role'] == 'ALL', 'Form_Rating'] += 1.0
    
    # Sorting players based on form and conditions
    df_sorted = df.sort_values(by="Form_Rating", ascending=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Safe Team (Small Leagues)")
        st.write("Yeh team un players ki hai jo bilkul safe points denge:")
        safe_team = df_sorted.head(7) # Top 7 players
        st.dataframe(safe_team[["Player", "Team", "Role"]])
        st.caption(f"**🔴 Captain:** {safe_team.iloc[0]['Player']} | **🔵 Vice-Captain:** {safe_team.iloc[1]['Player']}")
        
    with col2:
        st.subheader("🔥 Grand League Team (Mega Contest)")
        st.write("Yeh risky team hai, jo aapko bada jita sakti hai:")
        # Risky team filters some mid-tier players for surprise element
        risky_team = pd.concat([df_sorted.head(4), df_sorted.tail(3)])
        st.dataframe(risky_team[["Player", "Team", "Role"]])
        st.caption(f"**🔴 Captain:** {risky_team.iloc[3]['Player']} | **🔵 Vice-Captain:** {risky_team.iloc[4]['Player']}")