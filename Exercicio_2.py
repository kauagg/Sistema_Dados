
def fahrenheit_para_celsius(f):
    celsius = 5 * ((f - 32) / 9)
    return round(celsius, 2)

def main():
    try:
        fahrenheit = float(input("Informe a Temperatura em °F: "))
        
        # Removido a verificação de temperatura negativa
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura Correspondente em °C é: {celsius} °C")
        
    except ValueError:
        print("Erro? insira um número.")

if __name__ == "__main__":
    main()