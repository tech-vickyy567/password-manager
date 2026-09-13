from customtkinter import *

window = CTk()
window.title("Password Manager")
window.geometry("500x500")

app_label = CTkLabel(
    window,
    text= "Password Manager",
    fg_color= "black",
    corner_radius= 10,
    font= ("Arial", 40, "bold")
)
app_label.place(
    x= 55,
    y= 10
)

web_label = CTkLabel(
    window,
    text= "Website/App",
    fg_color= "black",
    corner_radius= 10,
    font= ("Arial", 20, "bold")
)
web_label.place(
    x= 20,
    y= 100
)

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

email_label = CTkLabel(
    window,
    text= "Email/Username",
    fg_color= "black",
    corner_radius= 10,
    font= ("Arial", 20, "bold")
)
email_label.place(
    x= 20,
    y= 150
)

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

pass_label = CTkLabel(
    window,
    text= "Password",
    fg_color= "black",
    corner_radius= 10,
    font= ("Arial", 20, "bold")
)
pass_label.place(
    x= 20,
    y= 200
)

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