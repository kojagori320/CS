import tkinter as tk
from datetime import datetime

# Function to calculate and display the year of birth [MAIN CODE]
def calculate_birth_year():
    try:
        # Get the age from the entry widget
        age = int(entry.get())  # Convert the input to an integer
        
        # Get the current year
        current_year = datetime.now().year
        
        # Calculate the year of birth
        birth_year = current_year - age
        
        # Update the result label with the year of birth
        result_label.config(text=f"You were born in: {birth_year}")
    except ValueError:
        # Handle non-integer inputs
        result_label.config(text="Please enter a valid age.")

#Adding animation on hovering over the button
def on_enter(e):
    button['background']='lightgreen'

#Adding animation on leaving the button
def on_leave(e):
    button['background']='SystemButtonFace'

#Create the main window
root=tk.Tk()
root.title('MY FIRST GUI APP')
root.geometry('600x400')

#Adding a label widget
label=tk.Label(root,text="Enter your age:",width=20,height=2,font=("Trebuchet MS", 14))
label.pack()

#Adding text or entry widgets
entry=tk.Entry(root,width=20)
entry.pack()

#Adding a button
button=tk.Button(root,text='CLICK ME',font=("Trebuchet MS", 14),bg='lightgray',command=calculate_birth_year)
button.pack(pady=20)
button.bind('<Enter>',on_enter)
button.bind('<Leave>',on_leave)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Trebuchet MS", 14))
result_label.pack(pady=20)

#Starting the GUI event loop
root.mainloop()