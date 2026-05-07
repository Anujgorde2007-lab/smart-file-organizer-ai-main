import os
import shutil
from ml_model import predict_category

folder_path = input("Enter folder path: ")

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        category = predict_category(file)

        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(category_folder, file))
        
print("Files organized successfully!")
