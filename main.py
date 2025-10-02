from student import Student
from actual_record import ActualRecord
from target_record import TargetRecord
from student_info import StudentInfo
from json_writer import JsonWriter
from xml_writer import XmlWriter
from csv_writer import CsvWriter

def main():
    student = Student("Didylivskyi Denys", "PD-41")
    
    course_list = ["Algorithms", "Databases", "Networks", "Python", "Java"]
    score_dict = {
        "Algorithms": [78, 80],
        "Databases": [88, 90],
        "Networks": [92, 94],
        "Python": [85, 87],
        "Java": [96, 98]
    }
    actual = ActualRecord(course_list, score_dict)
    
    target_score_dict = {
        "Algorithms": [90, 92],
        "Databases": [95, 96],
        "Networks": [98, 99],
        "Python": [92, 94],
        "Java": [100, 100]
    }
    target_means = {
        "Algorithms": 91,
        "Databases": 95.5,
        "Networks": 98.5,
        "Python": 93,
        "Java": 100
    }
    target = TargetRecord(course_list, target_score_dict, target_means)
    
    info = StudentInfo(student, actual, target)
    data_dictionary = info.convert_to_dictionary()
    
    base_name = f"{student.retrieve_name().replace(' ', '_')}_{student.retrieve_group()}"
    
    JsonWriter().write_to_file(data_dictionary, base_name + ".json")
    XmlWriter().write_to_file(data_dictionary, base_name + ".xml")
    CsvWriter().write_to_file(data_dictionary, base_name + ".csv")

if __name__ == "__main__":
    main()