"""
2) vytvořte funkci calculate, která bude přijímat 2 čísla a,b
- třetí parametr bude libovolná funkce, která se zavolá pro tyto čísla uvnotř funkce calculate
  - add
  - sub

funkce calculate bude mít parametry a, b, func
- calculate si uvnitř zavolá obecnou funkci func a vrátí její výsledek
funkce add a sub budou mít jen a, b


použití:

result1 = calculate(1, 2, add)
result2 = calculate(1, 2, sub)

print(result1, result2) # vyprintuje 3, -1
"""

def calculate(a, b, func):
    return func(a, b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

result1 = (calculate (1, 2, add))
result2 = (calculate (1, 2, sub))

print(result1,",", result2)