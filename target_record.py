from academic_record import AcademicRecord

class TargetRecord(AcademicRecord):
    def __init__(self, course_list: list[str], score_list: list[float], target_mean: float):
        super().__init__(course_list, score_list)
        self.__target_mean = target_mean

    def calculate_mean(self):
        return self.__target_mean