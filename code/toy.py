mem = [''] * 1000  # 主存
reg = [0] * 10  # 通用寄存器
pReg = 0  # 程序计数器
iReg = ''  # 指令寄存器


def loadProgram(file):
    global pReg, mem  # 全局变量声明
    fil = open(file, 'r')  # 打开文件
    first = True  # 用于标识是否为第1条指令
    while True:  # 每循环一次加载一条指令
        line = fil.readline()  # 读1行
        if line == '':  # 若读取完毕，则结束循环
            break
        flds = line.split()  # 将1行拆分为若干部分
        address = int(flds[0])  # 第0部分为地址
        instruc = flds[1]  # 将后面的部分重新拼接为指令
        for fld in flds[2:len(flds)]:
            instruc = instruc + ' ' + fld
        mem[address] = instruc  # 将指令加载到主存单元

        if first == True:  # 若是第1条指令
            pReg = address  # 则将其地址存入程序寄存器
            first = False  # 后面的指令不再是第1条指令'''
    fil.close()  # 关闭文件


def cycle():
    global pReg, iReg, reg, mem

    # 取指令
    iReg = mem[pReg]  # 根据pReg的值，将指令从mem取到iReg
    pReg = pReg + 1  # pReg加1，指向下一条指令

    # 译码
    flds = iReg.split()
    opcode = flds[0]  # 操作码
    if len(flds) > 1: op1 = int(flds[1])  # 操作数1
    if len(flds) > 2: op2 = int(flds[2])  # 操作数2

    # 执行和写结果
    if opcode == 'mov1':  # 数据移动指令：寄存器←主存
        reg[op1] = mem[op2]
    elif opcode == 'mov2':  # 数据移动指令：主存←寄存器
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
        reg[op1] = int(input('input:'))
    elif opcode == 'out':  # 输出指令
        print('output:', reg[op1])
    elif opcode == 'halt':  # 停止指令
        return False

    return True


def run(file):
    global pReg, iReg, reg, mem
    loadProgram(file)  # 加载TOY程序

    while True:  # 每循环一次，执行一条指令
        hasNextInstruc = cycle()  # 执行一条TOY指令
        if hasNextInstruc == False:  # 若执行的是halt指令
            break  # 则跳出循环


run('sum100.txt')  # 运行sum100.txt中的TOY程序
for i in range(11):
    print('主存单元', i, ':', mem[i])  # 打印当前主存单元中保存的程序
run('add.txt')  # 运行add.txt中的TOY程序
for i in range(5):
    print('主存单元', i, ':', mem[i])  # 打印当前主存单元中保存的程序


