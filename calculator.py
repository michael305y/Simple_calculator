"""
A simple calculator in python using Tkinter
"""

import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.configure(background='white')
        self.root.geometry("480x568+450+90")

        self.current = ''
        self.total = 0
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

        self.create_ui()

    def create_ui(self):
        self.entry = tk.Entry(self.root, font=('Helvetica', 20, 'bold'), bg='black', fg='white', bd=30, width=28, justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, pady=1)
        self.entry.insert(0, "0")

        button_grid = [
            "",
            "789x",
            "456-",
            "123+",
            "0."
        ]

        row, col = 1, 4
        for row_data in button_grid:
            for char in row_data:
                btn = self.create_button(char, row, col)
                col += 1
            row += 1
            col = 0

        special_buttons = [
            ("C", 1, 0, self.clear_entry),
            ("CE",1, 1, self.all_clear_entry),
            ("√", 1, 2, self.square_root),
            ("+", 1, 6, lambda: self.operation("add")),
            ("-", 2, 5, lambda: self.operation("sub")),
            ("*", 2, 3, lambda: self.operation("multi")),
            ("/", 1, 3, lambda: self.operation("divide")),
            ("=", 5, 3, self.sum_of_total),
        ]

        for label, r, c, command in special_buttons:
            self.create_button(label, r, c, command)
            

        scientific_functions = [
            ("pi", self.pi),
            ("e", self.e),
            ("+/-", self.math_pm),
            ("sin", self.sin),
            ("cos", self.cos),
            ("tan", self.tan),
            ("sinh", self.sinh),
            ("cosh", self.cosh),
            ("tanh", self.tanh),
            ("log", self.log),
            ("exp", self.exp),
        ]

        row, col = 1, 4
        for label, func in scientific_functions:
            self.create_button(label, row, col, func)
            if col == 7:
                col = 4
                row += 1
            else:
                col += 1

    def create_button(self, text, row, column, command=None):
        btn = tk.Button(self.root, text=text, width=6, height=2, bg='powder blue', font=('Helvetica', 20, 'bold'), bd=4,
                        command=command if command else lambda t=text: self.number_enter(t))
        btn.grid(row=row, column=column, pady=1)
        return btn

    def number_enter(self, num):
        if self.result:
            self.current = ''
            self.result = False

        if self.input_value:
            self.current = num
            self.input_value = False
        else:
            self.current += str(num)

        self.display(self.current)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = True


    def valid_function(self):
        if self.op == "add":
            self.total += float(self.current)
        if self.op == "sub":
            self.total -= float(self.current)
        if self.op == "multi":
            self.total *= float(self.current)
        if self.op == "divide":
            self.total /= float(self.current)
        self.input_value = True
        self.check_sum = True
        self.display(self.total)

    # def sum_of_total(self):
    #     self.result = True
    #     self.current = float(self.current)
    #     # self.current = (self.current)
    #     if self.check_sum:
    #         self.valid_function()
    #     else:
    #         self.total = float(self.entry.get())
    #         # self.total = (self.entry.get())
    #     self.display(self.total)

    # gets the total by eval() method
    def sum_of_total(self):
        self.result = True
        try:
            result = eval(self.current)  # Evaluate the expression
            self.current = str(result)  # Convert the result to a string
            self.total = result
            self.display(self.current)
        except Exception as error:
            self.display(error)
            self.current = "Error"  # Handle the case where the expression is invalid
            self.total = 0
            self.display(self.current)


    def display(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def math_pm(self):
        self.result = False
        self.current = -float(self.entry.get())
        self.display(self.current)

    def square_root(self):
        self.result = False
        self.current = math.sqrt(float(self.entry.get()))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(self.entry.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(self.entry.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(self.entry.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(self.entry.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(self.entry.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(self.entry.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(self.entry.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(self.entry.get()))
        self.display(self.current)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()