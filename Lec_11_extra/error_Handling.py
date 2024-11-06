# Error Handling (Extra Study)
# source: https://youtu.be/NIWwJbo-9_8?feature=shared 

try:
    f = open('practice.txt')
    if f.name == 'practice.txt':    # manually raising exception
        raise Exception
    # var  = bad_var 
except FileNotFoundError:          # named Exception
    print("Error: Sorry this file does'nt exist!")
except Exception:                  # general exception
    print("Error: Something went wrong!")
else:                              # No exception then executes
    f.read()
finally:                           # always executes no matter what!
    print("finally block always executes!!")
