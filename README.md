![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen)

👶 Baby Name Generator
LangChain · OpenAI · Streamlit

An AI-powered web application that generates meaningful Indian baby names based on gender and contextual preferences.
This project demonstrates real-world application of Large Language Models (LLMs) using LangChain (LCEL) with a clean Streamlit-based UI and secure cloud deployment.

🔍 Project Overview

Choosing a baby name is culturally significant and deeply personal.
This application leverages OpenAI-powered LLMs through LangChain Expression Language (LCEL) to generate context-aware Indian baby names, enriched with:

Semantic meaning of names

Cultural and regional relevance

User-specific contextual personalization

Famous personalities sharing the same name

The application is deployed on Streamlit Community Cloud, following production-grade best practices for secrets management and version control.

✨ Key Features

👶 AI-generated Indian baby names

🚻 Gender-based selection (Boy / Girl)

🧠 Context-aware generation (region, family background, values)

📖 Name meanings with famous personalities

🔗 Built using LangChain Expression Language (LCEL)

🎨 Interactive Streamlit UI

🔐 Secure API key handling using environment variables

☁️ Cloud deployment on Streamlit Community Cloud


## 🖼️ User Interface Preview

![Home Screen](images/ui-home.png)
![Generated Names](images/ui-output.png)
[gafafga](./src\images\wallpaper.jpg)

🛠️ Tech Stack
Python 3.10+

LangChain (LCEL architecture)

OpenAI API

Streamlit

dotenv

VS Code

📂 Project Structure
text
Copy code
Langchain-Final/
│
├── src/
│   └── main.py          # LangChain logic (LCEL pipeline)
│
├── app.py               # Streamlit UI
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example

⚙️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/your-username/baby-name-generator-langchain.git
cd baby-name-generator-langchain
2️⃣ Create Virtual Environment
bash
Copy code
python -m venv venv
Activate:

bash
Copy code
# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file in the root directory:

env
Copy code
OPENAI_API_KEY=your_openai_api_key_here
⚠️ Never commit .env to GitHub

▶️ Running the Application
Run backend (LangChain logic)
bash
Copy code
python src/main.py
Run Streamlit UI
bash
Copy code
streamlit run app.py
🧠 How It Works (Under the Hood)
Uses LangChain Expression Language (LCEL) for chaining

Prompt → LLM → Output Parser pipeline

Dynamic prompt construction based on:

Gender

User-provided baby description

Responses parsed into clean, readable output for UI rendering

🧪 Example Input
text
Copy code
Gender: Boy
Context: Born in Madhya Pradesh in a very rich landlord family,
         include meaning and famous personalities
✅ Sample Output
Rajveer — Meaning "brave king".
Famous personality: Rajveer Singh (Indian actor)

Arjun — Meaning "bright / shining".
Famous personality: Arjun Kapoor (Bollywood actor)

Veerendra — Meaning "brave lord".
Famous personality: Veerendra Heggade (Philanthropist)

Yashvardhan — Meaning "glory of the king".
Famous personality: Yashvardhan Ahuja (Actor)

Viraj — Meaning "illustrious".
Famous personality: Viraj Dayal (Musician)

🚀 Future Enhancements
🔍 RAG-based name suggestions using curated datasets

🌐 Multi-language support

📜 Explanation of cultural & historical relevance

☁️ Cloud deployment with CI/CD

🧩 Modular prompt templates

🎯 Why This Project Matters (Resume Value)
Demonstrates LLM application development

Shows modern LangChain (LCEL) usage

Covers frontend + backend integration

Highlights real-world AI product thinking

Deployable, scalable, and extensible

📄 License
This project is intended for educational and portfolio purposes.

👤 Author
Manthan Mahendra Adsul
Final-year Engineering student
Interested in AI, Automation, and Applied LLM Systems

🔗 LinkedIn: https://www.linkedin.com/in/manthan-adsul/
📧 Email: manthanadsul1@gmail.com