total_marks = 550


def get_marks() :
    s = int(input("Enter Science Marks (out of 100): "))
    e = int(input("Enter English Marks (out of 100): "))
    m = int(input("Enter Mathematics Marks (out of 100): "))
    u = int(input("Enter Urdu Marks (out of 100): "))
    i = int(input("Enter Islamiyat Marks (out of 100): "))
    p = int(input("Enter Pak Study Marks (out of 50): "))

    return s, e, m, u, i, p


def calculate_percentage(m1, m2, m3, m4, m5, m6) :
    ob_marks = m1 + m2 + m3 + m4 + m5 + m6
    percentage = (ob_marks * 100) / total_marks

    return ob_marks, percentage


def calculate_grade(per) :
    if per >= 90 :
        return "A"
    elif per >= 80 :
        return "B"
    elif per >= 70 :
        return "C"
    elif per >= 60 :
        return "D"
    elif per >= 50 :
        return "E"
    else :
        return "F"


def display_result(ob_marks, percentage, grade) :
    print("\n----- Results -----")
    print(f"Total Marks: {total_marks}")
    print(f"Obtained Marks: {ob_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


sci, eng, math, urd, isl, pak = get_marks()

ob_marks, percentage = calculate_percentage(
    sci, eng, math, urd, isl, pak
)

grade = calculate_grade(percentage)

display_result(ob_marks, percentage, grade)