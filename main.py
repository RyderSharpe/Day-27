
# #######################################################################################
# # Keyword Arguments
# def my_function(a, b, c):
#     # Do this with a
#     # Then do this with b
#     # Finally do this with c
# my_function(c=3, a=1, b=2) # a,b,c in any order we want as long as keyword is in front
#
# # Arguments with Default Values
# def my_function(a=1, b=2, c=3):
#     my_function()
#     # To modify
#     my_function(b=5)
# #######################################################################################

# Fixed arguments
def add(n1, n2):
    return n1 + n2
add(n1=5, n2=3)

# Unlimited Arguments
def add(*args): # '*' is required; 'args', short for arguments is a variable.
    for n in args:
        print(n)
add(n1=5, n2=3)
