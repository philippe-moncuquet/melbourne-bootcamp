import sys

my_list = sys.argv
argument_list = sys.argv[1:len(sys.argv)]
argument_list.sort()

#first_letter = argument_list[0][0]
#print first_letter
#upper_first_letter = first_letter.upper()
#print upper_first_letter
#exit
#argument_list[0].replace(first_letter, upper_first_letter)

title = argument_list[0].title()

print title + ","
for elt in range(1,len(argument_list)-1):
    print argument_list[elt] + ",",

print "and " + argument_list[-1] + "."

#print argument_list


#script_name = sys_argv[0]
#argument1 = sys_argv[1]
#argument2 = sys_argv[2]

# some new comment
