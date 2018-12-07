class rectangle(object):
    
    def __init__(self):
        
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.x3 = 0
        self.x4 = 0
        self.y3 = 0
        self.y4 = 0
        
        

        
        
    def input(self):
        print("1 прямоугольник:")
        self.x1 = int(input("Введите координату х левых точек: "))
        self.y1 = int(input("Введите координату y верхних точек: "))
        self.x2 = int(input("Введите координату х правых точек: "))
        self.y2 = int(input("Введите координату y нижних точек: "))
        
    def result(self):
        print("Вы ввели следующие координаты прямоугольника: ")
        print("A:",self.x1,",",self.y1)
        print("B:",self.x2,"," ,self.y1)
        print("C:",self.x2, ",",self.y2)
        print("D:",self.x1,",",self.y2)
    
    def peremeshenie(self):
        dx = int(input("На сколько единиц вы хотите переместить прямоугольник по оси X ?"))
        dy = int(input("На сколько единиц вы хотите переместить прямоугольник по оси Y ?"))
        
        print("Получились следующие координаты прямоугольника:")
        print("A:", self.x1+dx, ",", self.y1+dy)
        print("B:", self.x2+dx, ",", self.y1+dy)
        print("C:", self.x2+dx, ",", self.y2+dy)
        print("D:", self.x1+dx, ",", self.y2+dy)
        self.x1 = self.x1+dx
        self.x2 = self.x2+dx
        self.y1 = self.y1+dy
        self.y2 = self.y2+dy
        
    def size(self):
        r = int(input("Во сколько раз изменяем размер прямоугольника ?"))
        
        print("Получились следующие координаты прямоугольника:")
        print("A:",self.x1, ",",self.y1)
        print("B:",self.x2*r, ",",self.y1)
        print("C:",self.x2*r, ",",self.y2)
        print("D:",self.x1, ",",self.y2)
        self.x2 = self.x2*r
    
        
    def input2(self):
        print("2 прямоугольник:")
        self.x3 = int(input("Введите координату х левых точек"))
        self.y3 = int(input("Введите координату y верхних точек"))
        self.x4 = int(input("Введите координату х правых точек"))
        self.y4 = int(input("Введите координату y нижних точек"))
        
    def result2(self):
        print("Вы ввели следующие координаты 2 прямоугольника: ")
        print("A:",self.x3,",",self.y3)
        print("B:",self.x4,",",self.y3)
        print("C:",self.x4, ",",self.y4)
        print("D:",self.x3,",",self.y4)
        
    def minimal(self):
        
        x_min = self.x1
        x_max = self.x1
        y_min = self.y1
        y_max = self.y1
        self.input2()
        self.result()
        self.result2()

        A = [self.x1,self.x2,self.x3,self.x4]
        B = [self.y1,self.y2,self.y3,self.y4]
        
        for i in range(4):
            if(x_max < int(A[i])):
                x_max = A[i]
            if(y_max < int(B[i])):
                y_max = B[i]
            if(x_min > int(A[i])):
                x_min = A[i]
            if(y_min > int(B[i])):
                y_min = B[i]
        
        print("Наименьший прямоугольник содержащий оба предыдущих имеет следующие координаты: ")
        print("A:", x_min, ",", y_max)
        print("B:", x_max, ",", y_max)
        print("C:", x_max, ",", y_min)
        print("D:", x_min, ",", y_min)

    def cross(self):
        # x_min = self.x1
        # x_max = self.x1
        # y_min = self.y1
        # y_max = self.y1
        # x1_sred = 0
        # x2_sred = 0
        # y1_sred = 0
        # y2_sred = 0
        self.input2()
        self.result()
        self.result2()
        A = [self.x1,self.x2,self.x3,self.x4]
        B = [self.y1,self.y2,self.y3,self.y4]
        
        # for i in range(4):
        #     if (x_max < int(A[i])):
        #         x_max = A[i]
        #     if (y_max < int(B[i])):
        #         y_max = B[i]
        #     if (x_min > int(A[i])):
        #         x_min = A[i]
        #     if (y_min > int(B[i])):
        #          y_min = B[i]
        #
        #     for i in range(4):
        #         if ((A[i] != x_max) & (A[i] != x_min)):
        #             x1_sred = A[i]
        #             break
        #     for i in range(4):
        #         if ((A[i] != x_max) & (A[i] != x_min) & (A[i] != x1_sred)):
        #             x2_sred = A[i]
        #             break
        #     for i in range(4):
        #         if((B[i] != y_max) & (B[i] != y_min)):
        #             y1_sred = B[i]
        #             break
        #     for i in range(4):
        #         if((B[i] != y_max) & (B[i] != y_min) & (B[i] != y1_sred)):
        #             y2_sred = B[i]
        #             break
        A.sort()
        B.sort()
        A.pop(3)
        A.pop(0)
        B.pop(3)
        B.pop(0)


        print(" Прямоугольник на пересечении двух предыдущих имеет следующие координаты: ")
        print("A:",A[0],",",B[1])
        print("B:",A[1],",",B[1])
        print("C:",A[1], ",",B[0])
        print("D:",A[0],",",B[0])
    
    
    def showMenu(self):
        print("Прямоугольники \n Справка: \n 1 - Ввод данных \n 2 - Вывод \n 3 - Перемещение \n 4 - Изменение размера \n \
5 - Минимальный прямоугольник содержащий 2 заданных \n 6 - Прямоугольник получившийся на пересечении 2 заданных\n 0 - выход\n")
        a = int(input("Выберите цифру: "))
        if a == 1:
            self.input()
            self.showMenu()
        elif a == 2:
            self.result()
            self.showMenu()
        elif a == 3:
            self.peremeshenie()
            self.showMenu()
        elif a == 4:
            self.size()
            self.showMenu()
        elif a == 5: 
            self.minimal()
            self.showMenu()
        elif a == 6:
            self.cross()
            self.showMenu()
        elif a == 0:
            exit()
        else: 
            self.showMenu()

a = rectangle()
a.showMenu()

            
        




