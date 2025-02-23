import random
import json
import streamlit as st

# File to store questions
QUESTIONS_FILE = "questions.json"

# Load questions from JSON file
def load_questions():
    try:
        with open(QUESTIONS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
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

# Save questions to JSON file
def save_questions(questions):
    with open(QUESTIONS_FILE, "w") as file:
        json.dump(questions, file, indent=4)

# Load the questions
questions = load_questions()

# Streamlit Web UI
st.title("🎲 Scrum Icebreaker Question Generator")
st.write("Select a category or get a random question!")

# Dropdown to choose category
category = st.selectbox("Choose a category:", ["Random"] + list(questions.keys()))

# Button to generate a question
if st.button("Generate Question"):
    if category == "Random":
        all_questions = sum(questions.values(), [])
        question = random.choice(all_questions)
    else:
        question = random.choice(questions[category])

    st.success(f"**📝 Scrum Icebreaker Question:** {question}")

# Section to allow users to add new questions
st.subheader("➕ Add Your Own Icebreaker Question")

# Input fields for new question
new_question = st.text_area("Enter your icebreaker question:")
selected_category = st.selectbox("Choose a category for your question:", list(questions.keys()))

if st.button("Submit Question"):
    if new_question.strip():
        questions[selected_category].append(new_question.strip())
        save_questions(questions)
        st.success(f"✅ Your question has been added to the **{selected_category}** category!")
    else:
        st.warning("⚠️ Please enter a question before submitting.")

