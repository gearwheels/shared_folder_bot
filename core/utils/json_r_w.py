import json

# from core.utils.data.paths import path_to_input

# структора json-файла для хранения id пользователей которые могут им пользоватья - список

class JsonRW():
    filename = ""
    def __init__(self, file_name):
        self.filename =f'{file_name}'


    def creat_json(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            pass

    def add_write_json(self, data: tuple):
        if len(data) != 2:
            print("add_write_json принимает кортеж только из двух эллементов")
            return
        json_data = self.read_json()
        json_data[data[0]] = data[1]
        self.write_json(json_data)

    def write_json(self, data):
        data = json.dumps(data)
        data = json.loads(str(data))
        
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def read_json(self, key = None):
        with open(self.filename, "r", encoding="utf-8") as file:
            if key:
                dict_json = json.load(file)
                return dict_json[key]
            else:
                return json.load(file)


# file_name = "users_id.json"
# list_id = {"358929773":"Alexey Timofeev", "6654802779":"Alexey Timofeev"}

# users_id_file = JsonRW(file_name)
# users_id_file.creat_json()
# users_id_file.write_json(list_id)
# print(users_id_file.read_json())
# users_id_file.add_write_json(("110111","110111","110111"))

# print(users_id_file.read_json())

