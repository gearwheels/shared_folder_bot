
class dataForCallback():
    key_and_data = {}
    def __init__(self) -> None:
        pass

    def set_key_and_data(self, id: str, data: list):
        self.key_and_data[id] = data

    def get_data(self, id: str):
        return self.key_and_data[id]

    def add_items_to_key_and_data(self, id: str, item: str):
        self.key_and_data[id].append(item)

    def to_str(self):
        out_str = f"""Данные для клавиатуры: """

        key = list(self.key_and_data.keys())
        data = list(self.key_and_data.values())
        for num, drink in enumerate(key):
            out_str += f"\nKey: {drink}"
            for item in data[num]:
                out_str +=  f"\n\t{item}"

        return out_str