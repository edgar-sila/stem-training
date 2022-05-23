# Short hand syntax
op = int(input("Enter first number: "))
op_two = int(input("Enter second number: "))
op_three = input("Enter operator: ")

if "*" == op_three:
    print(op*op_two)
elif "+" == op_three:
    print(op+op_two)
elif"-"== op_three:
    print(op-op_two)
elif"%"==op_three:
    print(op%op_two)
elif"/"== op_three:
    print(op/op_two)
else:
    print("invalid option")
    