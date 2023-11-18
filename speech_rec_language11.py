import streamlit as st
import speech_recognition

st.title("Speech Recognition App")

# Add a selection box for the speech recognition API
speech_api = st.selectbox("Select Speech Recognition API", ["Google", "Sphinx", "Wit.ai"])
def transcribe_speech(api):
    # Initialize recognizer class
    r = sr.Recognizer()

    # Select the appropriate API
    if api == 'Google':
        recognizer_func = r.recognize_google
    elif api == 'Bing':
        recognizer_func = r.recognize_sphinx
    elif api == 'Amazon':
        recognizer_func = r.recognize_amazon
    elif api == "Watson":
        recognizer_func = r.recognize_ibm
    elif api == "DeepSpeech":
        recognizer_func = r.recognize_ds
    else:
        return "Invalid API selected."

    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # Use the selected API for recognition
            text = recognizer_func(audio_text)
            return text
        except:
            return "Sorry, I did not get that."

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # Select the API
    api_options = ['Google', 'Bing', 'Amazon', 'Watson','Deepspeech']
    selected_api = st.selectbox("Select API:", api_options)

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(selected_api)
        st.write("Transcription: ", text)




if st.button("Start Recognition"):
    # Call transcribe_speech function with selected API
    transcribe_speech(speech_api)


    def transcribe_speech(api):
        try:
            # Speech recognition logic based on the selected API
            # ...
            st.success("Speech recognition successful!")
        except Exception as e:
            st.error(f"Error during speech recognition: {str(e)}")
            if st.button("Save Transcription"):
                with open("transcription.txt", "w") as file:
                    file.write(transcription)
                st.success("Transcription saved successfully!")
                language = st.text_input("Enter the language for speech recognition", "en-US")
                # Pass the selected language to the speech recognition function
                transcribe_speech(speech_api, language)
                is_paused = st.checkbox("Pause Speech Recognition")

                if st.button("Start/Resume Recognition"):
                    # Call transcribe_speech function with pause parameter
                    transcribe_speech(speech_api, language, is_paused)
                    if __name__ == "__main__":
                        main()