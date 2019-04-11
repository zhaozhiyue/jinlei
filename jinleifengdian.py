import tkinter as tk  
from tkinter import messagebox
from yuanpan import yuanpan_calcu
from duanyuan import duanyuan_calcu
from mokuai import mokuai_calcu
from yuanhuan import yuanhuan_calcu
from tongti import tongti_calcu
from fengjizhou import fengjizhou_calcu
from taijiezhou import taijiezhou_calcu

#设置主界面
window = tk.Tk()
window.title('金雷风电预测锻件专用')
window.geometry('600x600')
canvas = tk.Canvas(window,height=500,width=5000)
canvas2=tk.Canvas(window,height=1000,width=9000)
# image_file = tk.PhotoImage(file='D:\plianxi\jinlei\welcome.gif')
image_file = tk.PhotoImage(file='images\welcomejinlei2.gif')
image_file2 = tk.PhotoImage(file='images\shanda2.gif')
image=canvas.create_image(0,0,anchor='nw',image=image_file)
image2=canvas.create_image(600,0,anchor='ne',image=image_file2)
canvas.pack(side='top')
canvas2.pack(side='top')

# 设置选项按钮
tk.Label(window,text='请选择您所要预测的锻件类型',bg='yellow',font=('Arial',20),\
    width=40,height=2).place(x=0,y=150)

# 设置零件参数的函数，软件的主体
def fengjizhou():
    #定义计算过程（核心部分）
    def fjz_calcu():
        H1=L1.get()#获取输入的值
        φ1=D1.get()
        H2=L2.get()
        φ2=D2.get()
        H3=L3.get()
        φ3=D3.get()
        H4=L4.get()
        H5=L5.get()
        φ4=D5.get()
        H6=L6.get()
        φ6=D6.get()
        # window_fjz.destroy()
        fengjizhou_calcu(H1,φ1,H2,φ2,H3,φ3,H4,H5,φ4,H6,φ6)
    #设置子窗口
    window_fjz=tk.Toplevel(window)
    window_fjz.geometry('720x720')
    window_fjz.title('风机轴')
    tk.Label(window_fjz,text='若无L5或L6，设置其值为0即可',font=(15),\
    width=40,height=2).place(x=0,y=0)

    render = tk.PhotoImage(file='images\\fengjizhou.gif')
    label=tk.Label(window_fjz,image=render)
    label.iamge=render
    label.place(x=150,y=50)

    #定义L的长度
    L1=tk.IntVar()
    tk.Label(window_fjz,text='L1').place(x=130,y=380)
    entry_L1=tk.Entry(window_fjz,textvariable=L1)
    entry_L1.place(x=180,y=380)
    L1.set(160)
    D1=tk.IntVar()
    tk.Label(window_fjz,text='D1').place(x=450,y=380)
    entry_D1=tk.Entry(window_fjz,textvariable=D1)
    entry_D1.place(x=500,y=380)
    D1.set(1600)

    L2=tk.IntVar()
    tk.Label(window_fjz,text='L2').place(x=130,y=430)
    entry_L2=tk.Entry(window_fjz,textvariable=L2)
    entry_L2.place(x=180,y=430)
    L2.set(240)
    D2=tk.IntVar()
    tk.Label(window_fjz,text='D2').place(x=450,y=430)
    entry_D2=tk.Entry(window_fjz,textvariable=D2)
    entry_D2.place(x=500,y=430)
    D2.set(1200)

    L3=tk.IntVar()
    tk.Label(window_fjz,text='L3').place(x=130,y=480)
    entry_L3=tk.Entry(window_fjz, textvariable=L3)
    entry_L3.place(x=180, y=480)
    L3.set(700)
    D3=tk.IntVar()
    tk.Label(window_fjz,text='D3').place(x=450,y=480)
    entry_D3=tk.Entry(window_fjz,textvariable=D3)
    entry_D3.place(x=500,y=480)
    D3.set(1100)

    L4=tk.IntVar()
    tk.Label(window_fjz,text='L4').place(x=130,y=530)
    entry_L4=tk.Entry(window_fjz,textvariable=L4)
    entry_L4.place(x=180,y=530)
    L4.set(300)

    L5=tk.IntVar()
    tk.Label(window_fjz,text='L5').place(x=130,y=580)
    entry_L5=tk.Entry(window_fjz,textvariable=L5)
    entry_L5.place(x=180,y=580)
    L5.set(800)
    D5=tk.IntVar()
    tk.Label(window_fjz,text='D5').place(x=450,y=580)
    entry_D5=tk.Entry(window_fjz,textvariable=D5)
    entry_D5.place(x=500,y=580)
    D5.set(800)

    L6=tk.IntVar()
    tk.Label(window_fjz,text='L6').place(x=130,y=630)
    entry_L6=tk.Entry(window_fjz,textvariable=L6)
    entry_L6.place(x=180,y=630)
    L6.set(0)
    D6=tk.IntVar()
    tk.Label(window_fjz,text='D6').place(x=450,y=630)
    entry_D6=tk.Entry(window_fjz,textvariable=D6)
    entry_D6.place(x=500,y=630)
    D6.set(0)
   
    # window_fjz.destroy
    btn_fejz_calcu=tk.Button(window_fjz,text='确定',command=fjz_calcu)
    btn_fejz_calcu.place(x=350,y=670,width=100)

