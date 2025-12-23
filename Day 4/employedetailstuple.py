employeedetails = [("Pulkit Vashishth", 8, "Digital Forensics Analyst")]
## add details of employees
emp2 = ("John Doe", 5, "Software Engineer")
## adding data in list by append method
employeedetails.append(emp2)
emp3 = ("Jane Smith", 10, "Project Manager")
employeedetails.append(emp3)
emp4 = ("Alice Johnson", 3, "Data Scientist")
emp5 = ("Bob Brown", 7, "System Administrator")
## adding multiple employee details using extend method
employeedetails.extend([emp4, emp5])
## print all employee details
print (employeedetails)
## remove any employee details by pop method and specific by number
employeedetails.pop(0)
print (employeedetails)
