# Speech Recognition Application

This project is a simple **Speech Recognition Application** built with Python. It allows you to listen to the microphone input in real-time, recognize the spoken words, and count the occurrences of specified target words. The application also logs the recognized text into a `notepad.txt` file and displays the results in a graphical user interface (GUI) created with Tkinter.

## Features

- **Real-Time Speech Recognition:** The application listens to the microphone input in real-time and transcribes the speech to text.
- **Target Word Counting:** You can specify a list of target words, and the application will count the occurrences of these words in the recognized speech.
- **Formatted Text Output:** The recognized text is formatted so that it breaks into a new line after every 10 words, making it suitable for OBS subtitles.
- **Logging:** The latest recognized text and word counts are saved to a `notepad.txt` file, which is updated each time new speech is recognized.
- **Graphical User Interface:** The application features a simple GUI with buttons to start/stop listening and fields to input target words.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/potatoref/Speech-Recognition-Application.git
   cd Speech-Recognition-Application
   ```

2. **Install the required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python newaudio.py
   ```

## Requirements

- Python 3.x
- `speech_recognition` library
- `pyaudio` library
- `tkinter` (included with standard Python installations)

If `pyaudio` is not installed on your system, you can install it using the following command:

```bash
pip install pipwin
pipwin install pyaudio
```

## Usage

1. **Specify Target Words:** Enter the target words separated by commas in the input field.
2. **Start/Stop Listening:** Click the "Start Listening" button to begin recognizing speech. The button text will change to "Stop Listening" to allow you to stop the process.
3. **View Results:** The recognized text and the count of each target word will be displayed in the GUI.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
