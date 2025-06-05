import speech_recognition as sr
import requests
import json
import os

# Path to the file that stores light states
state_file = "light_states.json"

# Load previous light states or initialize to 0
if os.path.exists(state_file):
    with open(state_file, "r") as f:
        states = json.load(f)
else:
    states = {"light1": 0, "light2": 0}

a = states["light1"]
b = states["light2"]

# ESP8266 URL
url = "http://192.168.194.210/command"

# Initialize recognizer
r = sr.Recognizer()

try:
    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

    # Recognize speech
    print("Recognizing...")
    command = r.recognize_google(audio)
    command = command.lower().strip()
    print("Your command is: " + command)

    # Match commands and update states
    if "turn on light one" in command:
        a = 1
    elif "turn off light one" in command:
        a = 0
    elif "turn on second light" in command or "second light on" in command:
        b = 1
    elif "turn off second light" in command or "second light off" in command:
        b = 0

    print(f"Light 1 state: {a}, Light 2 state: {b}")

    # Send updated states to ESP8266
    try:
        params = {'light1': a, 'light2': b}
        print(f"Sending request to: {url} with params: {params}")
        response = requests.get(url, params=params, timeout=15)
        print("ESP8266 response:", response.text)
    except requests.RequestException as e:
        print(f"Error communicating with ESP8266: {e}")

    # Save new states to file
    with open(state_file, "w") as f:
        json.dump({"light1": a, "light2": b}, f)

except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")
except sr.RequestError as e:
    print(f"Error with the speech recognition service: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
