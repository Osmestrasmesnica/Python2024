import pandas as pd

# Read Morse code CSV file into a pandas DataFrame
df = pd.read_csv("morse_code.csv")

# Create a dictionary from the DataFrame with characters as keys and Morse code as values
morse_code_dict = {row.character: row.morse_code for (_, row) in df.iterrows()}

print("Enter your text and I will convert it to Morse Code...")
user_input = input().upper()  # Convert input to uppercase as all characters in the dictionary are uppercase

# Construct Morse code string
morse_code_message = ' '.join([morse_code_dict.get(char, '') + ' ' if char != ' ' else ' ' * 3 for char in user_input])

print(f"Your message in Morse Code: {morse_code_message}")
