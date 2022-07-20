#(Functions- Passsing Arbitrary List as Argument
# Allows to collect an arbitrary number of arguments from the calling statement)

def make_pizza(size, *toppings): # '*' is given to indicate arbitrary parameter passing
    print(f"\nMaking a {size} - inch pizza with toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'pepperoni')
make_pizza(16,'mushrooms','green peppers')

#(REQUIRED AND KEYWORD ARGS
# Required Arguments : the arguments passed to a function in correct positional order. so the number of arguments in the fun call should match exactly with the function
# Keyword argument: the caller identifies the arguments by the parameter name )

#passing arguments as required and keyword args
def printInfo(name, age):
    print(f"name:", {name}, "age:",{age})

#calling with Required arguments
printInfo("Tom", 10)

#calling with keyword arguments
printInfo(age=10, name="Winnie")