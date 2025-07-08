import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_btn():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {website:
                    { "email" : email,
                      "password":password,}
                }

    if website == "" or password == "":
        messagebox.showinfo(title="Empty fields", message="Please fill in all the fields")
    else:
        try:
            with open("password_data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("password_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = website_entry.get()
    try:
        with open("password_data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data File Found",message="There isn't any entry")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Details", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="No details", message=f"There is no details for {website}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100,image = image)
canvas.grid(column=1,row=0)



website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry()
website_entry.grid(row=1,column=1,sticky="EW")
website_entry.focus()

search_btn = Button(text="Search",command=search)
search_btn.grid(row=1,column=2,sticky="EW")

email_user_entry = Entry()
email_user_entry.grid(row=2,column=1,columnspan=2,sticky="EW")
email_user_entry.insert(0,"example@gmail.com")

password_entry = Entry()
password_entry.grid(row=3,column=1,sticky="EW")

gen_pass_btn = Button(text="Generate Password",command=generate_password)
gen_pass_btn.grid(row=3,column=2, sticky="EW")


add_button = Button(text="Add",width=36,command=add_btn)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")











window.mainloop()