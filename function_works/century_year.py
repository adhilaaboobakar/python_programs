def is_century_year(year):
    if year%100 ==0:
        return True
    else:
        return False
    
print(is_century_year(1200))