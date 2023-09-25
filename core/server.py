from pathlib import Path
import asyncio
import os

from core.utils.data.paths import dir_for_search




def get_foldernames(folder_name: str):
    list_folders = []
    folder_name = "*" + folder_name + "*"
    for path in Path(dir_for_search).rglob(folder_name):
        if path.is_dir():
            list_folders.append(Path.joinpath(path.parent,path.name))
        # print(Path.joinpath(path.parent,path.name))
    return list_folders

def get_all_filenames(folder_name: str):
    list_files = []
    for path in Path(folder_name).rglob():
        if path.is_file():
            list_files.append(Path.joinpath(path.parent,path.name))
        # print(Path.joinpath(path.parent,path.name))
    return list_files

def creat_archive(folder_name: str):
    archive_name = str(folder_name).split("/")[-1]
    archive_name = archive_name + ".tar.gz"
    
    return archive_name

def send_all_files(paths_to_files: list):
    pass

def send_file(path_to_file: str):
    pass


async def main():
    list = await get_foldernames(folder_name = "main_")
    print("list ", list)


if __name__ == "__main__":
    asyncio.run(main())

