#Recursividad para calcular el factorial de un número.
from functools import cache

@cache
def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero positivo o cero.")
    
    return n * factorial(n-1) if n else 1

def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    try:
        print("The factorial of 5 is: ", factorial(5))
    except ValueError as e:
        print(e)
        
    print("=================================================================.")
    print("Test Case 2: Check the Factorial of a number of your choice.")
    print("=================================================================.")
    numero = input(">>> Dime el número del que quieres conocer su factorial: ")
    try:
        numero = int(numero)
        try:
            print(f"The factorial of {numero} is: ", factorial(numero))
        except ValueError as e:
            print(e)
    except:
        print("Debe introducir un número entero")
            
        
if __name__ == "__main__":
    main()
    