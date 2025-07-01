import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Função que realiza operações básicas. Retorna NaN se o operador for inválido.
    """
    result = float("nan")
    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            raise ZeroDivisionError
    elif operador == '**':
        result = num1 ** num2
    return result


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Operações disponíveis: +  -  *  /  **")
            operador = input("Escolha a operação: ")

            resultado = calculadora(num1, num2, operador)
            
            if resultado != resultado:  # verifica se é NaN
                print("\nOperação inválida!")
            else:
                print(f"\nResultado: {resultado}")

        except ValueError:
            print('\nDados inválidos! -> Tente novamente!')
            time.sleep(2)
            continue

        except ZeroDivisionError:
            print('\nImpossível dividir por zero! -> Tente novamente!')
            time.sleep(2)
            continue

        opcao = input("\nDeseja fazer outra operação? (s/n): ").lower()
        if opcao != 's':
            break

    print('\nVolte sempre!\n')
