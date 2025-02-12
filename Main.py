from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)

# Card Image
canvas = Canvas(width=800, height=526)
img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 250, image=img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)




# Buttons
cancel_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_image, highlightthickness=0)
cancel_button.grid(column=0, row=1)

confirm_image = PhotoImage(file="images/right.png")
confirm_button = Button(image=confirm_image, highlightthickness=0)
confirm_button.grid(column=1, row=1)



window.mainloop()
