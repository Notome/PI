#почти везде 4 и 6 варианты
#использовать только в кач-ве образца
#4-6 варианты заняты, смотреть на коды и делать свои варианты 
#возможны синтаксические ошибки

import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from itertools import permutations 

#3 задание 
def lab_3_2_1(x=0, y=0, x1=-4, y1=0, x2=0, y2=4, x3=4, y3=0):
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ABC = area(x1, y1, x2, y2, x3, y3)
    PBC = area(x, y, x2, y2, x3, y3)
    PAC = area(x1, y1, x, y, x3, y3)
    PAB = area(x1, y1, x2, y2, x, y)
    print(ABC == PBC + PAC + PAB) 
lab_3_2_1()    

def lab_3_2_2(x=0, y=0, radius=3, x1=0, y1=0, x2=0, y2=3, x3=6, y3=0):
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ins_circ = x**2 + y**2 <= radius ** 2 and x <= 0 and y >= 0
    ABC = area(x1, y1, x2, y2, x3, y3)
    PBC = area(x, y, x2, y2, x3, y3)
    PAC = area(x1, y1, x, y, x3, y3)
    PAB = area(x1, y1, x2, y2, x, y)
    print(ABC == PBC + PAC + PAB and ins_circ) 
lab_3_2_2()

def lab_3_2_3(x=0, y=0, radius1=4, radius2= 3):
    ins_circ1= x**2 + y**2 <= radius1**2 and x >= 0 
    ins_circ2= x**2 + y**2 <= radius2**2 and x >= 0 
    print(ins_circ1 and not ins_circ2)
lab_3_2_3()

def lab_3_2_4(x=0, y=0, x1=-6, y1=0, x2=0, y2=-6, x3=6, y3=0):
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ABC = area(x1, y1, x2, y2, x3, y3)
    PBC = area(x, y, x2, y2, x3, y3)
    PAC = area(x1, y1, x, y, x3, y3)
    PAB = area(x1, y1, x2, y2, x, y)
    print(ABC == PBC + PAC + PAB)
lab_3_2_4()

def lab_3_2_5(x=0, y=0):
    ins_1rec = y >= 0 and y <= 4 and x >= -2 and x <= 1
    ins_2rec = y <= 0 and y >= -3 and x >= -4 and x <= 4
    print(ins_1rec or ins_2rec)
lab_3_2_5() 

def lab_3_2_6(x=0, y=0, radius1= 6, radius2=3):
    ins1_circ = x**2 + y**2 <= radius1 ** 2 and y >= 0 and x <= 0
    ins2_circ = x**2 + y**2 <= radius1 ** 2 and y >= 0 and x >= 0 
    ins3_circ = x**2 + y**2 <= radius2 ** 2 and y >= 0 and x >= 0 
    print(ins1_circ or ins2_circ and not ins3_circ)
lab_3_2_6()

def lab_3_2_7(x=0, y=0, x1=1, y1=4, x2=4, y2=7, x3=7, y3=4, x4=4, y4=1):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    total_area = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x3, y3, x4, y4)
    area1 = area(x, y, x1, y1, x2, y2)
    area2 = area(x, y, x2, y2, x3, y3)
    area3 = area(x, y, x3, y3, x4, y4)
    area4 = area(x, y, x4, y4, x1, y1)
    print(total_area == (area1 + area2 + area3 + area4))
lab_3_2_7()

#lab_3_2_8 см. 5
#lab_3_2_9 см. 6 
#lab_3_2_10 см. 5 
#lab_3_2_11 cм. 5 
#lab_3_2__12 см. 2 
#lab_3_2__13 см. 5

