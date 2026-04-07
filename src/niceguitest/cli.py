from niceguitest import logic

def main() -> None:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Result: {logic.myTestAdd(a, b).add()}")

if __name__ == "__main__":
    main()