
import streamlit as st
import joblib
import numpy as np

# ----------------------------
# Load Model Bundle
# ----------------------------
BUNDLE_PATH = "/content/drive/MyDrive/AI_Safety_App/model_bundle.pkl"

@st.cache_resource
def load_model_bundle():
    bundle = joblib.load(BUNDLE_PATH)
    return bundle["vectorizer"], bundle["model"]

embedding_model, clf = load_model_bundle()

# ----------------------------
# App Layout
# ----------------------------
st.set_page_config(page_title="HoneyBadger AI", layout="wide")
st.title("🛡️ HoneyBadger AI")

# Purpose section (split into multiple markdown calls)
st.markdown("**Purpose:** HoneyBadger AI detects unsafe or hallucination text.")
st.markdown("It prevents accidental leaks of confidential, sensitive or hallucination information.")
st.markdown("It classifies text into **Safe**, **Unsafe**, or **Hallucination**,")
st.markdown("helping organizations and AI systems handle content responsibly.")
st.markdown("Powered by **SentenceTransformer embeddings + LightGBM**.")

# Add spacing
st.markdown("")
st.markdown("")

# Text input
user_input = st.text_area("Enter text to classify:", height=150)

if st.button("Classify"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text!")
    else:
        # Generate embedding and predict
        embedding = embedding_model.encode([user_input])
        prediction = clf.predict(embedding)[0]

        # Display results with color
        if prediction.lower() == "safe":
            st.success(f"✅ Prediction: **{prediction.upper()}**")
        elif prediction.lower() == "unsafe":
            st.error(f"❌ Prediction: **{prediction.upper()}**")
        else:  # hallucination
            st.info(f"💡 Prediction: **{prediction.upper()}**")

# Footer (multiple markdown calls)
st.markdown("---")
st.markdown("*Created for LoubbyAI Hackathon presentation.*")
st.markdown("*Team Inspiring.*")
st.markdown("*HoneyBadger AI.*")


