import asyncio
from datetime import datetime


async def _write_report(filename, students, title):

    with open(filename, "w") as f:

        f.write(f"{title}\n")
        f.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total     : {len(students)} students\n")
        f.write("=" * 55 + "\n\n")

        for student in students:
            f.write(str(student) + "\n")   # uses Student.__str__()
            await asyncio.sleep(0)         # yield to event loop after each line

        # Summary totals at the bottom
        if students:
            total_fines = sum(s.fine() for s in students)
            f.write("\n" + "=" * 55 + "\n")
            f.write(f"Total fines collected: ${total_fines}\n")

    print(f"  Report saved: {filename}")
    return filename


async def generate_reports(students):
    timestamp     = datetime.now().strftime("%H%M%S")
    failed        = [s for s in students if not s.passed()]

    full_file     = f"full_report_{timestamp}.txt"
    failed_file   = f"failed_report_{timestamp}.txt"

    await asyncio.gather(
        _write_report(full_file,   students, "FULL STUDENT REPORT"),
        _write_report(failed_file, failed,   "FAILED STUDENTS REPORT"),
    )

    return full_file, failed_file
