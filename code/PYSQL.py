import pymysql
import os  # 新增：用于获取脚本路径

# 格式化打印游标中存放的结果
def display(cursor):
    records = cursor.fetchall()
    print('\n-----', len(records), 'lines -----')
    for rec in records:
        s = ''
        for value in rec:
            s = s + str(value) + '\t'
        print(s)

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='PBH2006721',
    charset='gbk'
)

cs = conn.cursor()

# 创建数据库
cs.execute('drop database if exists nudt')
cs.execute('create database nudt')
cs.execute('show databases')

# 选择数据库
conn.select_db('nudt')

# 创建表 grade
cs.execute('''
create table grade(
    year   int,
    prov   char(100),
    ybx    int,
    jsMax  int,
    jsMin  int,
    jsAvg  int,
    hxMax  int,
    hxMin  int,
    hxAvg  int,
    primary key (year, prov))
''')
cs.execute('desc grade')

# ------------------- 关键修改开始 -------------------

# 获取当前脚本所在目录（绝对路径）
script_dir = os.path.dirname(os.path.abspath(__file__))

# 载入数据：将三个txt中的数据插入grade表
for year in range(2014, 2017):
    # 构建绝对路径
    file_path = os.path.join(script_dir, f"{year}年数据.txt")
    print(f"正在读取: {file_path}")  # 调试：确认路径

    try:
        with open(file_path, 'r', encoding='gbk') as f:  # 使用 with + 编码
            while True:
                line = f.readline()
                if not line:  # 读到文件末尾
                    break
                if line.strip() == '':
                    continue  # 跳过空行

                v = line.strip().split()
                if len(v) != 8:
                    print(f"警告: 数据列数错误，跳过 -> {line.strip()}")
                    continue

                sql = 'insert into grade values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                cs.execute(sql, (year, v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]))
        print(f"{year}年数据导入完成")
    except FileNotFoundError:
        print(f"错误：找不到文件 -> {file_path}")
    except Exception as e:
        print(f"错误：读取 {year} 年数据时出错 -> {e}")

# ------------------- 关键修改结束 -------------------

# 查询所有数据
cs.execute('select * from grade')
display(cs)

# 提交和关闭
conn.commit()
cs.close()
conn.close()