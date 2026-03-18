#name=input('enter your name:')
#age=int(input('please enter your age:'))

#print(f'Hello {name}, you are {age+1} years old next year')

#score=int(input('enter your score:'))

#if score >=90:
#    print('you got it right')
#elif score>=60:
#    print('keep working')
#else:
#    print('failed')

#for i in range(1,6):
#    print('第',i,'次循环')

##count=0
#while count <=3:
#    print('loading...',count)
#    count+=1

print('welcome to use the scores calculator')
scores=[]

while True:
    s=input('please enter your score or enter exit to exit:')
    if s == 'exit':
        break
    try:
        scores.append(float(s))
    except ValueError:
        print('please enter a number')
if scores:
    avg = sum(scores)/len(scores)
    if avg >= 90:
        print('fabulous')
    elif avg >= 70:
        print('good job')
    else:
        print('keep working')
else:
    print('no scores')