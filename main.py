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
    """ Do JSON tworzymy nowy słownik, który dla każdego klucza-website, będzie miał sam w sobie kolejny słownik, 
    z kluczami, email: username i password-password"""
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Puste pole.", message="Uzupełnij puste pola.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"Poniżej znajdują się wprowadzone szczegóły:"
                                                                   f" \nStrona: {website}\nLogin/Nazwa: {username}"
                                                                   f"\nHasło: {password}\nZapisać?")
        if is_ok:
            # with open("list_of_passwords", "a") as passwords:
            # passwords.write(f"\n{website} | {username} | {password}")
            # Aby zapisywać plik w formacie data, wystrczy go wywołac jak klasyczny tekstowy
            # with open("data_json", "w") as passwords:
                # JSON wymaga również, aby pliki zapisywać za pomocą swoich szczególnych method(wcześniej zaimportować)
                # Dane będą zapisywane w formie słownika (1.input - słownik, 2. input - plik, który chcemy stworzyć)
                # Aby takie dane łatwiej było czytać, możemy zastosować parametr wcięcia -wtedy będzie jak słownik
                # json.dump(new_data, passwords, indent=4)

                # Jak czytać pliki z JSON - load(tu podajemy plik, który chcemy czytać) a w open() zmieniamy na "r"
                # data = json.load(passwords)
                # print(data) - typ danych będzie dict
            with open("data_json", "r") as passwords:
                # Jak aktualizować plik? Po pierwsze trzeba załadować plik
                data = json.load(passwords)
                # Gdy plik jest załadowany, aktualizujemy go za pomocą nowych danych - new_data
                data.update(new_data)
            # Otwieramy plik ale w opcji "w"-write, aby dump-wsypać do niego dane, które zaktualizowaliśmy powyżej-update()
            with open("data_json", "w") as passwords:
                # Na koniec musimy zapisać ten plik za pomocą dump() - dlatego tu będzie tylko "data"
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

# columnspan = - określa, ile kolumn ma zajmować jakaś rzecz( przy użyciu grid())

# ---- Webiste ---- #
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
# Sprawia że po odpaleniu okna, pojawia się tam kursor
website_entry.focus()

# ---- Email/username ---- #
username_label = Label(text="Email/username:", font=FONT)
username_label.grid(column=0, row=2)
username_entry = Entry(width=38)
username_entry.grid(column=1, row=2, columnspan=2)
# Ustawia domyślnie wyświetlanie tekstu
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
