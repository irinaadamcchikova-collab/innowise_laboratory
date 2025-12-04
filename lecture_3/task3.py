# Анализатор оценок студентов
# Храним студентов как список словарей: [{'name': 'Alice', 'grades': [95, 88, ...]}, ...]

students = []  # основной список студентов


def print_menu():
    """Выводит меню программы"""
    print("--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")


def add_student():
    """Опция 1: Добавление нового студента"""
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return

    # Проверяем, существует ли уже студент с таким именем
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Student '{name}' already exists!")
            return

    # Создаём нового студента с пустым списком оценок
    students.append({'name': name, 'grades': []})
    print(f"Student '{name}' has been added successfully.")


def add_grades():
    """Опция 2: Добавление оценок для существующего студента"""
    if not students:
        print("No students in the system yet. Add a student first.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty!")
        return

    # Ищем студента
    student = None
    for s in students:
        if s['name'].lower() == name.lower():
            student = s
            break

    if not student:
        print(f"Student '{name}' not found.")
        return

    print(f"Enter grades for {student['name']} (type 'done' to finish):")
    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == 'done':
            break

        # Проверка, что введено число от 0 до 100
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student['grades'].append(grade)
                print(f"Grade {grade} added for {student['name']}.")
            else:
                print("Invalid grade. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")


def calculate_average(grades):
    """Безопасный расчёт среднего (с обработкой пустого списка)"""
    if not grades:
        return None
    return sum(grades) / len(grades)


def generate_report():
    """Опция 3: Полный отчёт по всем студентам"""
    if not students:
        print("No students in the system.")
        return

    print("--- Student Report ---")
    averages = []

    for student in students:
        avg = calculate_average(student['grades'])
        if avg is None:
            print(f"{student['name']}'s average grade is N/A.")
        else:
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)

    # Общая статистика
    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)
        print("---------------------------")
        print(f"Max Average: {max_avg:.1f}")
        print(f"Min Average: {min_avg:.1f}")
        print(f"Overall Average: {overall_avg:.1f}")
    else:
        print("No grades available to calculate statistics.")


def find_top_student():
    """Опция 4: Поиск студента с наивысшим средним баллом"""
    if not students:
        print("No students in the system.")
        return

    # Фильтруем студентов с хотя бы одной оценкой
    valid_students = [s for s in students if s['grades']]

    if not valid_students:
        print("No students have grades yet.")
        return

    # Используем max() с lambda-ключом по среднему баллу
    top_student = max(valid_students, key=lambda s: calculate_average(s['grades']))
    top_avg = calculate_average(top_student['grades'])

    print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")
def main():
    """Основной бесконечный цикл программы"""
    print("Welcome to the Student Grade Analyzer!")

    while True:
        print_menu()
        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                add_grades()
            elif choice == "3":
                generate_report()
            elif choice == "4":
                find_top_student()
            elif choice == "5":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")


        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Запуск программы
if __name__ == "__main__":
    main()