def yuanpan():
    def yp_calcu():
        φ2=D2.get()
        φ1=D1.get()
        L=H.get()
        # window_yp.destroy()

        yuanpan_calcu(φ2,φ1,L)
        
    window_yp=tk.Toplevel(window)
    window_yp.geometry('600x700')
    window_yp.title('圆盘冲孔')

    render = tk.PhotoImage(file='images\yuanpan.gif')
    label=tk.Label(window_yp,image=render)
    label.iamge=render
    label.place(x=50,y=50)

    H=tk.IntVar()
    tk.Label(window_yp,text='H').place(x=150,y=300)
    entry_H=tk.Entry(window_yp,textvariable=H)
    entry_H.place(x=300,y=300)
    H.set(360)

    D1=tk.IntVar()
    tk.Label(window_yp,text='D1（中间孔）').place(x=150,y=380)
    entry_yp_D1=tk.Entry(window_yp,textvariable=D1)
    entry_yp_D1.place(x=300,y=380)
    D1.set(90)
   
    D2=tk.IntVar()
    tk.Label(window_yp,text='D2（圆盘直径）').place(x=150,y=460)
    entry_yp_D2=tk.Entry(window_yp,textvariable=D2)
    entry_yp_D2.place(x=300,y=460)
    D2.set(900)

    btn_yp_calcu=tk.Button(window_yp,text='确定',command=yp_calcu)
    btn_yp_calcu.place(x=250,y=530,width=100)

def duanyuan():
    def dy_calcu():
        φ=D.get()
        H=L.get()
        # window_dy.destroy()

        duanyuan_calcu(φ,H)
    window_dy=tk.Toplevel(window)
    window_dy.geometry('500x600')
    window_dy.title('锻圆')

    render = tk.PhotoImage(file='images\duanyuan.gif')
    label=tk.Label(window_dy,image=render)
    label.iamge=render
    label.place(x=120,y=50)

    D=tk.IntVar()
    tk.Label(window_dy,text='D').place(x=100,y=200)
    entry_dy_D=tk.Entry(window_dy,textvariable=D)
    entry_dy_D.place(x=200,y=200)
    D.set(500)
    L=tk.IntVar()
    tk.Label(window_dy,text='L').place(x=100,y=300)
    entry_dy_L=tk.Entry(window_dy,textvariable=L)
    entry_dy_L.place(x=200,y=300)
    L.set(2500)

    btn_dy_calcu=tk.Button(window_dy,text='确定',command=dy_calcu)
    btn_dy_calcu.place(x=180,y=380,width=100)
    
