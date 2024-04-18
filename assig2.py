import os
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.title("File Sharing App")
def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def share_file():
    file_path = file_entry.get()
    # Implement file sharing functionality here
    # This could involve copying the file to a specific location or sending it over a network
    # You can use libraries like shutil for file operations or requests for network operations
    # Example: shutil.copy(file_path, destination_directory)
    #          Or send file over network
    print("File shared successfully!")
file_label = tk.Label(root, text="Select File:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

select_button = tk.Button(root, text="Browse", command=select_file)
select_button.pack()

share_button = tk.Button(root, text="Share File", command=share_file)
share_button.pack()
root.mainloop()