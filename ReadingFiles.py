
company_designations = open("Employees.txt","r")

##Checking if the file is readable or not
print(company_designations.readable())  #Returns true or false

#Reading the complete file
#print(company_designations.read())

#Reading line by line
#print(company_designations.readline())
#print(company_designations.readline())

#Reading the document and converting the line by line data in a list
#company_designations_list = company_designations.readlines()
#print(company_designations_list)
for designation in company_designations.readlines():
   print(designation)

company_designations.close()