import numpy as np
if __name__ == '__main__':
    fyp = 3.2
    sem_one = 3.48
                    #
    sem_two = np.divide(3.6 + 4.0 + 2.8 + 3.0, 4)

    fyp *= 3
    sem_one *= 5
    sem_two *= 4

    average = np.divide(fyp + sem_one + sem_two, 12)

    third_year_sem_one = 2.97 # from sisweb
    third_year_sem_two = 2.76666666667 # slight change due to a stage 2 repeat(logic)

    third_year_gpa = np.divide(third_year_sem_one + third_year_sem_two, 2)

    thirty = third_year_gpa * 0.3
    seventy = average * 0.7

    gpa = thirty + seventy

    print(gpa)
    stage_4_sisweb = 3.37 * 0.7
    print("direct from sisweb: ")
    print(str((2.87 * 0.3) + stage_4_sisweb))
    print()

    if gpa >= 3.67:
        print("1.1")
    elif gpa >= 3.08:
        print("2.1")
    elif gpa >= 2.48:
        print("2.2")
    elif gpa >= 2.0:
        print("3.1")
    else:
        print("FAIL")