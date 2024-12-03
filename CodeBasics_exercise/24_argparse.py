# Exercise: https://github.com/codebasics/py/blob/master/Basics/Exercise/24_argparse/24_argparse.md
import argparse
import statistics

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Average of marks")
    parser.add_argument('--physics',type= float, help='inputs physics marks')
    parser.add_argument('--chemistry', type= float, help='inputs chemistry marks')
    parser.add_argument('--maths',type= float, help='inputs maths marks')

    args = parser.parse_args()
    average =(args.physics+args.chemistry+args.maths)
    result = average/3
    print(f"Average of marks is {result}")