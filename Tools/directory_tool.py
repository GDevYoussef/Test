import os
import shutil

from Tools.extensions import Extension


class DirectoryTool:
    @staticmethod
    def get_all_files(in_path: str, with_ext: Extension = Extension.ALL_FILES):
        """
        Get all paths of files in source folder as a default function execution
        It can also get specific extension files in the folder

        :param in_path: The source folder path
        :param with_ext: The default value is empty string which means it can get all the files in the folder
        But, it can add extension type to get specific extension files
        :return: a list of tuples every tuple contain the name of the file as a first value and the path of the file as
        a second value
        """
        path: str = in_path
        ext: Extension = with_ext
        file_list: [tuple[str, str]] = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if ext == Extension.ALL_FILES:
                    file_data = (file, os.path.join(root, file))
                    file_list.append(file_data)
                elif file.endswith(ext.value):
                    file_data = (file, os.path.join(root, file))
                    file_list.append(file_data)
        return file_list

    @staticmethod
    def copy_files(in_files_data: [tuple[str, str]], to_target: str):
        """
        Copy files in source folder to destination folder

        :param in_files_data: is a list of tuples contains the file name and his path
        :param to_target: the final destination path
        :return: nothing
        """
        target: str = to_target
        files_data: [tuple[str, str]] = in_files_data
        for file_data in files_data:
            shutil.copyfile(file_data[1], f"{target}/{file_data[0]}")

    @staticmethod
    def delete_files(in_data: [tuple[str, str]]):
        """
        Delete files

        :param in_data: is the list of tuples contains the files name and the files paths which needed to delete the files
        :return: nothing
        """
        for path in in_data:
            os.remove(path[1])

