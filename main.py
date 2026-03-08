# Pipeline:
#Load CSV
#Validate rows → Student objects
#Print terminal summary
#Generate reports (async)

import asyncio
from loader     import load_csv, validate
from report     import generate_reports
from decorators import log_execution
from exceptions import PortalError

CSV_PATH = "students.csv"


def print_summary(students, errors):

    passed = [s for s in students if     s.passed()]
    failed = [s for s in students if not s.passed()]

    print("ACADEMIC PORTAL & STUDENT SUMMARY")


    for student in students:
        print(" ", student)

    print(f"Total loaded: {len(students)}")
    print(f"Passed: {len(passed)}")
    print(f"Failed: {len(failed)}")
    print(f"Total fines: ${sum(s.fine() for s in students)}")

    if errors:
        print(f"\n  Validation issues ({len(errors)} skipped rows):")
        for err in errors:
            print(f"    Error  {err}")



@log_execution
def run_pipeline():
    asyncio.run(_main_async())


async def _main_async():

    print("\nLoading student records...")

    # Step 1: load raw CSV rows
    rows = load_csv(CSV_PATH)
    print(f"  {len(rows)} rows read from '{CSV_PATH}'")

    # Step 2: validate and build Student objects
    students, errors = validate(rows)
    print(f"  {len(students)} valid students, {len(errors)} skipped")

    # Step 3: terminal summary
    print_summary(students, errors)

    # Step 4: generate both report files concurrently
    print("\nGenerating reports")
    full_path, failed_path = await generate_reports(students)

    print(f"\nDone! Reports written:")
    print(f"Full report {full_path}")
    print(f"Failed report {failed_path}\n")


if __name__ == "__main__":
    try:
        run_pipeline()
    except PortalError as e:
        print(f"\n[ERROR] {e}")
    except EnvironmentError as e:
        print(f"\n[CONFIG ERROR] {e}")
