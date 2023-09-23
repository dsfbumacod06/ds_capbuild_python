import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
root.geometry("600x400")
root.title("Annyeonghaseyo")
ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")
root.resizable(width=False, height=True)

top_frame = ctk.CTkFrame(master=root, fg_color="black")
bottom_frame = ctk.CTkFrame(master=root, fg_color="pink")
top_frame.pack(side="top",fill="both", expand=True)
bottom_frame.pack(side="top",fill="both", expand=True)


# frame1 = ctk.CTkFrame(master=root, fg_color="blue")
# frame1.pack()
# frame2 = ctk.CTkFrame(master=root, fg_color="green")
# frame2.pack()
# frame3 = ctk.CTkFrame(master=root, fg_color="orange")
# frame3.pack()
# frame4 = ctk.CTkFrame(master=root, fg_color="black")
# frame4.pack()


root.mainloop()