def lab_3_2_14(x=0, y=0, x1=-4, y1=0, x2=0, y2= 4, x3=4, y3=0, x4=0, y4=-4):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
    total_area1 = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x3, y3, x4, y4)
    total_area2 = area(x1+2, y1, x2, y2-2, x3-2, y3) + area(x1+2, y1, x3-2, y3, x4, y4+2)
    area1 = area(x, y, x1, y1, x2, y2)
    area2 = area(x, y, x2, y2, x3, y3)
    area3 = area(x, y, x3, y3, x4, y4)
    area4 = area(x, y, x4, y4, x1, y1)
    area1_2 = area(x, y, x1+2, y1, x2, y2-2)
    area2_2 = area(x, y, x2, y2-2, x3-2, y3)
    area3_2 = area(x, y, x3-2, y3, x4, y4+2)
    area4_2 = area(x, y, x4, y4+2, x1+2, y1)
    print (total_area1 == (area1 + area2 + area3 + area4) and not total_area2 == (area1_2 + area2_2 + area3_2 + area4_2))
lab_3_2_14()

#lab_3_2_15 см. 6 условие y >= 2 and y <= 6 

def lab_3_2_16(x=0, y=0, radius= 3, x1=-1, y1=0, x2=-1, y2=3, x3=-4, y3=3, x1_2 = -1, y1_2 = 0, x2_2 = -1, y2_2 = -3, x3_2 = -4, y3_2 = -3):
    ins_circ = x ** 2 + y ** 2 <= radius ** 2 and x >= -1
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ABC_1 = area(x1, y1, x2, y2, x3, y3)
    PBC_1 = area(x, y, x2, y2, x3, y3)
    PAC_1 = area(x1, y1, x, y, x3, y3)
    PAB_1 = area(x1, y1, x2, y2, x, y)
    ABC_2 = area(x1_2, y1_2, x2_2, y2_2, x3_2, y3_2)
    PBC_2 = area(x, y, x2_2, y2_2, x3_2, y3_2)
    PAC_2 = area(x1_2, y1_2, x, y, x3_2, y3_2)
    PAB_2 = area(x1_2, y1_2, x2_2, y2_2, x, y)
    print(ins_circ or ABC_1 == PBC_1 + PAC_1 + PAB_1 or ABC_2 == PBC_2 + PAC_2 + PAB_2)
lab_3_2_16()

#lab_3_2_17 см. 2 , 2 треугольника
#lab_3_2_18 см. 2, 6: 2 квадрата и триугольник 
#T2_19 см. T2_2, круг и треугольник 

def T2_20(x=1, y=2, radius1=2, radius2=2):
    center1_x, center1_y = 0, 3
    center2_x, center2_y = 1, 0
    
    in_both_circles = ((x - center1_x) ** 2 + (y - center1_y) ** 2 <= radius1 ** 2) and ((x - center2_x) ** 2 + (y - center2_y) ** 2 <= radius2 ** 2)
    in_first_circle = ((x - center1_x) ** 2 + (y - center1_y) ** 2 <= radius1 ** 2) and (y <= math.e ** x)
    in_second_circle = ((x - center2_x) ** 2 + (y - center2_y) ** 2 <= radius2 ** 2) and (y >= math.e ** x)
    
    result = in_both_circles or in_first_circle or in_second_circle
    
    print(result)
T2_20()

#T2_21 см. T2_2 круг с ограничением

def T2_22(x=-5, y=-1, radius1=3, radius2=1): #x не может быть 0
    center_x, center_y = -3, -3
    in_first_circle = (x - center_x) ** 2 + (y - center_y) ** 2 <= radius1 ** 2 and y <= 4 / x or y >= 4 * x 
    in_second_circle = x ** 2 + y ** 2 <= radius2 ** 2 and y <= 4 / x or y >= 4 * x  
    print(in_first_circle or in_second_circle) 
T2_22()

#T2_23 см. T2_2 
#T2_24 см. T2_2
#T2_25 см. T2_2
#T2_26 см. T2_2, T2_6 
#T2_27 см. T2_2 треугольник с ограничениями y >= 1 and y <= 6 
#T2_28 см. T2_2 
#T2_29 cм. T2_2 
#T2_30 см. T2_2 

