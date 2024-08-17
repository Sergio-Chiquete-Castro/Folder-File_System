

import os 
import shutil


def windows_py_create(filename):
    filename = filename + ".py"
    with open(filename, 'w') as file:
        pass

def windows_js_create(filename):
    filename = filename + ".js"
    with open(filename, 'w') as file:
        pass

def windows_txt_create(filename):
    try:
        with open(filename, 'w') as file:
            file.write("")
            print("Confirmed Creation")
    except Exception as e:
        print("Error while attempting to create file")

def windows_file_delete(filename):
    try:
        os.remove(filename)
        print("File removed")
    except FileNotFoundError:
        print("File does not exist")
    except Exception as e:
        print("Error while attempting to create file")

def windows_file_move(filename):
    current_dir = os.getcwd()
    username = os.environ.get('USERNAME')
    filename = "\\" + filename 
    current_file = current_dir + filename
    new_dir = ""
    print("\n1. Downloads")
    print("2. Documents")
    print("3. Desktop")
    print("5. Custom Location")
    move_dir = input("Where would you like to send the file?")
    if move_dir == "1" or move_dir == "Downloads":
        new_dir = "C:\\Users\\" + username + "\\Downloads" + filename
        shutil.move(current_file, new_dir)
    elif move_dir == "2" or move_dir == "Documents":
        new_dir = "C:\\Users\\" + username + "\\OneDrive" + "\\Documents" + filename
        shutil.move(current_file, new_dir)
    elif move_dir == "3" or move_dir == "Desktop":
        new_dir = "C:\\Users\\" + username + "\\OneDrive" + "\\Desktop" + filename
        shutil.move(current_file, new_dir)
    elif move_dir == "5" or move_dir == "Custom Location":
        print("Please specify the desired file location in C:\\...\\...\\...\\file.extension Format")
        custom_dir = input("")
        shutil.move(current_file, custom_dir)


# Folder Actions #

def windows_folder_create(createFName):
    createFolder_path = createFName
    os.makedirs(createFolder_path, exist_ok=True)
    print("Successfully Created")

def windows_folder_delete(deleteFName):
    deleteFolder_path = deleteFName
    os.rmdir(deleteFolder_path)
    print("Deleted Successfully")