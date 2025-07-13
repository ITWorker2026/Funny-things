import tkinter as tk

def popup():
    win = tk.Toplevel()
    win.title("警告！！！！！！！！！！")
    tk.Label(win, text="你的电脑是我的了！快去找黑心的电脑店老板重装系统吧！").pack()
    tk.Button(win, text="关闭", command=win.destroy).pack()

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

for _ in range(100):
    popup()

root.mainloop()