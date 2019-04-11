from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

#根据外径、内径和长度计算出毛坯质量
def calcu_quality(D2,D1,L):
    global volume_tt
    global quality_tt
    volume_tt=pi*L*(D2**2-D1**2)*(10**(-9))/4#计算体积 ，单位为立方米
    quality_tt=7.85*volume_tt#计算质量，单位为吨

#对余量进行适当修改后计算毛坯的质量
def calcu_again(D2,D1,L):
    def jisuan():
        global quality_tt
        φ2=int(D2a.get())#获取输入的值
        φ1=int(D1a.get())
        H=int(La.get())

        calcu_quality(φ2,φ1,H)
        quality_gd=quality_tt/0.75
        quality_gd=round(quality_gd,2)
        quality_tt=round(quality_tt,2)
        tk.Label(window_output2,text='毛坯锻件质量为'+str(quality_tt)+'吨。成材率≥75%,钢锭质量为'\
            +str(quality_gd)+'吨。',font=(20)).place(x=50,y=30)

    #建立新窗口
    window_output2=tk.Tk()
    window_output2.geometry('600x600')
    window_output2.title('筒体件计算结果')

    #设置输入框，获取输入值
    tk.Label(window_output2,text='L（加余量）为'+str(L)).place(x=100,y=80)
    La=tk.Entry(window_output2)
    La.place(x=300,y=80)
    La.insert(0,L)

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

def tongti_calcu(D2,D1,L):
    #直接计算出加余量后的毛坯质量和除以成形率后得到的钢锭质量
    def calcu_1():
        global quality_tt
        quality_gd=quality_tt/0.75
        quality_gd=round(quality_gd,2)
        quality_tt=round(quality_tt,2)
        tk.Label(window_output,text='毛坯锻件质量为'+str(quality_tt)+'吨'+\
         '成材率≥75%,钢锭质量为'+str(quality_gd)+'吨',font=(20)).place(x=50,y=30)

    global volume_tt
    global quality_tt
    allowance=0
    if D2<=500:
        if 0<L<2500:
            allowance=35
        elif 2500<=L<=9000:
            allowance=40
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 500<D2<=700:
        if 0<L<4000:
            allowance=40
        elif 4000<=L:
            allowance=45
    elif 700<=D2<900:
        if 0<L<2500:
            allowance=40
        elif 2500<=L<9000:
            allowance=45
        elif 9000<=L:
            allowance=50
    elif 900<=D2<1100:
        if 1000<=L<1600:
            allowance=40
        elif 1600<=L<6300:
            allowance=45
        elif 6300<=L:
            allowance=50
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1100<=D2<1350:
        if 1000<=L<2500:
            allowance=45
        elif 2500<=L<6300:
            allowance=50
        elif 6300<=L:
            allowance=55
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1350<=D2<1700:
        if 2500<=L<4000:
            allowance=50
        elif 4000<=L<6300:
            allowance=55
        elif 6300<=L:
            allowance=60
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1700<=D2:
        if 2500<=L<4000:
            allowance=55
        elif 4000<L<=9000:
            allowance=60
        elif 9000<=L:
            allowance=65
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')

    #加上余量
    if L<=1000:
        n=1.5
    elif 1000<L<2500:
        n=1.8
    elif 2500<=L<7000:
        n=2
    elif L>=7000:
        n=2.5
    D2=D2+allowance
    D1=D1-1.5*allowance
    if D1<0:
        D1=0
    L=L+n*allowance

    #取整 0 1 2舍去 8 9进10  3 4 5 6为5
    D2=quzheng(D2)
    D1=quzheng(D1)
    L=quzheng(L)

     # 计算体积 ，单位为立方米,计算质量，单位为吨
    calcu_quality(D2,D1,L)

    window_output=tk.Tk()
    window_output.geometry('600x600')
    window_output.title('筒体件计算结果')

    # 新建窗口上的label
    tk.Label(window_output,text='L（加余量）为'+str(L)).place(x=250,y=100)
    tk.Label(window_output,text='D1（加余量）为'+str(D1)).place(x=250,y=200)
    tk.Label(window_output,text='D2（加余量）为'+str(D2)).place(x=250,y=300)

    # 新建窗口上的button
    btn_yh_calcu=tk.Button(window_output,text='确定计算',command=calcu_1)
    btn_yh_calcu.place(x=250,y=400,width=100)
    btn_yh_calcu2=tk.Button(window_output,text='重新计算',command=lambda:calcu_again(D2,D1,L))
    btn_yh_calcu2.place(x=250,y=450,width=100)
    window_output.mainloop()  