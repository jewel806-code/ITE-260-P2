def calculate_average(activity1, activity2, activity3):
    return (activity1 + activity2 + activity3) / 3


for student in range(1, 4):

    print("\nStudent", student)
    name = input("Enter name: ")
    activity1 = float(input("Activity 1: "))
    activity2 = float(input("Activity 2: "))
    activity3 = float(input("Activity 3: "))

    average = calculate_average(activity1, activity2, activity3)

    if average >= 90:
        status = "Excellent"
    elif average >= 85:
        status = "Very Good"
    elif average >= 80:
        status = "Good"
    elif average >= 75:
        status = "Passed"
    else:
        status = "Failed"

    print("\nAverage:", round(average, 2))
    print("Status:", status)