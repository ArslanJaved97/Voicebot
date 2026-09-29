import sys
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import ollama
import pyttsx3

# ---------- CONFIG ----------
WHISPER_MODEL = "base.en"       # tiny.en | base.en | small.en
OLLAMA_MODEL  = "llama3.2"
SAMPLE_RATE   = 16000
RECORD_SECONDS = 6

# ---------- INIT ----------
print("Loading Whisper model (first run may take a minute)...")
whisper_model = whisper.load_model(WHISPER_MODEL)
print("Whisper ready.")

engine = pyttsx3.init()
engine.setProperty("rate", 175)   # speaking speed

try:
    with open("script.txt", "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read()
except FileNotFoundError:
    print("ERROR: script.txt not found in this folder.")
    sys.exit(1)

# ---------- HELPERS ----------
def record_audio():
    print("\n🎤 Listening (speak now)...")
    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE, channels=1, dtype="int16")
    sd.wait()
    write("input.wav", SAMPLE_RATE, audio)
    return "input.wav"

def transcribe(path):
    print("🧠 Transcribing...")
    result = whisper_model.transcribe(path, fp16=False)
    return result["text"].strip()

def speak(text):
    print(f"🤖 Bot: {text}")
    engine.say(text)
    engine.runAndWait()

# ---------- MAIN LOOP ----------
def main():
    print("=" * 50)
    print("Voice Bot is running. Press Ctrl+C to quit.")
    print("=" * 50)

    while True:
        try:
            audio_file = record_audio()
            user_text = transcribe(audio_file)

            if not user_text:
                print("(no speech detected, listening again)")
                continue

            print(f"👤 You: {user_text}")

            if any(w in user_text.lower() for w in ["goodbye", "exit", "quit", "stop"]):
                speak("Goodbye!")
                break

            print("💭 Thinking...")
            response = ollama.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_text},
                ],
            )
            reply = response["message"]["content"]
            speak(reply)

        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()