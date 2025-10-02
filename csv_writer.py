import csv
from file_writer import FileWriter

class CsvWriter(FileWriter):
    def write_to_file(self, content: dict, path: str):
        with open(path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter=',')
            
            headers = ["Name", "Group", "Course", "Score", "Mean Score", "Target Course", "Target Score", "Target Mean"]
            csv_writer.writerow(headers)
            
            courses = content["actual_record"]["courses"]
            scores = content["actual_record"]["scores"]
            mean_value = content["actual_record"]["mean"]
            target_courses = content["target_record"]["target_courses"]
            target_scores = content["target_record"]["target_scores"]
            target_mean = content["target_record"]["target_mean"]
            
            for course, score, target_course, target_score in zip(courses, scores, target_courses, target_scores):
                row = [
                    content["name"],
                    content["group"],
                    course,
                    score,
                    mean_value,
                    target_course,
                    target_score,
                    target_mean
                ]
                csv_writer.writerow(row)