import streamlit as st
import pandas as pd
import datetime

# Premium Look and Setup
st.set_page_config(page_title="Dream11 AI Pro Engine", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    h1 { color: #d71920; font-family: 'Arial Black', sans-serif; text-align: center; margin-bottom: 0px; }
    .match-card { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 15px; border-left: 5px solid #d71920; }
    .green-dot { color: #1d8815; font-weight: bold; }
    .red-dot { color: #d71920; font-weight: bold; }
    .stButton>button { background-color: #1d8815; color: white; border-radius: 8px; font-weight: bold; height: 45px; }
    .stButton>button:hover { background-color: #15660f; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🏏 Cricbuzz Style Dream11 AI Prediction Engine")
st.write("<p style='text-align: center; font-size: 15px; color: #555;'>Real-time Live Scores, Countdown Timer, Automated Lineups with Green/Red Dots</p>", unsafe_allow_html=True)
st.markdown("---")

# ----------------- LIVE CENTRAL ENGINE DATABASE -----------------
# Auto generating dynamic date times based on current date (June 2026)
today = datetime.date(2026, 6, 11)
tomorrow = today + datetime.timedelta(days=1)

mock_database = [
    {
        "id": "match_1",
        "type": "LIVE",
        "name": "West Indies vs Sri Lanka - 1st T20I",
        "venue": "Kensington Oval, Bridgetown, Barbados",
        "date_time": f"{today.strftime('%d %B %Y')} - 08:30 PM IST",
        "status": "West Indies won the toss and elected to bat pehle",
        "countdown": "🔴 MATCH LIVE IN PROGRESS",
        "lineup_out": True,
        "team1": "West Indies", "team2": "Sri Lanka",
        "squad1": [
            {"name": "Nicholas Pooran (WK)", "playing": True, "role": "WK", "form": 9.5, "vs_spin": 9.2},
            {"name": "Shai Hope", "playing": True, "role": "BAT", "form": 8.4, "vs_spin": 8.0},
            {"name": "Rovman Powell (C)", "playing": True, "role": "BAT", "form": 8.1, "vs_spin": 7.2},
            {"name": "Andre Russell", "playing": True, "role": "ALL", "form": 9.3, "vs_spin": 8.5},
            {"name": "Sherfane Rutherford", "playing": True, "role": "BAT", "form": 7.9, "vs_spin": 7.5},
            {"name": "Romario Shepherd", "playing": True, "role": "ALL", "form": 8.2, "vs_spin": 7.0},
            {"name": "Gudakesh Motie", "playing": True, "role": "BOWL", "form": 8.8, "vs_spin": 9.5},
            {"name": "Akeal Hosein", "playing": True, "role": "BOWL", "form": 8.6, "vs_spin": 9.0},
            {"name": "Alzarri Joseph", "playing": True, "role": "BOWL", "form": 8.3, "vs_spin": 5.0},
            {"name": "Shamar Joseph", "playing": True, "role": "BOWL", "form": 8.0, "vs_spin": 4.5},
            {"name": "Roston Chase", "playing": True, "role": "ALL", "form": 8.1, "vs_spin": 8.5},
            {"name": "Brandon King", "playing": False, "role": "BAT", "form": 7.5, "vs_spin": 7.8} # Bench
        ],
        "squad2": [
            {"name": "Kusal Mendis (WK)", "playing": True, "role": "WK", "form": 8.5, "vs_spin": 8.2},
            {"name": "Pathum Nissanka", "playing": True, "role": "BAT", "form": 8.9, "vs_spin": 8.5},
            {"name": "Charith Asalanka (C)", "playing": True, "role": "BAT", "form": 8.6, "vs_spin": 8.8},
            {"name": "Sadeera Samarawickrama", "playing": True, "role": "BAT", "form": 7.8, "vs_spin": 8.0},
            {"name": "Wanindu Hasaranga", "playing": True, "role": "ALL", "form": 9.4, "vs_spin": 9.8},
            {"name": "Kamindu Mendis", "playing": True, "role": "ALL", "form": 8.7, "vs_spin": 9.0},
            {"name": "Maheesh Theekshana", "playing": True, "role": "BOWL", "form": 8.8, "vs_spin": 9.4},
            {"name": "Matheesha Pathirana", "playing": True, "role": "BOWL", "form": 9.1, "vs_spin": 5.0},
            {"name": "Asitha Fernando", "playing": True, "role": "BOWL", "form": 8.0, "vs_spin": 4.0},
            {"name": "Dilshan Madushanka", "playing": True, "role": "BOWL", "form": 8.2, "vs_spin": 4.5},
            {"name": "Dunith Wellalage", "playing": True, "role": "ALL", "form": 8.3, "vs_spin": 8.9},
            {"name": "Bhanuka Rajapaksa", "playing": False, "role": "BAT", "form": 7.2, "vs_spin": 7.0} # Bench
        ]
    },
    {
        "id": "match_2",
        "type": "UPCOMING",
        "name": "Bangladesh vs Australia - 2nd ODI",
        "venue": "Shere Bangla National Stadium, Mirpur, Dhaka",
        "date_time": f"{tomorrow.strftime('%d %B %Y')} - 10:30 AM IST",
        "status": "Toss aur Lineups match shuru hone se 30 min pehle aayenge.",
        "countdown": "⏳ Starts in 14 Hours 08 Mins",
        "lineup_out": False,
        "team1": "Bangladesh", "team2": "Australia",
        "squad1": [
            {"name": "Litton Das (WK)", "playing": True, "role": "WK", "form": 7.8, "vs_spin": 7.5},
            {"name": "Tanzid Hasan", "playing": True, "role": "BAT", "form": 7.5, "vs_spin": 7.2},
            {"name": "Najmul Hossain Shanto (C)", "playing": True, "role": "BAT", "form": 8.2, "vs_spin": 8.5},
            {"name": "Shakib Al Hasan", "playing": True, "role": "ALL", "form": 9.4, "vs_spin": 9.2},
            {"name": "Towhid Hridoy", "playing": True, "role": "BAT", "form": 8.0, "vs_spin": 7.9},
            {"name": "Mahmudullah", "playing": True, "role": "BAT", "form": 7.9, "vs_spin": 8.0},
            {"name": "Mehidy Hasan Miraz", "playing": True, "role": "ALL", "form": 8.8, "vs_spin": 9.0},
            {"name": "Taskin Ahmed", "playing": True, "role": "BOWL", "form": 8.3, "vs_spin": 4.5},
            {"name": "Mustafizur Rahman", "playing": True, "role": "BOWL", "form": 8.5, "vs_spin": 5.0},
            {"name": "Shoriful Islam", "playing": True, "role": "BOWL", "form": 8.0, "vs_spin": 4.0},
            {"name": "Taijul Islam", "playing": True, "role": "BOWL", "form": 8.2, "vs_spin": 8.8}
        ],
        "squad2": [
            {"name": "Travis Head", "playing": True, "role": "BAT", "form": 9.6, "vs_spin": 8.0},
            {"name": "Jake Fraser-McGurk", "playing": True, "role": "BAT", "form": 8.4, "vs_spin": 7.2},
            {"name": "Mitchell Marsh (C)", "playing": True, "role": "ALL", "form": 9.0, "vs_spin": 7.8},
            {"name": "Glenn Maxwell", "playing": True, "role": "ALL", "form": 9.3, "vs_spin": 9.5},
            {"name": "Marcus Stoinis", "playing": True, "role": "ALL", "form": 8.5, "vs_spin": 7.5},
            {"name": "Tim David", "playing": True, "role": "BAT", "form": 8.0, "vs_spin": 7.6},
            {"name": "Alex Carey (WK)", "playing": True, "role": "WK", "form": 8.1, "vs_spin": 8.0},
            {"name": "Pat Cummins", "playing": True, "role": "BOWL", "form": 9.1, "vs_spin": 5.0},
            {"name": "Mitchell Starc", "playing": True, "role": "BOWL", "form": 9.4, "vs_spin": 4.0},
            {"name": "Adam Zampa", "playing": True, "role": "BOWL", "form": 9.5, "vs_spin": 9.8},
            {"name": "Josh Hazlewood", "playing": True, "role": "BOWL", "form": 8.9, "vs_spin": 4.8}
        ]
    }
]

# ----------------- TABS SYSTEM LIKE CRICBUZZ -----------------
tab_live, tab_upcoming = st.tabs(["🔴 LIVE MATCHES", "📅 UPCOMING MATCHES"])

def render_match_dashboard(m_data):
    st.markdown(f"""
    <div class='match-card'>
        <h3>{m_data['name']}</h3>
        <p><strong>🏟️ Venue:</strong> {m_data['venue']}</p>
        <p><strong>📅 Date & Time:</strong> {m_data['date_time']}</p>
        <p style='color: #d71920; font-weight: bold;'>⏰ {m_data['countdown']}</p>
        <p style='background-color: #e3f2fd; padding: 8px; border-radius: 5px;'>📢 <b>Toss Status:</b> {m_data['status']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pitch Control Selector
    pitch_type = st.selectbox(
        f"🧠 Select Real-Time Pitch For {m_data['name']}:",
        ["Flat & Batting Paradise (High Scoring)", "Slow & Spinning (Spinners Friendly)", "Green & Fast Bouncy (Seamers Friendly)", "Balanced Surface"],
        key=f"pitch_{m_data['id']}"
    )
    
    st.markdown("---")
    
    col_squad, col_analysis = st.columns([1, 1.2])
    
    with col_squad:
        st.subheader("👥 Playing Squads / Lineup Status")
        if m_data['lineup_out']:
            st.success("✅ Lineup Officially Out! Dots represent playing status.")
        else:
            st.warning("📋 Pre-Toss Mode (Predicted Squad). All shown with 🟢 as temporary.")
            
        # Displaying Players with Dots
        st.markdown(f"#### **🟢 {m_data['team1']} Lineup**")
        p1_list = []
        for p in m_data['squad1']:
            dot = "<span class='green-dot'>🟢 Playing</span>" if p['playing'] else "<span class='red-dot'>🔴 Benched</span>"
            st.markdown(f"- {p['name']} ({p['role']}) — {dot}", unsafe_allow_html=True)
            if p['playing'] or not m_data['lineup_out']:
                p1_list.append(p)
                
        st.markdown(f"#### **🟢 {m_data['team2']} Lineup**")
        p2_list = []
        for p in m_data['squad2']:
            dot = "<span class='green-dot'>🟢 Playing</span>" if p['playing'] else "<span class='red-dot'>🔴 Benched</span>"
            st.markdown(f"- {p['name']} ({p['role']}) — {dot}", unsafe_allow_html=True)
            if p['playing'] or not m_data['lineup_out']:
                p2_list.append(p)

    with col_analysis:
        st.subheader("📊 Tactical Match Fitment Grid")
        
        all_active_players = []
        
        # Expert Calculation Logic based on parameter selectors
        def calculate_fitment(p_obj, t_name):
            score = p_obj['form']
            fitment_text = "⭐ Highly Consistent"
            
            if "Spinning" in pitch_type:
                if p_obj['role'] == "ALL" or p_obj['vs_spin'] >= 9.0:
                    score += 1.3
                    fitment_text = "🔥 Spin Master (Key in Middle Overs)"
                elif p_obj['role'] == "BOWL" and p_obj['vs_spin'] < 6.0:
                    score -= 0.7
                    fitment_text = "⚠️ Medium Assistance for pacers"
            elif "Green" in pitch_type:
                if p_obj['role'] == "BOWL" and p_obj['vs_spin'] < 6.0:
                    score += 1.5
                    fitment_text = "⚡ Lethal (Early Swing Specialist)"
                elif p_obj['role'] == "BAT" and p_obj['form'] < 8.5:
                    score -= 1.0
                    fitment_text = "❌ Threat (Vulnerable against moving ball)"
            elif "Flat" in pitch_type:
                if p_obj['role'] == "BAT" or p_obj['role'] == "WK":
                    score += 1.1
                    fitment_text = "🚀 Run Machine (Boundaries King Today)"
                    
            return {
                "Player Name": p_obj['name'],
                "Team": t_name,
                "Form": f"⭐ {p_obj['form']}/10",
                "Tactical Fitting Time": fitment_text,
                "Expected DT %": f"{min(int(score * 10), 99)}%",
                "_score": score
            }

        for p in p1_list: all_active_players.append(calculate_fitment(p, m_data['team1']))
        for p in p2_list: all_active_players.append(calculate_fitment(p, m_data['team2']))
        
        df = pd.DataFrame(all_active_players)
        df_sorted = df.sort_values(by="_score", ascending=False)
        
        st.dataframe(df_sorted[["Player Name", "Team", "Form", "Tactical Fitting Time", "Expected DT %"]], use_container_width=True, height=280)
        
        st.markdown("---")
        st.subheader("🏆 AI Dream Winning Team Generation")
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("#### 🥇 Safe Team (H2H / Small Leagues)")
            safe = df_sorted.head(11)
            st.table(safe[["Player Name", "Expected DT %"]])
            if len(safe) >= 2:
                st.caption(f"🔴 **Captain (C):** {safe.iloc[0]['Player Name']} | 🔵 **Vice-Captain (VC):** {safe.iloc[1]['Player Name']}")
        with col_t2:
            st.markdown("#### 💣 Grand League Team (Mega Contest)")
            if len(df_sorted) >= 12:
                gl = pd.concat([df_sorted.head(6), df_sorted.iloc[8:11], df_sorted.tail(2)])
            else:
                gl = df_sorted
            st.table(gl[["Player Name", "Expected DT %"]])
            if len(gl) >= 5:
                st.caption(f"🔴 **Captain (C):** {gl.iloc[2]['Player Name']} | 🔵 **Vice-Captain (VC):** {gl_lineup = gl.iloc[4]['Player Name']}")

# Executing layout blocks inside respective tabs
with tab_live:
    render_match_dashboard(mock_database[0])

with tab_upcoming:
    render_match_dashboard(mock_database[1])
