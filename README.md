
# 📊 AI Data Analyst Assistant

An AI-powered web application that allows users to **upload a CSV dataset and ask questions in natural language**.
The system analyzes the data and automatically generates answers using **LLM (Groq + LangChain)**.

---

## 🚀 Features

* Upload any `.csv` dataset
* Automatic data preview
* Ask questions in simple English
* AI analyzes columns and values
* Instant human-like answers
* Chat-based interface (Streamlit)

---

## 🧠 Technologies Used

* Python
* Streamlit
* Pandas
* LangChain
* Groq LLM
* python-dotenv

---

## 🖥️ How It Works

1. User uploads a CSV file
2. Application reads data using Pandas
3. Data preview is displayed
4. User asks a question about the dataset
5. Question + dataset sent to LLM (Groq via LangChain)
6. AI analyzes the data
7. Natural language answer is generated
8. Response displayed in chat interface

---



## ⚙️ Installation & Run

### 1️⃣ Clone the repository

```
git clonehttps://github.com/mayuri-ai06/chat-with-data-ai
cd AI-Data-Analyst-Assistant
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Add API Key

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run the app

```
streamlit run app.py
```

---

## 💬 Example Questions

* Which student scored highest marks?
* What is the average salary?
* How many students took Python course?
* Show total sales amount.

---

## 📊 Application Flowchart

![Flowchart](https://github.com/mayuri-ai06/chat-with-data-ai/blob/main/assets/flowchart.jpeg?raw=true)

---
## 🧪 Application Output

![Output](https://github.com/mayuri-ai06/chat-with-data-ai/blob/main/assets/OUTPUT%202.png?raw=true)
![Output](https://github.com/mayuri-ai06/chat-with-data-ai/blob/main/assets/OUTPUT.png?raw=true)

## 🎯 Purpose

This project demonstrates how **AI + Data Analysis** can help non-technical users understand datasets without coding or SQL knowledge.

---

## 👩‍💻 Author

**Mayuri Khatarkar**
B.Tech (Artificial Intelligence & Machine Learning)

---

⭐ If you like this project, consider giving it a star!

