import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root, width=20, font=('Arial', 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 20))
            button.grid(row=row, column=col, padx=5, pady=5)
            button.config(command=lambda t=text: self.on_button_click(t))

        # Style configuration
        self.configure_styles()

    def configure_styles(self):
        self.root.configure(bg='#EAEAEA')  # Background color
        self.entry.configure(bg='white')   # Entry field color

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg='#E0E0E0', activebackground='#D0D0D0', fg='black', font=('Arial', 20))  # Button colors

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
