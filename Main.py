from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
    
# Tkinter Window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)

# Data
data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict()
values = random.randint(0, 100)
english_value = list(data_dict["English"].values())[values]
french_value = list(data_dict["French"].values())[values]

# Button Commands
def confirm_cancel():
    global word
    values = random.randint(0, 100)
    english_value = list(data_dict["English"].values())[values]
    french_value = list(data_dict["French"].values())[values]
    canvas.delete(word)
    word = canvas.create_text(400, 263, text=french_value, font=("Ariel", 60, "bold"))

# Card Image
canvas = Canvas(width=800, height=526)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 250, image=img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cancel_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_image, highlightthickness=0, command=confirm_cancel)
cancel_button.grid(column=0, row=1)

confirm_image = PhotoImage(file="images/right.png")
confirm_button = Button(image=confirm_image, highlightthickness=0, command=confirm_cancel)
confirm_button.grid(column=1, row=1)

window.mainloop()
