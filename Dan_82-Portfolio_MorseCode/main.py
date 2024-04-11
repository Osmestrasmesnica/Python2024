import pandas as pd
import time
from tkinter import *
import pygame
import os


# ---------------------------- Audio Set Up --------------------------- #
# File path to audio
long_audio = "Dan_82 - Portfolio_MorseCode/assets/long.wav"
short_audio = "Dan_82 - Portfolio_MorseCode/assets/short.wav"

# Check if audio files exist
if not os.path.exists(long_audio) or not os.path.exists(short_audio):
    print("Error: Audio files not found.")
    exit()

# Initialize Pygame mixer
pygame.mixer.init()

# Load audio files
long_sound = pygame.mixer.Sound(long_audio)
short_sound = pygame.mixer.Sound(short_audio)

# ---------------------------- Morse Code Dict ------------------------ #
# Read csv with morse code alphabet
df = pd.read_csv("Dan_82 - Portfolio_MorseCode/morse_code.csv")
MORSE_CODE_DICT = {row.character: row.morse_code for (_, row) in df.iterrows()}

# ---------------------------- FUNCTION SETUP -------------------------- #
# Clear explanatory texts
def clear_text(event=None):
    global widgets_cleared
    # Check if the widgets have not been cleared yet
    if not widgets_cleared:
        text.delete('1.0', END)  # Clear the text widget
        morse_code.delete('1.0', END)  # Clear the morse code widget
        widgets_cleared = True  # Update the flag to indicate that the widgets have been cleared  

# Convert text to morse code
def text_to_morse(event):
    for _ in morse_code_label:
        morse_code_label[_].config(bg='#FFD699', fg='black')
    
    input_text = event.widget.get('1.0', END)
    input_text = input_text.upper()
    morse_code_text = ''
    for char in input_text:
        if char in MORSE_CODE_DICT:
            morse_code_text += MORSE_CODE_DICT[char] + ' '
        elif char == '\n':
            continue
        else:
            morse_code_text += char + ' '

    if event.char.upper() in MORSE_CODE_DICT:
        morse_code_label[event.char.upper()].config(bg='yellow', fg='white')
        window.after(300, lambda: morse_code_label[event.char.upper()].config(bg='#FFD699', fg='black'))     
    
    morse_code.delete('1.0', END)
    morse_code.insert('1.0', morse_code_text.strip())
    

# Convert morse code to text
def morse_to_text(event):
    morse = event.widget.get('1.0', END)
    if not morse.strip():  # Handle empty input
        return
    
    words = morse.strip().replace(".", "•").split('   ')  # Split by space between words in Morse code
    message = []
    for word in words:
        chars = word.split()  # Split Morse code word into individual characters
        for char in chars:
            try:
                decoded_char = [key for key, value in MORSE_CODE_DICT.items() if value == char][0]
                message.append(decoded_char)
            except IndexError:
                message.append("[Unknown]")  # Add placeholder for unknown Morse code characters
        message.append(' ')  # Add space between words
    decoded_message = ''.join(message).rstrip()  # Join the decoded message and remove trailing whitespace
    text.delete('1.0', END)
    text.insert('1.0', decoded_message)

# Play Morse code audio
def play_morse_audio(morse_code):
    for signal in morse_code:
        if signal == '•':
            short_sound.play()
            pygame.time.wait(int(short_sound.get_length() * 1000))  # Wait for the short sound to finish
        elif signal == '-':
            long_sound.play()
            pygame.time.wait(int(long_sound.get_length() * 1000))  # Wait for the long sound to finish
        elif signal == ' ':
            pygame.time.wait(500)  # 200ms pause between characters, or make it longer to understand the sound easily
        else:
            # Ignore any other characters (like spaces between words)
            continue

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=10, pady=10, bg='skyblue')
window.attributes('-alpha', '1')
window.title('Text to Morse Code Converter by WLQ')
window.iconbitmap('Dan_82 - Portfolio_MorseCode/morse-icon.ico')
window.geometry("1040x950")  # Set initial window size

# Bind the function to left mouse clicks and any key presses
window.bind('<Button-1>', clear_text)
window.bind('<Key>', clear_text)

# Initialize a flag to keep track of whether the widgets have been cleared or not
widgets_cleared = False

morse_code_label = {}
i = 0
for _ in MORSE_CODE_DICT:
    label = Label(text=f"{_}\n{MORSE_CODE_DICT[_]}", width=8, relief='solid', borderwidth=2, font=('Arial', 16))
    label.grid(row=i // 10, column=int(str(i)[-1]))
    morse_code_label[_] = label
    i += 1

text = Text(width=80, height=10, font=('Arial', 16))
text.grid(row=7, column=0, columnspan=10,sticky='EW')
text.insert('1.0', 'Click Here and Insert Text to Encode')
window.rowconfigure(7, pad=10)
text.bind('<KeyRelease>', text_to_morse)

morse_code = Text(width=80, height=10, font=('Arial', 16))
morse_code.grid(row=8, column=0, columnspan=10, sticky='EW')
morse_code.insert('1.0', 'Enter Morse Code to Decode Separated by Space')
window.rowconfigure(8, pad=10)
morse_code.bind('<KeyRelease>', morse_to_text)

# Button to play Morse code audio
def play_morse_audio_button():
    morse = morse_code.get('1.0', END).strip()
    if morse:
        play_morse_audio(morse)

play_button = Button(text='Play', relief='solid', command=play_morse_audio_button, font=('Arial', 16))
play_button.grid(row=9, column=0, columnspan=10, sticky='EW')

window.mainloop()