def T2_31(x=0, y=0, radius=6):
    is_inside_circle = x**2 + y**2 <= radius**2
    is_not_in_first_quadrant = x <= 0 and y <= 0

    print(is_inside_circle and is_not_in_first_quadrant)
T2_31()

#T2_32 квадрат и 3 круга, один полный, 2 с ограничением x >= 0 y <= 0 с разным радиусом 
#T2_33 не помню где ромб у меня, там ромб с ограничением и круг 
#T2_34 см. T2_22 идет не в круге, больше обеих прямых, но y <= 4 
#T2_35 см. T2_2 
#T2_36 см. T2_22 
#T2_37 см. T2_6 

def T2_38(x = 0, y = 0):
    x_center, y_center, radius = 0, 2, 1
    parab = y >= x ** 2 - 7 and y <= 2
    square = x >= -1 and x <= 1 and y >= -3 and y <=2 #not
    circ = (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
    x1, x2, x3, x4 = -3, -1, 1, 3
    y1, y2, y3, y4 = 2, 4, 4, 2
    total_area = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x3, y3, x4, y4)
    area1 = area(x, y, x1, y1, x2, y2)
    area2 = area(x, y, x2, y2, x3, y3)
    area3 = area(x, y, x3, y3, x4, y4)
    area4 = area(x, y, x4, y4, x1, y1)
    print((total_area == (area1 + area2 + area3 + area4)) or circ or parab and not square)
T2_38()

#T2_39 см. T2_6 
#T2_40 см. T2_2


def lab_4_1_4(x, y):
    if x != y:
        if min(x, y) == x:
            x, y = (x + y) / 2, x * y * 2
        else:
            y, x = (x + y) / 2, x * y * 2
    return x, y

print(lab_4_1_4(1, 2))

def lab_4_1_6(m, n):
    if m == n: 
        m, n = 0, 0
    else: 
        m, n = max(m, n), max(m, n) 
    return m, n 

print(lab_4_1_6(1, 2))

def lab_4_2_4(n): 
    numsto = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 
              5:'Five', 6: 'Six', 7: 'Seven', 8:'Eight', 9: 'Nine'}
    return numsto.get(n, 'Не цифра')

print(lab_4_2_4(1)) 

def lab_4_2_6(n):
    points = {1:'плохо', 2:'неудовлитварительно', 3:'удовлитварительно', 4: 'хорошо', 5:'отлично'}
    return points.get(n, 'От 1 до 5')

print(lab_4_2_6(5))

def lab_5_1_4():
    x = -9
    h = 0.1  

    while x <= 9:
        if x <= -6: y = -7 + np.sqrt(9 - (x + 9)**2)
        elif x <= -4: y = y
        elif x <= -3: y = 5*x + 13
        elif x <= -2: y = x + 1
        elif x <= 7: y = -2/3 * x - 7/3
        else: y = 1/2 * x - 21/2
        print(f"x = {x}, y = {y}")
        x += h
lab_5_1_4()

def lab_5_1_6(): 
    x = -9 
    h = 0.1

    while x <= 10:
        if x <= -8: y = -5 - np.sqrt(1 - (x + 9) ** 2)
        elif x <= -7: y = -4 - np.sqrt(1 - (x + 8) ** 2)
        elif x <= -2: y = -3/5 * x - 41/5
        elif x <= 3: y = 9/5 * x - 17/5
        elif x <= 6: y = -1/3 * x + 3
        elif x <= 7: y = 2 - np.sqrt(1 - (x - 6) ** 2)
        elif x >= 7 and x <= 8: y = -0.8125*x + 8.75
        elif x <= 10: y = 2 - np.sqrt(4 - (x - 10) ** 2)
        
        print(f"x = {x}, y = {y}")
        x += h
lab_5_1_6()

def lab_5_2_4():
    h = 0.1

    for x in np.arange(-9, 9+h, h):
        if x <= -6: y = -7 + np.sqrt(9 - (x + 9)**2)
        elif x <= -4: y = y
        elif x <= -3: y = 5*x + 13
        elif x <= -2: y = x + 1
        elif x <= 7: y = -2/3 * x - 7/3
        else: y = 1/2 * x - 21/2
        print(f"x = {x}, y = {y}")
