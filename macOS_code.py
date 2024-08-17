import os 
import shutil


import mainFile


 
def mac_create_folder(folderpath):
    try:
        os.makedirs(folderpath, exist_ok=True)
        print("Successfully Created")
        
    except Exception as e:
        print("Error while attempting to create folder:", e)

def mac_delete_folder(folderpath):
    try:
        os.rmdir(folderpath)
        print("Successfully Deleted")
    except FileNotFoundError:
        print("Folder does not exist")
    except Exception as e:
        print("Error while attempting to delete folder:", e)

def mac_move_folder(src_folderpath, dest_folderpath):
    try:
        shutil.move(src_folderpath, dest_folderpath)
        print("Successfully Moved")
    except FileNotFoundError:
        print("Source folder does not exist")
    except Exception as e:
        print("Error while attempting to move folder:", e)

def mac_Folder_Menu():
    while True:
        print("\n------------------------------")
        print("Welcome to Folder Management Software")
        print("------------------------------")
        print("1. Create Folder")
        print("2. Delete Folder")
        print("3. Move Folder")
        mac_Folder_Choice = input("Enter your choice (1, 2, or 3): ")

        if mac_Folder_Choice == "1":
            
            file_directory = input("Type directory (e.g., '~/Downloads'): ")
            downloads_direct = os.path.expanduser(file_directory)

            foldername = input("Enter Folder Name: ")
            folderpath = os.path.join(downloads_direct, foldername)
            mac_create_folder(folderpath) 
            
        elif mac_Folder_Choice == "2":
            file_directory = input("Type directory (e.g., '~/Downloads'): ")
            downloads_direct = os.path.expanduser(file_directory)

            foldername = input("Enter Folder Name: ")
            folderpath = os.path.join(downloads_direct, foldername)
            mac_delete_folder(folderpath)    
                    
        elif mac_Folder_Choice == "3":
            
                foldername = input("Enter Folder Name: ")
                folderpath = os.path.join(downloads_direct, foldername)
                dest_directory = input("Type destination directory (e.g., '~/Documents'): ")
                dest_path = os.path.expanduser(dest_directory)
                mac_move_folder(folderpath, dest_path)  
        else:
            print("error!")

 
   
def mac_delete_file():
    cfile_name = input("Enter the name of the file: ")
    mac_cfile_directory = input("Enter the directory as [~/Downloads] : ")
    
    cfile_name = cfile_name + ".txt"
    
    mac_cfile_directory = os.path.expanduser(mac_cfile_directory)
    file_path = os.path.join(mac_cfile_directory, cfile_name)
    
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Successfully deleted {file_path}")
        else:
            print("The file does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
    
def mac_move_file():
    file_name = input("Enter the name of the file: ")
    old_directory = input("Enter the current directory as [~/Downloads]: ")
    new_directory = input("Enter the new directory as [~/Documents]: ")

    file_name = file_name + ".txt"
    old_directory = os.path.expanduser(old_directory)
    new_directory = os.path.expanduser(new_directory)
    old_path = os.path.join(old_directory, file_name)
    new_path = os.path.join(new_directory, file_name)

    try:
        if os.path.exists(old_path):
            os.makedirs(new_directory, exist_ok=True)
            os.rename(old_path, new_path)
            print(f"Successfully moved {file_name} to {new_directory}")
        else:
            print("The file does not exist in the specified directory.")
    except Exception as e:
        print(f"An error occurred while moving the file: {e}")

        
def mac_create_file():
    
    file_name = input("Enter the name of the file: ")
    mac_file_directory = input("Enter the directory as [~/Downloads] : ")

   
    file_name = file_name + ".txt"
    
    mac_file_directory = os.path.expanduser(mac_file_directory)
    file_path = os.path.join(mac_file_directory, file_name)
    os.makedirs(mac_file_directory, exist_ok=True)
    
    
    content = input("Write in file ['Hello World'] : ")

    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Successfully Create at {file_path}")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
            
  
def mac_File_Menu():
    print("\n------------------------------")
    print("Welcome to File Management Software")
    print("------------------------------")
    print("1. Create File")
    print("2. Delete File")
    print("3. Move File")
    mac_File_Choice = input("Enter your choice (1, 2 ,3): ")
        
        
    if mac_File_Choice == '1':
        mac_create_file()
    elif mac_File_Choice == '2':
        mac_delete_file()
        
    elif mac_File_Choice == '3':
        mac_move_file()
        
    else:
        print('error')
        




 
def mac_code_Files_Menu() :
    print("\n------------------------------")
    print("Welcome to Coding Files Software")
    print("------------------------------")
    print("1. Python file")
    print("2. Javascript file")
    
    mac_code_Files_Choice = input("Enter: ")
    
    if mac_code_Files_Choice == "1":
        mac_making_Py_File()
    elif mac_code_Files_Choice == "2":
        mac_makingJSFile()
    else: 
        print("Error")


 

def mac_making_Py_File():
     
    py_Code_File_name = input("Enter the name of the file: ")
    mac_pyCodeFile_directory = input("Enter the directory as [~/Downloads] : ")
   
    py_Code_File_name = py_Code_File_name + ".py"
    
    mac_pyCodeFile_directory = os.path.expanduser(mac_pyCodeFile_directory)
    pyCodeFile_path = os.path.join(mac_pyCodeFile_directory, py_Code_File_name)
    os.makedirs(mac_pyCodeFile_directory, exist_ok=True)
    
    
    content = "print('Hello World')"

    try:
        with open(pyCodeFile_path, 'w') as file:
            file.write(content)
        print(f"Successfully Create at {pyCodeFile_path}")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
    


    
def mac_makingJSFile() :
    
    jsCodeFile_name = input("Enter the name of the file: ")
    mac_jsCodeFile_directory = input("Enter the directory as [~/Downloads] : ")
   
    jsCodeFile_name =jsCodeFile_name+ ".js"
    
    mac_jsCodeFile_directory = os.path.expanduser(mac_jsCodeFile_directory)
    jsCodeFile_path = os.path.join(mac_jsCodeFile_directory, jsCodeFile_name)
    os.makedirs(mac_jsCodeFile_directory, exist_ok=True)
    
    
    content = 'System.out.println("Hello, World!");'
     
    try:
        with open(jsCodeFile_path, 'w') as file:
            file.write(content)
        print(f"Successfully Create at {jsCodeFile_path}")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
    