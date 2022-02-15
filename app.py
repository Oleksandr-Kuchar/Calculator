# import module
import math
from tkinter import * 
from tkinter import font

# create class
class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()

        # edit default font
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Segoe UI", size=18)

        # place for enter numbers
        self.input_field = Entry(font=self.defaultFont, width=16, bd=10, justify="right")
        self.input_field.grid(row=0, columnspan=4)

        # buttons
        self.factorial_button = Button(text="n!", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = self.factorial)
        self.factorial_button.grid(row=1, column=0)

        self.sqrt_button = Button(text="√x", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = self.sqrt)
        self.sqrt_button.grid(row=1, column=1)

        self.sqare_button = Button(text="x²", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = self.square)
        self.sqare_button.grid(row=1, column=2)

        self.clear_button = Button(text="C", width=3, bd=5, foreground="#FF0000", activeforeground="#FF0000", command = self.clear_input)
        self.clear_button.grid(row=1, column=3)

        self.button_7 = Button(text="7", width=3, bd=5, command = lambda: self.input_field.insert("end","7"))
        self.button_7.grid(row=2, column=0)

        self.button_8 = Button(text="8", width=3, bd=5, command = lambda: self.input_field.insert("end","8"))
        self.button_8.grid(row=2, column=1)

        self.button_9 = Button(text="9", width=3, bd=5, command = lambda: self.input_field.insert("end","9"))
        self.button_9.grid(row=2, column=2)

        self.addition_button = Button(text="+", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = lambda: self.input_field.insert("end","+"))
        self.addition_button.grid(row=2, column=3)

        self.button_4 = Button(text="4", width=3, bd=5, command = lambda: self.input_field.insert("end","4"))
        self.button_4.grid(row=3, column=0)

        self.button_5 = Button(text="5", width=3, bd=5, command = lambda: self.input_field.insert("end","5"))
        self.button_5.grid(row=3, column=1)

        self.button_6 = Button(text="6", width=3, bd=5, command = lambda: self.input_field.insert("end","6"))
        self.button_6.grid(row=3, column=2)

        self.subtraction_button = Button(text="-", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = lambda: self.input_field.insert("end","-"))
        self.subtraction_button.grid(row=3, column=3)

        self.button_1 = Button(text="1", width=3, bd=5, command = lambda: self.input_field.insert("end","1"))
        self.button_1.grid(row=4, column=0)

        self.button_2 = Button(text="2", width=3, bd=5, command = lambda: self.input_field.insert("end","2"))
        self.button_2.grid(row=4, column=1)

        self.button_3 = Button(text="3", width=3, bd=5, command = lambda: self.input_field.insert("end","3"))
        self.button_3.grid(row=4, column=2)

        self.division_button = Button(text="/", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = lambda: self.input_field.insert("end","/"))
        self.division_button.grid(row=4, column=3)

        self.button_0 = Button(text="0", width=3, bd=5, command = lambda: self.input_field.insert("end","0"))
        self.button_0.grid(row=5, column=0)

        self.dot_button = Button(text=".", width=3, bd=5, command = lambda: self.input_field.insert("end","."))
        self.dot_button.grid(row=5, column=1)

        self.solution_button = Button(text="=", width=3, bd=5, foreground="#FF0000", activeforeground="#FF0000", command = self.problem_solution)
        self.solution_button.grid(row=5, column=2)

        self.multiplication_button = Button(text="*", width=3, bd=5, foreground="#0000FF", activeforeground="#0000FF", command = lambda: self.input_field.insert("end","*"))
        self.multiplication_button.grid(row=5, column=3)

    # cleared display
    def clear_input(self):
    	self.input_field.delete(0, "end")

    # solution
    def problem_solution(self):
        try:
            self.solution = eval(self.input_field.get())
            self.clear_input()
            self.input_field.insert(0, round(self.solution, 10))
        except ZeroDivisionError:
            self.clear_input()
            self.input_field.insert(0, "division error")
        except SyntaxError:
            self.clear_input()
            self.input_field.insert(0, "wrong value")

    # factorial
    def factorial(self):
        try:
            self.solution = math.factorial(int(self.input_field.get()))
            self.clear_input()
            self.input_field.insert(0, self.solution)
        except ValueError:
            self.clear_input()
            self.input_field.insert(0, "wrong value")

    # sqrt
    def sqrt(self):
        try:
            self.solution = math.sqrt(float(self.input_field.get()))
            self.clear_input()
            self.input_field.insert(0, round(self.solution, 10))
        except ValueError:
            self.clear_input()
            self.input_field.insert(0, "wrong value")

    # number squared
    def square(self):
        try:
            self.solution = float(self.input_field.get())**2
            self.clear_input()
            self.input_field.insert(0, round(self.solution, 10))
        except ValueError:
            self.clear_input()
            self.input_field.insert(0, "wrong value")

# create the application
myapp = App()

myapp.master.title("Calculator")
myapp.master.iconbitmap("calculator.ico")
myapp.master.resizable(False, False)

# start the program
myapp.mainloop()
