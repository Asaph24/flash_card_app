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
def next():
    global timer
    window.after_cancel(timer)
    values = random.randint(0, 100)
    english_value = list(data_dict["English"].values())[values]
    french_value = list(data_dict["French"].values())[values]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french_value, fill="black")
    canvas.itemconfig(first_image, image=img)
    timer = window.after(3000, func=flip)

# Time change
def flip():
    
    canvas.itemconfig(first_image, image=new_image)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_value, fill="White")

# Card Image
canvas = Canvas(width=800, height=526)
img = PhotoImage(file="images/card_front.png")
first_image = canvas.create_image(400, 250, image=img)
new_image = PhotoImage(file="images/card_back.png")
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cancel_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_image, highlightthickness=0, command=next)
cancel_button.grid(column=0, row=1)

confirm_image = PhotoImage(file="images/right.png")
confirm_button = Button(image=confirm_image, highlightthickness=0, command=next)
confirm_button.grid(column=1, row=1)

# Start Timer
timer = window.after(3000, flip)

window.mainloop()
