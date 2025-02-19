import random
import streamlit as st

# Define the icebreaker questions
questions = {
    "Sprint Overview": [
        "During the sprint, what did you find to be the most rewarding aspect?",
        "Which user story or assignment was your favorite to work on?",
        "Which sprint results are we most pleased with?",
        "Was the sprint goal achieved?",
        "Did the stakeholders get what they expected from the sprint?",
    ],
    "Team Interaction": [
        "What was our level of teamwork?",
        "Had everyone a clear idea of what they were supposed to do?",
        "Was there an open and constructive exchange of feedback?",
        "Did any disagreements arise? What happened to fix them?",
        "How can we improve our mutual support for the upcoming sprint?",
    ],
    "Efficiency & Results": [
        "How can we improve our approach to dividing up tasks?",
        "Was burnout a problem throughout this sprint? What was the cause?",
        "How can we ensure that future sprints do not end in burnout?",
        "How productive was our use of working time?",
        "Is it possible to automate any of the routine processes?",
    ],
    "Innovation & Creativity": [
        "How can we foster an atmosphere that encourages creativity?",
        "What are some ways to promote more brainstorming sessions?",
        "During the sprint, what was the most creative solution that we developed?",
        "How do we encourage creativity and new ideas?",
        "Can we say that we’re successfully juggling innovation with our primary duties?",
    ]
}

# Streamlit Web App
st.title("🎲 Scrum Icebreaker Question Generator")
st.write("Select a category or get a random question!")

# Dropdown to choose category
category = st.selectbox("Choose a category:", ["Random"] + list(questions.keys()))

# Button to generate question
if st.button("Generate Question"):
    if category == "Random":
        all_questions = sum(questions.values(), [])
        question = random.choice(all_questions)
    else:
        question = random.choice(questions[category])
    
    st.success(f"**📝 Scrum Icebreaker Question:** {question}")