lab_5_2_4()

def lab_5_2_6():
    h = 0.1

    for x in np.arange(-9, 10+h, h):
        if x <= -8: y = -5 - np.sqrt(1 - (x + 9) ** 2)
        elif x <= -7: y = -4 - np.sqrt(1 - (x + 8) ** 2)
        elif x <= -2: y = -3/5 * x - 41/5
        elif x <= 3: y = 9/5 * x - 17/5
        elif x <= 6: y = -1/3 * x + 3
        elif x <= 7: y = 2 - np.sqrt(1 - (x - 6) ** 2)
        elif x <= 10: y = 2 - np.sqrt(4 - (x - 10) ** 2)
        print(f"x = {x}, y = {y}")
lab_5_2_6() 

def lab_6_1_4(start_x, end_x, step):
    def calculate_angle(x, y):
        if x <= y:
            return None
        angle_rad = math.acos(y / x)  
        angle_deg = math.degrees(angle_rad)  
        return angle_deg
    
    for y in range(2, 4, step):
        for x in range(start_x, end_x + 1):
            angle = calculate_angle(x, y)
            if angle is not None:
                print(f'При x = {x} м, y = {y} м, угол a = {angle} градусов')
            else:
                print(f'При x = {x} м, y = {y} м, невозможно вычислить угол')
lab_6_1_4(1, 10, 1)

def lab_6_1_6():
    def task(total_head, total_cost)
        for bulls in range(total_head + 1):
            for cows in range(total_head + 1):
                calfs = total_head - bulls - cows
                if calfs >= 0:
                    cost = 10 * bulls + 5 * cows + 0.5 * calfs
                    if cost == total_cost:
                        return bulls, cows, calfs
        return None, None, None
    
    total_head = 100
    total_cost = 100
    b, co, ca = task(total_head, total_cost)
    
    print(f"Количество быков: {b}")
    print(f"Количество коров: {co}")
    print(f"Количество телят: {ca}")
lab_6_1_6()

def lab_7_1_4():
    x = -9
    h = 0.1  
    x_values = []
    y_values = []

    while x <= 9:
        if x <= -6: y = -7 + np.sqrt(9 - (x + 9)**2)
        elif x <= -4: y = y
        elif x <= -3: y = 5*x + 13
        elif x <= -2: y = x + 1
        elif x <= 7: y = -2/3 * x - 7/3
        else: y = 1/2 * x - 21/2
        x_values.append(x)
        y_values.append(y)
        x += h

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid(True)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.savefig('graph_lab.png', format='png')

    plt.show()
    img = Image.open('graph_image.png')
    img.save('graph_image_pillow.png', 'PNG')
lab_7_1_4()

def lab_7_1_6():
    x = -9 
    h = 0.1
    x_values = []
    y_values = []

    while x <= 10:
        if x <= -8: y = -5 - np.sqrt(1 - (x + 9) ** 2)
        elif x <= -7: y = -4 - np.sqrt(1 - (x + 8) ** 2)
        elif x <= -2: y = -3/5 * x - 41/5
        elif x <= 3: y = 9/5 * x - 17/5
        elif x <= 6: y = -1/3 * x + 3
        elif x <= 7: y = 2 - np.sqrt(1 - (x - 6) ** 2)
        elif x >= 7 and x <= 8: y = -0.8125*x + 8.75
        else: y = 2 - np.sqrt(4 - (x - 10) ** 2)

        x_values.append(x)
        y_values.append(y)
        x += h
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid(True)
    plt.savefig('graph_image.png')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.show()
    img = Image.open('graph_image.png')
    img.save('graph_image_pillow.png', 'PNG')
lab_7_1_6()

