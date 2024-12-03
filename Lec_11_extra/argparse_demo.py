# Tutorial: https://www.youtube.com/watch?v=OxpBMNalsDM
import argparse

if __name__ == "__main__":
    # Initialize the parser
    parser = argparse.ArgumentParser(description="Perform basic arithmetic operations.")

    # Add arguments
    parser.add_argument('--n1', type=int, help='Input number 1')
    parser.add_argument('--n2', type=int, help='Input number 2')
    parser.add_argument('--op', type=str, help="Specify the operation: add, sub, mul, or div")

    # Parse the command-line arguments
    args = parser.parse_args()
    result  = None
    # Perform the operation based on the 'op' argument
    if args.op == "add":
        result = args.n1 + args.n2
        print(f"Sum: {args.n1} + {args.n2} = {result}")
    elif args.op == "sub":
        result = args.n1 - args.n2
        print(f"Difference: {args.n1} - {args.n2} = {result}")
    elif args.op == "mul":
        result = args.n1 * args.n2
        print(f"Product: {args.n1} * {args.n2} = {result}")
    elif args.op == "div":
        if args.n2 != 0:
            result = args.n1 / args.n2
            print(f"Quotient: {args.n1} / {args.n2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Use one of: add, sub, mul, div.")