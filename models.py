import matplotlib.pyplot as plt
import numpy as np

#Функция для 3D-моделей
def plot_implicit(fn, bbox=(-2.5,2.5)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100)
    B = np.linspace(xmin, xmax, 15)
    A1,A2 = np.meshgrid(A,A)
    for z in B:
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')
    for y in B:
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y')
    for x in B:
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x')
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)
    plt.show()

#Модель 1 - Решётка
def Model1(x,y,R):
    R=1
    return ((x**(2/3))+(y**(2/3))-(R**(2/3)))

#Модель 2 - 4 решётки
def Model2(x,y,z):
    z=1
    return (((np.sqrt(((((np.sqrt(x**2))-1)**2)-(((np.sqrt(y**2))-1)**2))**2))-1)*z)

#Модель 3 - Решётчатая труба
def Model3(x,y,z):
    a=1
    b=1
    c=1
    return ((((x**2)/(a**2))+((y**2)/(b**2))-((z**2)/(c**2)))-1)

plot_implicit(Model1)
plot_implicit(Model2)
plot_implicit(Model3)

#Модели-поверхности

#Модель 4 - Падающий платок
x = np.outer(np.linspace(-3,3,6),np.ones(6))
y = x.copy().T
z = ((x**2)+(y**2))
fig = plt.figure(figsize =(15, 15))
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, z)
plt.show()

#Модель 5 - Горный склон
x = np.outer(np.linspace(-3,3,6),np.ones(6))
y = x.copy().T
z = (x+np.cos(x*y))
fig = plt.figure(figsize =(15, 15))
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, z)
plt.show()

#Модель 6 - Маленькая лиса
x = np.outer(np.linspace(-3,3,6),np.ones(6))
y = x.copy().T
z = (np.tan(x*y))
fig = plt.figure(figsize =(15, 15))
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, z)
plt.show()