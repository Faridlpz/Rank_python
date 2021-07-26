if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() # ejemplo name = farid|||| *line = [23,34,56] split me separa mis datos 23 34 67
        scores = list(map(float, line)) 
        student_marks[name] = scores
    query_name = input()
    suma = [ sum(student_marks[add])/3 for add in student_marks if query_name == add]
    for i in suma:
        print("{:.2f}".format(i))