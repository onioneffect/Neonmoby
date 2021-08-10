import neonmob

my_cool_set = neonmob.get_set_by_id(input("Enter an id number from neonmob.com: "))
my_cool_tuple = my_cool_set.get_values("id", "name", "preview_0")

print(type(my_cool_set))
print("Set id: ", my_cool_tuple[0])
print("Set name: ", my_cool_tuple[1])
print("Preview image: ", my_cool_tuple[2])
