exp = input()

operand = []

cur_num = 0
prev = True
for i in exp:
    
    if 48<=ord(i)<=57:
        cur_num = cur_num*10 + int(i)
        prev = True
    if i==' ' and prev:
        operand.append(cur_num)
        cur_num = 0 
    if i in '+-*/':
        prev = False
        o1 = operand.pop()
        o2 = operand.pop()
        if i=='+': operand.append(o1+o2)
        elif i=='-': operand.append(o2-o1)
        elif i=='*': operand.append(o1*o2)
        elif i=='/': operand.append(o2/o1)
        
print(operand[0])