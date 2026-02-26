# How to Use File Organizer

1. Install Docker
2. Pull image:
   docker pull 23z332/file-organizer:1.0.0

3. Run:

    Windows:
        docker run --rm -v "%cd%":/data 23z332/file-organizer:1.0.0 /data
    
    Linux :
        docker run --rm -v "$(pwd)":/data 23z332/file-organizer:1.0.0 /data
    
    