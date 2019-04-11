from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

#根据直径D1 2 4和长度L1 2 3 4和总长L计算出毛坯的质量 
def calcu_quality(L1,D1,L2,D2,L3,D3,L4,L5,D5,L6,D6):
    global volume_fjz
    global quality_fjz
    volume_fjz=(pi*(D1**2)*L1/4+pi*(D2**2-D3**2)*L2/16+pi*(D3**2)*(L2+L3)/4+\
        pi*L4*(D3**2+D5**2+D3*D5)/12+pi*L5*(D5**2)/4+pi*L6*(D6**2)/4)*(10**(-9))
    quality_fjz=7.85*volume_fjz#计算质量，单位为吨

#对余量进行适当的修改后计算毛坯的质量
def calcu_again(L1,D1,L2,D2,L3,D3,L4,L5,D5,L6,D6):
    def jisuan():
        global quality_fjz
        H1=int(L1a.get())#获取输入的值
        φ1=int(D1a.get())
        H2=int(L2a.get())
        φ2=int(D2a.get())
        H3=int(L3a.get())
        φ3=int(D3a.get())
        H4=int(L4a.get())
        H5=int(L5a.get())
        φ5=int(D5a.get())
        H6=int(L6a.get())
        φ6=int(D6a.get())

        calcu_quality(H1,φ1,H2,φ2,H3,φ3,H4,H5,φ5,H6,φ6)
        quality_gd=quality_fjz/0.75
        quality_gd=round(quality_gd,2)
        quality_fjz=round(quality_fjz,2)
        tk.Label(window_output2,text='毛坯锻件质量为'+str(quality_fjz)+\
            '吨。成材率≥75%,钢锭质量为'+str(quality_gd)+'吨。',font=(20)).place(x=50,y=30)
        
    #建立新窗口
    window_output2=tk.Tk()
    window_output2.geometry('800x800')
    window_output2.title('风机轴件计算结果')

    #设置输入框，获取输入值
    tk.Label(window_output2,text='L1（加余量）为'+str(L1)).place(x=80,y=100)
    L1a=tk.Entry(window_output2)
    L1a.place(x=200,y=100)
    L1a.insert(0,L1)
    tk.Label(window_output2,text='D1（加余量）为'+str(D1)).place(x=400,y=100)
    D1a=tk.Entry(window_output2)
    D1a.place(x=550,y=100)
    D1a.insert(0,D1)

    tk.Label(window_output2,text='L2（加余量）为'+str(L2)).place(x=80,y=150)
    L2a=tk.Entry(window_output2)
    L2a.place(x=200,y=150)
    L2a.insert(0,L2)
    tk.Label(window_output2,text='D2（加余量）为'+str(D2)).place(x=400,y=150)
    D2a=tk.Entry(window_output2)
    D2a.place(x=550,y=150)
    D2a.insert(0,D2)

    tk.Label(window_output2,text='L3（加余量）为'+str(L3)).place(x=80,y=200)
    L3a=tk.Entry(window_output2)
    L3a.place(x=200,y=200)
    L3a.insert(0,L3)
    tk.Label(window_output2,text='D3（加余量）为'+str(D3)).place(x=400,y=200)
    D3a=tk.Entry(window_output2)
    D3a.place(x=550,y=200)
    D3a.insert(0,D3)

    tk.Label(window_output2,text='L4（加余量）为'+str(L4)).place(x=80,y=250)
    L4a=tk.Entry(window_output2)
    L4a.place(x=200,y=250)
    L4a.insert(0,L4)

    tk.Label(window_output2,text='L5（加余量）为'+str(L5)).place(x=80,y=300)
    L5a=tk.Entry(window_output2)
    L5a.place(x=200,y=300)
    L5a.insert(0,L5)
    tk.Label(window_output2,text='D5（加余量）为'+str(D5)).place(x=400,y=300)
    D5a=tk.Entry(window_output2)
    D5a.place(x=550,y=300)
    D5a.insert(0,D5)

    tk.Label(window_output2,text='L6（加余量）为'+str(L6)).place(x=80,y=350)
    L6a=tk.Entry(window_output2)
    L6a.place(x=200,y=350)
    L6a.insert(0,L6)
    tk.Label(window_output2,text='D6（加余量）为'+str(D6)).place(x=400,y=350)
    D6a=tk.Entry(window_output2)
    D6a.place(x=550,y=350)
    D6a.insert(0,D6)

    #设置button
    btn_yh_calcu=tk.Button(window_output2,text='重新计算',command=jisuan)
    btn_yh_calcu.place(x=300,y=420,width=100)
    window_output2.mainloop() 

