for students in range(1, 17):
    student_name = input(f'\nEnter the name of student NO.{students}: ')
    score_1 = int(input('Enter test score 1: '))
    score_2 = int(input('Enter test score 2: '))
    score_3 = int(input('Enter test score 3: '))
    score_4 = int(input('Enter test score 4: '))
    average = (score_1 + score_2 + score_3 + score_4) / 4
    print(f"The average score of {student_name} is {average}")
