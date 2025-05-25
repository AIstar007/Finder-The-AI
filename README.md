# 🤖 Finder-The-AI

Finder is a voice-activated desktop assistant built using Python. It can respond to your queries, search Wikipedia, open websites, tell you the time and date, send emails, and more — all using voice commands.

---

## 🎯 Features

- Voice interaction using speech recognition
- Text-to-speech responses with `pyttsx3`
- Wikipedia integration
- Web browser control (YouTube, Google, Instagram, etc.)
- Tells the current time, date, and whether it’s a leap year
- Sends emails via Gmail (with authentication)
- Personalized greetings
- Basic conversation ability

---

## 🚀 How It Works

1. The assistant greets you based on the time of day.  
2. Listens for your voice command.  
3. Executes the command — from telling the time to sending an email or searching Wikipedia.

---

## 🛠️ Requirements

Install required Python packages:

   ```bash
   pip install speechrecognition wikipedia pyttsx3 pyaudio
   pip install pipwin
   pipwin install pyaudio
   ```

## 🧠 Technologies Used
- speech_recognition — for converting voice to text
- pyttsx3 — for text-to-speech
- wikipedia — for fetching info from Wikipedia
- webbrowser — to open websites
- datetime — to fetch current time/date
- smtplib — to send emails via Gmail
- os & random — for optional desktop control or randomness

## 📝 How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Finder-The-AI.git
   cd Finder-The-AI

2. **Run the script:**
   ```bash
   python finder.py

3. **Start speaking! Try commands like:**
   - "Tell me the time"
   - "Search Wikipedia for Artificial Intelligence"
   - "Open YouTube"
   - "Send email to [recipient]"

## 📌 Notes
- Ensure your microphone is enabled and accessible by Python.
- You can personalize Finder-The-AI with your own greetings or functionality.

## 🤝 Contributing
**Feel free to fork this repository, enhance the assistant’s abilities, or contribute new features via pull requests.**
