import tkinter as tk
from math import sqrt, pow, sin, cos, tan, radians

# Main application class
class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        
        # Entry field for the calculator
        self.entry = tk.Entry(master, width=20, font=('Arial', 14), bd=4, insertwidth=4, bg="powder blue", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, pady=1)
        self.entry.focus_set()  # Sets focus on the input text area
        
        # Button layout
        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'pow',
            '1', '2', '3', '-', 'sin',
            '0', '.', '=', '+', 'cos',
            'C', '(', ')', 'tan', 'pi'
        ]
        i = 0
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            i += 1
            col_val += 1
            if i % 5 == 0:
                row_val += 1
                col_val = 0
    
    # Function to create buttons
    def create_button(self, val, row, col):
        if val == '=':
            btn = tk.Button(self.master, text=val, width=5, height=2, bd=4, command=lambda: self.calculate())
        elif val == 'C':
            btn = tk.Button(self.master, text=val, width=5, height=2, bd=4, command=lambda: self.clear())
        elif val in ['sqrt', 'pow', 'sin', 'cos', 'tan', 'pi']:
            btn = tk.Button(self.master, text=val, width=5, height=2, bd=4, command=lambda: self.special_function(val))
        else:
            btn = tk.Button(self.master, text=val, width=5, height=2, bd=4, command=lambda: self.entry.insert(tk.END, val))
        
        btn.grid(row=row, column=col, sticky='nsew')
    
    # Function to clear the entry field
    def clear(self):
        self.entry.delete(0, tk.END)
    
    # Function to calculate the result
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.clear()
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.clear()
            self.entry.insert(tk.END, 'Error')
    
    # Function for special operations like sqrt, pow, etc.
    def special_function(self, operator):
        if operator == 'sqrt':
            value = sqrt(float(self.entry.get()))
        elif operator == 'pow':
            value = pow(float(self.entry.get()), 2)
        elif operator == 'sin':
            value = sin(radians(float(self.entry.get())))
        elif operator == 'cos':
            value = cos(radians(float(self.entry.get())))
        elif operator == 'tan':
            value = tan(radians(float(self.entry.get())))
        elif operator == 'pi':
            value = 3.141592653589793
        self.clear()
        self.entry.insert(tk.END, str(value))

# Main function
def main():
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

if __name__ == '__main__':
    main()
