import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("🎤 Speak now...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
    audio_data = recognizer.listen(source)
    print("🔍 Recognizing...")

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        print("📝 You said: ", text)

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")

    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")

