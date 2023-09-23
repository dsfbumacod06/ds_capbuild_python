import tkinter as tk
from tkinter import messagebox


class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Force Close", command=exit)
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")
        
        self.action_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.action_menu.add_command(label="Show Message", command=self.show_message)
        self.menu_bar.add_cascade(menu=self.action_menu, label="Action")
        
        self.root.config(menu=self.menu_bar)
        
        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=5, font=("Arial", 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=("Arial", 18), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clearbtn = tk.Button(self.root, text="Clear", font=("Arial", 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get("1.0", tk.END))
    
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
            
    def on_closing(self):
        print("Goodbye World")
        if messagebox.askyesno(title="Quit", message="Do you really want to quit?"):
            self.root.destroy()
            
    def clear(self):
        self.textbox.delete("1.0", tk.END)
        
        
def main():
    MyGui()


if __name__ == "__main__":
    main()