def yuanhuan():
    def yh_calcu():
        φ2=D2.get()
        φ1=D1.get()
        L=H.get()
        # window_yh.destroy()
        yuanhuan_calcu(φ2,φ1,L)

    window_yh=tk.Toplevel(window)
    window_yh.geometry('600x600')
    window_yh.title('圆环')


    render = tk.PhotoImage(file='images\yuanhuan.gif')
    label=tk.Label(window_yh,image=render)
    label.iamge=render
    label.place(x=70,y=50)

    H=tk.IntVar()
    tk.Label(window_yh,text='H').place(x=150,y=280)
    entry_H=tk.Entry(window_yh,textvariable=H)
    entry_H.place(x=300,y=280)
    H.set(500)
    D1=tk.IntVar()
    tk.Label(window_yh,text='D1（内径）').place(x=150,y=360)
    entry_yh_D1=tk.Entry(window_yh,textvariable=D1)
    entry_yh_D1.place(x=300,y=360)
    D1.set(1000)
    D2=tk.IntVar()
    tk.Label(window_yh,text='D2（外径）').place(x=150,y=440)
    entry_yh_D2=tk.Entry(window_yh,textvariable=D2)
    entry_yh_D2.place(x=300,y=440)
    D2.set(1200)

    btn_yh_calcu=tk.Button(window_yh,text='确定',command=yh_calcu)
    btn_yh_calcu.place(x=250,y=510,width=100)

