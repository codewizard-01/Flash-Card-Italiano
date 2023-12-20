from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/italian.csv")
to_read = data.to_dict(orient="records")
current_card = random.choice(to_read)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_read)
    canvas.itemconfig(title_text, text="Italian", fill="black")
    canvas.itemconfig(word_text, text=current_card["Italiano"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_time = window.after(3000, func=flip_card)


def is_known():
    to_read.remove(current_card)
    data = pandas.DataFrame(to_read)
    data.to_csv("data/words_to_learn.csv")
    next_card()



window = Tk()
window.title("Flash Brain")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Italian", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=current_card["Italiano"], font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, command=next_card)
unknown_button.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, command=is_known)
known_button.grid(column=1, row=1)


window.mainloop()