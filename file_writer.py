from abc import ABC, abstractmethod

class FileWriter(ABC):
    @abstractmethod
    def write_to_file(self, content: dict, path: str):
        pass