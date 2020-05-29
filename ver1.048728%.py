#篮球决赛专用能力分析装置
#ver1.048728%
'''
一些思路：
    ·值分为五项={得分,助攻,抢断,篮板,帽}
        ·每一项值上限为全场最高值
        ·获得最多该值的球员该项能力为满，其余球员按百分比计算//类似赋分值
'''

import tkinter as tk

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
#面对ctrl编程（不）
#导入制图用的库和字体


#定义指令——Draw
def Draw():
        #设置五项数值
        lab=np.array(["得分","助攻",'篮板',"抢断","盖帽"])
        datalen = 5




        #当 指令 生效时  =>  抓取输入框中的数据并且处理
        name=str(name_i.get())
        score=float(score_i.get())/50
        assist=float(assist_i.get())/10
        rebound=float(rebound_i.get())/10
        steals=float(steals_i.get())/10
        block_shot=float(block_shot_i.get())/5
        #该项为比赛之后待填的数值
        #最值！！！修改！！！看这里！！！看这里！！！！！！






        #建立数值列表
        grade=[score,assist,rebound,steals,block_shot]
        data = np.array(grade)


        #制图-极坐标
        angles = np.linspace(0,2*np.pi,datalen,endpoint=False)#切开

        data = np.concatenate((data,[data[0]]))#闭合！
        angles = np.concatenate((angles,[angles[0]]))#闭合！角的之前弄错了！！怪不得出错！！

        plt.polar(angles,data,'ro-',linewidth=3)#建系
        plt.thetagrids(angles * 180 / np.pi,lab)#标签
        plt.fill(angles,
                data,
                facecolor='g',
                alpha=1/2 )

        #尺 规 作 图（确信
        plt.ylim(0,1)

        #标题制作
        plt.title(name+"的战绩",fontsize='large')

        #输出图！
        plt.show()      
#定义指令结束


#建立窗口 打上标题 设置大小
win = tk.Tk()
win.title("篮球决赛分析装置ver1.048728%")
win.geometry("300x350")


#输入框设置↓
#注意 请不要设置初始数值 容易出问题 
#注意 不要pack

#得分
tk.Label(win,text="得分/分：").place(x=10,y=10)
score_i = tk.Entry(win,show=None)
score_i.place(x=100,y=10)


#助攻
tk.Label(win,text="助攻/次：").place(x=10,y=50)
assist_i = tk.Entry(win,show=None)
assist_i.place(x=100,y=50)


#篮板
tk.Label(win,text="篮板/次：").place(x=10,y=90)
rebound_i = tk.Entry(win,show=None)
rebound_i.place(x=100,y=90)


#抢断
tk.Label(win,text="抢断/次").place(x=10,y=130)
steals_i = tk.Entry(win,show=None)
steals_i.place(x=100,y=130)


#盖帽
tk.Label(win,text="盖帽/次").place(x=10,y=170)
block_shot_i = tk.Entry(win,show=None)
block_shot_i.place(x=100,y=170)

#名字
tk.Label(win,text="选手名字:").place(x=10,y=210)
name_i=tk.Entry(win,text="name",show=None)
name_i.place(x=100,y=210)

#设置按钮
btn=tk.Button(win,text="  制图按钮  ",command=Draw)
btn.place(x=110,y=250)



#制作人
tk.Label(win,text="制作者：迷亭").place(x=10,y=300)
tk.Label(win,text="( •̀ ω •́ )").place(x=10,y=320)
#开始循环!
win.mainloop()