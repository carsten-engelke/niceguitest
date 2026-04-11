from niceguitest import logic
import sys, argparse

def main(argv=sys.argv[1:]) -> None:
    try:
        test_add = parse_arguments(argv)
        if len(argv) > 1: # set minimum number of arguments to trigger automated calculation, otherwise fall back to interactive mode
            print(f"Result: {test_add.add()}")
        else:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            print(f"Result: {logic.myTestAdd(a, b).add()}")
    except ValueError as e:
        print(f"Error: {e}")

def parse_arguments(argv):
    print("Parsing CLI arguments:", argv)
    parser = argparse.ArgumentParser(description="A simple CLI for adding two numbers.")
    parser.add_argument("a", type=int, help="The first number to add.", default=0, nargs='?')
    parser.add_argument("b", type=int, help="The second number to add.", default=0, nargs='?')
    args = parser.parse_args(argv)
    return logic.myTestAdd(args.a, args.b)

if __name__ == "__main__":
    main(sys.argv[1:])