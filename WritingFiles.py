
#Append Mode
company_designations = open("Employees.txt","a")

#Checking the writability
print(company_designations.writable())
#Appending text in document
company_designations.write("\nPrateek - Human Resources")

company_designations.close()

#Overriding By Write Mode
company_designations = open("Employees.txt","w")
company_designations.write("This is the first line of Employees.txt file")
company_designations.close()

#Finally reading out the file
company_designations = open("Employees.txt","r")
print(company_designations.read())
company_designations.close()
