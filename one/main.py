

def reve():
    # 如果是一个list
    tempList = [1,2,3,4]
    tempList.reverse()
    for x in tempList:
        print(x,end=' ')

    print('\n------')
    #如果不是list
    tempTuple = (1,2,3,4)
    for i in range(len(tempTuple)-1,-1,-1):
        print(tempTuple[i],end=' ')
    print()
    ## 当然还有这个方法
    print(tempTuple[::-1])

def sub():
    # 使用Python中的replace()可以替换一个文本字符串
    tempstr = 'Hello Java,Hello Python,Use javaScript!'
    print(tempstr.replace('Hello','Bye'))
    # 使用Python中的sub()，可以用来查找并替换字符串，sub是通过正则来匹配的
    import re
    rex = r'(Hello|Use)'
    print(re.sub(rex,'Bye',tempstr))


if __name__ == '__main__':
    sub()