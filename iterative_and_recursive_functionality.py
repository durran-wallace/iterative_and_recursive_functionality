#Marty Wallace CIS261 iterative and recusive functionality

def iterative_factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    print(str(n) + "! = %s" % result)  

def recursive_factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recursive_factorial(n-1)
    
def print_output(n):
    print(str(n) + "! = %s" % recursive_factorial(n))
 
def main():
    print("Factorial results using an iterative function")
    iterative_factorial(0)
    iterative_factorial(5)
    iterative_factorial(10)
    iterative_factorial(25)
    iterative_factorial(50)
    iterative_factorial(100)
    print("Factorial results using a reecursive function")    
    print_output(0)
    print_output(5)
    print_output(10)
    print_output(25)
    print_output(50)
    print_output(100)
    
if __name__ == "__main__":
    main()

    
