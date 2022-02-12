def calculate (number1, op, number2):
    if op == '+' : return number1 + number2
    elif op == '-' : return number1 - number2
    elif op == '*' : return number1 * number2
    elif op == '/' : return number1 / number2
    else : return "invalid operand"
    

if __name__ == "__main__":
    number1 = input("input number1 : ")
    
    op = input("input operator : ")
    
    number2 = input("input number2 : ")
    
    res = calculate(float(number1), op, float(number2))
    print("res : " + str(res))