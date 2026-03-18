from PIL import Image
boy = Image.open("boy.png")
playground = Image.open("playground.jpg")
w,h = boy.size
boy=boy.resize((w//2,h//2))#缩放
playground.paste(boy,(620,140),mask=boy.split()[3])#（620，140）表示小男孩图标左上角像素在场景中位置，后表示将a作为透明度分量
playground.save("final.jpg")
from PIL import Image
boy = Image.open('boy.jpg')
boy=boy.convert('RGBA')#switch the mode
w,h=boy.size
for x in range(0,w):
    for y in range(0,h):
        r,g,b,a=boy.getpixel((x,y)) #取出（x，y）处颜色
        if(g+1)/(r+g+b+3)>0.4 and g>60:
            a=0
            boy.putpixel((x, y), (r, g, b, a))  # 修改（x,y)处函数
boy.save('boy.png') #png格式支持透明度