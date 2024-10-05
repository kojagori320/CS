import tkinter as tk
from tkinter import messagebox

def open_request_form():
    request_window = tk.Toplevel(root)
    request_window.title("Request Form")
    
    tk.Label(request_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(request_window)
    name_entry.pack(pady=5)

    tk.Label(request_window, text="Email:").pack(pady=5)
    email_entry = tk.Entry(request_window)
    email_entry.pack(pady=5)

    tk.Label(request_window, text="Product Description:").pack(pady=5)
    product_entry = tk.Text(request_window, height=5, width=40)
    product_entry.pack(pady=5)

    tk.Label(request_window, text="Country of Purchase:").pack(pady=5)
    country_entry = tk.Entry(request_window)
    country_entry.pack(pady=5)

    def submit_request():
        messagebox.showinfo("Submitted", "Request submitted successfully!")
        request_window.destroy()

    submit_button = tk.Button(request_window, text="Submit Request", command=submit_request)
    submit_button.pack(pady=10)

def open_intermediary_list():
    intermediary_window = tk.Toplevel(root)
    intermediary_window.title("Intermediaries")

    intermediaries = [
        {"name": "John Doe", "location": "USA"},
        {"name": "Jane Smith", "location": "UK"}
    ]

    for intermediary in intermediaries:
        frame = tk.Frame(intermediary_window)
        frame.pack(pady=10)
        tk.Label(frame, text=f"Name: {intermediary['name']}").pack(side=tk.LEFT, padx=10)
        tk.Label(frame, text=f"Location: {intermediary['location']}").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Connect", command=lambda: messagebox.showinfo("Connected", f"Connected with {intermediary['name']}")).pack(side=tk.LEFT)

root = tk.Tk()
root.title("Gift Parcel")
root.geometry("300x200")

header = tk.Label(root, text="Welcome to Gift Parcel", font=("Helvetica", 16))
header.pack(pady=20)

request_button = tk.Button(root, text="Request a Gift", command=open_request_form)
request_button.pack(pady=10)

intermediary_button = tk.Button(root, text="View Intermediaries", command=open_intermediary_list)
intermediary_button.pack(pady=10)

root.mainloop()