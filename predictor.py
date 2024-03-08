import streamlit as st

# Sample data for demonstration (you would need a more extensive database)
college_data = {
    "IIT Bombay": {
        "Computer Science": 100,
        "Mechanical Engineering": 200,
        "Electrical Engineering": 300,
        "Civil Engineering": 250,
        "Aerospace Engineering": 350,
    },
    "IIT Delhi": {
        "Computer Science": 150,
        "Civil Engineering": 250,
        "Chemical Engineering": 350,
        "Electronics and Communication": 175,
        "Mathematics and Computing": 100,
    },
    "IIT Madras": {
        "Computer Science": 120,
        "Mechanical Engineering": 180,
        "Electrical Engineering": 280,
        "Civil Engineering": 230,
        "Aerospace Engineering": 320,
    },
    "IIT Kanpur": {
        "Computer Science": 130,
        "Mechanical Engineering": 210,
        "Electrical Engineering": 310,
        "Civil Engineering": 260,
        "Aerospace Engineering": 360,
    },
    "IIT Kharagpur": {
        "Computer Science": 110,
        "Mechanical Engineering": 220,
        "Electrical Engineering": 320,
        "Civil Engineering": 270,
        "Aerospace Engineering": 380,
    },
    "IIT Guwahati": {
        "Computer Science": 140,
        "Mechanical Engineering": 230,
        "Electrical Engineering": 330,
        "Civil Engineering": 280,
        "Aerospace Engineering": 400,
    },
    "IIT Roorkee": {
        "Computer Science": 160,
        "Mechanical Engineering": 240,
        "Electrical Engineering": 340,
        "Civil Engineering": 290,
        "Aerospace Engineering": 420,
    },
    "IIT Bhubaneswar": {
        "Computer Science": 170,
        "Mechanical Engineering": 260,
        "Electrical Engineering": 360,
        "Civil Engineering": 310,
        "Aerospace Engineering": 430,
    },
    "IIT Gandhinagar": {
        "Computer Science": 180,
        "Mechanical Engineering": 270,
        "Electrical Engineering": 370,
        "Civil Engineering": 320,
        "Aerospace Engineering": 450,
    },
    "IIT Hyderabad": {
        "Computer Science": 190,
        "Mechanical Engineering": 280,
        "Electrical Engineering": 380,
        "Civil Engineering": 330,
        "Aerospace Engineering": 470,
    },
    "IIT Jodhpur": {
        "Computer Science": 200,
        "Mechanical Engineering": 290,
        "Electrical Engineering": 390,
        "Civil Engineering": 340,
        "Aerospace Engineering": 500,
    },
    "IIT Patna": {
        "Computer Science": 210,
        "Mechanical Engineering": 300,
        "Electrical Engineering": 400,
        "Civil Engineering": 350,
        "Aerospace Engineering": 520,
    },
    "IIT Indore": {
        "Computer Science": 220,
        "Mechanical Engineering": 310,
        "Electrical Engineering": 410,
        "Civil Engineering": 360,
        "Aerospace Engineering": 550,
    },
    "IIT Mandi": {
        "Computer Science": 180,
        "Mechanical Engineering": 280,
        "Electrical Engineering": 380,
        "Civil Engineering": 330,
        "Aerospace Engineering": 470,
    },
    "IIT (BHU) Varanasi": {
        "Computer Science": 160,
        "Mechanical Engineering": 260,
        "Electrical Engineering": 360,
        "Civil Engineering": 310,
        "Aerospace Engineering": 430,
    },
    "IIT Palakkad": {
        "Computer Science": 220,
        "Mechanical Engineering": 320,
        "Electrical Engineering": 420,
        "Civil Engineering": 370,
        "Aerospace Engineering": 510,
    },
    "IIT Tirupati": {
        "Computer Science": 190,
        "Mechanical Engineering": 290,
        "Electrical Engineering": 390,
        "Civil Engineering": 340,
        "Aerospace Engineering": 480,
    },
    "IIT Dhanbad": {
        "Computer Science": 230,
        "Mechanical Engineering": 330,
        "Electrical Engineering": 430,
        "Civil Engineering": 380,
        "Aerospace Engineering": 550,
    },
    "IIT Bhilai": {
        "Computer Science": 210,
        "Mechanical Engineering": 310,
        "Electrical Engineering": 410,
        "Civil Engineering": 360,
        "Aerospace Engineering": 530,
    },
    # Add more IITs and courses here...
}
# Function to predict colleges and courses based on rank
def college_predictor(rank):
    predictions = []
    for college, courses in college_data.items():
        for course, cutoff in courses.items():
            if rank <= cutoff:
                predictions.append((college, course))
    return predictions

# Streamlit app
st.title("College Predictor")

rank = st.number_input("Enter your rank:")
if rank > 0:
    predictions = college_predictor(rank)
    if predictions:
        st.header("Predicted Colleges and Courses:")
        for college, course in predictions:
            st.write(f"College: {college}, Course: {course}")
    else:
        st.warning("No colleges found for the given rank.")
else:
    st.warning("Please enter a valid rank.")

# You would typically connect to a database or an API to get real data.
# This is just a simplified example for demonstration.