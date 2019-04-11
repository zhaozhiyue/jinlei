from math import pi
import tkinter as tk
from quzhengshu import quzheng
from tkinter import messagebox

#根据直径D1 2 4和长度L1 2 3 4和总长L计算出毛坯的质量 
def calcu_quality(L1,D1,L2,D2,L3,D3,L4,D4,L5,D5,L6,D6,L7,D7,L8,D8,L9,D9,L10,D10,D_k):
    global volume_tjz
    global quality_tjz
    L=L1+L2+L3+L4+L5+L6+L7+L8+L9+L10
    volume_tjz=(pi*(D1**2)*L1+pi*(D2**2)*L2+pi*(D3**2)*L3+pi*(D4**2)*L4+pi*(D5**2)*L5+\
        pi*(D6**2)*L6+pi*(D7**2)*L7+pi*(D8**2)*L8+pi*(D9**2)*L9+pi*(D10**2)*L10)/4-pi*L*(D_k**2)/4
    volume_tjz=volume_tjz*(10**(-9))
    quality_tjz=7.85*volume_tjz

#对余量进行适当的修改后计算毛坯的质量
def calcu_again(L1,D1,L2,D2,L3,D3,L4,D4,L5,D5,L6,D6,L7,D7,L8,D8,L9,D9,L10,D10,D_k):
    def jisuan():
        global quality_tjz
        H1=int(L1a.get())#获取输入的值
        φ1=int(D1a.get())
        H2=int(L2a.get())
        φ2=int(D2a.get())
        H3=int(L3a.get())
        φ3=int(D3a.get())
        H4=int(L4a.get())
        φ4=int(D4a.get())
        H5=int(L5a.get())
        φ5=int(D5a.get())
        H6=int(L6a.get())
        φ6=int(D6a.get())
        H7=int(L7a.get())
        φ7=int(D7a.get())
        H8=int(L8a.get())
        φ8=int(D8a.get())
        H9=int(L9a.get())
        φ9=int(D9a.get())
        H10=int(L10a.get())
        φ10=int(D10a.get())
        φ_k=int(D_ka.get())

        L=H1+H2+H3+H4+H5+H6+H7+H8+H9+H10
        tk.Label(window_output2,text='L总（加余量）为'+str(L)).place(x=80,y=70)

        calcu_quality(H1,φ1,H2,φ2,H3,φ3,H4,φ4,H5,φ5,H6,φ6,H7,φ7,H8,φ8,H9,φ9,H10,φ10,φ_k)
        quality_gd=quality_tjz/0.77
        quality_gd=round(quality_gd,2)
        quality_tjz=round(quality_tjz,2)
        tk.Label(window_output2,text='毛坯锻件质量为'+str(quality_tjz)+\
            '吨。成材率≥77%,钢锭质量为'+str(quality_gd)+'吨。',font=(20)).place(x=50,y=30)

        #建立新窗口
    window_output2=tk.Tk()
    window_output2.geometry('720x720')
    window_output2.title('台阶轴件计算结果')

    

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
    tk.Label(window_output2,text='D4（加余量）为'+str(D4)).place(x=400,y=250)
    D4a=tk.Entry(window_output2)
    D4a.place(x=550,y=250)
    D4a.insert(0,D4)

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

    tk.Label(window_output2,text='L7（加余量）为'+str(L7)).place(x=80,y=400)
    L7a=tk.Entry(window_output2)
    L7a.place(x=200,y=400)
    L7a.insert(0,L7)
    tk.Label(window_output2,text='D7（加余量）为'+str(D7)).place(x=400,y=400)
    D7a=tk.Entry(window_output2)
    D7a.place(x=550,y=400)
    D7a.insert(0,D7)

    tk.Label(window_output2,text='L8（加余量）为'+str(L8)).place(x=80,y=450)
    L8a=tk.Entry(window_output2)
    L8a.place(x=200,y=450)
    L8a.insert(0,L8)
    tk.Label(window_output2,text='D8（加余量）为'+str(D8)).place(x=400,y=450)
    D8a=tk.Entry(window_output2)
    D8a.place(x=550,y=450)
    D8a.insert(0,D8)

    tk.Label(window_output2,text='L9（加余量）为'+str(L9)).place(x=80,y=500)
    L9a=tk.Entry(window_output2)
    L9a.place(x=200,y=500)
    L9a.insert(0,L9)
    tk.Label(window_output2,text='D9（加余量）为'+str(D9)).place(x=400,y=500)
    D9a=tk.Entry(window_output2)
    D9a.place(x=550,y=500)
    D9a.insert(0,D9)

    tk.Label(window_output2,text='L10（加余量）为'+str(L10)).place(x=80,y=550)
    L10a=tk.Entry(window_output2)
    L10a.place(x=200,y=550)
    L10a.insert(0,L10)
    tk.Label(window_output2,text='D10（加余量）为'+str(D10)).place(x=400,y=550)
    D10a=tk.Entry(window_output2)
    D10a.place(x=550,y=550)
    D10a.insert(0,D10)

    tk.Label(window_output2,text='D_孔（加余量）为'+str(D_k)).place(x=250,y=600)
    D_ka=tk.Entry(window_output2)
    D_ka.place(x=400,y=600)
    D_ka.insert(0,D_k)

    #设置button
    btn_yh_calcu=tk.Button(window_output2,text='重新计算',command=jisuan)
    btn_yh_calcu.place(x=300,y=650,width=100)
    window_output2.mainloop() 

