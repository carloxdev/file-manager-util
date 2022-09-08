File:

    __init__(_name, _path=None)

        Description:
            This method is the constructor of the class.

        Parameters:
            * _name: name of the file with extention. Example:
                -> "photo.jpg"
                -> "video.mp4"

            * _path: Folder name with absulute path. Examples:
                -> "/home/MyFolder"
                -> "C:/files/MyFolder"

        Behaviour and Validations:
            * If the value of "_name" parameter doesn't containt a extention then it
            will raise "ExtentionMissingError"
            * If the value of "_name" parameter is not a string or None then it will
            raise "InvalidFileNameError"
            * If the value of "_path" parameter is not a string or None then it will
            raise "InvalidPathError"

    create()

        Description:
            This method will create a file with the values specified in the parameters
            of constructor function.

        Behaviour and Validations:
            * If "_path" value did not specify in constructor then the file will be created
            in the folder where is running the program.
            * If "_path" value was specified in in constructor then the file will be created
            in that path
            * If "_path" value was specified in in constructor and doesn't exist then then
            it will raise "PathDoesNotExistError"
            * If there is a file with the same specified name in the specified path then it
            will raise "FileAlreadyExistsError"

    move(_new_path)

        Description:
            This method will move a file to new location.

        Parameters:
            * _path: absolute path where we want to move the file. Examples:
                -> "/home/NewLocation"
                -> "C:/files/NewLocation"

        Behaviour:
            * If "_new_path" value is not a string then will raise "InvalidPathError"
            * If the file doesn't exist then will raise "FileDoesNotExistError"
            * If the path specified in "_new_path" parameter doesn't exist then it will
            raise "PathDoesNotExistError"
            * If there is a file with the same specified name in the specified path then it
            will raise "FileAlreadyExistsError"

    exists()


Folder

    __init__(_name, _path=None)

        Description:
            This method is the constructor of the class.

    create()
        Description:
            This method will create a folder with the values specified in the parameters
            of constructor function.

        Behaviour and Validations:
            * If "_path" value did not specify in constructor then the folder will be created
            in the folder where is running the program.
            * If "_path" value was specified in in constructor then the folder will be created
            in that path
            * If "_path" value was specified in in constructor and doesn't exist then then
            it will raise "PathDoesNotExistError"
            * If there is a folder with the same specified name in the specified path then it
            will raise "FolderAlreadyExistsError"

    move(_new_path)
        Description:
            This method will move a folder to new location.

        Parameters:
            * _path: absolute path where we want to move the folder. Examples:
                -> "/home/NewLocation"
                -> "C:/files/NewLocation"

        Behaviour:
            * If "_new_path" value is not a string then will raise "InvalidPathError"
            * If the folder doesn't exist then will raise "FileDoesNotExistError"
            * If the path specified in "_new_path" parameter doesn't exist then it will
            raise "PathDoesNotExistError"
            * If there is a folder with the same specified name in the specified path then it
            will raise "FolderAlreadyExistsError"

    exists()

    get_Content()

    get_File(_filename)

