from matplotlib import pyplot as plt
import numpy
from textwrap import wrap

def fun_chis(v2): # функция нахождения концентрации от скорости звука в атмосферном воздухе
    # от скорости в атмосферном воздухе
    #константы
    r=8.31446
    t=298.3
    #noa это смесь азот + кислород + аргон
    x_NOA=0.99964 
    m_NOA=0.02897
    c_p_NOA=1.0036
    c_v_NOA=0.7166
    #углекислого газа
    m_y=0.04401
    c_p_y=0.838 
    c_v_y=0.649
    #для воды
    m_h=0.01801 
    c_p_h=1.863
    c_v_h=1.403
    #введенные переменные для упрощения уравнения
    n=1-(0.33*3170)/(101375) # коэфиициент домножения содержания газа
    # для учета влажности воздуха
    k1=n*m_y*c_p_y
    k2=n*m_y*c_v_y
    k3=n*m_y
    a=x_NOA*n*m_NOA*c_p_NOA + (1-n)*m_h*c_p_h
    b=x_NOA*n*m_NOA*c_v_NOA + (1-n)*m_h*c_v_h
    c=x_NOA*n*m_NOA + (1-n)*m_h
    #коэффициенты квадратного уранения
    e1=v2*k2*k3
    e2=v2*(k2*c+k3*b)-k1*r*t
    e3=v2*b*c-a*r*t
    # решение квадратного уравнения
    d = e2 ** 2 - 4 * e1 * e3
    x = (-e2 + d ** 0.5) / (2 * e1)
    if x>-0.0002 and x<=0.001:
        print(x)
        print(v2**0.5)
    return x

def fun_graz(v2): # функция нахождения концентрации от скорости звука в воздухе из лёгких
    r=8.31446
    t=296.3
    x_NOA=0.99964
    m_NOA=0.02897
    c_p_NOA=1.0036
    c_v_NOA=0.7166
    m_y=0.04401
    c_P_y=0.838
    c_V_y=0.649
    m_h=0.01801
    c_P_h=1.863
    c_V_h=1.403
    n=1-(0.82*3170)/(101375)
    k1=n*(m_y-m_NOA)*c_P_y
    k2=n*(m_y-m_NOA)*c_V_y
    k3=n*(m_y-m_NOA)
    a=x_NOA*n*m_NOA*c_p_NOA + (1-n)*m_h*c_P_h
    b=x_NOA*n*m_NOA*c_v_NOA + (1-n)*m_h*c_V_h
    c=x_NOA*n*m_NOA + (1-n)*m_h
    e1=v2*k2*k3
    e2=v2*(k2*c+k3*b)-k1*r*t
    e3=v2*b*c-a*r*t
    d = e2 ** 2 - 4 * e1 * e3
    x = (-e2 + d ** 0.5) / (2 * e1)
    if x>=0.035 and x<=0.045:
        print(x)
        print(v2**0.5)
    return x

#график для чистого воздуха
mas_x_chis=[i/10 for i in range(3350, 3469)]
mas_y_chis=[fun_chis(i**2) for i in mas_x_chis]
#график для воздуха из лёгких
mas_x_graz=[i/10 for i in range(3420, 3465)]
mas_y_graz=[fun_graz(i**2) for i in mas_x_graz]

fig, ax=plt.subplots()
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.plot([i*100 for i in mas_y_chis], mas_x_chis, label = 'атмосферный')
ax.plot([i*100 for i in mas_y_graz], mas_x_graz, label = 'выдыхаемый')
#установка двух точек, найденных по найденной скорости и концентрации,
#полученной подстановкой этой скорости в уравнение
ax.scatter(0.0007*100, 346.7, c='green')
ax.scatter(0.0296*100, 343.8, c='brown')

ax.legend(shadow = False, loc = 'right', fontsize = 10)
ax.set_xlabel("содержание углекислого газа, %")
ax.set_ylabel("скорость звука, м/с")
plt.show()


