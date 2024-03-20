def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = '+'
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if char in "+-*/" or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            sign = char
            num = 0
    return sum(stack)


s = "3+2*2"
print("Expression:", s)
print("Result:", calculate(s))

s = " 3/2 "
print("Expression:", s)
print("Result:", calculate(s))

s = " 3+5 / 2 "
print("Expression:", s)
print("Result:", calculate(s))
