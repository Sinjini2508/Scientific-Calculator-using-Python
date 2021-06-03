import tkinter
import math
from math import asin, acos, atan, sin, cos, tan, log, pi, exp, sqrt, factorial

window = tkinter.Tk()
window.title("Scientific Calculator")
window.wm_iconbitmap('C:\\Users\\Sinjini\\Downloads\\3700465-business-calculating-calculator-finance-maths-technological_108748.ico')

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression + " ")

def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)

def btn_equal():
    global expression
    new_expression = ""
    # For PI
    if ("π" in expression):
        for i in range(len(expression)):
            if (expression[i] == "π"):
                new_expression += str(pi)
            else:
                new_expression += expression[i]
        expression = new_expression

    # For e
    if ("e" in expression):
        for i in range(len(expression)):
            if (expression[i] == "e"):
                new_expression += str(math.exp(1))
            else:
                new_expression += expression[i]
        expression = new_expression

    # For power function
    if ("^" in expression):
        for i in range(len(expression)):
            if (expression[i] == "^"):
                expression = expression.replace("^", "**")

    code = compile(expression, "<string>", "eval")
    expression = str(eval(code))
    input_text.set(expression)


expression = ""
input_text = tkinter.StringVar()
input_frame = tkinter.Frame(window, width=312, height=100, bd=0)
input_frame.pack(side=tkinter.TOP)

input_field = tkinter.Entry(input_frame, font=("courier new",30, "bold"), textvariable=input_text)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = tkinter.Frame(window, width=312, height=250, bg="black")
btns_frame.pack(expand = False)

numbers_font = ("helvetica", 15,"bold")
operations_font = ("courier new", 15, "bold")

clear = tkinter.Button(btns_frame, text="C", bd=0, command=btn_clear,bg = "light steel blue",  height=5, width=22, font = operations_font)
clear.grid(row=1, column=0, columnspan=2, padx=1, pady=1, sticky='nesw')

back = tkinter.Button(btns_frame, text="Backspace", command=lambda:backspace(), bg="light steel blue", height=5, width=10, font=operations_font)
back.grid(row=1, column=2, padx=1, pady=1, sticky='nesw')

sine = tkinter.Button(btns_frame, text="sin", command=lambda:btn_click("sin("), bg="plum3",height=5, width=10, font=operations_font)
sine.grid(row=1, column=3, padx=1, pady=1, sticky="nesw")

cosine = tkinter.Button(btns_frame, text="cos", command=lambda:btn_click("cos("), bg="plum3", height=5, width=10, font=operations_font)
cosine.grid(row=1, column=4, padx=1, pady=1, sticky="nesw")

tangent = tkinter.Button(btns_frame, text="tan", command=lambda:btn_click("tan("), bg="plum3", height=5, width=10, font=operations_font)
tangent.grid(row=1, column=5, padx=1, pady=1, sticky="nesw")

div =tkinter.Button(btns_frame, text="/", command=lambda:btn_click("/"),bg="LightPink1", height=5, width=10, font=operations_font)
div.grid(row=1, column=6, padx=1, pady=1, sticky="nesw")

logarithm = tkinter.Button(btns_frame, text="log", command=lambda:btn_click("log("), bg="light pink", height=5, width=10, font=operations_font)
logarithm.grid(row=2, column=0, padx=1, pady=1, sticky="nesw")

euler_number = tkinter.Button(btns_frame, text="e", command=lambda:btn_click("e"),bg="light goldenrod", height=5, width=10, font=operations_font)
euler_number.grid(row=2, column=1, padx=1, pady=1, sticky="nesw")

power = tkinter.Button(btns_frame, text="^", command=lambda:btn_click("^"),bg="light pink", height=5, width=10, font=operations_font)
power.grid(row=2, column=2, padx=1, pady=1, sticky="nesw")

one = tkinter.Button(btns_frame, text="1", command=lambda:btn_click("1"), bg="orchid3", height=5, width=10, font=numbers_font)
one.grid(row=2, column=3, padx=1, pady=1, sticky="nesw")

two = tkinter.Button(btns_frame, text = "2", command=lambda:btn_click("2"), bg="orchid3", height=5, width=10, font=numbers_font)
two.grid(row =2, column=4, padx=1, pady=1, sticky="nesw")

three = tkinter.Button(btns_frame, text="3", command=lambda:btn_click("3"), bg="orchid3", height=5, width=10, font=numbers_font)
three.grid(row=2, column= 5, padx=1, pady=1, sticky="nesw")

plus = tkinter.Button(btns_frame, text="+", command=lambda:btn_click("+"), bg="LightPink1", height=5, width=10, font=operations_font)
plus.grid(row=2, column=6, padx=1, pady=1, sticky="nesw")

absolute_value = tkinter.Button(btns_frame, text="|x|", command=lambda:btn_click("abs("), bg="light pink", height=5, width=10, font=operations_font)
absolute_value.grid(row=3, column=0, padx=1, pady=1, sticky="nesw")

