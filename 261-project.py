import requests
equation=input("Enter your Equation:")
result='https://newton.now.sh/api/v2//simplify/'+equation
data=requests.get(result).json()
print("Operation of Equation is:",data['operation'])
print("Expression of Equation is:",data['expression'])
print("Answer of Equation is:",data['result'])

