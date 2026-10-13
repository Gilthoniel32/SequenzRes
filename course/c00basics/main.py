import sys 
def stop_here():
    sys.exit(0)

"""Command line output"""

print("Hallo, Welt")

stop_here()


#TODO: print "HALLOMEINNAMEISTHASE" 




"""for loops"""

for x in "ABCDEFG":
    print(x,end="")
    print("x",end="")
print()


#TODO: print this pattern (fewest lines of code wins):
#A
# B
#  C
#   D
#    E
#     F
#      G


numbers = [1,8,1,4,5]
sum = 0
for x in numbers:
    sum=sum+x

print("The sum is",sum)


#TODO: calculate the product of these numbers


#TODO: calculate the sum of all integers from 0 to 100000
for i in range(100000):
    pass



"""
File reading.
"""

with open("../data/test.fasta") as fl:
    for line in fl:
        if line.startswith(">"):
            print(line,end="")


#TODO: print all lines that do not start with ">"

"""
string slicing
"""

string = "MEINNAMEISTHASEN"
print(string[3:5])


#TODO: Use a string slice to output "EIS"


"""
functions
"""

def add(x:int,y:int)->int:
    return x+y

print("2 + 3 =",add(2,3))

#TODO: use only this function to calculate 2+3+4

#TODO: Write a function that calculates (x+y)*z


