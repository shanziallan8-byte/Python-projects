num1 = float(input("Enter the first number:"))
operator = input("Enter the operator (+,-,*,/,%,**):")
num2 = float(input("Enter the second number:"))
if operator =="+":
  result = num1 + num2
elif operator =="-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  result = num1/num2 if num2!=0 else print("Error: Division by zero")
elif operator =="%":
  result = num1 % num2 if num2!=0 else print("Error:Modulo by zero")
elif operator == "**":
  result = num1 ** num2
else:
  result = "lnvalid operator!"

print(f"Result: {result}")
