import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Create main window
root = tk.Tk()
root.title("Smart File Organizer AI")
root.geometry("550x350")

# Theme mode
dark_mode = True

# Variable to store folder path
folder_path = ""


# Apply theme function
def apply_theme():

    if dark_mode:

        bg_color = "#1e1e1e"
        fg_color = "white"
        entry_bg = "#2d2d2d"

    else:

        bg_color = "white"
        fg_color = "black"
        entry_bg = "white"

    root.config(bg=bg_color)

    title.config(
        bg=bg_color,
        fg=fg_color
    )

    folder_label.config(
        bg=bg_color,
        fg=fg_color
    )

    folder_entry.config(
        bg=entry_bg,
        fg=fg_color,
        insertbackground=fg_color
    )


# Toggle theme
def toggle_theme():

    global dark_mode

    dark_mode = not dark_mode

    apply_theme()


# Select folder function
def select_folder():

    global folder_path

    folder_path = filedialog.askdirectory()

    if folder_path:

        folder_entry.delete(0, tk.END)

        folder_entry.insert(0, folder_path)

        folder_label.config(text="Folder Selected")


# Organize files function
def organize_files():

    if not folder_path:

        messagebox.showerror(
            "Error",
            "Please select a folder first!"
        )

        return

    FILE_CATEGORIES = {

        "Images": [".jpg", ".jpeg", ".png", ".gif"],

        "Documents": [".pdf", ".docx", ".txt", ".pptx"],

        "Videos": [".mp4", ".mkv", ".avi"],

        "Music": [".mp3", ".wav"],

        "Programs": [".exe", ".msi"],

        "Archives": [".zip", ".rar"]
    }

    try:

        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):

                file_extension = os.path.splitext(filename)[1].lower()

                moved = False

                # Move categorized files
                for category, extensions in FILE_CATEGORIES.items():

                    if file_extension in extensions:

                        category_folder = os.path.join(
                            folder_path,
                            category
                        )

                        os.makedirs(
                            category_folder,
                            exist_ok=True
                        )

                        shutil.move(
                            file_path,
                            os.path.join(
                                category_folder,
                                filename
                            )
                        )

                        moved = True
                        break

                # Move uncategorized files
                if not moved:

                    others_folder = os.path.join(
                        folder_path,
                        "Others"
                    )

                    os.makedirs(
                        others_folder,
                        exist_ok=True
                    )

                    shutil.move(
                        file_path,
                        os.path.join(
                            others_folder,
                            filename
                        )
                    )

        messagebox.showinfo(
            "Success",
            "Files Organized Successfully!"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# Title
title = tk.Label(
    root,
    text="Smart File Organizer AI",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)


# Folder label
folder_label = tk.Label(
    root,
    text="No Folder Selected",
    font=("Arial", 10)
)

folder_label.pack(pady=5)


# Folder entry
folder_entry = tk.Entry(
    root,
    width=50,
    font=("Arial", 11)
)

folder_entry.pack(pady=10)


# Browse button
browse_button = tk.Button(
    root,
    text="Browse Folder",
    command=select_folder,
    bg="#0078D7",
    fg="white",
    padx=10,
    pady=5
)

browse_button.pack(pady=10)


# Organize button
organize_button = tk.Button(
    root,
    text="Organize Files",
    command=organize_files,
    bg="green",
    fg="white",
    padx=10,
    pady=5
)

organize_button.pack(pady=10)


# Theme button
theme_button = tk.Button(
    root,
    text="Toggle Dark / Light Mode",
    command=toggle_theme,
    bg="#444444",
    fg="white",
    padx=10,
    pady=5
)

theme_button.pack(pady=10)


# Apply default theme
apply_theme()

# Run app
root.mainloop()