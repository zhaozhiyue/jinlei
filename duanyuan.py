from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

#根据直径和长度计算出毛坯质量
def calcu_quality(D,L):
    global volume_dy
    global quality_dy
    volume_dy=pi*L*(D**2)*(10**(-9))/4
    quality_dy=7.85*volume_dy

#修改余量后计算毛坯的质量
def calcu_again(D,L):
    def jisuan():
        global quality_dy
        D=int(Da.get())
        L=int(La.get())
        calcu_quality(D,L)
        quality_gd=quality_dy/0.8
        quality_gd=round(quality_gd,2)
        quality_dy=round(quality_dy,2)
        tk.Label(Window_output2,text='毛坯锻件质量为'+str(quality_dy)+'吨。成材率≥80%，钢锭质量为'\
            +str(quality_gd)+'吨。',font=(20)).place(x=30,y=30)
    #新建窗口，对余量进行修改
    Window_output2=tk.Tk()
    Window_output2.geometry('800x800')
    Window_output2.title('锻圆件计算结果')

    #设置输入框，获取输入值
    tk.Label(Window_output2,text='D（加余量）为'+str(D)).place(x=100,y=160)
    Da=tk.Entry(Window_output2)
    Da.place(x=300,y=160)
    Da.insert(0,D)
    tk.Label(Window_output2,text='L（加余量）为'+str(L)).place(x=100,y=240)
    La=tk.Entry(Window_output2)
    La.place(x=300,y=240)
    La.insert(0,L)

    #设置button
    btn_dy_calcu=tk.Button(Window_output2,text='重新计算',command=jisuan)
    btn_dy_calcu.place(x=250,y=350,width=100)
    Window_output2.mainloop()

def duanyuan_calcu(D,L):
    #直接结算出不修改的值
    def calcu_1():
        global volume_dy
        global quality_dy
        quality_gd=quality_dy/0.8
        quality_gd=round(quality_gd,2)
        quality_dy=round(quality_dy,2)
        tk.Label(Window_output,text='毛坯锻件质量为'+str(quality_dy)+'吨。成材率≥80%，钢锭质量为'\
            +str(quality_gd)+'吨。',font=(20)).place(x=30,y=30)
    global volume_dy
    global quality_dy
    allowance=0
    if 0<L<=1000:
        if 0<D<700:
            allowance=35
        elif 700<=D<850:
            allowance=40
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1000<L<2000:
        if 0<D<700:
            allowance=35
        elif 700<=D<850:
            allowance=40
        elif 850<=D<1600:
            allowance=45
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 2000<=L<3500:
        if 0<D<550:
            allowance=35
        elif 550<=D<850:
            allowance=40
        elif 850<=D:
            allowance=45
    elif 3500<=L<5000:
        if 0<D<550:
            allowance=35
        elif 550<=D<850:
            allowance=40
        elif 850<=D<1300:
            allowance=45
        elif 1300<=D:
            allowance=50
    elif 5000<=L<7500:
        if 0<D<700:
            allowance=40
        elif 700<=D<1050:
            allowance=45
        elif 1050<=D<1300:
            allowance=50
        elif D>=1300:
            allowance=55
    elif 7500<=L<10000:
        if 0<D<700:
            allowance=45
        elif 750<=D<1050:
            allowance=50
        elif 1050<=L<1600:
            allowance=55
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif L>=10000:
        if 0<D<550:
            allowance=45
        elif 550<=D<700:
            allowance=50
        elif 700<=D<1300:
            allowance=55
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    else:
        tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
        

    #确定余量系数
    if L/D>=15:
        allowance=1.1*allowance
    elif L/D>=30:
        allowance=1.3*allowance

    #加上余量
    D=D+allowance
    L=L+2*allowance


    #取整 个位数为5或0
    D=quzheng(D)
    L=quzheng(L)

    #计算体积，单位为立方米，质量，单位为吨
    calcu_quality(D,L)

    #建立新窗口
    Window_output = tk.Tk()
    Window_output.geometry('600x600')
    Window_output.title('锻圆件计算结果')

    #新建窗口上的label
    tk.Label(Window_output,text='D（加余量）为'+str(D)).place(x=250,y=100)
    tk.Label(Window_output,text='L（加余量）为'+str(L)).place(x=250,y=200)

    #新建窗口上的button
    btn_dy_calcu=tk.Button(Window_output,text='确定计算',command=calcu_1)
    btn_dy_calcu.place(x=250,y=400,width=100)
    btn_dy_calcu2=tk.Button(Window_output,text='重新计算',command=lambda:calcu_again(D,L))
    btn_dy_calcu2.place(x=250,y=450,width=100)
    Window_output.mainloop()