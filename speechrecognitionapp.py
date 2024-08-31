import speech_recognition as sr
import pyaudio
import tkinter as tk
import threading

# Global variables
is_listening = False
target_words = []  # A list to store target words
word_counts = {}   # Count for each word (defined globally)

def format_text(text, max_words_per_line=10):
    """Formats the text to break the line after every 10 words."""
    words = text.split()
    formatted_text = ''
    
    for i in range(0, len(words), max_words_per_line):
        line = ' '.join(words[i:i + max_words_per_line])
        formatted_text += line + '\n'
    
    return formatted_text.strip()

def start_listening_thread():
    """Starts the listening process in a separate thread."""
    listening_thread = threading.Thread(target=start_listening)
    listening_thread.start()

def start_listening():
    global is_listening, target_words, word_counts
    is_listening = True
    r = sr.Recognizer()
    # Reset all counts when starting to listen
    word_counts = {word: 0 for word in target_words}

    with sr.Microphone() as source:
        result_label.config(text="Listening...")
        while is_listening:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio, language="tr-TR")
                print(f"Recognized Text: {text}")
                
                words = text.lower().split()
                
                for word in target_words:
                    occurrences = words.count(word.lower())
                    word_counts[word] += occurrences
                    print(f"Word '{word}' found {occurrences} times, total: {word_counts[word]}")
                
                # Display the result in the interface
                result_text = f"Recognized Text: {text}\n"
                for word, count in word_counts.items():
                    result_text += f"Target word '{word}' mentioned {count} times.\n"
                
                result_label.config(text=result_text)
                
                # Write only the last spoken text to the notepad.txt file (overwrite previous)
                with open("notepad.txt", "w", encoding="utf-8") as file:  # 'w' mode resets the file each time
                    file.write(f"{text}\n")
                    for word, count in word_counts.items():
                        file.write(f"'{word}' {count} \n")
                    file.write("\n")  # Add a blank line afterwards

            except sr.UnknownValueError:
                result_label.config(text="Could not understand")
            except sr.RequestError as e:
                result_label.config(text=f"Google Speech Recognition service is not working; {0}".format(e))

def stop_listening():
    global is_listening
    is_listening = False
    result_label.config(text="Listening stopped.")

def start_stop_button_text():
    return "Stop Listening" if is_listening else "Start Listening"

def update_button():
    button.config(text=start_stop_button_text())

def set_target_words():
    global target_words
    input_text = entry.get()  # input_text is defined here
    target_words = [word.strip() for word in input_text.split(',')]  # Convert words to a list by separating with commas
    print(f"Target words set as '{target_words}'.")
    count_label.config(text=f"Target words: {', '.join(target_words)}")

# Create the Tkinter window
root = tk.Tk()
root.title("Speech Recognition Application")
root.geometry("400x400")  # Window size

# Target word entry field
entry_label = tk.Label(root, text="Target Words (Separate with commas):", font=("Helvetica", 12))
entry_label.pack(pady=10)
entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=5)

# Button to set target words
set_word_button = tk.Button(root, text="Set Target Words", command=set_target_words)
set_word_button.pack(pady=10)

# Button to start/stop listening
button = tk.Button(root, text=start_stop_button_text(), command=lambda: [start_listening_thread() if not is_listening else stop_listening(), update_button()])
button.pack(pady=10)

# Area to display the recognized text
result_label = tk.Label(root, text="Results will be displayed here", font=("Helvetica", 12))
result_label.pack(pady=10)

# Area to display the count of target words mentioned
count_label = tk.Label(root, text="Target words not set yet.", font=("Helvetica", 12))
count_label.pack(pady=10)

update_button()  # Update the button text initially

root.mainloop()
