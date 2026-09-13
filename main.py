from customtkinter import *

def label_creator(window, text, fgcolor, cornerradius, font, x, y):
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

window = CTk()
window.title("Password Manager")
window.geometry("500x500")

app_label = label_creator(window, "Password Manager", "black", 10, ("Arial", 40, "bold"), 55, 10)

web_label = label_creator(window, "Website/App Name", "black", 10, ("Arial", 20, "bold"), 20, 100)

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
    font= ("Arial", 15, "bold")
)
save_button.place(
    x= 250,
    y= 250
)

window.mainloop()