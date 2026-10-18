def check_eligibility(marks, attendance, project_completed):
    is_project_done = project_completed in ['yes', 'true', 'completed']

    if marks >= 60 and attendance >= 75 and is_project_done:
        return "Eligible"
    else:
        return "Not Eligible"

marks = int(input())
attendance = int(input())
project_completed = input().strip().lower()

result = check_eligibility(marks, attendance, project_completed)
print(result)