from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

#根据长L,宽B,高H计算出毛坯的质量
def calcu_quality(L,B,H):
    global volume_mk
    global quality_mk
    volume_mk=L*B*H*(10**(-9))
    quality_mk=7.85*volume_mk

#修改余量后计算毛坯的质量
def calcu_again(L,B,H):
    def jisuan():
        global quality_mk
        L=int(La.get())
        B=int(Ba.get())
        H=int(Ha.get())
        calcu_quality(L,B,H)
        quality_gd=quality_mk/0.75
        quality_gd=round(quality_gd,2)
        quality_mk=round(quality_mk,2)
        tk.Label(window_ouput2,text='模块毛坯锻件质量为'+str(quality_mk)+'吨。成材率≥75%，钢锭质量为'+\
            str(quality_gd)+'吨。',font=(20)).place(x=30,y=30)

    #新建窗口，获取修改余量后的尺寸
    window_ouput2=tk.Tk()
    window_ouput2.geometry('800x800')
    window_ouput2.title('模块件计算结果')

    #设置输入框，获取输入值
    tk.Label(window_ouput2,text='L（加余量）为'+str(L)).place(x=100,y=80)
    La=tk.Entry(window_ouput2)
    La.place(x=300,y=80)
    La.insert(0,L)

    tk.Label(window_ouput2,text='B（加余量）为'+str(B)).place(x=100,y=160)
    Ba=tk.Entry(window_ouput2)
    Ba.place(x=300,y=160)
    Ba.insert(0,B)

    tk.Label(window_ouput2,text='H（加余量）为'+str(H)).place(x=100,y=240)
    Ha=tk.Entry(window_ouput2)
    Ha.place(x=300,y=240)
    Ha.insert(0,H)

    # 设置button
    btn_mk_calcu=tk.Button(window_ouput2,text='重新计算',command=jisuan)
    btn_mk_calcu.place(x=250,y=350,width=100)
    window_ouput2.mainloop()
def mokuai_calcu(L,B,H):
    #计算出不修改的值
    def calcu_1():
        global volume_mk
        global quality_mk
        quality_gd=quality_mk/0.75
        quality_gd=round(quality_gd,2)
        quality_mk = round(quality_mk, 2)
        tk.Label(window_ouput,text='模块毛坯锻件质量为'+str(quality_mk)+'吨。成材率≥75%，钢锭质量为'+\
            str(quality_gd)+'吨。',font=(20)).place(x=30,y=30)

    global volume_mk
    global quality_mk
    allowance = 0
    D=max(B,H)
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

    #加上余量
    L=L+1.5*allowance
    B=B+allowance
    H=H+allowance

    #取整个位数为5 或 0
    L=quzheng(L)
    B=quzheng(B)
    H=quzheng(H)

    #计算毛坯的体积和质量
    calcu_quality(L,B,H)

    #建立新窗口
    window_ouput=tk.Tk()
    window_ouput.geometry('600x600')
    window_ouput.title('模块件计算结果')

    #新建窗口上的label
    tk.Label(window_ouput,text='L（加余量）为'+str(L)).place(x=250,y=100)
    tk.Label(window_ouput,text='B（加余量）为'+str(B)).place(x=250,y=200)
    tk.Label(window_ouput,text='H（加余量）为'+str(H)).place(x=250,y=300)
    
    #新建窗口上的button
    btn_mk_calcu=tk.Button(window_ouput,text='确定计算',command=calcu_1)
    btn_mk_calcu.place(x=250,y=400,width=100)
    btn_mk_calcu2=tk.Button(window_ouput,text='重新计算',command=lambda:calcu_again(L,B,H))
    btn_mk_calcu2.place(x=250,y=450,width=100)
    window_ouput.mainloop()