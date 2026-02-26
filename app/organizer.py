import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"],
}


def organize_folder(path: str) -> None:
    if not os.path.exists(path):
        raise FileNotFoundError("Path does not exist")

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            move_to_category(path, filename)


def move_to_category(base_path: str, filename: str) -> None:
    moved = False

    for category, extensions in FILE_CATEGORIES.items():
        if filename.lower().endswith(tuple(extensions)):
            move_file(base_path, filename, category)
            moved = True
            break

    if not moved:
        move_file(base_path, filename, "Others")


def move_file(base_path: str, filename: str, folder: str) -> None:
    target_folder = os.path.join(base_path, folder)
    os.makedirs(target_folder, exist_ok=True)

    shutil.move(
        os.path.join(base_path, filename),
        os.path.join(target_folder, filename),
    )