def taijiezhou():
    def tjz_calcu():
        H1=L1.get()#获取输入的值
        φ1=D1.get()
        H2=L2.get()
        φ2=D2.get()
        H3=L3.get()
        φ3=D3.get()
        H4=L4.get()
        φ4=D4.get()
        H5=L5.get()
        φ5=D5.get()
        H6=L6.get()
        φ6=D6.get()
        H7=L7.get()
        φ7=D7.get()
        H8=L8.get()
        φ8=D8.get()
        H9=L9.get()
        φ9=D9.get()
        H10=L10.get()
        φ10=D10.get()
        φ_k=D_k.get()
        # window_tjz.destroy()
        taijiezhou_calcu(H1,φ1,H2,φ2,H3,φ3,H4,φ4,H5,φ5,H6,φ6,H7,φ7,H8,φ8,H9,φ9,H10,φ10,φ_k)

    #设置子窗口
    window_tjz=tk.Toplevel(window)
    window_tjz.geometry('720x720')
    window_tjz.title('台阶轴')
    tk.Label(window_tjz,text='若台阶轴无孔，则设置孔的直径为0即可',font=(15),\
    width=40,height=2).place(x=0,y=0)

    render = tk.PhotoImage(file='images\\taijiezhou.gif')
    label=tk.Label(window_tjz,image=render)
    label.iamge=render
    label.place(x=100,y=50)

    # lb=tk.Listbox(window_tjz)
    sl=tk.Scrollbar(window_tjz)
    sl.set(0.6,0)
    sl.pack(side='right',fill = 'y')
    # lb['yscrollcommand']=sl.set
    #定义L的长度
    L1=tk.IntVar()
    tk.Label(window_tjz,text='L1').place(x=130,y=260)
    entry_L1=tk.Entry(window_tjz,textvariable=L1)
    entry_L1.place(x=180,y=260)
    L1.set(160)
    D1=tk.IntVar()
    tk.Label(window_tjz,text='D1').place(x=450,y=260)
    entry_D1=tk.Entry(window_tjz,textvariable=D1)
    entry_D1.place(x=500,y=260)
    D1.set(1600)

    L2=tk.IntVar()
    tk.Label(window_tjz,text='L2').place(x=130,y=295)
    entry_L2=tk.Entry(window_tjz,textvariable=L2)
    entry_L2.place(x=180,y=295)
    L2.set(240)
    D2=tk.IntVar()
    tk.Label(window_tjz,text='D2').place(x=450,y=295)
    entry_D2=tk.Entry(window_tjz,textvariable=D2)
    entry_D2.place(x=500,y=295)
    D2.set(1200)

    L3=tk.IntVar()
    tk.Label(window_tjz,text='L3').place(x=130,y=330)
    entry_L3=tk.Entry(window_tjz, textvariable=L3)
    entry_L3.place(x=180, y=330)
    L3.set(700)
    D3=tk.IntVar()
    tk.Label(window_tjz,text='D3').place(x=450,y=330)
    entry_D3=tk.Entry(window_tjz,textvariable=D3)
    entry_D3.place(x=500,y=330)
    D3.set(1100)

    L4=tk.IntVar()
    tk.Label(window_tjz,text='L4').place(x=130,y=365)
    entry_L4=tk.Entry(window_tjz,textvariable=L4)
    entry_L4.place(x=180,y=365)
    L4.set(300)
    D4=tk.IntVar()
    tk.Label(window_tjz,text='D4').place(x=450,y=365)
    entry_D4=tk.Entry(window_tjz,textvariable=D4)
    entry_D4.place(x=500,y=365)
    D4.set(900)

    L5=tk.IntVar()
    tk.Label(window_tjz,text='L5').place(x=130,y=400)
    entry_L5=tk.Entry(window_tjz,textvariable=L5)
    entry_L5.place(x=180,y=400)
    L5.set(800)
    D5=tk.IntVar()
    tk.Label(window_tjz,text='D5').place(x=450,y=400)
    entry_D5=tk.Entry(window_tjz,textvariable=D5)
    entry_D5.place(x=500,y=400)
    D5.set(800)

    L6=tk.IntVar()
    tk.Label(window_tjz,text='L6').place(x=130,y=435)
    entry_L6=tk.Entry(window_tjz,textvariable=L6)
    entry_L6.place(x=180,y=435)
    L6.set(0)
    D6=tk.IntVar()
    tk.Label(window_tjz,text='D6').place(x=450,y=435)
    entry_D6=tk.Entry(window_tjz,textvariable=D6)
    entry_D6.place(x=500,y=435)
    D6.set(0)

    L7=tk.IntVar()
    tk.Label(window_tjz,text='L7').place(x=130,y=470)
    entry_L7=tk.Entry(window_tjz,textvariable=L7)
    entry_L7.place(x=180,y=470)
    L7.set(0)
    D7=tk.IntVar()
    tk.Label(window_tjz,text='D7').place(x=450,y=470)
    entry_D7=tk.Entry(window_tjz,textvariable=D7)
    entry_D7.place(x=500,y=470)
    D7.set(0)

    L8=tk.IntVar()
    entry_L8=tk.IntVar()
    tk.Label(window_tjz,text='L8').place(x=130,y=505)
    entry_L8=tk.Entry(window_tjz,textvariable=L8)
    entry_L8.place(x=180,y=505)
    L8.set(0)
    D8=tk.IntVar()
    tk.Label(window_tjz,text='D8').place(x=450,y=505)
    entry_D8=tk.Entry(window_tjz,textvariable=D8)
    entry_D8.place(x=500,y=505)
    D8.set(0)

    L9=tk.IntVar()
    tk.Label(window_tjz,text='L9').place(x=130,y=540)
    entry_L9=tk.Entry(window_tjz,textvariable=L9)
    entry_L9.place(x=180,y=540)
    L9.set(0)
    D9=tk.IntVar()
    tk.Label(window_tjz,text='D9').place(x=450,y=540)
    entry_D9=tk.Entry(window_tjz,textvariable=D9)
    entry_D9.place(x=500,y=540)
    D9.set(0)

    L10=tk.IntVar()
    tk.Label(window_tjz,text='L10').place(x=130,y=575)
    entry_L10=tk.Entry(window_tjz,textvariable=L10)
    entry_L10.place(x=180,y=575)
    L10.set(0)
    D10=tk.IntVar()
    tk.Label(window_tjz,text='D10').place(x=450,y=575)
    entry_D10=tk.Entry(window_tjz,textvariable=D10)
    entry_D10.place(x=500,y=575)
    D10.set(0)

    D_k=tk.IntVar()
    tk.Label(window_tjz,text='D_内孔').place(x=250,y=610)
    entry_D_k=tk.Entry(window_tjz,textvariable=D_k)
    entry_D_k.place(x=300,y=610)
    D_k.set(0)

    # window_tjz.destroy
    btn_tjz_calcu=tk.Button(window_tjz,text='确定',command=tjz_calcu)
    btn_tjz_calcu.place(x=310,y=650,width=100)

