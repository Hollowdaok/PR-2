from abc import ABC, abstractmethod

class AcademicRecord(ABC):
    def __init__(self, course_list: list[str], score_dict: dict[str, list[float]]):
        self.__course_list = course_list
        self.__score_dict = score_dict

    def retrieve_courses(self):
        return self.__course_list

    def retrieve_scores(self):
        return self.__score_dict

    @abstractmethod
    def calculate_mean_per_course(self):
        pass