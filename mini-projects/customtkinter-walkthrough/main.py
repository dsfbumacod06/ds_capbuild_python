import customtkinter as ctk  # customtkinter version 5.2.0
from PIL import Image, ImageTk
import tkinter as tk
import images as img

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()

root.title("CustomTkinter Walkthrough")
root.iconphoto(False, tk.PhotoImage(file=img.ROBOT_ICON))
root.geometry("600x350")

def hello():
    mylabel.configure(text=mybutton.cget("text"))


mybutton = ctk.CTkButton(root, 
                         text="Click for a Surprise", 
                         command=hello,
                         height=100,
                         width=200,
                         font=("Helvetica", 24),
                         text_color="yellow",
                         fg_color="yellow",
                         hover_color="blue",
                         corner_radius=50,
                         bg_color="green",
                         border_width=10,
                         border_color="white",
                         state="normal")
mybutton.pack(pady=80)


mylabel = ctk.CTkLabel(root, text="text")
mylabel.pack(pady=20)


root.mainloop()