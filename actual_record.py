from academic_record import AcademicRecord

class ActualRecord(AcademicRecord):
    def calculate_mean_per_course(self):
        means = {}
        for course in self.retrieve_courses():
            scores = self.retrieve_scores()[course]
            if len(scores) == 0:
                means[course] = 0.0
            else:
                means[course] = sum(scores) / len(scores)
        return means