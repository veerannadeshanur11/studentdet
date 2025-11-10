import sys
#checks if coreect number of argument a

if len(sys.argv) ==3;
    script_name=sys.argv[0]
    name= sys.argy[1]
    rollno=sys.argv[2]
    print("User provide input values:")
else:
    script_name=sys.argv[0]
    name= "Sayed"
    rollno="067"
    print("No Input given -using default values:")
print("Script Name:",script_name)
print("Student Name:",name)
print("Student Rollno:",rollno)
