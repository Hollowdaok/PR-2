from academic_record import AcademicRecord

class TargetRecord(AcademicRecord):
    def __init__(self, course_list: list[str], score_dict: dict[str, list[float]], target_means: dict[str, float]):
        super().__init__(course_list, score_dict)
        self.__target_means = target_means

    def calculate_mean_per_course(self):
        return self.__target_means