import os
import shutil

  

import macOS_code
import windowsOS_code
import database


def main():
    print("----------Welcome to [File Organizing Software]----------")
    print("1. Navigate with MAC")
    print("2. Navigate with WINDOWS")
    OS_Choice = input("Type 1 or 2: ")
    
    #MACOS
    if OS_Choice == '1':
        mac_Selection_Software()
    elif OS_Choice == '2':
        windows_Selection_Software()
    else:
        print("Error")
    
    
def mac_Selection_Software():
    print("------------------- MAC OS SETTINGS -----------------------")
    print("---------- Welcome to [File Organizing Software] ----------")
    print("1. Navigate to File Settings")
    print("2. Navigate to Folder Settings")
    print("3. Make Code Files")
    print("4. Navigate to tag settings")

    
    
    mac_Nav_Choice = input("Enter : ")
    if mac_Nav_Choice == "1":
        macOS_code.mac_File_Menu()
    elif mac_Nav_Choice == "2":
        macOS_code.mac_Folder_Menu()
    elif mac_Nav_Choice == "3":
        macOS_code.mac_code_Files_Menu()
    elif mac_Nav_Choice == "4":
        mac_Tags_Menu()
    else: 
        print("Error!")
    
    
def mac_Tags_Menu():
    print()
    print("\n----------Welcome to Tags Settings----------\n")
    print("1. Setup Tags (If it's your first time)")
    print("2. Create File and Tag")
    print("3. Add tag(s) to pre-existing file")
    print("4. Check Tags")
    print("5. Go Back\n")
    db_choice = input("Type desired action: ")

    if db_choice =="1":
        database.setup_database()
        print("Completed! You are now ready to use tags!")
    elif db_choice == "2":
        file_name = input("Enter the file name: ")
        tag = input("Enter the tag: ")
        with open(file_name, 'w') as file:
            file.write("")
            print(f"Confirmed Creation of {file_name}")
        database.add_file_and_tag(file_name, tag)
    elif db_choice == "3":
        print("Currently unavailable")
    elif db_choice == "4":
        file_name = input("Enter the file name: ")
        print("Fetching Tags\n")
        database.fetch_tags(file_name)
    elif db_choice == "5":
        mac_Selection_Software()
    else:
        print("Error, Try Again")
    
    



    
def windows_Selection_Software():
    print("1. Python File")
    print("2. JavaScript File")
    print("3. Text File")
    print("4. Go Back\n")
    file_choice = input("Type desired action: ")
    if file_choice == "1":
        filename = input("Enter filename: ")
        windowsOS_code.windows_py_create(filename)
    elif file_choice == "2":
        filename = input("Enter filename: ")
        windowsOS_code.windows_js_create(filename)
    elif file_choice == "3":
        filename = input("Enter filename: ")
        windowsOS_code.windows_txt_create(filename)
 

if __name__ == "__main__":
    main()
