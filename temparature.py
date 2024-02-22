def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    else:
        print("Invalid choice. Please enter either 1 or 2.")
