employee={"id":1000,"name":"hari","department":"developer","salary":40000}

# update the depmnt to senior developer

employee.update({"department":"senior_developer"})
print(employee)

# print("salary" in employee)

if"salary" not in employee:
    employee["salary"] =45000
else:
    employee["salary"]+=1000
print(employee)
