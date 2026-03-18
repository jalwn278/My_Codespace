import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

#主窗口
window = tk.Tk()
window.title('文件合并工具')
window.geometry('440x600+300+200')
window.resizable(False, False)

def clickButton_addFile():
    filePaths=filedialog.askopenfilenames(title='选择文件', filetypes=[('txt', '.txt')])
    for filePath in filePaths:
        textbox_txtPath.insert(tk.END, filePath+'\n')
    textbox_txtPath.see(tk.END)

import wenben
import jinchen
def clickButton_adDir():
    dirpath=filedialog.askdirectory(title='选择文件夹')
    filePaths= wenben.getFilePaths(dirpath)
    for filePath in filePaths:
        textbox_txtPath.insert(tk.END, filePath+'\n')
    textbox_txtPath.see(tk.END)

def clickButton_merge():
    tmp=textbox_txtPath.get(0.0, tk.END)
    filePaths=tmp.split('\n')
    destPath= wenben.mergeTxts(filePaths, 'result.txt')
    textbox_resultPath.configure(state=tk.NORMAL)
    textbox_resultPath.delete(0.0, tk.END)
    textbox_resultPath.insert(0.0, destPath)
    textbox_resultPath.configure(state=tk.DISABLED)

def clickButton_openAll():
    tmp = textbox_txtPath.get(0.0, tk.END)
    filePaths = tmp.split('\n')
    jinchen.openManyTxt(filePaths)

def clickButton_closeAll():
    jinchen.closeAllTxt()

#“添加文件”按钮
button_addFile=tk.Button(window,text='添加文件',font=('楷体',12),command=clickButton_addFile)
button_addFile.place(x=20, y=20, width=120, height=40)

#“添加文件夹”按钮
button_addDir=tk.Button(window,text='添加文件夹',font=('楷体',12))
button_addDir.place(x=160, y=20, width=120, height=40)

#“开始合并”按钮
button_merge=tk.Button(window,text='开始合并',font=('楷体',12), bg='orange')
button_merge.place(x=300, y=20, width=120, height=40)

#用于展示所选文件对应路径的文本框（可滚动）
textbox_txtPath=scrolledtext.ScrolledText(window)
textbox_txtPath.place(x=20,y=70,width=400,height=400)

#“生成结果”标签
label=tk.Label(window, text='生成结果：', font=('楷体',12))
label.place(x=20,y=490,width=100,height=40)

#用于展示生成结果路径的文本框
textbox_resultPath=tk.Text(window)
textbox_resultPath.place(x=120,y=490,width=300,height=40)
textbox_resultPath.configure(state=tk.DISABLED)#不可修改

#“打开结果”按钮
button_openResult=tk.Button(window,text='打开结果',font=('楷体',12), bg='orange')
button_openResult.place(x=20, y=540, width=120, height=40)

#“打开所有”按钮
button_openAll=tk.Button(window,text='打开原始文件',font=('楷体',12))
button_openAll.place(x=160, y=540, width=120, height=40)

#“关闭所有”按钮
button_closeAll=tk.Button(window,text='关闭所有文件',font=('楷体',12))
button_closeAll.place(x=300, y=540, width=120, height=40)

#显示图形化界面
window.mainloop()

