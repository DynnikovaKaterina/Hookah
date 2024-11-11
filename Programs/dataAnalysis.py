import matplotlib.pyplot as plt
import numpy as np

#Функция для нахождения точной точки макимума
def max_id_1(mas):
    maxa=max(mas)
    id = 0
    for i in range(len(mas)):
        if maxa <= mas[i]:
            id = i
    return id

#Функция для нахождения максимума с погрешностью
def max_id_2(mas):
    maxa = max(mas)
    id = 0
    for i in range(len(mas)):
        if maxa <= mas[i]:
            id = i
    return id

def speed_for_data(Nu, id_a, id_b, dlin):
    v = dlin/((id_b-id_a)/Nu)
    return v

def file_open(name):
    with open(name, 'r') as file:
        data = []
        for f in file:
            data.append(int(f.split()[0]))
    return data
#Переменные
Nu = 500000
dlin = 1.158


data_0_air = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_0_clear.txt", dtype = float)
data_1_air = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_1_clear.txt", dtype = float)
data_0_co2 = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_0_unclear.txt", dtype = float)
data_1_co2 = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_1_unclear.txt", dtype = float)


id_0_air = 1294
id_1_air = max_id_1(data_1_air)
v_air = speed_for_data(Nu, id_0_air, id_1_air, dlin)

id_0_co2 = max_id_2(data_0_co2)
id_1_co2 = 2372
v_co2 = speed_for_data(Nu, id_0_co2, id_1_co2, dlin)



print('Скорость для звука в сухом воздухе (влажность 28.6%)')
print(v_air)
print('Скорость звука во влажном воздухе (влажность 83.4%)')
print(v_co2)