#本文件的主函数
def fengjizhou_calcu(L1,D1,L2,D2,L3,D3,L4,L5,D5,L6,D6):
    #直接计算出加余量后的毛坯质量和除以成形率后得到的钢锭质量
    def calcu_1():
        global volume_fjz
        global quality_fjz
        # print("毛坯质量calcu_1"+str(quality_fjz))
        quality_gd=quality_fjz/0.75
        quality_gd=round(quality_gd,2)
        quality_fjz=round(quality_fjz,2)
        tk.Label(window_output,text='风机轴毛坯锻件质量为'+str(quality_fjz)+'吨。成材率≥75%，钢锭质量为'+\
            str(quality_gd)+'吨。',font=(20)).place(x=30,y=30)

    global volume_fjz
    global quality_fjz
    allowance_D1=0#法兰直径余量
    allowance_H=0#法兰厚度余量
    allowance_S=0#轴身直径余量
    if 1200<=D1<1500:
        allowance_D1=55
        allowance_H=45
        allowance_S=40
    elif 1500<=D1<1800:
        allowance_D1=65
        allowance_H=50
        allowance_S=40
    elif 1800<=D1<2100:
        allowance_D1=75
        allowance_H=50
        allowance_S=45
    elif 2100<=D1:
        allowance_D1=80
        allowance_H=55
        allowance_S=45
    else:
        # print("请检查输入的数据是否在合理范围内")
        tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')

    #加上余量
    L1=L1+allowance_H
    D1=D1+allowance_D1
    D2=D2+allowance_S
    D3=D3+allowance_S
    if D5!=0:
        D5=D5+allowance_S
    if D6!=0:
        D6=D6+allowance_S

    #取整 0 1 2舍去 8 9进10  3 4 5 6为5
    L1=quzheng(L1)    
    D1=quzheng(D1)    
    D2=quzheng(D2)
    D3=quzheng(D3)
    D5=quzheng(D5)
    D6=quzheng(D6)

    # 计算体积 ，单位为立方米,计算质量，单位为吨
    calcu_quality(L1,D1,L2,D2,L3,D3,L4,L5,D5,L6,D6)
    # print("毛坯质量"+str(quality_fjz))

    window_output=tk.Tk()
    window_output.geometry('600x600')
    window_output.title('风机轴件计算结果')

    # 新建窗口上的label
    tk.Label(window_output,text='L1（加余量）为'+str(L1)).place(x=150,y=100)
    tk.Label(window_output,text='D1（加余量）为'+str(D1)).place(x=350,y=100)
    tk.Label(window_output,text='L2（加余量）为'+str(L2)).place(x=150,y=150)
    tk.Label(window_output,text='D2（加余量）为'+str(D2)).place(x=350,y=150)
    tk.Label(window_output,text='L3（加余量）为'+str(L3)).place(x=150,y=200)
    tk.Label(window_output,text='D3（加余量）为'+str(D3)).place(x=350,y=200)
    tk.Label(window_output,text='L4（加余量）为'+str(L4)).place(x=150,y=250)
    tk.Label(window_output,text='L5（加余量）为'+str(L5)).place(x=150,y=300)
    tk.Label(window_output,text='D5（加余量）为'+str(D5)).place(x=350,y=300)
    tk.Label(window_output,text='L6（加余量）为'+str(L6)).place(x=150,y=350)
    tk.Label(window_output,text='D6（加余量）为'+str(D6)).place(x=350,y=350)

    # 新建窗口上的button
    btn_yh_calcu=tk.Button(window_output,text='确定计算',command=calcu_1)
    btn_yh_calcu.place(x=250,y=400,width=100)
    btn_yh_calcu2=tk.Button(window_output,text='重新计算',command=lambda:\
        calcu_again(L1,D1,L2,D2,L3,D3,L4,L5,D5,L6,D6))
    btn_yh_calcu2.place(x=250,y=460,width=100)
    window_output.mainloop() 