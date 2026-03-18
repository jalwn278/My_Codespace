import pymysql

#格式化打印游标中存放的结果
def display(cursor):
    records=cursor.fetchall()   #获取结果，结果的类型是嵌套元组，即元组中包含了很多小元组，小元组对应结果中的一行
    print('\n-----', len(records), 'lines -----')   #总行数
    for rec in records:         #对于每个小元组rec（对应表中一行）
        s=''
        for value in rec:       #value相当于一行中的一个单元格
            s=s+str(value)+'\t' #用制表符把这一行各单元格拼接成一个字符串
        print(s)

#连接数据库，相当于在命令行中执行mysql -uroot -p
conn=pymysql.connect(host='localhost',  #MySQL所在主机（主机名、IP地址或域名），localhost为本机
                     user='root',       #账号
                     passwd='111111',   #密码，根据情况进行修改
                     charset='gbk')     #字符编码方式
#print(conn.get_host_info())            #显示MySQL所在主机信息(主机、端口等)

#获取游标
cs = conn.cursor()  #用于执行SQL语句并存放结果

#创建数据库
cs.execute('drop database if exists nudt')  #若存在nudt数据库则删除，execute函数用于执行括号内的SQL语句，若有结果则存于游标cs中
cs.execute('create database nudt')          #创建nudt数据库
cs.execute('show databases')                #获取所有数据库名字
#display(cs)                                 #格式化打印所有数据库名字

#创建表grade
conn.select_db('nudt')              #选择数据库nudt，相当于use nudt
cs.execute('create table grade(\
                year   int,\
                prov   char(100),\
                ybx    int,\
                jsMax  int,\
                jsMin  int,\
                jsAvg  int,\
                hxMax  int,\
                hxMin  int,\
                hxAvg  int,\
                primary key (year, prov))')  #创建grade表（斜杠用于换行）
cs.execute('desc grade')            #获取表格的描述信息
#display(cs)                         #打印表格的描述信息

#载入数据：将三个txt中的数据插入grade表
for year in range(2014, 2017):              #对于2014~2016年中的某一年
    f=open(str(year)+'年数据.txt', 'r')     #打开这一年数据所在的txt文件
    while True:                             #依次处理文件中的每一行
        line=f.readline()                   #读取一行
        if line=='':                        #若这一行为空，表示文件读取完毕，跳出循环
            break                  
        v=line.split()                      #拆分这一行，得到对应的属性值
                                            #构建这一行对应的insert语句（斜杠用于换行）
        sql='insert into grade values\
                 (%s, "%s", %s, %s, %s, %s, %s, %s, %s)'\
                 % (year,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7])
        cs.execute(sql)                     #执行插入语句，将这一行添加到grade表
    f.close()
cs.execute('select * from grade')           #查询表中所有数据
display(cs)

#提交和关闭
conn.commit()#提交结果
cs.close()   #关闭游标
conn.close() #断开连接
