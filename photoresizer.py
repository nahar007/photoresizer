import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

def browse_source_folder():
    source_folder = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_folder)

def browse_dest_folder():
    dest_folder = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_folder)

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
    source_entry.delete(0, tk.END)
    source_entry.insert(0, file_path)

def convert_images():
    source = source_entry.get()
    dest_folder = dest_entry.get()
    width = int(width_entry.get())
    height = int(height_entry.get())

    try:
        os.makedirs(dest_folder, exist_ok=True)

        if os.path.isdir(source):
            for filename in os.listdir(source):
                if filename.endswith(".jpg"):
                    image_path = os.path.join(source, filename)
                    img = Image.open(image_path)
                    img = img.resize((width, height), Image.ANTIALIAS)
                    img.save(os.path.join(dest_folder, filename))
        else:
            img = Image.open(source)
            img = img.resize((width, height), Image.ANTIALIAS)
            img.save(os.path.join(dest_folder, os.path.basename(source)))

        messagebox.showinfo("Success", "Images converted successfully!")

        # Clear the entry fields
        source_entry.delete(0, tk.END)
        dest_entry.delete(0, tk.END)
        width_entry.delete(0, tk.END)
        height_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Image Resizer Developed By NaharInfocom")
root.geometry("400x300")

# Source folder or file entry
source_label = tk.Label(root, text="Source Folder:")
source_label.pack()
source_entry = tk.Entry(root)
source_entry.pack()

browse_source_button = tk.Button(root, text="Browse Folder", command=browse_source_folder)
browse_source_button.pack()

or_label = tk.Label(root, text="or")
or_label.pack()

select_file_button = tk.Button(root, text="Select File", command=select_file)
select_file_button.pack()

# Destination folder entry
dest_label = tk.Label(root, text="Destination Folder:")
dest_label.pack()
dest_entry = tk.Entry(root)
dest_entry.pack()
browse_dest_button = tk.Button(root, text="Browse", command=browse_dest_folder)
browse_dest_button.pack()

# Width entry
width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

# Height entry
height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_images)
convert_button.pack()

# Run the main loop
root.mainloop()
