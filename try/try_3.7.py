guest_list = ["Imran","Shuvo","Arif","Roni","Hira"]
a = guest_list.pop()



guest_list.append("Asraf")


print(f"{guest_list[0]} you are invited to have your dinner with me.")
print(f"{guest_list[1]} you are invited to have your dinner with me.")
print(f"{guest_list[2]} you are invited to have your dinner with me.")
print(f"{guest_list[3]} you are invited to have your dinner with me.")
print(f"{guest_list[4]} you are invited to have your dinner with me.")

print(f"{guest_list[0]} I have found a bigger table for the guest")
print(f"{guest_list[1]} I have found a bigger table for the guest")
print(f"{guest_list[2]} I have found a bigger table for the guest")
print(f"{guest_list[3]} I have found a bigger table for the guest")
print(f"{guest_list[4]} I have found a bigger table for the guest")

guest_list.insert(0,"Limon")
guest_list.insert(3,"Prince")
guest_list.insert(7,"Hasib")

print(guest_list)


print("I can invite only two people")
a = guest_list.pop(7)
print(f"{a} sorry, I can't invite you to dinner")

b = guest_list.pop(6)
print(f"{b} sorry, I can't invite you to dinner")

c = guest_list.pop(5)
print(f"{c} sorry, I can't invite you to dinner")

d = guest_list.pop(4)
print(f"{d} sorry, I can't invite you to dinner")

e = guest_list.pop(3)
print(f"{e} sorry, I can't invite you to dinner")

f = guest_list.pop(2)
print(f"{f} sorry, I can't invite you to dinner")

print(f"{guest_list[0]}, you are still invited")
print(f"{guest_list[1]}, you are still invited")

del guest_list[0]
del guest_list[1]


print(guest_list)