factorial_button = tkinter.Button(btns_frame, text="!", command=lambda:btn_click("factorial("), bg="light pink", height=5, width=10, font=operations_font)
factorial_button.grid(row=3, column=1, padx=1, pady=1, sticky="nesw")

square_root = tkinter.Button(btns_frame, text="√", command=lambda:btn_click("sqrt("), bg="light pink", height=5, width=10, font=operations_font)
square_root.grid(row=3, column=2, padx=1, pady=1, sticky="nesw")

four = tkinter.Button(btns_frame, text="4", command=lambda:btn_click("4"), height=5, bg="orchid3", width=10, font=numbers_font)
four.grid(row=3, column=3, padx=1, pady=1, sticky="nesw")

five = tkinter.Button(btns_frame, text="5", command=lambda:btn_click("5"), bg="orchid3", height=5, width=10, font=numbers_font)
five.grid(row=3, column=4, padx=1, pady=1, sticky="nesw")

six = tkinter.Button(btns_frame, text="6", command=lambda:btn_click("6"), bg="orchid3", height=5, width=10, font=numbers_font)
six.grid(row=3, column=5, padx=1, pady=1, sticky="nesw")

minus = tkinter.Button(btns_frame, text="-", command=lambda:btn_click("-"),bg="LightPink1", height=5, width=10, font=operations_font)
minus.grid(row=3, column=6, padx=1, pady=1, sticky="nesw")

pie = tkinter.Button(btns_frame, text="π", command=lambda:btn_click("π"), bg="light goldenrod", height=5, width=10, font=numbers_font)
pie.grid(row=4, column=0, padx=1, pady=1, sticky="nesw")

opening_parenthesis = tkinter.Button(btns_frame, text="(", command=lambda:btn_click("("), bg="LightPink1", height=5, width=10, font=operations_font)
opening_parenthesis.grid(row=4, column=1, padx=1, pady=1, sticky="nesw")

closing_parenthesis = tkinter.Button(btns_frame, text=")", command=lambda:btn_click(")"), bg="LightPink1", height=5, width=10, font=operations_font)
closing_parenthesis.grid(row=4, column=2, padx=1, pady=1, sticky="nesw")

seven = tkinter.Button(btns_frame, text="7", command=lambda:btn_click("7"), bg="orchid3", height=5, width=10, font=numbers_font)
seven.grid(row=4, column=3, padx=1,pady=1, sticky="nesw")

eight = tkinter.Button(btns_frame, text="8", command=lambda:btn_click("8"), bg="orchid3", height=5, width=10, font=numbers_font)
eight.grid(row=4, column=4, padx=1, pady=1, sticky="nesw")

nine = tkinter.Button(btns_frame, text="9", command=lambda:btn_click("9"), bg="orchid3", height=5, width=10, font=numbers_font)
nine.grid(row=4, column=5, padx=1, pady=1, sticky="nesw")

multiplication = tkinter.Button(btns_frame, text="*", command=lambda:btn_click("*"),bg="LightPink1", height=5, width=10, font=operations_font)
multiplication.grid(row=4, column=6, padx=1, pady=1, sticky="nesw")

modulus = tkinter.Button(btns_frame, text="%", command=lambda:btn_click("%"), bg="LightPink1", height=5, width=10, font=operations_font)
modulus.grid(row=5, column=3, padx=1, pady=1, sticky="nesw")

decimal_point = tkinter.Button(btns_frame, text=".", command=lambda:btn_click("."),bg="LightPink1", height=5, width=10, font=operations_font)
decimal_point.grid(row=5, column=4, padx=1, pady=1, sticky="nesw")

sin_inverse = tkinter.Button(btns_frame, text="asin ", command=lambda:btn_click("asin("), bg="plum3", height=5, width=10, font=operations_font)
sin_inverse.grid(row=5, column=0, padx=1, pady=1, sticky="nesw")

cos_inverse = tkinter.Button(btns_frame, text="acos", command=lambda:btn_click("acos("), bg="plum3", height=5, width=10, font=operations_font)
cos_inverse.grid(row=5, column=1, padx=1, pady=1, sticky="nesw")

tan_inverse = tkinter.Button(btns_frame, text="atan", command=lambda:btn_click("atan("), bg="plum3", height=5, width=10, font=operations_font)
tan_inverse.grid(row=5, column=2, padx=1, pady=1, sticky="nesw")

zero = tkinter.Button(btns_frame, text="0", command=lambda:btn_click("0"), bg="orchid3", height=5, width=10, font=numbers_font)
zero.grid(row=5, column=5, padx=1, pady=1, sticky="nesw")

equal_to = tkinter.Button(btns_frame, text="=", command=btn_equal, bg="light steel blue", height=5, width=10, font=operations_font)
equal_to.grid(row=5, column=6, padx=1, pady=1, sticky="nesw")

window.mainloop()