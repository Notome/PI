import numpy as np
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

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

def lab_6_1_6(total_head, total_cost):
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
b, co, ca = lab_6_1_6(total_head, total_cost)

print(f"Количество быков: {b}")
print(f"Количество коров: {co}")
print(f"Количество телят: {ca}")

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
