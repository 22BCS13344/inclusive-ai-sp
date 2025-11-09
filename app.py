import streamlit as st
import joblib
import numpy as np
import pandas as pd
import pyttsx3
import tempfile
import os
import time

st.set_page_config(page_title="Inclusive Learning AI", page_icon="🎓", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎓 Inclusive Learning Assistant</h1>", unsafe_allow_html=True)
st.write("This AI system recommends personalized content formats for students with different disabilities.")
st.markdown("---")

model = joblib.load("model.pkl")
le_dis = joblib.load("le_disability.pkl")
le_con = joblib.load("le_content.pkl")

disability = st.selectbox("Disability type", options=list(le_dis.classes_))
engagement = st.slider("Engagement score (approx)", 0.0, 1.0, 0.75, 0.01)
comprehension = st.slider("Comprehension score (approx)", 0.0, 1.0, 0.75, 0.01)

pred_label = None

if st.button("Get Recommendation"):
    dis_code = le_dis.transform([disability])[0]
    try:
        X = np.array([[dis_code]])
        pred_code = model.predict(X)[0]
    except Exception:
        X = np.array([[dis_code, engagement, comprehension]])
        pred_code = model.predict(X)[0]

    pred_label = le_con.inverse_transform([pred_code])[0]
    st.success(f"✅ Recommended content format: **{pred_label.upper()}**")

    if pred_label.lower() == "audio":
        engine = pyttsx3.init()
        engine.say("Recommended learning content is Audio.")
        engine.runAndWait()
        engine.stop()

if 'pred_label' in locals() and st.button("Generate Sample Content"):
    if pred_label.lower() == "text":
        st.write("📝 Example Text Content: 'The water cycle involves evaporation, condensation, and precipitation.'")
    elif pred_label.lower() == "audio":
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
    elif pred_label.lower() == "video":
        st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")

st.markdown("---")
st.write("### Example use-cases:")
st.write("- Visual impairment → audio with clear narration")
st.write("- Hearing impairment → text + captions/subtitles")
st.write("- Cognitive impairment → simplified text/audio + chunked content")


st.markdown("---")
st.subheader("🗣️ Convert Text or File to Speech")

text_input = st.text_area("Enter text here:")
uploaded_file = st.file_uploader("Or upload a text file (.txt)", type=["txt"])

if st.button("Convert to Speech"):
    text_to_read = ""

    if text_input:
        text_to_read = text_input
    elif uploaded_file is not None:
        text_to_read = uploaded_file.read().decode("utf-8")
    else:
        st.warning("Please enter text or upload a file.")

    if text_to_read:
        try:
            temp_path = os.path.join(tempfile.gettempdir(), "tts_output.wav")
            engine = pyttsx3.init()
            engine.save_to_file(text_to_read, temp_path)
            engine.runAndWait()
            engine.stop()

            time.sleep(0.5)

            if os.path.exists(temp_path):
                st.success("✅ Speech generated successfully!")
                st.audio(temp_path, format="audio/wav")
            else:
                st.error("❌ Failed to generate speech. Try again.")
        except Exception as e:
            st.error(f"Error generating audio: {e}")

st.markdown("---")
st.subheader("💬 User Feedback")

feedback = st.text_area("Was this recommendation helpful?")
if st.button("Submit Feedback"):
    if 'pred_label' not in locals() or pred_label is None:
        st.warning("Please get a recommendation before submitting feedback.")
    else:
        with open("user_feedback.txt", "a", encoding="utf-8") as f:
            f.write(f"{disability},{pred_label},{feedback}\n")
        st.success("✅ Feedback saved successfully! Thank you!")
st.markdown("---")
data = pd.read_csv("learning_data.csv")
st.subheader("📊 Example Training Data")
st.dataframe(data)
