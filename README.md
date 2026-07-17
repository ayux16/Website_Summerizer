# 🤖 AI Website Summarizer

A simple AI-powered web application that summarizes the content of any website using a Large Language Model (LLM).

Built as my first AI project while beginning my AI Engineering journey.

---

## 🚀 Features

- 🌐 Summarize any website by simply providing its URL.
- 🧠 AI-generated concise and readable summaries.
- 🕸️ Extracts meaningful website content by removing unnecessary HTML elements.
- 🎨 Simple and interactive UI built with Gradio.
- ⚡ Fast and lightweight.

---

## 🛠️ Tech Stack

- Python
- Gradio
- BeautifulSoup4
- Requests
- Groq API (Llama 3.3 70B)
- python-dotenv

---

## 📂 Project Structure

```
.
├── app.py              # Gradio UI
├── scraper.py          # Website content extraction
├── summarizer.py       # LLM integration & summarization
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. Enter a website URL.
2. The application extracts the readable content from the webpage.
3. The extracted content is sent to an LLM.
4. The model generates a concise summary.
5. The summary is displayed through a simple Gradio interface.

---

## 🖥️ Installation

Clone the repository

```bash
git clone https://github.com/ayux16/Ai_Battle_Arina.git
cd Ai_Battle_Arina
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install openai gradio requests beautifulsoup4 python-dotenv
```

Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

Run the application

```bash
python app.py
```

---

## 📸 Demo

> Add screenshots or a short GIF here.

---

## 💡 What I Learned

- Integrating LLMs using APIs
- Prompt Engineering fundamentals
- Web scraping using BeautifulSoup
- Building interactive AI applications with Gradio
- Managing secrets securely using `.env`

---

## 🔮 Future Improvements

- Support multiple AI models
- Streaming responses
- Better content extraction
- Export summary as PDF
- Browser extension support

---

## 👨‍💻 Author

**Ayush Verma**

Java Backend Developer exploring AI Engineering.

If you found this project interesting, feel free to ⭐ the repository.
