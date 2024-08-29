def copy_file(src_file, dest_file):
    try:
        with open(src_file, 'r') as file1, open(dest_file, 'w') as file2:
            for line in file1:
                file2.write(line)
        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found!")

src_file = input("Enter the source file name: ")
dest_file = input("Enter the destination file name: ")

copy_file(src_file, dest_file)