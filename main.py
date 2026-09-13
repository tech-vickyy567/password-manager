from customtkinter import *
import json
import os

#Created a label creator to avoid hard coding
def label_creator(window, text, fgcolor, cornerradius, font, x, y, **kwargs):
    CTkLabel(
        window,
        text= text,
        fg_color= fgcolor,
        corner_radius= cornerradius,
        font= font
    ).place(
        x= x,
        y= y
    )

DATA_FILE = "data.json"

#Loading the data to the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
    
#Saving the data to the JSON file
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(datas, f, indent= 4)

window = CTk()
window.title("Password Manager")
window.geometry("500x500")

datas = load_data()

#Adding a custom function to add the data
def add_data():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if not website or not email or not password:
        return 

    data = {
        "Website": website,
        "Email": email,
        "Password": password
    }

    datas.append(data)
    save_data()
    custom_height = 300 + len(datas)*100
    window.geometry(f"500x{custom_height}")
    create_data(data["Website"], data["Email"], data["Password"], len(datas) - 1)

    web_entry.delete(0, END)
    email_entry.delete(0, END)
    pass_entry.delete(0, END)

#Adding a custom function to create data
def create_data(website, email, password, i):
    frame = CTkFrame(
       window,
       bg_color= "white" 
    )
    frame.place(
        x= 75,
        y= 300 + i*100
    )

    CTkLabel(
        frame,
        text= f"Website/App: {website}, \nEmail/Username: {email}, \nPassword: {password}",
        font= ("Arial", 20) 
    ).pack(anchor= "e")

app_label = label_creator(window, "Password Manager", "black", 10, ("Arial", 40, "bold"), 55, 10)

web_label = label_creator(window, "Website/App Name", "black", 10, ("Arial", 18, "bold"), 20, 100)

web_entry = CTkEntry(
    window,
    width= 250,
    height= 30,
    placeholder_text= "Enter Website/App Name"
)
web_entry.place(
    x= 200,
    y= 100
)

email_label = label_creator(window, "Email/Username", "black", 10, ("Arial", 20, "bold"), 20, 150)

email_entry = CTkEntry(
    window,
    width= 250,
    height= 30,
    placeholder_text= "Enter Email/Username"
)
email_entry.place(
    x= 200,
    y= 150
)

pass_label = label_creator(window, "Password", "black", 10, ("Arial", 20, "bold"), 20, 200)

pass_entry = CTkEntry(
    window,
    width= 250,
    height= 30,
    placeholder_text= "Enter Password"
)
pass_entry.configure(show="*")  # This will hide the password input
pass_entry.place(
    x= 200,
    y= 200
)

gen_pass_button = CTkButton(
    window,
    text= "Generate Password",
    corner_radius= 10,
    font= ("Arial", 15, "bold")
)
gen_pass_button.place(
    x= 80,
    y= 250
)

save_button = CTkButton(
    window,
    text= "Save",
    corner_radius= 10,
    font= ("Arial", 15, "bold"),
    command= add_data
)
save_button.place(
    x= 250,
    y= 250
)

for i, j in enumerate(datas):
    create_data(
        j["Website"],
        j["Email"],
        j["Password"],
        i
    )

window.mainloop()