import tkinter as tk
from tkinter import messagebox

# Function to check user's mood and provide feedback
def check_mood():
    mood = mood_entry.get().lower()

    if mood == "happy":
        response = "That's great! Keep up the positive vibes! 😊"
    elif mood == "sad":
        response = "Sorry to hear that. Remember, it's okay to feel sad sometimes. 💙"
    elif mood == "stressed":
        response = "Take a deep breath, maybe a break would help. You got this! 💪"
    elif mood == "anxious":
        response = "Anxiety can be tough. Try to focus on things you can control. 💜"
    else:
        response = "Thanks for sharing your feelings. Take care of yourself! 🌸"
    
    messagebox.showinfo("Mood Check-In", response)

# Set up the Tkinter window
root = tk.Tk()
root.title("Mental Health Check-In")

# Create and place the GUI components
prompt_label = tk.Label(root, text="How are you feeling today?")
prompt_label.pack(pady=10)

mood_entry = tk.Entry(root, width=40)
mood_entry.pack(pady=10)

check_button = tk.Button(root, text="Check-In", command=check_mood)
check_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()