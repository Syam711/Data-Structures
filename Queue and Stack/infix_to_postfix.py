exp = input()

op = []
res = ''
for i in exp:
    if i=='(':
        op.append(i)
    elif i==')':
        while op and op[-1]!='(':
            res += op.pop()
        op.pop()
    elif i in '*/+-^':
        if i in '+-':
            while op and op[-1] in '*/-+^':
                res+=op.pop()
            op.append(i)
        elif i in '*/':
            while op and op[-1] in '*/':
                res += op.pop()
            op.append(i)
        elif i=='^':
            while op and op[-1]=='^':
                res += op.pop()
            op.append(i)
        
    else:
        res += i

while(op): res += op.pop()
print(res)