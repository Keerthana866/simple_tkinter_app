import tkinter as tk

root = tk.Tk()
root.title("sample tkinter app")
root.geometry("300x200")

def hello():
    print("Hello World!")
    print("Good Bye!")
    
hello_button = tk.Button(root, text="Hello", command=hello)
hello_button.pack(pady=20)



import random 

def genrate_pass():
    password = random.randint(100000, 999999)
    print(password)
    
pass_button = tk.Button(root, text="Generate Password", command=genrate_pass)
pass_button.pack(pady=20)

def greet():
    name = tk.StringVar()
    name_entry = tk.Entry(root, textvariable=name)
    name_entry = name.get()
    print(f"Hello {name_entry}")

root.mainloop()