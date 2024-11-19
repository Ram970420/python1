

def calculate_total(total):
    if total > 600:
        return "Total exceeded"
    if total > 550:
        return "A+"
    if total >= 500:
        return "A"
    if total >= 450:
        return "B"
    if total >= 400:
        return "C"
    if total >= 350:
        return "D"
    if total >= 300:
        return "G"
    else:
        return "F"

def calculate_percentage(total):
    return (total / 600) * 100

def results(name, total, percent, grade):
    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percent:.2f}%")
    print(f"Grade: {grade}")

def main():    
    name = input("Enter your name: ")
    print("Enter your marks: ")
    Telugu = float(input("Telugu: "))
    Hindi = float(input("Hindi: "))
    English = float(input("English: "))
    Maths = float(input("Maths: "))
    Sience = float(input("Sience: "))
    Social = float(input("Social: "))

    total = Telugu + Hindi + English + Maths + Social + Sience

    percent = calculate_percentage(total)
    grade = calculate_total(total)

    results(name, total, percent, grade)

main()