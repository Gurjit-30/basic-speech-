import speech_recognition as sr
import streamlit as st

recogniser = sr.Recognizer()

# diff languages
languages = {
    "English (India)": "en-IN",
    "Hindi": "hi-IN",
     "Punjabi": "pa-IN",
    "Bengali": "bn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Marathi": "mr-IN",
    "Gujarati": "gu-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
   
    "Urdu": "ur-IN"
}

# Streamlit UI
st.title("Speech Recognition App")

# Language selection
language_list = st.selectbox("Select Language", list(languages.keys()))
language_code = languages[language_list]
st.write("You selected:", language_list)
ans=True
def speech_recog(lang_code):
    with sr.Microphone() as source:
        st.write("Listening... Please speak now.")
        audio = recogniser.listen(source)

    try:
        query = recogniser.recognize_google(audio, language=lang_code)
        return query
    except sr.UnknownValueError:
        ans=False
        return "[Could not understand audio]"

    except sr.RequestError:
        return "[Error connecting to Google API]"

# Button to trigger speech recognition
if st.button("🎙️ Speak Now"):
    result = speech_recog(language_code)
    st.write("📣 You said:", result)

    if result.lower() in ["exit", "quit"]:
        st.warning("🛑 Exit command received. Ending session.")
    elif ans==False:
        st.success("You did not speak anything.")
    else:
        st.write("✅ Command received.")

# import speech_recognition as sr 
# import streamlit as st
# recognise=sr.Recognizer()

# languages = {
# "English (India)": "en-IN",
#     "Hindi": "hi-IN",
#     "Bengali": "bn-IN",
#     "Tamil": "ta-IN",
#     "Telugu": "te-IN",
#     "Marathi": "mr-IN",
#     "Gujarati": "gu-IN",
#     "Kannada": "kn-IN",
#     "Malayalam": "ml-IN",
#     "Punjabi": "pa-IN",
#     "Urdu": "ur-IN"
# }
# # converting dict into list
# language_list=st.selectbox("Select the language: ",list(languages.keys()))
# st.write("You choose ",language_list)
# # to get language code
# language_code=languages[language_list]
# def speech_recog(language_code):
#   with sr.Microphone() as source:
#         print("Speak something...............")
#         audio=recognise.listen(source)
#     try:
#         query=recognise.recognize_google(audio,language=language_code)
#         print("You said ",query.lower())
#         return query
#     except sr.UnknownValueError:
#         print("Unknown value error occured")
#     except sr.RequestError:
#         print("Error plz try again google speech")
#         return None
    
# st.title("Speech Recognistion App ")
# st.write("To speak click the button below")
# if st.button("Speak Something.."):
    # listened_cmd=speech_recong(language_code)
    # st.write("You spoke: ",listened_cmd)

# cmd=speech_recong()
# # converting the text inot lower case
# cmd=cmd.lower()
# if cmd:
#     if cmd=='exit' or cmd=='quit':
#         print("You said ",cmd)
#         print('Happy to see you again........')
#     # break
# else:
#     print("you said ",cmd)
    
  