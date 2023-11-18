import random

def first_task():
    a = random.choice(range(1, 1000))
    b = random.choice(range(1, 1000)) 
    if a + b >= 1000:
        print(a * b)
    else:
        print(a + b)

def second_task():
    lst = [x for x in range(1, 11)]
    result = []
    for i in range(len(lst) - 1):
        result.append(lst[i] + lst[i + 1])
    print(result)

def third_task():
    number_of_students = random.randint(1, 10)
    height_list = []
    for _ in range(number_of_students):
        height_list.append(random.randint(150, 210))
    average_height = sum(height_list) / number_of_students
    print(average_height)

def fourth_task():
    a = [x for x in range(1, 36)]
    print (sum(a[1::3])) 

def fifth_task():
    a = [x for x in range(1, 10)]
    b = [1] * len(a)
    for i in range(len(a)):
        b[i] = b[i] / a[i]
    print(sum(b))

def sixth_task():
    lst_of_numbers = [x for x in range(1, 114)]
    lower_number = [x for x in lst_of_numbers if x % 2 != 0]
    upper_number = [x for x in range(2, 114) if x % 2 == 0]
    lower_number = lower_number[:len(upper_number)]
    result  = []
    for i in range(len(upper_number)):
        result.append(upper_number[i] / lower_number[i])
    print(sum(result))
    
def seventh_task():
    lst = [3] * 7
    i = 0
    result = 3
    while i < len(lst) - 1:
        result *= lst[i] 
        i += 1
    print(result)
    
def eighth_task():
    upper_numbers = [1, 2]
    lower_numbers = [1, 1]
    result = []
    i = 0 
    while i < 10:
        upper_numbers.append(sum(upper_numbers[-2:]))  
        lower_numbers.append(sum(lower_numbers[-2:]))  
        i += 1
    for k in range(len(upper_numbers)):
        if lower_numbers[k] != 0:
            result.append(upper_numbers[k] / lower_numbers[k]) 
    print(result[5]) 

def ninth_task():
    number = 123
    lst = [int(x) for x in str(number)] 
    print(lst)

def tenth_task():
    seconds = random.choice(range(40, 81))
    minutes, remaining_seconds = divmod(seconds, 60)
    time = [minutes, remaining_seconds]
    print(time)
    
def eleventh_task():
    n = 9
    result = ""
    for i in range(1, n+1):  
        result += str(i) * i + "\n"  
    print(result)

def twelfth_task():
    a = random.choice(range(10, 100))
    result = []
    i = 1
    while i <= a:
        if a % i == 0:
            result.append([a // i, i])
        i += 1 
    print(a)
    print (result)


def thirteenth_task():
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2: 
            return True
        if n % 2 == 0: 
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    a = random.randint(1, 1000)
    b = random.randint(1, 1000) 
    result = [] 
    for x in range(min(a, b), max(a, b)):
        if is_prime(x): 
            result.append(x)
    print(result)
    
def solutions():
    first_task()
    second_task()
    third_task()
    fourth_task()
    fifth_task()
    sixth_task()
    seventh_task()
    eighth_task()
    ninth_task()
    tenth_task()
    eleventh_task()
    twelfth_task()
    thirteenth_task()
    
    
solutions()
