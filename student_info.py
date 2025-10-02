from student import Student
from academic_record import AcademicRecord
from target_record import TargetRecord

class StudentInfo:
    def __init__(self, student: Student, actual_record: AcademicRecord, target_record: TargetRecord):
        self.__student = student
        self.__actual_record = actual_record
        self.__target_record = target_record

    def convert_to_dictionary(self):
        result = {
            "name": self.__student.retrieve_name(),
            "group": self.__student.retrieve_group(),
            "actual_record": {
                "courses": self.__actual_record.retrieve_courses(),
                "scores": self.__actual_record.retrieve_scores(),
                "mean": self.__actual_record.calculate_mean()
            },
            "target_record": {
                "target_courses": self.__target_record.retrieve_courses(),
                "target_scores": self.__target_record.retrieve_scores(),
                "target_mean": self.__target_record.calculate_mean()
            }
        }
        return result