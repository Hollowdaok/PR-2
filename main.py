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
    score_list = [78, 88, 92, 85, 96]
    actual = ActualRecord(course_list, score_list)
    
    target_scores = [90, 95, 98, 92, 100]
    target_mean_value = 98
    target = TargetRecord(course_list, target_scores, target_mean_value)
    
    info = StudentInfo(student, actual, target)
    data_dictionary = info.convert_to_dictionary()
    
    base_name = f"{student.retrieve_name().replace(' ', '_')}_{student.retrieve_group()}"
    
    JsonWriter().write_to_file(data_dictionary, base_name + ".json")
    XmlWriter().write_to_file(data_dictionary, base_name + ".xml")
    CsvWriter().write_to_file(data_dictionary, base_name + ".csv")

if __name__ == "__main__":
    main()