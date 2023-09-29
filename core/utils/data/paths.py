from pathlib import Path
import os

id_client_json = str(Path.cwd() / "core" / "utils" / "data" / "users_id.json") # путь до файла с id тех кому разрешена работа с ботом
path_to_input = str(Path.cwd() / "core" / "utils" / "data" / "input.txt")
dir_for_search = "/home/dude/test" # путь откуда бот начинает искать папку, название которой ему прислал клиент 
