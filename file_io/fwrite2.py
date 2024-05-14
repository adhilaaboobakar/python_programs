# Write all century years from 1800 to 2024 in to century_years.txt


# path="C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\century_years.txt"

# f=open(path,"w")

# for year in range(1800,2025):
#     if year%100==0:
#         f.write(str(year)+"\n")


# Write all years from 1800 to 2024 in to years.txt

# path="C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\years.txt"

# f=open(path,"w")

# for year in range(1800,2025):
#     f.write(str(year)+"\n")


# read all years from years.txt and print leap years.

# path="C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\years.txt"
# f=open(path,"r")

# for line in f:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         print(year)

# write all the leap_years in to leap_years.txt (read from years.txt)

read_path=path="C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\years.txt"

write_path="C:\\Users\\adhil\\Desktop\\Luminar\\python_programs\\file_io\\leap_years.txt"


fr=open(read_path,"r")
fw=open(write_path,"w")

for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        fw.write(str(year)+"\n")