import csv
from file_writer import FileWriter

class CsvWriter(FileWriter):
    def write_to_file(self, content: dict, path: str):
        with open(path, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter=',')
            
            headers = ["Name", "Group", "Course", "Scores", "Mean Score", "Target Scores", "Target Mean"]
            csv_writer.writerow(headers)
            
            courses = content["actual_record"]["courses"]
            scores_dict = content["actual_record"]["scores"]
            means = content["actual_record"]["mean_per_course"]
            target_scores_dict = content["target_record"]["target_scores"]
            target_means = content["target_record"]["mean_per_course"]
            
            for course in courses:
                row = [
                    content["name"],
                    content["group"],
                    course,
                    ";".join(map(str, scores_dict[course])),
                    means[course],
                    ";".join(map(str, target_scores_dict[course])),
                    target_means[course]
                ]
                csv_writer.writerow(row)