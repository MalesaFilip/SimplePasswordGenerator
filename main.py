from tkinter import messagebox
from tkinter import *
import json

FONT = ("Ariel", 12, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = "abcdefghijklmnoprstuwxyz"
big_letters = "ABCDEFGHIJKLMNOPRSTUWXYZ"
numbers = "1234567890"
characters = "!@#$%^&*(){}><"

summary = letters + big_letters + numbers + characters
length = 10
random_password = "".join(random.sample(summary, length))


def generate_password():
    password_entry.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    """We create a new dictionary for JSON, which for each key-website will have another dictionary in itself,
     with keys, email: username and password-password"""
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Empty fields.", message="Complete the empty fields."
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Below are the entered details:"
                                                                   f" \nWebsite: {website}\nLogin/Name: {username}"
                                                                   f"\nPassword: {password}\nSave it??")
        if is_ok:
            with open("data_json", "r") as passwords:
                # First you need to upload the file
                data = json.load(passwords)
                # When the file is loaded, we update it with new data - new_data
                data.update(new_data)
            # We open the file but in the "w"-write option to put into it the data that we updated above-update()
            with open("data_json", "w") as passwords:
                # Finally, we need to save this file with dump() - so there will only be "date" here
                json.dump(data, passwords, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)


# ---- Webiste ---- #
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
# Makes the cursor appear there after launching the window
website_entry.focus()

# ---- Email/username ---- #
username_label = Label(text="Email/username:", font=FONT)
username_label.grid(column=0, row=2)
username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
# Sets text display by default
username_entry.insert(0, "here you can provide your email to start with")

# ---- Password ---- #
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)
password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", font=FONT, width=15, command=generate_password)
password_button.grid(column=2, row=3)

# --- Add button --- #
add_button = Button(text="Add", width=28, font=("Arial", 10, "bold"), command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
