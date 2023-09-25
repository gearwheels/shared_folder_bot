from pathlib import Path
import os

path_to_stuff = str(Path.cwd() / "core" / "utils" / "data" / "users_id.json")
path_to_input = str(Path.cwd() / "core" / "utils" / "data" / "input.txt")
dir_for_search = "/home/dude/test" # путь откуда бот начинает искать папку, название которой ему прислал клиент 