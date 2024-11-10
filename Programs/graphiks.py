import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


#для чистого воздуха
data_array = [0,0]
data_array[0] = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_0_clear.txt", dtype = float)
data_array[1] = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_1_clear.txt", dtype = float)
start = [1218, 2885] #начало записи хлопка
average_noise = [0, 0]
the_loudest = [0, 0]

for i in range(2):
    average_noise[i] = sum(data_array[i][:start[i]])/start[i] #среднее значение звука до хлопка
    # data_array[i] -= average_noise[i] #убираем шум
    # the_loudest[i] = max(data_array[i]) #максимальное значение первых пиков
    # data_array[i] /= the_loudest[i] #теперь максимальные значения 1

tau = start[1] - start[0] #время между началами записей
# data_array[0] = data_array[0][:-tau] #отрезание хвоста первго графика
# data_array[1] = data_array[1][tau:] #сдвиг второго графика
print('tau for clear air:', tau)

##построение графика
fig, ax = plt.subplots(figsize = (16, 10), dpi = 300)
ax.xaxis.set_major_locator(ticker.MultipleLocator(500)) #частота крупных делений по х
ax.xaxis.set_minor_locator(ticker.MultipleLocator(100)) #частота мелких делений по х
ax.yaxis.set_major_locator(ticker.MultipleLocator(500)) #частота крупных делений по y
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100)) #частота мелких делений по y

ax.grid(which = 'major', color = 'k')#крупная сетка
ax.minorticks_on()
ax.grid(which = 'minor', color = 'grey')#мелкая сетка

plt.plot(data_array[0])
plt.plot(data_array[1])
plt.savefig("/Users/katerinadynnikova/Desktop/Hookah/Data/Sound_in_clear_1.png")


#для воздуха с повышенной концентрации углекислого газа
data_array = [0,0]
data_array[0] = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_0_unclear.txt", dtype = float)
data_array[1] = np.loadtxt("/Users/katerinadynnikova/Desktop/Hookah/Data/data_1_unclear.txt", dtype = float)
start = [633, 2325] #начало записи хлопка  
average_noise = [0, 0]
the_loudest = [0, 0]

for i in range(2):
    average_noise[i] = sum(data_array[i][:start[i]])/start[i] #среднее значение звука до хлопка
    # data_array[i] -= average_noise[i] #убираем шум
    # the_loudest[i] = max(data_array[i]) #максимальное значение первых пиков
    # data_array[i] /= the_loudest[i] #теперь максимальные значения 1

tau = start[1] - start[0] #время между началами записей
# data_array[0] = data_array[0][:-tau] #отрезание хвоста первго графика
# data_array[1] = data_array[1][tau:] #сдвиг второго графика
print('tau for unclear air:', tau)

#print(average_noise, data_array[0], the_loudest)
fig, ax = plt.subplots(figsize = (16, 10), dpi = 300)

# ax.set_xlabel('номер измерения',fontsize = 10) #подпись к оси х
# ax.set_ylabel('напряжение на конденсаторе в Вольтах',fontsize = 10) #подпись к оси у

ax.xaxis.set_major_locator(ticker.MultipleLocator(500)) #частота крупных делений по х
ax.xaxis.set_minor_locator(ticker.MultipleLocator(100)) #частота мелких делений по х
ax.yaxis.set_major_locator(ticker.MultipleLocator(500)) #частота крупных делений по y
ax.yaxis.set_minor_locator(ticker.MultipleLocator(100)) #частота мелких делений по y

ax.grid(which = 'major', color = 'k')#крупная сетка
ax.minorticks_on()
ax.grid(which = 'minor', color = 'grey')#мелкая сетка

plt.plot(data_array[0])
plt.plot(data_array[1])
plt.savefig("/Users/katerinadynnikova/Desktop/Hookah/Data/Sound_in_unclear_1.png")