from app.organizer import organize_folder
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        sys.exit(1)

    organize_folder(sys.argv[1])
    print("Files organized successfully!")


if __name__ == "__main__":
    main()