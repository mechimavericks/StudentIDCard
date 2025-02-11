import base64
import streamlit as st
import pandas as pd
import random
import json
import os
from PIL import Image
from datetime import datetime
import time


# Set page config
st.set_page_config(
    page_title="Team Generator",
    page_icon="🎲",
    layout="wide"
)

# Updated Custom CSS
st.markdown("""
<style>
/* Global Styles */
body {
    background-color: #008080;
    color: #f5f5f5;
}

.stApp {
    background: linear-gradient(135deg, #008080, #006666);
}

/* Card Styles */
.team-card {
    padding: 25px;
    border-radius: 15px;
    background: rgba(51, 51, 51, 0.9);
    margin: 15px 0;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 20px;
    animation: popUpAndStay 2s ease-out forwards;
    opacity: 0;
}

.team-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.student-name {
    color: #f5f5f5;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 8px;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.student-info {
    color: #cccccc;
    font-size: 15px;
    line-height: 1.6;
}

.team-header {
    background: linear-gradient(90deg, #008080, #006666);
    color: #f5f5f5;
    padding: 15px 25px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    text-align: center;
    font-size: 1.2em;
    font-weight: bold;
    animation: slideInFromTop 1s ease-out forwards;
}

.statistics-card {
    background: rgba(51, 51, 51, 0.9);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
    color: #f5f5f5;
}

/* Button Styles */
.stButton > button {
    background: linear-gradient(135deg, #008080, #006666);
    color: #f5f5f5;
    padding: 15px 30px;
    border-radius: 10px;
    border: none;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
    background: linear-gradient(135deg, #006666, #008080);
}

/* Team Summary Styles */
.team-summary {
    padding: 20px;
    background: rgba(51, 51, 51, 0.9);
    border-radius: 15px;
    margin: 15px 0;
    border-left: 5px solid #008080;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    backdrop-filter: blur(10px);
    color: #f5f5f5;
}

.team-summary h4 {
    color: #008080;
    margin-bottom: 15px;
    font-size: 1.2em;
}

/* Profile Image Styles */
.profile-image {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #008080;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.student-details {
    flex-grow: 1;
    padding-left: 15px;
}

/* Header Styles */
h1, h2, h3 {
    color: #f5f5f5;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Expander Styles */
.streamlit-expanderHeader {
    background: rgba(51, 51, 51, 0.9) !important;
    border-radius: 10px !important;
    color: #f5f5f5 !important;
    padding: 10px 20px !important;
}

/* Divider Style */
hr {
    border-color: rgba(245, 245, 245, 0.2);
    margin: 30px 0;
}

@keyframes popUpAndStay {
    0% {
        transform: scale(0);
        opacity: 0;
    }
    20% {
        transform: scale(1.2);
    }
    40% {
        transform: scale(1);
        opacity: 1;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}

.delay-1 { animation-delay: 0s; }
.delay-2 { animation-delay: 2s; }
.delay-3 { animation-delay: 4s; }
.delay-4 { animation-delay: 6s; }
.delay-5 { animation-delay: 8s; }

@keyframes slideInFromTop {
    0% {
        transform: translateY(-50px);
        opacity: 0;
    }
    100% {
        transform: translateY(0);
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('studentdata.csv')
    return df[['fullname', 'rollno', 'email']]

# Initialize session state
if 'teams' not in st.session_state:
    st.session_state.teams = []
if 'remaining_students' not in st.session_state:
    st.session_state.remaining_students = load_data().to_dict('records')
if 'team_counter' not in st.session_state:
    st.session_state.team_counter = 1

def generate_team():
    if len(st.session_state.remaining_students) >= 5:
        team = random.sample(st.session_state.remaining_students, 5)
        for student in team:
            st.session_state.remaining_students.remove(student)
        # Insert new team at the beginning of the list
        st.session_state.teams.insert(0, {
            'team_number': st.session_state.team_counter,
            'members': team,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.session_state.team_counter += 1
        return True
    return False

# Add this function near the top of your file
def get_image_path(rollno):
    image_path = f"images/{rollno}.jpg"
    default_image_path = "images/default.png"
    
    if os.path.exists(image_path):
        return image_path
    return default_image_path

# Main app
st.markdown("""
<div style='text-align: center; padding: 40px 0;'>
    <h1 style='color: #f5f5f5; font-size: 3em; margin-bottom: 10px; text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);'>
        🎲 Random Team Generator
    </h1>
    <h3 style='color: #cccccc; font-weight: normal; margin-bottom: 30px;'>
        BCA First Semester - Roadmap 2.0
    </h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

# Modified team display section
with col1:
    if st.button("Generate New Team", key="generate", use_container_width=True):
        if generate_team():
            st.success(f"Team {st.session_state.team_counter-1} generated successfully!")
        else:
            st.error("Not enough students remaining to form a complete team!")

    # Display teams with enhanced styling
    for team in st.session_state.teams:
        with st.expander(f"Team {team['team_number']} | Generated at {team['timestamp']}", expanded=True):
            st.markdown(f"""<div class="team-header">Team {team['team_number']}</div>""", unsafe_allow_html=True)
            for member in team['members']:
                image_path = get_image_path(member['rollno'])
                try:
                    image = Image.open(image_path)
                    st.markdown(f"""
                    <div class="team-card">
                        <div style="width: 80px; height: 80px; overflow: hidden; border-radius: 50%; border: 3px solid #FF9933;">
                            <img src="data:image/jpg;base64,{base64.b64encode(open(image_path, 'rb').read()).decode()}" 
                                 class="profile-image" alt="Profile photo">
                        </div>
                        <div class="student-details">
                            <div class="student-name">📌 {member['fullname']}</div>
                            <div class="student-info">
                                🎯 Roll No: {member['rollno']}<br>
                                📧 {member['email']}
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error loading image for roll no {member['rollno']}: {str(e)}")

# Modified statistics section
with col2:
    st.markdown("""<div class="statistics-card">""", unsafe_allow_html=True)
    st.subheader("📊 Statistics")
    st.write(f"📑 Total Teams: {len(st.session_state.teams)}")
    st.write(f"👥 Remaining Students: {len(st.session_state.remaining_students)}")
    st.markdown("""</div>""", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("💾 Save Teams", key="save"):
        with open('teams.json', 'w') as f:
            json.dump(st.session_state.teams, f, indent=4)
        st.success("Teams saved successfully!")
    
    if st.button("🔄 Reset All", key="reset"):
        st.session_state.teams = []
        st.session_state.remaining_students = load_data().to_dict('records')
        st.session_state.team_counter = 1
        st.experimental_rerun()

# Team Summary Section
st.markdown("---")
st.subheader("🎯 Team Summary")
col3, col4 = st.columns([1, 1])

with col3:
    for i in range(1, 7):
        team_members = [team for team in st.session_state.teams if team['team_number'] == i]
        if team_members:
            st.markdown(f"""
            <div class="team-summary">
                <h4>Team {i}</h4>
                {"<br>".join([f"• {member['fullname']} (Roll: {member['rollno']})" for member in team_members[0]['members']])}
            </div>
            """, unsafe_allow_html=True)

with col4:
    for i in range(7, 14):
        team_members = [team for team in st.session_state.teams if team['team_number'] == i]
        if team_members:
            st.markdown(f"""
            <div class="team-summary">
                <h4>Team {i}</h4>
                {"<br>".join([f"• {member['fullname']} (Roll: {member['rollno']})" for member in team_members[0]['members']])}
            </div>
            """, unsafe_allow_html=True)

# Display remaining students with enhanced styling
if st.session_state.remaining_students:
    st.markdown("---")
    with st.expander("📋 Remaining Students"):
        for student in st.session_state.remaining_students:
            st.markdown(f"""
            <div class="team-card">
                <div class="student-name">{student['fullname']}</div>
                <div class="student-info">Roll No: {student['rollno']}</div>
            </div>
            """, unsafe_allow_html=True)