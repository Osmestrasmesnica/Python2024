from tkinter import *
import os
import pandas as pd

# Read Morse code CSV file into a pandas DataFrame
df = pd.read_csv("morse_code.csv")
MORSE_CODE_DICT = {row.character: row.morse_code for (_, row) in df.iterrows()}

# Create the Tkinter window
window = Tk()
window.config(padx=5, pady=5, bg='yellow')
window.attributes('-alpha', '0.8')
window.title('Text to Morse Code Converter')

# Create labels for each character and its Morse code
morse_code_label = {}
i = 0
for char in MORSE_CODE_DICT:
    label = Label(text=f"{char}\n{MORSE_CODE_DICT[char]}", width=6, relief='solid', borderwidth=1)
    label.grid(row=i // 10, column=i % 10)
    morse_code_label[char] = label
    i += 1

# Text widget for input text
text = Text(window, width=50, height=10)
text.grid(row=7, column=0, columnspan=10, sticky='EW')
text.insert('1.0', 'Enter Text to Encode') #TODO add function_text_to_morse
window.rowconfigure(7, pad=10)

# Text widget for Morse code output
morse_code = Text(window, width=50, height=10)
morse_code.grid(row=8, column=0, columnspan=10, sticky='EW')
morse_code.insert('1.0', 'Enter Morse Code to Decode Separated by Space') #TODO add function_morse_to_text
window.rowconfigure(8, pad=10)

# Additional button to play Morse code sound
play_button = Button(window, text='Play', relief='solid') #TODO add command=function_play_sound
play_button.grid(row=9, column=0, columnspan=10, sticky='EW')

window.mainloop()
