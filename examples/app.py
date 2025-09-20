import streamlit as st
import random

# --- Civic test questions. Expand this list for more!
QUESTIONS = [
    {
        "question": "What is the supreme law of the land?",
        "choices": [
            "The Constitution",
            "The Declaration of Independence",
            "The Emancipation Proclamation",
            "The Bill of Rights"
        ],
        "answer": "The Constitution"
    },
    {
        "question": "How many amendments does the Constitution have?",
        "choices": [
            "27",
            "10",
            "23",
            "21"
        ],
        "answer": "27"
    },
    {
        "question": "What are the two parts of the U.S. Congress?",
        "choices": [
            "The Senate and House of Representatives",
            "The Supreme Court and the President",
            "The FBI and CIA",
            "The Treasury and State Department"
        ],
        "answer": "The Senate and House of Representatives"
    },
    {
        "question": "Who signs bills to become laws?",
        "choices": [
            "The President",
            "The Chief Justice",
            "The Speaker of the House",
            "The Vice President"
        ],
        "answer": "The President"
    },
    {
        "question": "What do we call the first ten amendments to the Constitution?",
        "choices": [
            "The Bill of Rights",
            "The Articles of Confederation",
            "The Preamble",
            "The Federalist Papers"
        ],
        "answer": "The Bill of Rights"
    }
    # Add more questions as desired
]

NUM_QUESTIONS = 5  # Number of questions per quiz; adjust as needed

def get_random_questions(num):
    return random.sample(QUESTIONS, min(num, len(QUESTIONS)))

def main():
    st.title("N400 Civic Test Practice Quiz")
    st.write("Answer the following randomly-selected civic questions. Good luck!")

    # Session state setup
    if "quiz" not in st.session_state:
        st.session_state.quiz = get_random_questions(NUM_QUESTIONS)
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.selected = [None] * NUM_QUESTIONS
        st.session_state.show_result = False

    # Main quiz loop
    if st.session_state.q_index < len(st.session_state.quiz) and not st.session_state.show_result:
        idx = st.session_state.q_index
        q = st.session_state.quiz[idx]
        st.subheader(f"Question {idx + 1} of {len(st.session_state.quiz)}")
        st.write(q["question"])
        choices = q["choices"].copy()
        random.shuffle(choices)
        option = st.radio(
            "Select your answer:",
            choices,
            key=f"q{idx}"
        )
        if st.button("Submit", key=f"submit{idx}"):
            st.session_state.selected[idx] = option
            if option == q["answer"]:
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(f"Incorrect. The correct answer is: {q['answer']}")
            st.session_state.q_index += 1

    # Show results
    if (st.session_state.q_index >= len(st.session_state.quiz)) or st.session_state.show_result:
        st.write("## Quiz Complete!")
        st.write(f"Your final score is {st.session_state.score} out of {len(st.session_state.quiz)}.")
        if st.button("Restart Quiz"):
            for k in ["quiz", "q_index", "score", "selected", "show_result"]:
                del st.session_state[k]
            st.experimental_rerun()
        else:
            for i, q in enumerate(st.session_state.quiz):
                st.write(f"**Q{i+1}:** {q['question']}")
                st.write(f"Your answer: {st.session_state.selected[i]}")
                st.write(f"Correct answer: {q['answer']}")
                st.write("---")

if __name__ == "__main__":
    main()
