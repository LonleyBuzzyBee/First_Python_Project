from sys import argv

# script, first, second, third = argv
#
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third


first = raw_input("How old are you? ")
second = raw_input("How tall are you? ")
third = raw_input ("How much do you weight? ")

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print argv
