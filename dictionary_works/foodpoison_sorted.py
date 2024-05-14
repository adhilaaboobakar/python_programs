sh_death={"tsr":2,"kzd":3,"ekm":5,"tvm":4,"alpy":2}

sh_sort=sorted(sh_death,key=lambda k:sh_death.get(k),reverse=True)
print(sh_sort)