import base64
import streamlit as st
import pandas as pd
import random
import json
import os
from PIL import Image
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Team Generator",
    page_icon="🎲",
    layout="wide"
)

# Enhanced Custom CSS
st.markdown("""
<style>
.team-card {
    padding: 20px;
    border-radius: 10px;
    background-color: #f0f2f6;
    margin: 10px 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: transform 0.2s;
    display: flex;
    align-items: center;
    gap: 10px;
}
.team-card:hover {
    transform: translateY(-2px);
}
.student-name {
    color: #FF9933;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
}
.student-info {
    color: #666;
    font-size: 14px;
}
.team-header {
    background-color: #1E88E5;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    margin-bottom: 15px;
}
.statistics-card {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #dee2e6;
}
.big-button {
    padding: 20px;
    font-size: 24px;
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
}
.team-summary {
    padding: 15px;
    background-color: #fff;
    border-radius: 8px;
    margin: 10px 0;
    border-left: 5px solid #FF9933;
}

/* New styles */
.profile-image {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    float: right;
    margin-left: 15px;
    border: 3px solid #FF9933;
    flex-shrink: 0;
}

.student-details {
    flex-grow: 1;
    padding-left: 10px;
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
st.title("🎲 Random Team Generator")
st.subheader("BCA First Semester - Roadmap 2.0")

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