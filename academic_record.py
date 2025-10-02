from abc import ABC, abstractmethod

class AcademicRecord(ABC):
    def __init__(self, course_list: list[str], score_list: list[float]):
        self.__course_list = course_list
        self.__score_list = score_list

    def retrieve_courses(self):
        return self.__course_list

    def retrieve_scores(self):
        return self.__score_list

    @abstractmethod
    def calculate_mean(self):
        pass