#set is a collection which is unordered, unindexed

utensils = {"fork", "spoon", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}



#utensils.add("napkin")    
#utensils.remove("fork")
utensils.update(dishes)
#utensils.clear()
dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
#for x in dinner_table:
#    print(x)