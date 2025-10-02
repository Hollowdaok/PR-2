import json
from file_writer import FileWriter

class JsonWriter(FileWriter):
    def write_to_file(self, content: dict, path: str):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(content, file, indent=2, ensure_ascii=False)