exp = input()

operand = []

cur_num = ''
prev = True
for i in exp:
    
    if 48<=ord(i)<=57:
        cur_num += i
        prev = True
    if i==' ' and prev:
        operand.append(cur_num)
        cur_num = ''
    if i in '+-*/':
        prev = False
        o1 = operand.pop()
        o2 = operand.pop()
        if i=='+': operand.append(f'({o1}+{o2})')
        elif i=='-': operand.append(f'({o2}-{o1})')
        elif i=='*': operand.append(f'({o1}*{o2})')
        elif i=='/': operand.append(f'({o2}/{o1})')
        
print(operand[0])

