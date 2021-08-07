import neonmob

set_id = input("Enter a set id from neonmob.com: ")
my_cool_set = neonmob.get_set_by_id(set_id)

for j in my_cool_set.get_values("name", "id", "description"):
    print(j)
