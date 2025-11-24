# FINAL COMBINED VERSION - Student Marks Analyzer

def get_student_marks():
    marks = []
    print("Enter marks for each student (press 'q' to stop):")
    while True:
        mark = input("Enter mark: ")
        if mark.lower() == 'q':
            break
        try:
            marks.append(float(mark))
        except:
            print("Invalid input! Enter a number or 'q' to quit.")
    return marks

def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks) if marks else 0

def find_highest(marks):
    return max(marks) if marks else 0

def generate_report(marks):
    if not marks:
        print("No marks entered!")
        return
        
    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    
    print("\n" + "="*40)
    print("STUDENT MARKS ANALYSIS REPORT")
    print("="*40)
    print(f"Number of students: {len(marks)}")
    print(f"Total marks: {total}")
    print(f"Average mark: {average:.2f}")
    print(f"Highest mark: {highest}")
    print("="*40)

# Main program
def main():
    print("=== Student Marks Analyzer ===")
    marks = get_student_marks()
    generate_report(marks)

if __name__ == "__main__":
    main()