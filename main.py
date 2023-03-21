import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def addition(x, y):
    logging.info(f"Dodaję {x} i {y}")
    print(f"{x} + {y} = {x + y}")

def subtraction(x, y):
    logging.info(f"Odejmuję {y} od {x}")
    print(f"{x} - {y} = {x - y}")

def multiplication(x, y):
    logging.info(f"Mnożę {x} i {y}")
    print(f"{x} * {y} = {x * y}")

def division(x, y):
    logging.info(f"Dzielę {x} przez {y}")
    print(f"{x} / {y} = {x / y}")

if __name__ == "__main__":
        operation = int(input("""Podaj działanie, posługując się odpowiednią liczbą: 
        1 Dodawanie, 
        2 Odejmowanie, 
        3 Mnożenie, 
        4 Dzielenie: """))
        if operation == 1:
                x = int(input("Podaj składnik 1: "))
                y = int(input("Podaj składnik 2: "))
                addition(x, y)
        if operation == 2:
                x = int(input("Podaj składnik 1: "))
                y = int(input("Podaj składnik 2: "))
                subtraction(x, y)
        if operation == 3:
                x = int(input("Podaj składnik 1: "))
                y = int(input("Podaj składnik 2: "))
                multiplication(x, y)
        if operation == 4:
                x = int(input("Podaj składnik 1: "))
                y = int(input("Podaj składnik 2: "))
                division(x, y)