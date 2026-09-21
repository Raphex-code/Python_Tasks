def course_grader(average):
    if average >= 70:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    elif average >= 45:
        return 'D'
    elif average >= 40:
        return 'E'
    else:
        return 'F'


def grade_runner():
    name = input('Enter Your Name: ').strip()
    subjects = ['APL302', 'APL342', 'CSC303', 'APL322']
    total_score = 0.0

    for subject in subjects:
        valid_input = False
        score = 0.0

        while not valid_input:
            main_score = input('Enter score for ' + subject + ': ')
            score = float(main_score)

            if score >= 0 and score <= 100:
                valid_input = True
            else:
                print('Invalid score! enter score between 0-100')

        total_score = total_score + score

    average = total_score / 4

    grade = course_grader(average)

    if grade == 'A':
        status = 'EXCELLENT'
    elif grade != 'F':
        status = 'PASS'
    else:
        status = 'FAIL'

    print('\n==============================="')
    print('Name: ' + name)
    print('Average: ' + str(round(average, 2)))
    print('Grade: ' + grade)
    print('Status: ' + status)
    print('\n===============================')


keep_running = True
while keep_running:
    grade_runner()
    repeat = input('Do you want to check another student score? (yes/no): ')
    if repeat != 'yes' and repeat != 'y':
        keep_running = False
        print('Program Closed!')
