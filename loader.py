import csv
from student    import Student
from exceptions import FileLoadError, ValidationError


def load_csv(path):
    try:
        with open(path, "r") as f:
            rows = list(csv.DictReader(f))
        return rows
    except FileNotFoundError:
        raise FileLoadError(f"File not found: '{path}'")
    except Exception as e:
        raise FileLoadError(f"Could not read file: {e}")


def validate(rows):
    students = []
    errors   = []

    for row in rows:
        sid  = row.get("id","").strip()
        name = row.get("name","").strip()
        raw_marks     = row.get("marks","").strip()
        raw_late_days = row.get("late_days","").strip()

        if not sid or not name:
            errors.append(f"Missing id or name in row: {dict(row)}")
            continue

        if not raw_marks:
            errors.append(f"{sid} ({name}): marks field is empty — skipped")
            continue

        try:
            marks = int(raw_marks)
        except ValueError:
            errors.append(f"{sid} ({name}): marks '{raw_marks}' is not a number — skipped")
            continue

        try:
            late_days = int(raw_late_days) if raw_late_days else 0
        except ValueError:
            errors.append(f"{sid} ({name}): late_days '{raw_late_days}' is not a number — skipped")
            continue

        students.append(Student(sid, name, marks, late_days))

    return students, errors
