def T2_1(x=0, y=0, x1=-4, y1=0, x2=0, y2=4, x3=4, y3=0):
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ABC = area(x1, y1, x2, y2, x3, y3)
    PBC = area(x, y, x2, y2, x3, y3)
    PAC = area(x1, y1, x, y, x3, y3)
    PAB = area(x1, y1, x2, y2, x, y)
    print(ABC == PBC + PAC + PAB) 
T2_1()    

def T2_2(x=0, y=0, radius=3, x1=0, y1=0, x2=0, y2=3, x3=6, y3=0):
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ins_circ = x**2 + y**2 <= radius ** 2 and x <= 0 and y >= 0
    ABC = area(x1, y1, x2, y2, x3, y3)
    PBC = area(x, y, x2, y2, x3, y3)
    PAC = area(x1, y1, x, y, x3, y3)
    PAB = area(x1, y1, x2, y2, x, y)
    print(ABC == PBC + PAC + PAB and ins_circ) 
T2_2()

def T2_3(x=0, y=0, radius1=4, radius2= 3):
    ins_circ1= x**2 + y**2 <= radius1**2 and x >= 0 
    ins_circ2= x**2 + y**2 <= radius2**2 and x >= 0 
    print(ins_circ1 and not ins_circ2)
T2_3()

def T2_4(x=0, y=0, x1=-6, y1=0, x2=0, y2=-6, x3=6, y3=0):
    def area(x1, y1, x2, y2, x3, y3):
        return abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    ABC = area(x1, y1, x2, y2, x3, y3)
    PBC = area(x, y, x2, y2, x3, y3)
    PAC = area(x1, y1, x, y, x3, y3)
    PAB = area(x1, y1, x2, y2, x, y)
    print(ABC == PBC + PAC + PAB)
T2_4()

def T2_5(x=0, y=0):
    ins_1rec = y >= 0 and y <= 4 and x >= -2 and x <= 1
    ins_2rec = y <= 0 and y >= -3 and x >= -4 and x <= 4
    print(ins_1rec or ins_2rec)
T2_5() 

def T2_6(x=0, y=0, radius1= 6, radius2=3):
    ins1_circ = x**2 + y**2 <= radius1 ** 2 and y >= 0 and x <= 0
    ins2_circ = x**2 + y**2 <= radius1 ** 2 and y >= 0 and x >= 0 
    ins3_circ = x**2 + y**2 <= radius2 ** 2 and y >= 0 and x >= 0 
    print(ins1_circ or ins2_circ and not ins3_circ)
T2_6()

def T2_7(x=0, y=0, x1=1, y1=4, x2=4, y2=7, x3=7, y3=4, x4=4, y4=1):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)

    total_area = area(x1, y1, x2, y2, x3, y3) + area(x1, y1, x3, y3, x4, y4)
    area1 = area(x, y, x1, y1, x2, y2)
    area2 = area(x, y, x2, y2, x3, y3)
    area3 = area(x, y, x3, y3, x4, y4)
    area4 = area(x, y, x4, y4, x1, y1)
    print(total_area == (area1 + area2 + area3 + area4))
T2_7()

#T2_8 см. T2_5
#T2_9 см. T2_6 
#T2_10 см. T2_5 
#T2_11 cм. T2_5 
#T2_12 см. T2_2 
#T2_13 см. T2_5

def T2_14(x=0, y=0, x1=-4, y1=0, x2=0, y2= 4, x3=4, y3=0, x4=0, y4=-4):
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
T2_14()

#T2_15 см. T2_6 условие y >= 2 and y <= 6 

def T2_16(x=0, y=0, radius= 3, x1=-1, y1=0, x2=-1, y2=3, x3=-4, y3=3, x1_2 = -1, y1_2 = 0, x2_2 = -1, y2_2 = -3, x3_2 = -4, y3_2 = -3):
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
T2_16()

#T2_17 см. T2_2 , 2 треугольника
#T2_18 см. T2_2, T2_6, 2 квадрата и триугольник 
#T2_19 см. T2_2, круг и треугольник 
import math

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
