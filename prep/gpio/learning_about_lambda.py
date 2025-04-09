print("Learning about lambda")

def def_syntax(a, b):
    print("def is a syntax to make a function")
    print("You can have many lines!")
    print(a, b)

def_syntax("Dave", "Fisher")
print(type(def_syntax))

lambda_syntax = lambda a, b: print("lambda syntaxt.  Single executable only!", a, b)

lambda_syntax("Dr.", "David Fisher")
print(type(lambda_syntax))

def real_function(a, b):
    print("Real way to use def+lambda")
    print(a, b)

callback = lambda : real_function("David", "Fisher")
callback()
