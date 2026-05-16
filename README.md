# 🎙️ Speech Recognition App with Transcript

🧠 Powered by Python + Streamlit + Google Speech Recognition API

This is a multi-language **Speech-to-Text** web application built using **Streamlit** for the interface and the **SpeechRecognition** library for audio processing. It allows you to speak in various Indian languages and get instant transcriptions. The app also maintains a running transcript of everything you say in the session.

---

## 📌 Features

- 🎤 **Live Speech Recognition** using your microphone
- 🌐 **Multiple Indian Language Support**
- 📝 **Running Transcript** of recognized speech
- 🗑 **Clear Transcript** with one click
- ⚡ **Simple & Interactive Web UI** built with Streamlit
- 📜 **Powered by Google Speech Recognition API**

---

## 🧠 How it Works

The app uses Python’s **SpeechRecognition** library to capture audio from your microphone, sends it to the **Google Speech Recognition API**, and returns the detected text.  
Streamlit is used to make the interface interactive and easy to use. Session state is leveraged to keep the transcript persistent during the app's run.

---

## 📁 Project Structure


File Structure
speech-recognition-app/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation


