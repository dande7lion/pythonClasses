# What is wrong with that code?

# a)
L = [3, 5, 4] ; L = L.sort()
# This code will work, but probably not the way that we expected. Now in variable L we keep that what "sort" function
# returned - which is "None". If we want to sort our list, we should use just
L.sort()
# instead of L = L.sort()

#b)
x, y = 1, 2, 3
# We want to assign three values to only two variables. Instead of this we can e. g. use:
x, y, z = 1, 2, 3 #or
x, y = 1, 2

#c)
X = 1, 2, 3 ; X[1] = 4
# With X = 1, 2, 3 we create a tuple, which does not support item assignment and is unchangeable. 
# Probably the best way to make this code work in way that we want is to use list:
X = [1, 2, 3]
X[1] = 4    # works fine, X = [1, 4, 3]

#d)
X = [1, 2, 3] ; X[3] = 4
# We can not do this, becuase list assignment index is out of range. We can only assign items from indexes 0 - 2.
# If we want to add a new item, we should use e.g:
X.append(4)

#e)
X = "abc" ; X.append("d")
# X is a string and it has no attribute "append". If we want to add "d" to our string we should use e.g.:
X += "d"

#f)
L = list(map(pow, range(8)))
# This code will not work, because "pow" function needs two arguments. In this example it got only one argument.
