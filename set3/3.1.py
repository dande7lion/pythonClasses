# a)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# This code will probably work properly, but in python we do not use semicolon (;) at the end of statement.

##########################

# b)
for i in "qwerty": if ord(i) < 100: print (i)

# This code is invalid. In python it is important to use new line and tabulators
# Proper version of this code:

for i in "qwerty":
    if ord(i) < 100:
        print (i)

##########################

#c)
for i in "axby": print (ord(i) if ord(i) < 100 else i)

# This code works fine, but it will be better to put the print statement at the next line
