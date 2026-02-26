import sys
from app.organizer import organize_folder
from app.logger import setup_logger


def run():
    setup_logger()

    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        organize_folder(path)
        print("Files organized successfully!")
    except Exception as e:
        print(f"Error: {e}")