def taijiezhou_calcu(L1,D1,L2,D2,L3,D3,L4,D4,L5,D5,L6,D6,L7,D7,L8,D8,L9,D9,L10,D10,D_k):
    def calcu_1():
        global quality_tjz
        global volume_tjz

        quality_gd=quality_tjz/0.77
        quality_gd=round(quality_gd,2)
        quality_tjz=round(quality_tjz,2)
        tk.Label(window_output,text='台阶轴毛坯锻件质量为'+str(quality_tjz)+'吨。成材率≥77%，钢锭质量为'+\
            str(quality_gd)+'吨。',font=(20)).place(x=30,y=30)

    global volume_tjz
    global quality_tjz
    D_list=[D1,D2,D3,D4,D5,D6,D7,D8,D9,D10]
    L_list=[L1,L2,L3,L4,L5,L6,L7,L8,L9,L10]
    # D_max=max(D1,D2,D3,D4,D5,D6,D7,D8,D9,D10)
    D_max=max(D_list)
    D_min=min(D_list)
    L=L1+L2+L3+L4+L5+L6+L7+L8+L9+L10
    allowance=0
    if 0<L<=4000:
        if 0<D_max<=400:
            allowance=30
        elif 400<D_max<600:
            allowance=35
        elif 600<=D_max<1000:
            allowance=40
        elif 1000<=D_max:
            allowance=45
    elif 4000<L<7000:
        if 0<D_max<=400:
            allowance=35
        elif 400<D_max<800:
            allowance=40
        elif 800<=D_max:
            allowance=45
    elif 7000<=L<10000:
        if 0<D_max<=400:
            allowance=40
        elif 400<D_max<1000:
            allowance=45
        elif 1000<=D_max:
            allowance=50
    elif L>=10000:
        if 0<D_max<600:
            allowance=45
        elif 600<=D_max<1200:
            allowance=50
        elif 1200<=D_max:
            allowance=55
    else:
        tk.messagebox.showinfo(title='出错',message='请检查输入的数据是否在合理范围内')

     #加上余量
    for i in range(len(D_list)):
        
        if D_list[i] == D_max:
            L_list[i]=L_list[i]+1.6*allowance#加轴向余量
        L_list[i]=quzheng(L_list[i])    
        if D_list[i] != 0:
            D_list[i]=D_list[i]+allowance#加径向余量
            D_list[i]=quzheng(D_list[i])#取整

    D1=D_list[0];D2=D_list[1];D3=D_list[2]
    D4=D_list[3]
    D5=D_list[4]
    D6=D_list[5]
    D7=D_list[6]
    D8=D_list[7]
    D9=D_list[8]
    D10=D_list[9]

    L1=L_list[0]
    L2=L_list[1]
    L3=L_list[2]
    L4=L_list[3]
    L5=L_list[4]
    L6=L_list[5]
    L7=L_list[6]
    L8=L_list[7]
    L9=L_list[8]
    L10=D_list[9]
    L=L1+L2+L3+L4+L5+L6+L7+L8+L9+L10
    if D_k !=0:
        D_k=D_k-1.5*allowance
    if D_k <0:
        D_k=0
    D_k=quzheng(D_k)

    #计算体积，单位为立方米，质量，单位为吨
    calcu_quality(L1,D1,L2,D2,L3,D3,L4,D4,L5,D5,L6,D6,L7,D7,L8,D8,L9,D9,L10,D10,D_k)

    window_output=tk.Tk()
    window_output.geometry('650x720')
    window_output.title('台阶轴件计算结果')

    # 新建窗口上的label
    tk.Label(window_output,text='L总（加余量）为'+str(L)).place(x=150,y=70)
    tk.Label(window_output,text='L1（加余量）为'+str(L1)).place(x=150,y=110)
    tk.Label(window_output,text='D1（加余量）为'+str(D1)).place(x=350,y=110)
    tk.Label(window_output,text='L2（加余量）为'+str(L2)).place(x=150,y=150)
    tk.Label(window_output,text='D2（加余量）为'+str(D2)).place(x=350,y=150)
    tk.Label(window_output,text='L3（加余量）为'+str(L3)).place(x=150,y=190)
    tk.Label(window_output,text='D3（加余量）为'+str(D3)).place(x=350,y=190)
    tk.Label(window_output,text='L4（加余量）为'+str(L4)).place(x=150,y=230)
    tk.Label(window_output,text='D4（加余量）为'+str(D4)).place(x=350,y=230)
    tk.Label(window_output,text='L5（加余量）为'+str(L5)).place(x=150,y=270)
    tk.Label(window_output,text='D5（加余量）为'+str(D5)).place(x=350,y=270)
    tk.Label(window_output,text='L6（加余量）为'+str(L6)).place(x=150,y=310)
    tk.Label(window_output,text='D6（加余量）为'+str(D6)).place(x=350,y=310)
    tk.Label(window_output,text='L7（加余量）为'+str(L7)).place(x=150,y=350)
    tk.Label(window_output,text='D7（加余量）为'+str(D7)).place(x=350,y=350)
    tk.Label(window_output,text='L8（加余量）为'+str(L8)).place(x=150,y=390)
    tk.Label(window_output,text='D8（加余量）为'+str(D8)).place(x=350,y=390)
    tk.Label(window_output,text='L9（加余量）为'+str(L9)).place(x=150,y=430)
    tk.Label(window_output,text='D9（加余量）为'+str(D9)).place(x=350,y=430)
    tk.Label(window_output,text='L10（加余量）为'+str(L10)).place(x=150,y=470)
    tk.Label(window_output,text='D10（加余量）为'+str(D10)).place(x=350,y=470)
    tk.Label(window_output,text='D_孔（加余量）为'+str(D_k)).place(x=200,y=510)

     # 新建窗口上的button
    btn_yh_calcu=tk.Button(window_output,text='确定计算',command=calcu_1)
    btn_yh_calcu.place(x=250,y=550,width=100)
    btn_yh_calcu2=tk.Button(window_output,text='重新计算',command=lambda:\
    calcu_again(L1,D1,L2,D2,L3,D3,L4,D4,L5,D5,L6,D6,L7,D7,L8,D8,L9,D9,L10,D10,D_k))
    btn_yh_calcu2.place(x=250,y=600,width=100)
    window_output.mainloop() 