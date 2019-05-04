def cleanfiles():
  counter = 0
  file1 = open(input("Enter the first file name: "),"r")
  firstfile = file1.readlines()
  file2 = open(input("Enter the second file name: "), "r")
  secondfile = file2.readlines()
  file3 = open("output.txt", "w")
  for line in firstfile:
    if line in secondfile:
      counter += 1
    else:
      file3.write(line)
	  
  print("removed {} lines".format(counter))
    
def cleandupes():
  lines = []
  file = open(input("Enter the name of the file you would like to remove dupes from: "), "r")
  output = open("output.txt", "w")
  for line in file.readlines():
    if line not in lines:
      lines.append(line)
      output.write(line)
  print("Complete!")
def mergefiles():
  file1 = open(input("Enter the name of the first file you would like to merge: "), "r")
  file2 = open(input("Enter the name of the second file you would like to merge: "), "r")
  output = open("output.txt", "w")
  for line in file1.readlines():
    output.writelines(line)
  output.writelines("\n")
  for line in file2.readlines():
    output.writelines(line)

print("Sywren's List Manipulator\n" + "*" * 30)
print("Options\n1: Clean Two Files from Cross Duplicates\n2: Clean a File from Duplicate Lines\n3: Merge Two files\n9: Exit")
option = int(input("Enter option: "))
if option == 1:
  cleanfiles()
elif option == 2:
  cleandupes()
elif option == 3:
  mergefiles()
elif option == 9:
  exit()
else:
  print("Invalid option!")
