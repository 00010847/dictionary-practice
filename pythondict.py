myFinalMarks = {'CSF': 85, 'FunPro': 80, 'WT': 75}

marks = myFinalMarks.values()


def calculate(marks):
    return sum(marks) / len(marks)

average = calculate(marks)
print(average)