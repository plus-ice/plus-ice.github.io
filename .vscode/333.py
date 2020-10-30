import math 
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig=plt.figure(figsize=(6,4)) #新建画布
ax=axisartist.Subplot(fig,111) #使用axisartist.Subplot方法创建一个绘图区对象ax
fig.add_axes(ax) #将绘图区对象添加到画布中

def exponential_func(x, a=2): #定义指数函数
  y=math.pow(a, x)
  return y

X=np.linspace(-4, 4, 40) #构造自变量组
Y=[exponential_func(x) for x in X] #求函数值
ax.plot(X, Y) #绘制指数函数
plt.show()