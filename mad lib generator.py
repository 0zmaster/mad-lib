#open file
#set variable for all the mad libs
#once a mad lib is selected, call a fuction to interpret more

with open('./mad libs.txt', 'r') as file:
    mad_libs = file.read()

mad_libs1 = mad_libs.encode("utf-8")
    
mad_libs1 = mad_libs1.split('#')


print(mad_libs)
