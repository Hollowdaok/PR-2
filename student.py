class Student:
    def __init__(self, name: str, group: str):
        self.__name = name
        self.__group = group

    def retrieve_name(self):
        return self.__name

    def retrieve_group(self):
        return self.__group
    
    def set_full_name(self, name: str):
        self.__name = name

    def set_group_number(self, group: str):
        self.__group = group