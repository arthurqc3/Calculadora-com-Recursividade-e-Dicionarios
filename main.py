from art import logo
from replit import clear

# Calculador

# Adição
def add(n1, n2):
  return n1 + n2

# Subtração
def subtract(n1, n2):
  return n1 - n2

# Multiplicação
def multiply(n1, n2):
  return n1 * n2

# Divisão
def divide(n1, n2):
  return n1 / n2

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("Qual é o primeiro numero da operação?: "))

  print("Deseja fazer qual operação?")
  should_continue = True

  while should_continue:
    for key in operations:
      print(key)
    symbol = input("= ")
    num2 = float(input("Qual é o próximo numero da operação?: "))

    calculation = operations[symbol]
    answer = calculation(num1, num2)

    print(f"{num1} {symbol} {num2} = {answer}")

    if input(f"Digite 'y' continuar a fazer operação com {answer} ou 'n' para fazer uma nova operação: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()
    
calculator()
