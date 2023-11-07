# A module is a simple file containing diffeent python definitions and statements


# print(__name__)

# if __name__ == "__main__":
#     print("Arithmetics module is initialised")



def add(a,b):
   return a + b

if __name__ == "__main__":
# This if statement restricts subtract, divide 
# and multiply from being imported, but add can be imported
    def subtract(a,b):
        return a - b

    def divide(a,b):
        return a / b

    def multiply(a,b):
        return a * b