def lab_7_2_4(x1=-6, y1=0, x2=0, y2=-6, x3=6, y3=0):
    image = Image.new('RGB', (200, 200), 'white')
    draw = ImageDraw.Draw(image)
    
    points = [(x1+100, 100-y1), (x2+100, 100-y2), (x3+100, 100-y3)]
    draw.polygon(points, fill='blue')

    image.show()
    image.save('724.png', 'PNG')
lab_7_2_4()

def lab_7_2_6():
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)

    draw.pieslice((50, 50, 350, 350), 180, 270, fill='black')
    draw.pieslice((50, 50, 350, 350), 270, 360, fill='black')
    draw.pieslice((100, 100, 300, 300), 270, 360, fill='white')

    img.show()
    img.save('726.png', 'PNG')
lab_7_2_6()

def lab_7_3_4():
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    draw.ellipse([100, 100, 300, 300], fill='red')
    draw.rectangle([190, 60, 210, 100], fill='brown')
    draw.polygon([(170, 120), (140, 110), (160, 70), (200, 90)], fill='green')
    img.save('apple.png')
    img.show()
lab_7_3_4()

def lab_7_3_6():
    img = Image.new('RGB', (400, 300), color='white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([(50, 50), (350, 250)], outline='black') 
    draw.rectangle([(70, 70), (330, 200)], outline='black') 
    draw.rectangle([(50, 200), (350, 250)], fill='gray')    
    key_width = 50
    key_height = 20
    key_padding = 5
    for i in range(5):
        key_left = 60 + i * (key_width + key_padding)
        key_top = 205
        key_right = key_left + key_width
        key_bottom = key_top + key_height
        draw.rectangle([(key_left, key_top), (key_right, key_bottom)], outline='black', fill='white')
    for i in range(5):
        key_left = 60 + i * (key_width + key_padding)
        key_top = 230
        key_right = key_left + key_width
        key_bottom = key_top + key_height
        draw.rectangle([(key_left, key_top), (key_right, key_bottom)], outline='black', fill='white')
    img.save('laptop.png')
    img.show()
lab_7_3_6() 

def lab_8_1_4(sum=0, count=0):
    num = input("Введите число (или '*' для завершения): ")
    
    if num == '*':
        if count == 0:
            print("Вы не ввели ни одного числа.")
        else:
            average = sum / count
            print(f"Среднее значение элементов массива: {average}")
    else:
        sum += float(num)
        count += 1
        lab_8_1_4(sum, count)
lab_8_1_4()

def lab_8_1_6(lst=None):
    if lst is None:
        lst = []

    num = input('Введите число (или \'*\' для завершения): ')

    if num == '*':
        if not lst:
            print('Список пустой')
            return None
        else:
            return sum([int(x) for x in lst if x < 0])
    else:
        lst.append(int(num))
        print(lst)
        return lab_8_1_6(lst)
lab_8_1_6()

def lab_8_2_4(lst=[1,2,3,4,5]):
    print(lst == sorted(lst)) 
lab_8_2_4()

def lab_8_2_6(lst=[1,2,3,4,5,6,7,8], Z=5):
    count = 0 
    for i in range(len(lst)):
        if lst[i] > Z:
            lst[i] = Z
            count += 1
    print(count,lst,Z)
lab_8_2_6() 

def lab_9_2_4(string='01010101010010010101001010101010'):
    zeros, ones = '0' * string.count('0'), '1' * string.count('1')
    print(zeros + ones)
lab_9_2_4()

def lab_9_2_6(lst=[1,2,3,4,5,6,7,8,9,10,11,12,13]):
    ind1, ind2 = 0, -1 
    new_lst = []
    for _ in range(len(lst) // 2):
        new_lst.append(lst[ind1] + lst[ind2])
        ind1 += 1 
        ind2 -= 1 
    print(new_lst)
lab_9_2_6()

def matrix_generatror(m, n):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(-9, 9)
    #matrix = np.array(matrix) 
    return matrix 

def lab_10_1_4():
    def task(matrix):
        average = np.mean(matrix)
        
        count_greater = np.sum(matrix > average)
        count_less = np.sum(matrix < average)
        
        if count_greater > count_less:
            result = f"элементов больше среднего ({count_greater}), чем меньше ({count_less})."
        elif count_less > count_greater:
            result = f"элементов меньше среднего ({count_less}), чем больше ({count_greater})."
        else:
            result = "Количество элементов больше и меньше среднего равны."
        
        return average, result
    
    a= matrix_generatror(3,3)
    print(a)
    print(task(a))
lab_10_1_4()

def lab_10_1_6():
    def task(matrix):
        max_abs_element = np.max(np.abs(matrix)) 
        new_matrix = matrix / max_abs_element  
        return new_matrix
        
    b= matrix_generatror(3,3)
    print(b)
    print(task(a))
lab_10_1_6()

def lab_10_2_4():
    def task(matrix):
        answer = []
        for i in range(len(matrix[0])): 
            count = 0
            for j in range(len(matrix)):  
                if matrix[j][i] < 0:
                    count += 1
            answer.append(count)
        return answer
    
    c= matrix_generatror(3,3)
    print(c)
    print(task(c))
lab_10_2_4()

def lab_10_2_6():
    def task(matrix):
        result = []
        for col in range(len(matrix[0])):
            column_sum = 0
            for row in range(len(matrix)):
                if row % 2 == 1:  
                    column_sum += matrix[row][col]
            result.append(column_sum)
        return matrix 

    d= matrix_generatror(2,2)
    print('\n',d)
    print(task(d))
lab_10_2_6()

def lab_10_3_4():
    def task(matrix):
        N = len(matrix) // 2
        for i in range(N):
            for j in range(N):
                matrix[i][j], matrix[i + N][j + N] = matrix[i + N][j + N], matrix[i][j]
        return matrix
    
    e = matrix_generatror(2,2)
    print('\n',e)
    print(task(e))
lab_10_3_4()
    
def lab_10_3_6():
    def task(matrix):
        min_element = min(matrix[i][i] for i in range(len(matrix)))
        min_index = [i for i in range(len(matrix)) if matrix[i][i] == min_element][0]
    
        new_matrix = []
        for i in range(len(matrix)):
            if i != min_index:
                new_row = []
                for j in range(len(matrix)):
                    if j != min_index:
                        new_row.append(matrix[i][j])
                new_matrix.append(new_row)
    
        return new_matrix
    
    f = matrix_generatror(3,3)
    print('\n',f) 
    print(task(f))
lab_10_3_6()

def lab_10_4_4():
    def task(N):
        matrix = [[0] * N for _ in range(N)]  
    
        for i in range(N):
            for j in range(N):
                if i == j:  
                    matrix[i][j] = 1
                elif i < j: 
                    matrix[i][j] = j - i + 1
                else: 
                    matrix[i][j] = i - j + 1
    
        return np.array(matrix)
    
    g = 3 
    print('\n', task(g))
lab_10_4_4()

def lab_10_4_6():
    def task(matrix):
        if not matrix or not matrix[0]:
            return []
        
        result = []
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1
        
        while row_begin <= row_end and col_begin <= col_end:
            for j in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][j])
            row_begin += 1
            for i in range(row_begin, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1
            if row_begin <= row_end:
                for j in range(col_end, col_begin - 1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1
        return result
    
    g1 = matrix_generatror(3, 3)
    print('\n',task(g1))
lab_10_4_6()

def lab_11_1_4():
    def task(N):
        matrix = [[0] * N for _ in range(N)]  
        i, j = 1, 2 
        for x in range(N):
            for y in range(N):
                if x == y:
                    matrix[x][y] = i * j 
                    i += 1
                    j += 1
        return np.array(matrix) 
    h = 3 
    print('\n', task(h))
lab_11_1_4()

def lab_11_1_6():
    def task(N):
        matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if j >= N - i:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = i + 1
        return np.array(matrix)
    
    j = 9
    print(task(j)) 
lab_11_1_6()

def lab_11_2_4():
    def task(matrix):
        print(matrix)
        for row in matrix:
            if len(row) < 2:
                continue
            
            max_val = max(row)
            min_val = min(row)
            
            max_index = row.index(max_val)
            min_index = row.index(min_val)
            
            row[0], row[max_index] = row[max_index], row[0]
            row[-1], row[min_index] = row[min_index], row[-1]
        
        return matrix
    
    k = matrix_generatror(3, 3)
    print(task(k))
lab_11_2_4()

def lab_11_2_6():
    def task(matrix):
        print(np.array(matrix))
        saddle_points = []
        for i in range(len(matrix)):
            row = matrix[i]
            min_in_row = min(row)
            col_index = row.index(min_in_row)
            if all(row[col_index] >= matrix[j][col_index] for j in range(len(matrix))):
                saddle_points.append((i, col_index))
        
        return saddle_points
    
    l = matrix_generatror(3, 3)
    print(task(l)) 
lab_11_2_6()

def lab_12_1_4():
    def task(string):
        return string.count('*') + string.count(';') + string.count(':') 
    m = '123124;:*vkdfnwvjnjnqewjcnwejhcbje' 
    print(task(m))
lab_12_1_4()

def lab_12_1_6():
    def task(string):
        return string.index(':') + 1 
    n = '123456789:'
    print(task(n))
lab_12_1_6()

def lab_12_2_4():
    def task(lst):
        return sorted(lst) 
    o = ['cde', 'abc', 'bcd']
    print(task(o))
lab_12_2_4()

def lab_12_2_6():
    def task(string):
        vowels = ['а', 'е', 'у', 'ы', 'о', 'э', 'я', 'и', 'ю', 'ё']
        vowels_c, conson_c = 0, 0
        for x in string:
            if x in vowels:
                vowels_c += 1
            else:
                conson_c += 1 
        return f'Количество гласных: {vowels_c}, согласных: {conson_c}'
    p = 'абвгдеё' 
    print(task(p))
lab_12_2_6()

def lab_13_1_4():
    def calculate_y(x):
        F1 = lambda num: -7 + np.sqrt(9 - (num + 9)**2)
        F2 = lambda num: None
        F3 = lambda num: 5*num + 13
        F4 = lambda num: num + 1
        F5 = lambda num: -2/3 * num - 7/3
        F6 = lambda num: 1/2 * num - 21/2

        return (
            F1(x) if x <= -6 else
            F2(x) if x <= -4 else
            F3(x) if x <= -3 else
            F4(x) if x <= -2 else
            F5(x) if x <= 7 else
            F6(x)
        )

    x = -9
    h = 0.1  

    while x <= 9:
        y = calculate_y(x)
        print(f"x = {x}, y = {y}")
        x += h
lab_13_1_4()

def lab_13_1_6():
    def calculate_y(x):
        F1 = lambda num: -5 - np.sqrt(1 - (num + 9) ** 2)
        F2 = lambda num: -4 - np.sqrt(1 - (num + 8) ** 2)
        F3 = lambda num: -3/5 * num - 41/5
        F4 = lambda num: 9/5 * num - 17/5
        F5 = lambda num: -1/3 * num + 3
        F6 = lambda num: 2 - np.sqrt(1 - (num - 6) ** 2)
        F7 = lambda num: -0.8125*num + 8.75
        F8 = lambda num: 2 - np.sqrt(4 - (num - 10) ** 2)

        return (
            F1(x) if x <= -8 else
            F2(x) if x <= -7 else
            F3(x) if x <= -2 else
            F4(x) if x <= 3 else
            F5(x) if x <= 6 else
            F6(x) if x <= 7 else
            F7(x) if x >= 7 and x <= 8 else
            F8(x) if x <= 10 else None
        )

    x = -9
    h = 0.1

    while x <= 10:
        y = calculate_y(x)
        print(f"x = {x}, y = {y}")
        x += h
lab_13_1_6()

def lab_13_2_4():
    def get_number():
        num = input("Введите число (или '*' для завершения): ")
        return num

    def calculate_average(sum, count):
        if count == 0:
            print("Вы не ввели ни одного числа.")
        else:
            average = sum / count
            print(f"Среднее значение элементов: {average}")

    def process_numbers(sum=0, count=0):
        num = get_number()
        
        if num == '*':
            calculate_average(sum, count)
        else:
            sum += float(num)
            count += 1
            process_numbers(sum, count)

    process_numbers()
lab_13_2_4()

def lab_13_2_6():
    def get_number():
        num = input('Введите число (или \'*\' для завершения): ')
        return num

    def process_list(lst):
        if not lst:
            print('Список пустой')
            return None
        else:
            return sum([int(x) for x in lst if x < 0])

    def collect_numbers(lst=None):
        if lst is None:
            lst = []

        num = get_number()

        if num == '*':
            return process_list(lst)
        else:
            lst.append(int(num))
            print(lst)
            return collect_numbers(lst)

    result = collect_numbers()
    print(f"Сумма отрицательных чисел в списке: {result}")
lab_13_2_6()

def lab_13_3_4():
    def task(matrix):
        def check1(x):
            return x < 0
        columns = len(matrix[0])
        counts = [0] * columns
    
        for row in matrix:
            for i in range(columns):
                if check1(row[i]):
                    counts[i] += 1
    
        return counts
    
    c_2 = matrix_generatror(3,3)
    print('\n',np.array(c_2))
    print(task(c_2))
lab_13_3_4()

def lab_13_3_6():
    def task(matrix):
        def calculate_column_sum(matrix, col):
            column_sum = 0
            for row in range(len(matrix)):
                if row % 2 == 1:
                    column_sum += matrix[row][col]
            return column_sum
        result = []
        for col in range(len(matrix[0])):
            column_sum = calculate_column_sum(matrix, col)
            result.append(column_sum)
        return result
    
    d_2= matrix_generatror(3,3)
    print('\n',np.array(d_2))
    print(task(d_2))
lab_13_3_6()

def lab_14_4_4(a, b, c, d):
    def perms(n1, n2, n3, n4):
        lst = [n1, n2, n3, n4]
        lst = list(permutations(lst, 3))
        lst = list(map(sorted, lst))  # Применяем функцию sorted к каждому элементу списка
        return lst

    def check_triangle(sides):
        a, b, c = sorted(sides)
        if a + b > c and b + c > a and a + c > b:
            return True
        return False

    def check_triangle_type(segment):
        a, b, c = sorted(segment)
        if a == b == c:
            return "Равносторонний треугольник"
        elif a == b or b == c or a == c:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    
    segments = perms(a, b, c, d)

    for x in segments:
        if check_triangle(x):
            print(f'{x} это - {check_triangle_type(x)}')
        else:
            print(f'{x} - не треугольник')

lab_14_4_4(5, 4, 4, 4)
def lab_14_4_6():
    def compare_investments(principal1, time1, principal2, time2, rate):
        def calculate_income(principal, rate, time):
            return principal * rate * time / 100
        income1 = calculate_income(principal1, rate, time1)
        income2 = calculate_income(principal2, rate, time2)
        
        if income1 > income2:
            return f"Большой вклад на малый срок принесет больший доход.Больший вклад: {income1}, меньший вклад: {income2}"
        elif income1 < income2:
            return f"Небольшой вклад на длительный срок принесет больший доход.Больший вклад: {income1}, меньший вклад: {income2}"
        else:
            return f"Доход от обоих вложений одинаковый.Больший вклад: {income1}, меньший вклад: {income2}"
    
    principal1 = 1000
    time1 = 1
    principal2 = 500
    time2 = 5
    rate = 5  
    
    result = compare_investments(principal1, time1, principal2, time2, rate)
    print(result)
lab_14_4_6()

