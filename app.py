import os
import openai
import streamlit as st
import os
import openai
import streamlit as st

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found. Add it in Streamlit Cloud Secrets.")
else:
    openai.api_key = api_key

if not api_key:
    st.error("OpenAI API key not found. Add it in Streamlit Cloud Secrets.")
else:
    openai.api_key = api_key


# --- Load environment variables ---

# --- Function to call OpenAI ---
def ask_llm(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful AI tutor that explains concepts clearly, summarizes notes concisely, and creates quizzes or flashcards for students."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        if response.choices:
            return response.choices[0].message.content.strip()
        return "Error: No response choices received."
    except Exception as e:
        return f"Error: Could not get response from LLM. {e}"

# --- Streamlit UI ---
st.title("🤖 AI-Powered Study Buddy")
st.write("Get simplified explanations, summaries, and quizzes/flashcards on any topic!")

# Step 1: User input
topic_or_notes = st.text_area("Enter a topic or paste your study notes here:", height=150)

# Step 2: Choose action
action = st.radio("What do you want to do?", ["Explain Concept", "Summarize Notes", "Generate Quiz/Flashcards"])

# Step 3: Trigger AI
if st.button("Get AI Help"):
    if not topic_or_notes.strip():
        st.warning("Please enter a topic or notes first!")
    else:
        if action == "Explain Concept":
            prompt = f"Explain the following concept in simple, beginner-friendly terms:\n\n{topic_or_notes}"
            output = ask_llm(prompt)
            st.subheader("📝 Explanation")
            st.write(output)

        elif action == "Summarize Notes":
            prompt = f"Summarize the following study notes concisely with key points:\n\n{topic_or_notes}"
            output = ask_llm(prompt)
            st.subheader("📝 Summary")
            st.write(output)

        elif action == "Generate Quiz/Flashcards":
            prompt = f"Create a short multiple-choice quiz or flashcards based on the following notes:\n\n{topic_or_notes}\nFormat as questions and answers or flashcards."
            output = ask_llm(prompt)
            st.subheader("📝 Quiz / Flashcards")
            st.write(output)
