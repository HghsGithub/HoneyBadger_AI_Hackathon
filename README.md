

# 🛡️ HoneyBadger AI

**Team Name:** Inspiring  
**Hackathon:** LoubbyAI Hackathon  
**Track:** Innovation & Infrastructure  

---

## Project Overview
HoneyBadger AI is a text classification system designed to **detect unsafe or hallucination text**.  
It prevents accidental leaks of confidential, sensitive, or private information and classifies text into **Safe**, **Unsafe**, or **Hallucination**, helping organizations and AI systems handle content responsibly.

- **Embedding Model:** `all-MiniLM-L6-v2` (SentenceTransformer)  
- **Classifier:** LightGBM  
- **Purpose:** Prevents leaks of sensitive data and handles unsafe or hallucinated content intelligently.

---

## Demo
- Live Demo: [Insert your Streamlit link here]  
- YouTube Demo: [Watch here](https://youtu.be/yZJ2KRvARVo?feature=shared)

---

## Project Structure
HoneyBadger_AI_Hackathon/
├── app.py # Streamlit application
├── train.py # Optional: training script
├── model_bundle.pkl # Full model bundle
├── requirements.txt # Python dependencies
├── README.md # This file
├── LICENSE # MIT License


---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/HghsGithub/HoneyBadger_AI_Hackathon.git
cd HoneyBadger_AI_Hackathon

#Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


Example Usage

Enter text in the input area of the app.

Click Classify.

The app predicts if the text is Safe, Unsafe, or Hallucination.

Example Inputs:

Safe: "Thank you, Jesus, Hallelujah"

Unsafe: "This contains private passwords or secret information"

Hallucination: "The moon is made of cheese"


Team Members

. Oluwasegun Jacobs

. Chidinma Cynthia Mmeje

. Fortune Richman

. Shittu Oluwashola


License

This project is licensed under the MIT License.
© 2025 HoneyBadger AI

