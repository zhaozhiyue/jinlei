from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

def calcu_quality(D2,D1,H):
    global volume_yh
    global quality_yh
    volume_yh=pi*H*(D2**2-D1**2)*(10**(-9))/4#计算体积 ，单位为立方米
    quality_yh=7.85*volume_yh
def calcu_again(D2,D1,H):
    def jisuan():
        global quality_yh
        φ2=int(D2a.get())#获取输入的值
        φ1=int(D1a.get())
        L=int(Ha.get())

        calcu_quality(φ2,φ1,L)
        quality_gd=quality_yh/0.75
        quality_gd=round(quality_gd,2)
        quality_yh=round(quality_yh,2)
        tk.Label(window_output2,text='毛坯锻件质量为'+str(quality_yh)+'吨。'+\
             '成材率不低于75%,钢锭质量为'+str(quality_gd)+'吨',font=(20)).place(x=50,y=30)

    #建立新窗口
    window_output2=tk.Tk()
    window_output2.geometry('600x600')
    window_output2.title('圆环件计算结果')
    
    #设置输入框，获取输入值
    tk.Label(window_output2,text='H（加余量）为'+str(H)).place(x=100,y=80)
    Ha=tk.Entry(window_output2)
    Ha.place(x=300,y=80)
    Ha.insert(0,H)
    tk.Label(window_output2,text='D1（加余量）为'+str(D1)).place(x=100,y=160)
    D1a=tk.Entry(window_output2)
    D1a.place(x=300,y=160)
    D1a.insert(0,D1)
    tk.Label(window_output2,text='D2（加余量）为'+str(D2)).place(x=100,y=240)
    D2a=tk.Entry(window_output2)
    D2a.place(x=300,y=240)
    D2a.insert(0,D2)

    #设置button
    btn_yh_calcu=tk.Button(window_output2,text='重新计算',command=jisuan)
    btn_yh_calcu.place(x=250,y=350,width=100)
    window_output2.mainloop()

def yuanhuan_calcu(D2,D1,H):
    #直接计算出不修改的值
    def calcu_1():
        global volume_yh
        global quality_yh

        quality_gd=quality_yh/0.75
        quality_gd=round(quality_gd,2)
        quality_yh=round(quality_yh,2)
        tk.Label(window_output,text='毛坯锻件质量为'+str(quality_yh)+'吨。成材率≥75%，钢锭质量为'+\
            str(quality_gd)+'吨。',font=20).place(x=30,y=30)

    global volume_yh
    global quality_yh
    allowance=0

    if 0<H<=300:
        if 0<D2<=500:
            allowance=30
        elif 500<D2<850:
            allowance=35
        elif 850<=D2<1300:
            allowance=40
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 300<H<450:
        if 0<D2<=500:
            allowance=30
        elif 500<D2<850:
            allowance=35
        elif 850<=D2<1100:
            allowance=40
        elif 1100<=D2<1300:
            allowance=45
        elif 1300<=D2<1750:
            allowance=50
        elif 1750<=D2<2000:
            allowance=55
        elif 2000<=D2<2300:
            allowance=60
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 450<=H<600:
        if 0<D2<650:
            allowance=35
        elif 650<=D2<850:
            allowance=40
        elif 850<=D2<1300:
            allowance=45
        elif 1300<=D2<1500:
            allowance=50
        elif 1500<=D2<2000:
            allowance=55
        elif 2000<=D2<2300:
            allowance=60
        elif 2300<=D2<2600:
            allowance=65
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 600<=H<800:
        if 0<D2<650:
            allowance=40
        elif 650<=D2<1100:
            allowance=45
        elif 1100<=D2<1300:
            allowance=50
        elif 1300<=D2<1750:
            allowance=55
        elif 1750<=D2<2000:
            allowance=60
        elif 2000<=D2<2300:
            allowance=65
        elif 2300<=D2<2900:
            allowance=70
        elif 2900<=D2<3300:
            allowance=75
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 800<=H<1050:
        if 650<=D2<1100:
            allowance=45
        elif 1100<=D2<1300:
            allowance=50
        elif 1300<=D2<1500:
            allowance=55
        elif 1500<=D2<1750:
            allowance=60
        elif 1750<=D2<2300:
            allowance=65
        elif 2300<=D2<2600:
            allowance=70
        elif 2600<=D2<2900:
            allowance=75
        elif 2900<=D2<3300:
            allowance=85
        elif 3300<=D2<3600:
            allowance=90
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1050<=H<1400:
        if 850<=D2<1300:
            allowance=50
        elif 1300<=D2<1500:
            allowance=55
        elif 1500<=D2<1750:
            allowance=60
        elif 1750<=D2<2000:
            allowance=65
        elif 2000<=D2<2300:
            allowance=70
        elif 2300<=D2<2600:
            allowance=75
        elif 2600<=D2<2900:
            allowance=80
        elif 2900<=D2<3300:
            allowance=90
        elif 3300<=D2<3600:
            allowance=100
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1400<=H<1900:
        if 1100<=D2<1300:
            allowance=55
        elif 1300<=D2<1500:
            allowance=60
        elif 1500<=D2<1750:
            allowance=65
        elif 1750<=D2<2000:
            allowance=70
        elif 2000<=D2<2300:
            allowance=75
        elif 2300<=D2<2600:
            allowance=80
        elif 2600<=D2<2900:
            allowance=90
        elif 2900<=D2<3300:
            allowance=100
        elif 3300<=D2<3600:
            allowance=110
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')

    #加上余量
    D2=D2+allowance
    D1=D1-1.2*allowance
    H=H+1.2*allowance
    if D1<0:
        D1=0

    #取整 个位数为5或0
    D2=quzheng(D2)
    D1=quzheng(D1)
    H=quzheng(H)

    #计算毛坯的体积和质量，单位为立方米和吨
    calcu_quality(D2,D1,H)

    #建立新窗口
    window_output = tk.Tk()
    window_output.geometry('600x600')
    window_output.title('圆环件计算结果')

    #新建窗口上的label
    tk.Label(window_output,text='D2（加余量）为'+str(D2)).place(x=250,y=300)
    tk.Label(window_output,text='D1（加余量）为'+str(D1)).place(x=250,y=200)
    tk.Label(window_output,text='H（加余量）为'+str(H)).place(x=250,y=100)

    #新建窗口上的button
    btn_yh_calcu=tk.Button(window_output,text='确定计算',command=calcu_1)
    btn_yh_calcu.place(x=250,y=400,width=100)
    btn_yh_calcu2=tk.Button(window_output,text='重新计算',command=lambda:calcu_again(D2,D1,H))
    btn_yh_calcu2.place(x=250,y=450,width=100)
    window_output.mainloop()