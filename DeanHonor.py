def get_deans_list_and_honors():
    deans_list = []
    honors = []

    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            deans_list.append((first_name, last_name))
        elif gpa >= 3.25:
            honors.append((first_name, last_name))

    return deans_list, honors

deans_list, honors = get_deans_list_and_honors()

print("Students who qualify for the Dean's List:")
for student in deans_list:
    print(f"{student[0]} {student[1]}")

print("Students who made the Honor Roll:")
for student in honors:
    print(f"{student[0]} {student[1]}")
