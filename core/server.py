from pathlib import Path
import asyncio
import zipfile
import os

# from core.utils.data.paths import dir_for_search

dir_for_search = "/home/dude/test"


def get_foldernames(folder_name: str):
    list_folders = []
    folder_name = "*" + folder_name + "*"
    for path in Path(dir_for_search).rglob(folder_name):
        if path.is_dir():
            list_folders.append(str(Path.joinpath(path.parent,path.name)))
        # print(str(Path.joinpath(path.parent,path.name)))

    return list_folders

def get_all_filenames(folder_name: str):
    list_files = []
    # for path in Path(folder_name).rglob():
    for root, dirs, files in os.walk(folder_name):
        for file in files:
            abs_path_file = os.path.join(root,file)
            # if abs_path_file.is_file():
            list_files.append(str(abs_path_file))
        # print(str(Path.joinpath(path.parent,path.name)))
        
    return list_files

def creat_folder(path: str, foldername: str):
	path = os.path.join(path, foldername)
	if (not os.path.exists(path)) or (not os.path.isdir(path)): # делаем папку для созданной копии проекта 
			os.mkdir(path)
	return path

def creat_archive(folder_path: str, user_id: int):
    archive_name = str(folder_path).split("/")[-1]
    archive_name = archive_name + str(user_id) + ".zip"
    archive_name_abs_path = creat_folder(path=Path.cwd(), foldername="archive_data")

    len_dir_path = len(folder_path)

    with zipfile.ZipFile(os.path.join(archive_name_abs_path, archive_name), 'w') as zip_file:
        for root, dirs, files in os.walk(folder_path):
                for file in files:
                    arch_name = os.path.join(root,file)
                    zip_file.write(os.path.join(root,file), 
                                   arcname=arch_name[len_dir_path :], 
                                   compress_type=zipfile.ZIP_DEFLATED) 
    
    return os.path.join(archive_name_abs_path, archive_name)

async def del_archive(archive_path: str):
    try:
         os.remove(archive_path)
    except OSError:
         print("ERROR: Удаляемый архив не существует. \nПуть - {}".format(archive_path))
    pass


async def main():
    list = get_foldernames(folder_name = "main_")
    # print("list ", list)
    path = creat_archive('/home/dude/test/main_papka', 2)
    # await del_archive(path)


if __name__ == "__main__":
    asyncio.run(main())

