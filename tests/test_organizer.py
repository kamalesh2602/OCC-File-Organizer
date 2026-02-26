import os
from app.organizer import organize_folder


def test_invalid_path():
    try:
        organize_folder("invalid_path")
    except FileNotFoundError:
        assert True
    else:
        assert False


def test_file_moved(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello")

    organize_folder(tmp_path)

    assert os.path.exists(tmp_path / "Documents" / "sample.txt")
