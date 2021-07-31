def count_substring(string, sub_string):
    s = len(string)
    s1 = len(sub_string)
    p = 0
    aux = s - s1 
    for a in range(aux+1):
        if string[a:a+s1] == sub_string:
            p +=1
    return p 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)