import streamlit as st
import pandas as pd
import random
import base64
import os
import time

# Set Streamlit page config
st.set_page_config(page_title="Team Generator", page_icon="🎲", layout="wide")

# Load student data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('studentdata.csv')
        return df[['fullname', 'rollno', 'email']]
    except FileNotFoundError:
        st.error("studentdata.csv not found!")
        return pd.DataFrame(columns=['fullname', 'rollno', 'email'])

# Get student profile image
def get_image_base64(rollno):
    """
    Tries to load a student's profile image and convert it to base64.
    Falls back to default.png if the student's image is missing.
    """
    try:
        image_path = f"images/{rollno}.jpg"
        default_image_path = "images/default.png"
        
        if not os.path.exists(image_path):
            if not os.path.exists(default_image_path):
                return ""  # Return empty if no image found
            image_path = default_image_path
            
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        st.warning(f"Error loading image for roll no {rollno}: {str(e)}")
        return ""

# Initialize session state
if 'remaining_students' not in st.session_state:
    st.session_state.remaining_students = load_data().to_dict('records')
if 'teams' not in st.session_state:
    st.session_state.teams = []
if 'team_counter' not in st.session_state:
    st.session_state.team_counter = 1
if 'animation_complete' not in st.session_state:
    st.session_state.animation_complete = False

# CSS for wheel styling
st.markdown("""
<style>
.wheel-container {
    position: relative;
    width: 600px;
    height: 600px;
    margin: 0 auto;
    border-radius: 50%;
    background: rgba(0, 128, 128, 0.1);
    border: 3px solid #008080;
    overflow: hidden;
}

.wheel {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    transform: rotate(0deg);
    transition: transform 5s cubic-bezier(0.17, 0.67, 0.12, 0.99);
}

.wheel-item {
    position: absolute;
    width: 120px;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transform-origin: 50% 300px;
    background: transparent;
    padding: 5px;
}

.profile-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    border: 3px solid #008080;
    object-fit: cover;
    background-color: #f0f0f0;
}

.student-info {
    text-align: center;
    margin-top: 5px;
}

.student-name {
    font-size: 14px;
    font-weight: bold;
    color: #008080;
}

.student-roll {
    font-size: 12px;
    color: #666;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(1800deg); }
}

.spinning {
    animation: spin 5s cubic-bezier(0.17, 0.67, 0.12, 0.99);
}
</style>
""", unsafe_allow_html=True)

# Function to create the student wheel
def create_wheel_html(students, spinning=False):
    """
    Generates the HTML for the spinning wheel with student images and details.
    """
    n = len(students)  # Number of students in the current team
    angle_step = 360 / max(n, 1)  # Avoid division by zero
    wheel_items = ""
    
    for i, student in enumerate(students):
        angle = i * angle_step  # Angle for positioning
        img_b64 = get_image_base64(student['rollno'])
        img_src = f"data:image/jpg;base64,{img_b64}" if img_b64 else "images/default.png"
        
        wheel_items += f'''
        <div class="wheel-item" style="transform: rotate({angle}deg) translate(250px) rotate(-{angle}deg);">
            <img src="{img_src}" 
                 class="profile-image" 
                 onerror="this.src='images/default.png'"
                 alt="{student['fullname']}">
            <div class="student-info">
                <div class="student-name">{student['fullname']}</div>
                <div class="student-roll">Roll: {student['rollno']}</div>
            </div>
        </div>
        '''
    
    spin_class = "spinning" if spinning else ""
    return f'''
    <div class="wheel-container">
        <div class="wheel {spin_class}">{wheel_items}</div>
    </div>
    '''

# Function to generate teams
def generate_team():
    """
    Selects a random set of students to form a team and removes them from the remaining list.
    """
    team_size = 5
    total_students = len(st.session_state.remaining_students)
    
    if total_students < team_size:
        return []
        
    # Handle last team if students aren't perfectly divisible
    if total_students >= team_size:
        selected_students = random.sample(st.session_state.remaining_students, team_size)
        for student in selected_students:
            st.session_state.remaining_students.remove(student)
        
        st.session_state.teams.insert(0, {
            'team_number': st.session_state.team_counter,
            'members': selected_students
        })
        st.session_state.team_counter += 1
        return selected_students
    return []

# UI Layout
st.title("🎲 Random Team Generator")
col1, col2 = st.columns([2, 1])

with col1:
    total_remaining = len(st.session_state.remaining_students)
    teams_possible = total_remaining // 5
    
    if st.button(f"Spin the Wheel & Generate Team ({teams_possible} teams possible)", 
                 use_container_width=True, 
                 disabled=teams_possible == 0):
        selected_students = generate_team()
        if selected_students:
            st.markdown(create_wheel_html(selected_students, spinning=True), unsafe_allow_html=True)
            time.sleep(5)  # Increased spin time to 5 seconds
            st.success(f"Team {st.session_state.team_counter-1} generated successfully!")
        else:
            st.error("Not enough students remaining to form a complete team!")

with col2:
    st.info(f"""
    📊 Statistics:
    - Total Teams Formed: {len(st.session_state.teams)}
    - Students Remaining: {total_remaining}
    - Teams Possible: {teams_possible}
    """)

# Display Teams
for team in st.session_state.teams:
    with st.expander(f"Team {team['team_number']}"):
        for member in team['members']:
            st.write(f"📌 {member['fullname']} - Roll No: {member['rollno']}")

# Remaining students
if st.session_state.remaining_students:
    with st.expander("📋 Remaining Students"):
        for student in st.session_state.remaining_students:
            st.write(f"{student['fullname']} (Roll: {student['rollno']})")
