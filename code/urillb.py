import urllib.request as req
import re


url='https://www.nudt.edu.cn/bkzs/xxgk/lqfs/index.htm'
webpage=req.urlopen(url)
webdata=webpage.read().decode('utf-8')
for year in range(2016, 2019):
    substr=str(year)+'年录取分数统计'
    index=webdata.find(substr)
    href=webdata[ index-133 : index-97 ]
    href='https://www.nudt.edu.cn/bkzs/xxgk/lqfs/'+href
    webpage=req.urlopen(href)
    content=webpage.read().decode('utf-8')
    tables=re.findall(r'<table.*?>(.*?)</table>',content, re.S)
    table=tables[0]
    rows = re.findall(r'<tr.*?>(.*?)</tr>', table, re.S)
    datalist=[]
    for row in rows:
        tds = re.findall(r'<td.*?>(.*?)</td>', row, re.S)
        data_row=[]
        for td in tds:
            items = re.findall(r'<p.*?>(.*?)</p>', td, re.S)
            if len(items)>0:
                data_row.append(items[0])
        datalist.append(data_row)
    outfile=open(str(year)+'年数据.txt','w',encoding='utf-8')
    for rows in datalist:
        for cell in rows:
            outfile.write(cell+'\t')
        outfile.write('\n')
    outfile.close()
