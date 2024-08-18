
num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))
if num2 != 0:
   
    result = num1 / num2
   
    print(f"The result of dividing {num1} by {num2} is: {result}")
else:
    
    print("Division by zero is not allowed. Please enter a non-zero second number.")
