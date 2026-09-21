def practice_grade(average):
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


def runner_grade():
    name = input('Enter your name: ').strip()
    subjects = ['RAP401', 'RAP404', 'RAP433']
    total = 0.0

    for subject in subjects:
        valid_input = False
        score = 0.0

        while not valid_input:
            main_score = input('Enter Score for ' + subject + ': ')
            score = float(main_score)

            if score >= 0 and score <= 100:
                valid_input = True
            else:
                print('Enter valid score!')
                
        total = total + score

    average = total / 3

    grade = practice_grade(average)

    if grade == 'A':
        status = 'Excellent'
    elif grade != 'F':
        status = 'Pass'
    else:
        status = 'Fail'


    print('\n============================')
    print('Name: ' + name)
    print('Average: ' + str(round(average)))
    print('Grade: ' + grade)
    print('Status: ' + status)
    print('============================')


keep_running = True
while keep_running:
    runner_grade()
    repeat = input('Do you want to continue? (yes/no)')
    if repeat != 'yes' and repeat != 'y':
        keep_running = False
        print('Program Closed!')
        
