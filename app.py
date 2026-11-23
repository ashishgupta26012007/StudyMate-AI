
import os
import json
import urllib.request
import urllib.error
import streamlit as st

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="centered"
)

st.title("📚 StudyMate AI")
st.caption("Your AI-powered academic study planner")

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(prompt):
    if not API_KEY:
        raise ValueError("Gemini API key is missing.")

    url = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-3.5-flash-lite:generateContent?key="
    + API_KEY
)

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["candidates"][0]["content"]["parts"][0]["text"]


if not API_KEY:
    st.warning("Please configure your Gemini API key.")

st.header("Create Your Study Plan")

with st.form("study_form"):
    subjects = st.text_input(
        "Subjects",
        "Data Structures, DBMS, Operating Systems"
    )

    exam_date = st.date_input("Exam Date")

    hours = st.slider(
        "Daily Study Hours",
        1, 12, 3
    )

    level = st.selectbox(
        "Preparation Level",
        ["beginner", "intermediate", "advanced"]
    )

    weak_topics = st.text_input(
        "Weak Topics",
        "Trees, Normalization, CPU Scheduling"
    )

    submitted = st.form_submit_button("Generate My Study Plan")

if submitted:
    prompt = f"""
You are StudyMate AI, an academic planning assistant.

Create a realistic 7-day study plan.

Student Details:
Subjects: {subjects}
Exam Date: {exam_date}
Daily Study Hours: {hours}
Preparation Level: {level}
Weak Topics: {weak_topics}

Requirements:
1. Create a weekly timetable.
2. Prioritize weak topics.
3. Include practice and revision.
4. Keep the schedule realistic.
5. Explain the revision strategy.
6. Do not guarantee examination results.

Use clear headings and a Markdown table.
"""

    try:
        with st.spinner("AI is creating your study plan..."):
            answer = ask_gemini(prompt)

        st.success("Study plan generated!")
        st.markdown(answer)

    except Exception as e:
        st.error(f"Error: {e}")


st.divider()

st.header("Ask Your Academic Doubts")

question = st.text_area(
    "Enter your academic question"
)

if st.button("Explain This Topic"):
    if question.strip():
        try:
            with st.spinner("AI is preparing your explanation..."):
                answer = ask_gemini(
                    "Explain this academic question step by step "
                    "in beginner-friendly language with an example: "
                    + question
                )

            st.markdown(answer)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