def tongti():
    def tt_calcu():
        φ2=D2.get()
        φ1=D1.get()
        H=L.get()
        tongti_calcu(φ2,φ1,H)
        # window_tt.destroy()
    window_tt=tk.Toplevel(window)
    window_tt.geometry('550x650')
    window_tt.title('筒体')

    render = tk.PhotoImage(file='images\\tongti.gif')
    label=tk.Label(window_tt,image=render)
    label.iamge=render
    label.place(x=70,y=50)

    L=tk.IntVar()
    tk.Label(window_tt,text='L').place(x=100,y=300)
    entry_L=tk.Entry(window_tt,textvariable=L)
    entry_L.place(x=250,y=300)
    L.set(1800)
    D1=tk.IntVar()
    tk.Label(window_tt,text='D1（内径）').place(x=100,y=380)
    entry_tt_D1=tk.Entry(window_tt,textvariable=D1)
    entry_tt_D1.place(x=250,y=380)
    D1.set(120)
    D2=tk.IntVar()
    tk.Label(window_tt,text='D2（外径）').place(x=100,y=460)
    entry_tt_D2=tk.Entry(window_tt,textvariable=D2)
    entry_tt_D2.place(x=250,y=460)
    D2.set(950)

    btn_tt_calcu=tk.Button(window_tt,text='确定',command=tt_calcu)
    btn_tt_calcu.place(x=200,y=550,width=100)

def mokuai():
    def mk_calcu():
        C=L.get()#C  K G分别为长宽高
        K=B.get()
        G=H.get()
        # window_mk.destroy()
        mokuai_calcu(C,K,G)
    window_mk=tk.Toplevel(window)
    window_mk.geometry('600x600')
    window_mk.title('模块')

    render = tk.PhotoImage(file='images\mokuai.gif')
    label=tk.Label(window_mk,image=render)
    label.iamge=render
    label.place(x=50,y=50)

    L=tk.IntVar()
    tk.Label(window_mk,text='L').place(x=100,y=250)
    entry_mk_L=tk.Entry(window_mk,textvariable=L)
    entry_mk_L.place(x=250,y=250)
    L.set(2500)

    B=tk.IntVar()
    tk.Label(window_mk,text='B').place(x=100,y=330)
    entry_mk_B=tk.Entry(window_mk,textvariable=B)
    entry_mk_B.place(x=250,y=330)

    B.set(500)
    H=tk.IntVar()
    tk.Label(window_mk,text='H').place(x=100,y=410)
    entry_mk_H=tk.Entry(window_mk,textvariable=H)
    entry_mk_H.place(x=250,y=410)
    H.set(450)



    btn_mk_calcu=tk.Button(window_mk,text='确定',command=mk_calcu)
    btn_mk_calcu.place(x=200,y=480,width=100)

#定义选项的按钮
btn_fengjizhou=tk.Button(window,text='风机轴（常规产品）',width=15,command=fengjizhou)
btn_fengjizhou.place(x=80,y=250)
btn_yuanpan=tk.Button(window,text='圆盘冲孔',width=15,command=yuanpan)
btn_yuanpan.place(x=350,y=250)
btn_duanyuan=tk.Button(window,text='锻圆（圆钢）',width=15,command=duanyuan)
btn_duanyuan.place(x=80,y=300)
btn_yuanhuan=tk.Button(window,text='圆环（圈子）',width=15,command=yuanhuan)
btn_yuanhuan.place(x=350,y=300)
btn_taijiezhou=tk.Button(window,text='台阶轴',width=15,command=taijiezhou)
btn_taijiezhou.place(x=80,y=350)
btn_mokuai=tk.Button(window,text='模块',width=15,command=mokuai)
btn_mokuai.place(x=350,y=350)
btn_tongti=tk.Button(window,text='筒体',width=15,command=tongti)
btn_tongti.place(x=80,y=400)

window.mainloop()