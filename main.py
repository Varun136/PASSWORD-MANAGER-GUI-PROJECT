import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import json

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(5,6)
    nr_symbols = random.randint(3,7)
    nr_numbers = random.randint(5,8)

    password=[]

    for n in range(1,nr_letters+1):
        password.append(random.choice(letters))
    for n in range(1,nr_symbols+1):
        password.append(random.choice(symbols))
    for n in range(1,nr_numbers+1):
        password.append(random.choice(numbers))
    random.shuffle(password)
    PASSWORD = ''
    for n in password:
        PASSWORD +=n
    password_entry.insert(0,PASSWORD)

def save():
    web=website_entry.get().title()
    mail=email_entry.get().title()
    password=password_entry.get().title()
    new_data={
        web:{"email":mail,"password":password}
    }
    if len(web) == 0 or len(password) == 0 or len(mail) == 0:
        messagebox.showwarning(title="Warning", message="Oops,Make sure your haven't left any field empty")
    else:
        try:
            with open("json_data.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
                with open("json_data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
        except:
            with open("json_data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        messagebox.showinfo(title="READY TO SAVE", message=f"{web}|{mail}|{password}")

def search():
    web = website_entry.get()
    try:
        with open("json_data.json", mode="r") as file:
            data = json.load(file)
    except:
        messagebox.showerror(title="Warning",message="Sorry no information loaded")
    if web in data:
        mail=data[web]["email"]
        password=data[web]["password"]
        messagebox.showinfo(title="Got it",message=f"Mail:{mail}\nPassword:{password}")
    else:
        messagebox.showinfo(title="Not avilable", message=f"Sorry {web} does not match with any")



def exit():
    msg = messagebox.askokcancel(title="WARNING", message="ARE YOU SURE YOU WANT TO EXIT?")
    if msg == True:
        windows.destroy()


windows=Tk()
windows.title("PASSWORD MANAGER")
windows.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
image = Image.open("Lock.png")
resize_image = image.resize((200, 200))
img = ImageTk.PhotoImage(resize_image)
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1,columnspan=2)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0,pady=5)
website_entry=Entry(width=26)
website_entry.grid(row=1,column=1,pady=5)
website_entry.focus()
search_button=Button(text="Search",width=16,command=search)
search_button.grid(row=1,column=2,padx=5)

email_label=Label(text="Email/User_id:")
email_label.grid(row=2,column=0,pady=5)
email_entry=Entry(width=46)
email_entry.grid(row=2,column=1,columnspan=2,pady=5)
email_entry.insert(0,"user123@gmail.com")

password_label=Label(text="Password:")
password_label.grid(row=3,column=0,pady=5)
password_entry=Entry(width=26)
password_entry.grid(row=3,column=1,pady=5)
password_button=Button(text="Generate Password",command=generate)
password_button.grid(row=3,column=2,columnspan=2,pady=5)

add_button=Button(text="Add",width=23,command=save)
add_button.grid(row=4,column=1,columnspan=1,pady=5)

exit_button=Button(text="Exit",width=16,command=exit)
exit_button.grid(row=4,column=2,pady=5)
windows.mainloop()
