# Alexa-like Voice Assistant

This project is an Alexa-like voice assistant that uses Python to recognize speech commands and perform various actions. It leverages libraries such as `speech_recognition`, `pyttsx3`, `pywhatkit`, `datetime`, `wikipedia`, and `pyjokes` to deliver functionalities like playing music, telling jokes, fetching Wikipedia summaries, and more.

## Features

- **Voice Recognition**: Uses `speech_recognition` to listen and recognize spoken commands.
- **Text-to-Speech**: Uses `pyttsx3` to convert text responses into speech.
- **YouTube Integration**: Plays requested songs or videos using `pywhatkit`.
- **Wikipedia Integration**: Fetches and reads summaries from Wikipedia.
- **Jokes**: Tells jokes using the `pyjokes` library.
- **Date and Time**: Provides the current date and time.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `voice_assistant.py` script:
```bash
python voice_assistant.py
```

The assistant will start listening for your commands. Here are some example commands you can use:

- "Alexa, play [song name]"
- "Alexa, what time is it?"
- "Alexa, who is [person]?"
- "Alexa, tell me a joke"
- "Alexa, what's the date today?"

## Project Structure

- `voice_assistant.py`: Main script that runs the voice assistant.
- `requirements.txt`: List of required Python packages.

## Dependencies

- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `datetime`
- `wikipedia`
- `pyjokes`

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to modify any part to better suit your project's needs!
