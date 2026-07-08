from statistics import median, mode


def menu() :
    print("\n===== Class Performance Analyzer =====")
    print("1. English Analysis")
    print("2. Math Analysis")
    print("3. Science Analysis")
    print("4. Islamiyat Analysis")
    print("5. Urdu Analysis")
    print("6. Pak Study Analysis")
    print("7. Exit")


def get_choice() :
    valid_choices = ["1", "2", "3", "4", "5", "6", "7"]

    while True :
        choice = input("Enter your choice: ")

        if choice in valid_choices :
            return choice

        print("Invalid choice! Enter again.")


def get_marks() :
    while True :
        try :
            marks = int(input("Enter Marks: "))

            if 0 <= marks <= 100 :
                return marks

            print("Marks must be between 0 and 100.")

        except :
            print("Invalid input! Enter integer marks.")


def collect_marks(class_name, subject) :
    marks_list = []

    print(f"\nEnter {subject} Marks for {class_name}:")

    for student in range(1, 11) :
        print(f"Student {student}:")
        mark = get_marks()
        marks_list.append(mark)

    return marks_list


def calculate_mean(marks) :
    return sum(marks) / len(marks)


def compare_classes(mean1, mean2) :
    if mean1 > mean2 :
        return "Class 1 Performed Better"

    elif mean2 > mean1 :
        return "Class 2 Performed Better"

    else :
        return "Both Classes Performed Equally"


def subject_analysis(subject) :

    class1_marks = collect_marks("Class 1", subject)
    class2_marks = collect_marks("Class 2", subject)

    class1_mean = calculate_mean(class1_marks)
    class2_mean = calculate_mean(class2_marks)

    class1_median = median(class1_marks)
    class2_median = median(class2_marks)

    class1_mode = mode(class1_marks)
    class2_mode = mode(class2_marks)

    result = compare_classes(class1_mean, class2_mean)

    print("\n===== Analysis Report =====")

    print(f"\nSubject: {subject}")

    print("\nClass 1")
    print(f"Marks: {class1_marks}")
    print(f"Mean: {class1_mean:.2f}")
    print(f"Median: {class1_median}")
    print(f"Mode: {class1_mode}")

    print("\nClass 2")
    print(f"Marks: {class2_marks}")
    print(f"Mean: {class2_mean:.2f}")
    print(f"Median: {class2_median}")
    print(f"Mode: {class2_mode}")

    print(f"\nFinal Result: {result}")


while True :

    menu()

    choice = get_choice()

    if choice == "1" :
        subject_analysis("English")

    elif choice == "2" :
        subject_analysis("Math")

    elif choice == "3" :
        subject_analysis("Science")

    elif choice == "4" :
        subject_analysis("Islamiyat")

    elif choice == "5" :
        subject_analysis("Urdu")

    elif choice == "6" :
        subject_analysis("Pak Study")

    elif choice == "7" :
        print("Thank you for using Class Performance Analyzer.")
        break