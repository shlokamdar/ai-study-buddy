
# AI Study Buddy 📚

**AI Study Buddy** is your personal AI-powered learning companion. Get explanations, summaries, and quizzes on any topic—perfect for students, lifelong learners, or anyone curious. Built with Python, Streamlit, and OpenAI API for a seamless study experience.

---

## Features

- **Instant explanations**: Understand complex topics in simple terms.  
- **Custom summaries**: Summarize textbooks, notes, or articles quickly.  
- **Quizzes & practice**: Test your knowledge interactively.  
- **Multi-topic support**: Learn anything from programming to history.  
- **Lightweight & fast**: Runs locally with minimal setup.

---

## Project Structure

```

ai-study-buddy/
├── .gitignore         # ignores local secrets and environment files
├── README.md          # project overview
├── app.py             # main application
├── requirements.txt   # project dependencies
└── .env-example       # template for environment variables

````

---

## Installation

1. **Clone the repository**  
```bash
git clone https://github.com/shlokamdar/ai-study-buddy.git
cd ai-study-buddy
````

2. **Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/macOS
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

* Copy `.env-example` to `.env`
* Add your **OpenAI API key**:

```
OPENAI_API_KEY="sk-xxxxxxx"
```

---

## Usage

```bash
python app.py
```

* Open the app in your browser (Streamlit usually runs at `http://localhost:8501`)
* Enter a topic, choose your preferred output (explanation, summary, or quiz), and start learning!

---

## Notes

* Never commit your `.env` file with API keys to GitHub.
* Make sure your `.env` is listed in `.gitignore`.
* This project uses OpenAI API, so usage may incur costs depending on your plan.

---

## Contributing

Contributions are welcome!

* Bug fixes, feature suggestions, and improvements are encouraged.
* Please fork the repo, create a new branch, and submit a pull request.

---

## License

MIT License © 2025 Shloka Kamdar

```

---



Do you want me to do that too?
```
