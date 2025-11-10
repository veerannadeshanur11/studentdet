import sys
if len(sys.argy)== 3:
  script_name=sys.argv[0]
  name=sys.argv[1]
  print("User provided input values:")
else:
  script_name=sys.argv[0]
  name="shreyas"
  rollno="101"
  print("No input given - using default values:")
print("Script Name:", script_name)
print("Student Name:", name)
print("Roll Nuumber:",rollno)
