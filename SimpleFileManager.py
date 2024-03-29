import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import os

def create_file():
    filename = filedialog.asksaveasfilename(title="Create New File", defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if filename:
        with open(filename, 'w'):
            pass
        messagebox.showinfo("Success", f"File '{os.path.basename(filename)}' created successfully.")

def delete_file():
    filename = filedialog.askopenfilename(title="Delete File", filetypes=(("All Files", "*.*"),))
    if filename:
        try:
            os.remove(filename)
            messagebox.showinfo("Success", f"File '{os.path.basename(filename)}' deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete file '{os.path.basename(filename)}': {str(e)}")

def copy_file():
    source = filedialog.askopenfilename(title="Copy File", filetypes=(("All Files", "*.*"),))
    if source:
        destination = filedialog.askdirectory(title="Select Destination Folder")
        if destination:
            try:
                shutil.copy(source, destination)
                messagebox.showinfo("Success", f"File '{os.path.basename(source)}' copied to '{destination}' successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy file '{os.path.basename(source)}': {str(e)}")

def move_file():
    source = filedialog.askopenfilename(title="Move File", filetypes=(("All Files", "*.*"),))
    if source:
        destination = filedialog.askdirectory(title="Select Destination Folder")
        if destination:
            try:
                shutil.move(source, destination)
                messagebox.showinfo("Success", f"File '{os.path.basename(source)}' moved to '{destination}' successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to move file '{os.path.basename(source)}': {str(e)}")

# Creating the main window
root = tk.Tk()
root.title("File and Directory Manager")

# Define buttons
buttons = [
    ("Create File", create_file),
    ("Delete File", delete_file),
    ("Copy File", copy_file),
    ("Move File", move_file)
]

# Create buttons and assign functionality
for text, command in buttons:
    btn = tk.Button(root, text=text, padx=20, pady=10, command=command)
    btn.pack(pady=5)

root.mainloop()
