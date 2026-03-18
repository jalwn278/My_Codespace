mem=['']*1000 #toy计算机主存,1000个空列表
reg=[0]*10 #通用寄存器，存放操作数和结果
pReg=0  #pc保存下条指令地址
iReg=''  #ir保存当前执行指令
def loadProgram(file):#调用文件的函数 文件从硬盘到内存
    global pReg, mem#在全局中用到的函数要说明
    fil = open(file, 'r') #open（file)函数用r模式打开了文件并将文件定义为fil
    first = True
    while True: #永远为真，循环执行
        line = fil.readline()  #读取文件fil中的每一个指令
        if line == '':  #读取到的是个空字符串
            break  #结束循环
###下面是加载一条指令
        flds=line.split()  #split（）函数根据空格或tab读取字符串，并将字符串储存在列表里
        address=int(flds[0]) #字符串中000类的为顺序编号，为方便索引要把字符串换为整数形
        ###下面把剩下的字符串构建一个列表
        instrcu=flds[1]
        for fld in flds[2:len(flds)]:
          instrcu=instrcu+''+fld #每个字符串间用空格隔开
        mem[address] = instrcu #mem列表上address所代表的内容用instruc赋值
        if first == True:  # 若是第1条指令
            pReg = address  # 则将其地址存入程序寄存器
            first = False
    fil.close()

def cycle(): #模拟cpu
    global pReg,iReg,reg,mem
    ###取指令
    iReg=mem[pReg] #从mem中取preg所代表序号的内容赋给ireg
    pReg=pReg+1 #取下一个指令
    flds=iReg.split()
    opcode = flds[0]  # 操作码
    if len(flds)>1:
        op1=int(flds[1] )
    if len(flds)>2:
        op2=int(flds[2] )
        # 执行和写结果
        if opcode == 'mov1':  # 数据移动指令：寄存器←主存
            reg[op1] = mem[op2]
        elif opcode == 'mov2':  # 数据移动指令：主存←寄存器,elif 是 "else if" 的缩写，表示在之前的 if 或 elif 条件不满足时，检查另一个条件
            mem[op1] = reg[op2]
        elif opcode == 'mov3':  # 数据移动指令：寄存器←数字
            reg[op1] = op2
        elif opcode == 'add':  # 加法指令
            reg[op1] = reg[op1] + reg[op2]
        elif opcode == 'sub':  # 减法指令
            reg[op1] = reg[op1] - reg[op2]
        elif opcode == 'mul':  # 乘法指令
            reg[op1] = reg[op1] * reg[op2]
        elif opcode == 'div':  # 除法指令
            reg[op1] = reg[op1] / reg[op2]
        elif opcode == 'jmp':  # 无条件跳转指令
            pReg = op1
        elif opcode == 'jz':  # 条件跳转指令
            if reg[op1] == 0:
                pReg = op2
        elif opcode == 'in':  # 输入指令
            reg[op1] = int(input('input:')) #内层input显示信息让用户输入 外层input把输入的内容转化为字符串
        elif opcode == 'out':  # 输出指令
            print('output:', reg[op1])
        elif opcode == 'halt':  # 停止指令
            return False

        return True#继续执行
###构造执行整个循环的程序
def run(filename):
    global pReg,iReg,mem,reg

    loadProgram(filename)

    while True:
        hasNextInstruc=cycle()
        if hasNextInstruc == False:
            break
run('sum100.txt')
for i in range(11):
    print('主存单元',i,':',mem[i])
run('add.txt')  # 运行add.txt中的TOY程序
for i in range(5):
    print('主存单元', i, ':', mem[i])  # 打印当前主存单元中保存的程序