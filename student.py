from config import PASS_MARK, LATE_FINE_PER_DAY


class Student:

    def __init__(self, sid, name, marks, late_days):
        self.sid       = sid
        self.name      = name
        self.marks     = marks        # stored as int after validation
        self.late_days = late_days    # stored as int after validation

    def passed(self):
        return self.marks >= PASS_MARK

    def fine(self):
        return self.late_days * LATE_FINE_PER_DAY

    def status(self):
        return "PASS" if self.passed() else "FAIL"

    # __str__ is what prints when you do  print(student)
    def __str__(self):
        return (f"{self.sid} | {self.name:<15} | "
                f"Marks: {self.marks:>3} | {self.status()} | "
                f"Fine: ${self.fine()}")
