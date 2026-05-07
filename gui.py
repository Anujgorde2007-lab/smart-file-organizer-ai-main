def organize_files():
    folder_path = folder_entry.get()

    if not folder_path:
        messagebox.showerror("Error", "Please select a folder")
        return

    FILE_CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"],
    }

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            _, extension = os.path.splitext(filename)
            extension = extension.lower()

            moved = False

            # Normal extension-based sorting
            for category, extensions in FILE_CATEGORIES.items():

                if extension in extensions:

                    category_folder = os.path.join(folder_path, category)

                    os.makedirs(category_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(category_folder, filename)
                    )

                    moved = True
                    break

            # AI-based smart sorting
            filename_lower = filename.lower()

            if not moved:

                if "resume" in filename_lower or "cv" in filename_lower:

                    ai_folder = os.path.join(folder_path, "Career")

                    os.makedirs(ai_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(ai_folder, filename)
                    )

                elif "assignment" in filename_lower or "college" in filename_lower:

                    ai_folder = os.path.join(folder_path, "Education")

                    os.makedirs(ai_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(ai_folder, filename)
                    )

                elif "invoice" in filename_lower or "bill" in filename_lower:

                    ai_folder = os.path.join(folder_path, "Finance")

                    os.makedirs(ai_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(ai_folder, filename)
                    )

                else:

                    other_folder = os.path.join(folder_path, "Others")

                    os.makedirs(other_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(other_folder, filename)
                    )

    messagebox.showinfo("Success", "Files Organized Successfully!")