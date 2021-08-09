import os

from Tools.directory_tool import DirectoryTool
from Tools.extensions import Extension
from helper_methods import choice_random_objects


def main():
    image_folder_path: str = os.path.join(os.path.dirname(__file__), '../Test/Images/')
    backup_folder_path: str = os.path.join(os.path.dirname(__file__), '../Test/Destination/')
    kill_half_of_the_images(original_path=image_folder_path, backup_path=backup_folder_path)


def kill_half_of_the_images(original_path: str, backup_path: str):
    images_paths = DirectoryTool.get_all_files(in_path=original_path, with_ext=Extension.JPG)
    half_random_victim_images = choice_random_objects(from_list=images_paths)
    DirectoryTool.copy_files(in_files_data=half_random_victim_images, to_target=backup_path)
    DirectoryTool.delete_files(in_data=half_random_victim_images)


if __name__ == "__main__":
    main()
