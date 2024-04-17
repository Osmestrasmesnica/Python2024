from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import os

SOURCE_DIRECTORY = os.getcwd()
TARGET_DIRECTORY = "Dan_85-Portfolio_Watermark/water_marked_pictures"

# Construct the full path to the target directory
target_path = os.path.join(SOURCE_DIRECTORY, TARGET_DIRECTORY)

# Check if the target directory exists, and create it if it doesn't
if not os.path.exists(target_path):
    os.makedirs(target_path)


def open_file():
    browse_text.set("Loading...")
    photo_name = filedialog.askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File", filetypes=
        (("All files", "*.*"),))
    if photo_name:
        image = Image.open(photo_name).convert("RGBA")
        wm_image = Image.open("Dan_85-Portfolio_Watermark/img/logo-letter-rbg.png").convert("RGBA")

        # Determine the maximum size for the watermark based on the base image size
        max_width = image.size[0] // 5  # You can adjust this ratio as needed
        max_height = image.size[1] // 5  # You can adjust this ratio as needed

        # Resize the watermark while maintaining its aspect ratio
        wm_resized = wm_image.copy()
        wm_resized.thumbnail((max_width, max_height))

        # Set position to lower right corner
        position = (image.size[0] - wm_resized.size[0], image.size[1] - wm_resized.size[1])

        transparent = Image.new('RGBA', image.size, (0, 0, 0, 0))
        transparent.paste(image, (0, 0))
        transparent.paste(wm_resized, position, mask=wm_resized)

        # Construct the target file path
        target_file_path = os.path.join(target_path, os.path.basename(photo_name)[:-4] + "_WM.jpg")

        # Save watermarked photo
        finished_img = transparent.convert("RGB")
        finished_img.save(target_file_path)

        # Open saved photo
        os.startfile(target_file_path)

        success_text.set(f"Success! File saved to {target_file_path}.")
        browse_text.set("Browse")


def quit():
    root.destroy()

# GUI
root = tk.Tk()
root.title("Watermark App WLQ")

# Logo
logo = Image.open("Dan_85-Portfolio_Watermark/img/logo.png")
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo)
logo_label.grid(column=3, row=0)

# Instructions
instruction_label = tk.Label(root, text="Select photo to watermark.", font=("Arial", 12))
instruction_label.grid(columnspan=5, column=0, row=1)

# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=open_file, font=("Arial", 12), bg="#20bebe", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=2)

# Success Message
success_text = tk.StringVar()
success_text.set("Made by WLQ Innovations 2024")
success_label = tk.Label(root, textvariable=success_text, font=("Arial", 8))
success_label.grid(columnspan=5, column=0, row=3)

# Cancel Button
cancel_btn = tk.Button(root, text="Quit", command=quit, font=("Arial", 12), bg="#20bebe", fg="white", height=2, width=15)
cancel_btn.grid(column=4, row=2)

root.mainloop()