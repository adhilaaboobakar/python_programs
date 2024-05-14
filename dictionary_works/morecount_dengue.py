# more count dengue 

dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]

dengue_dict={}

for dist in dengue_list:
    if dist in dengue_dict:
        dengue_dict[dist]+=1
    else:
        dengue_dict[dist]=1
print(dengue_dict)

srt_dict=sorted(dengue_dict,key=lambda k: dengue_dict.get(k),reverse=True)
print(srt_dict)


