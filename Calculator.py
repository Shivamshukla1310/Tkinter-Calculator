# This project is to create an GUI based calculator

from tkinter import * # this line imports tkinter library
import ast # this is an inbuilt python library basically used for calculation purpose


i = 0
def get_number(num): # this function is to insert the numbers in the display section
  global i 
  display.insert(i,num)
  i += 1

def get_operator(operator): # this i for the operator we are going to add in the display
  global i 
  length = len(operator) # we took length of operator because as digit they only have 1 space whereas some operator consume more then one space such as ** or *3.14 etc
  display.insert(i,operator)
  i += length
  
def clear_all(): # this is for all clear function 
  display.delete(0,END)
  
  
def calculate(): # this is to calculate the input passed by the user
  entire_String = display.get() # first we take the entrie string into this variable
  try: # just in case any exception occur such as zero division
    node = ast.parse(entire_String,mode="eval") # we are storing the entire string into parsing of ast module 
    result = eval(compile(node,'string','eval')) # here we get the answer in the result 
    clear_all() # we clear the input from the user
    display.insert(0,result) # and then display the output in the form of result
  except Exception as e:
    clear_all()
    display.insert(0, "Error")
    print("Error:", e)  # Print the exact error for debugging

    
def undo(): # this function is just to undo the input user has entered well user can directly click on display and backspace it but this will help to look like real calculator
  entire_string = display.get()
  if len(entire_string):
    new_string = entire_string[:-1] # taking of the last value by using string slicing
    clear_all()
    display.insert(0,new_string) # after clearing the entire string again the new string is displayed 
  else:
    clear_all()
    display.insert(0,"")

root = Tk() # this creates an object to use tkinter library
root.title("Colorful GUI Calculator")
root.configure(bg="#1e1e2f")  # Dark background

font_style = ("Arial", 14)

display = Entry(root, font=font_style, bg="#f8f8f8", fg="black", bd=8, relief=RIDGE, justify="right")
display.grid(row=1, columnspan=6, ipadx=8, ipady=8, padx=10, pady=10)  # this will display the entry in 2nd row and will cover 6 column 

# Colors for different button types
number_bg = "#4caf50"       # Green
operator_bg = "#2196f3"     # Blue
control_bg = "#f44336"      # Red
equal_bg = "#ff9800"        # Orange

# To create the buttons for numbers
# with the help of for loop and this list we can not only create multiple buttons but also we can access each index of the list and use them as an input to the display section.
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0
for x in range(3):
  for y in range(3):
    button_text = numbers[counter]
    button = Button(root, text=button_text, font=font_style, bg=number_bg, fg="white", height=2, width=4, bd=4,command=lambda text=button_text: get_number(text)) # lambda text=button_text: stores the current loop value (avoids late binding bug).This way, each button behaves correctly when clicked.
    button.grid(row=x+2,column=y,padx=3, pady=3)
    counter+=1
    
button = Button(root, text="0", font=font_style, bg=number_bg, fg="white", height=2, width=4, bd=4,command=lambda :get_number(0))
button.grid(row=5,column=1, padx=3, pady=3)

# To create the buttons for operators
count = 0
operations = ["+","-","*","/","*3.14","%","(","**",")","**2","."]
for x in range(4):
  for y in range(3):
    if count < len(operations):
      button = Button(root, text=operations[count], font=font_style, bg=operator_bg, fg="white", height=2, width=4, bd=4,command=lambda text=operations[count]: get_operator(text))
      count += 1
      button.grid(row=x + 2,column=y+3, padx=3, pady=3)

# Control buttons for all clear, equals and backspace
Button(root, text="AC", font=font_style, bg=control_bg, fg="white", height=2, width=4, bd=4,command=clear_all).grid(row=5, column=0, padx=3, pady=3)

Button(root, text="=", font=font_style, bg=equal_bg, fg="white", height=2, width=4, bd=4, command=calculate).grid(row=5, column=2, padx=3, pady=3)

Button(root, text="<-", font=font_style, bg=control_bg, fg="white", height=2, width=4, bd=4, command=undo).grid(row=5, column=5, padx=3, pady=3)

display.bind("<Return>", lambda event: calculate())
display.bind("<BackSpace>", lambda event: undo())

root.mainloop()