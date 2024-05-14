students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"}
]


# q1 total number of students

# print("total students :",len(students))

# q2 print all student names

# for student in students:
#     print(student.get("name"))

# std_name=[stud.get("name") for stud in students]
# print(std_name)

# q3 print the students name with experience greater than 2

# exp_get_one=[stud.get("name") for stud in students if stud.get("exp")>1]
# print(exp_get_one)

# q4 print students name whose skills contains both java and python

# python_and_java = [stud.get("name") for stud in students if "java" in stud.get("skills") and "python" in stud.get("skills")]
# print(python_and_java)

# for stud in students:
#     if "java" in stud.get("skills") and "python" in stud.get("skills"):
#         print(stud.get("name"))

# q5 print mca students name

# mca_students=[stud.get("name") for stud in students if stud.get("qualification")=="mca"]
# print(mca_students)

# q6 most experienced student


# most_exp_stud=max(students,key=lambda d: d.get("exp"))

# highest_exp=most_exp_stud.get("exp")

# highest_exp_students=[stud.get("name")for stud in students if stud.get("exp")==highest_exp]
# print(highest_exp_students)

# q7 print students names having skills>2

# for stud in students:
#     if len(stud.get("skills"))>2:
#         print(stud.get("name"))

# q8 print students name start with j

# for stud in students:
#     if stud.get("name").startswith("j"):
#         print(stud.get("name"))

# q9:print ravi's experience

# for stud in students:
#     if stud.get("name")=="ravi":
#         print(stud.get("exp"))

# q10:print most selected skill


skill_count={}
for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)

max_value=max(skill_count,key=lambda x:skill_count.get(x))
print(max_value)