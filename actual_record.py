from academic_record import AcademicRecord

class ActualRecord(AcademicRecord):
    def calculate_mean(self):
        all_scores = self.retrieve_scores()
        if len(all_scores) == 0:
            return 0.0
        total = sum(all_scores)
        count = len(all_scores)
        return total / count