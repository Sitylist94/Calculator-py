import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x600")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        
        # Set the icon and background color
        self.window.iconbitmap("Calculator_icon.svg")  # Path to your .ico file
        self.window.configure(bg="#2E2E2E")  # Set the main window background color
        
        self._create_display()  # Add the display
        self._create_buttons()  # Add buttons

    def _create_display(self):
        # Create an entry widget for the display
        self.display = tk.Entry(
            self.window,
            font=("Arial", 24),
            borderwidth=2,
            relief="flat",
            justify="right",
            bg="#3C3C3C",  # Background color of the display
            fg="#FFFFFF"   # Text color of the display
        )
        self.display.pack(expand=True, fill="both", pady=10)

    def _create_buttons(self):
        # Frame to hold the buttons
        btn_frame = tk.Frame(self.window, bg="#2E2E2E")  # Button frame background color
        btn_frame.pack(expand=True, fill="both")

        # Buttons configuration
        buttons = [
            ("C", 1, 0), ("CE", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("", 5, 3),
        ]

        for (text, row, col) in buttons:
            if text:
                btn = tk.Button(
                    btn_frame,
                    text=text,
                    font=("Arial", 18),
                    borderwidth=0,
                    fg="#FFFFFF",  # Button text color
                    bg="#3C3C3C",  # Button background color
                    activebackground="#505050",  # Button active background
                    activeforeground="#FFFFFF",  # Button active text color
                    command=lambda t=text: self._on_button_click(t),
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Configure grid rows and columns
        for i in range(6):
            btn_frame.rowconfigure(i, weight=1)
        for i in range(4):
            btn_frame.columnconfigure(i, weight=1)

    def _on_button_click(self, value):
        if value == "C":
            self.display.delete(0, tk.END)
        elif value == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, value)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
