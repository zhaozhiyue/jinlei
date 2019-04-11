from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

#根据外径、内径和高计算出毛坯质量
def calcu_quality(D2,D1,H):
    global volume_yp
    global quality_yp
    
    volume_yp=pi*H*(D2**2-D1**2)*(10**(-9))/4#计算体积 ，单位为立方米
    quality_yp=7.85*volume_yp#计算质量，单位为吨

#对余量进行适当的修改后计算毛坯的质量
def calcu_again(D2,D1,H):
    def jisuan():
        global quality_yp
        φ2=int(D2a.get())#获取输入的值
        φ1=int(D1a.get())
        L=int(Ha.get())

        calcu_quality(φ2,φ1,L)
        quality_gd=quality_yp/0.77
        quality_gd=round(quality_gd,2)
        quality_yp=round(quality_yp,2)
        tk.Label(window_output2,text='毛坯锻件质量为'+str(quality_yp)+\
         '吨。成材率≥77%,钢锭质量为'+str(quality_gd)+'吨。',font=(20)).place(x=50,y=30)

    #建立新窗口
    window_output2=tk.Tk()
    window_output2.geometry('600x600')
    window_output2.title('圆盘件计算结果')

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

def yuanpan_calcu(D2,D1,H):
    def calcu_1():
        # 直接计算出加余量后的毛坯质量和除以成形率后得到的钢锭质量
        global quality_yp
        quality_gd=quality_yp/0.77
        quality_gd=round(quality_gd,2)
        quality_yp =round(quality_yp,2)
        tk.Label(window_output,text='毛坯锻件质量为'+str(quality_yp)+'吨'+\
         '成材率≥77%,钢锭质量为'+str(quality_gd)+'吨',font=(20)).place(x=50,y=30)

    global volume_yp
    global quality_yp
    allowance=0
    if 0<D2<500:
        if 0<H<200:
            allowance=30
        elif 200<=H<550:
            allowance=35
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 500<=D2<800:
        if 0<H<=100:
            allowance=30
        elif 100<H<550:
            allowance=35
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 800<=D2<1100:
        if 0<H<350:
            allowance=35
        elif 350<=H<800:
            allowance=40
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1100<=D2<1450:
        if 0<H<=100:
            allowance=35
        elif 100<H<550:
            allowance=40
        elif 550<=H<1050:
            allowance=45
        elif 1050<=H<1300:
            allowance=50
        else:
            tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    elif 1450<=D2<1800:
        if 0<H<=100:
            allowance=40
        elif 100<H<800:
            allowance=45
        elif 800<=H<1300:
            allowance=50
        elif 1300<=H<1600:
            allowance=55
    elif 1800<=D2<2150:
        if 0<H<350:
            allowance=45
        elif 350<=H<1050:
            allowance=50
        elif 1050<=H<1300:
            allowance=55
        elif 1300<=H<1600:
            allowance=60
    elif 2150<=D2<2550:
        if 100<=H<200:
            allowance=45
        elif 200<=H<800:
            allowance=50
        elif 800<=H<1300:
            allowance=55
        elif 1300<=H<1600:
            allowance=65
    elif 2550<=D2<3000:
        if 100<=H<350:
            allowance=50
        elif 350<=H<800:
            allowance=55
        elif 800<=H<1050:
            allowance=60
        elif 1050<=H<1300:
            allowance=65
        elif 1300<=H<1600:
            allowance=70
    else:
        tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')
    if H>1600:
        tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')

    #加上余量
    D2=D2+allowance
    D1=D1-1.5*allowance
    H=H+0.9*allowance

    if D1<0:
        D1=0
    #取整 0 1 2舍去 8 9进10  3 4 5 6为5
    D2=quzheng(D2)
    D1=quzheng(D1)
    H=quzheng(H)

    # 计算体积 ，单位为立方米,计算质量，单位为吨
    calcu_quality(D2,D1,H)

    window_output=tk.Tk()
    window_output.geometry('600x600')
    window_output.title('圆盘件计算结果')

    # 新建窗口上的label
    tk.Label(window_output,text='H（加余量）为'+str(H)).place(x=250,y=100)
    tk.Label(window_output,text='D1（加余量）为'+str(D1)).place(x=250,y=200)
    tk.Label(window_output,text='D2（加余量）为'+str(D2)).place(x=250,y=300)

    # 新建窗口上的button
    btn_yh_calcu=tk.Button(window_output,text='确定计算',command=calcu_1)
    btn_yh_calcu.place(x=250,y=400,width=100)
    btn_yh_calcu2=tk.Button(window_output,text='重新计算',command=lambda:calcu_again(D2,D1,H))
    btn_yh_calcu2.place(x=250,y=450,width=100)
    window_output.mainloop()  