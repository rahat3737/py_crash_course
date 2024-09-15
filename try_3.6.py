guest_list = ["Imran","Shuvo","Arif","Roni","Hira"]
a = guest_list.pop()
print(f"{guest_list[0]} you are invited to have your dinner with me.")
print(f"{guest_list[1]} you are invited to have your dinner with me.")
print(f"{guest_list[2]} you are invited to have your dinner with me.")
print(f"{guest_list[3]} you are invited to have your dinner with me.")
# print(f"{guest_list[4]} you are invited to have your dinner with me.")
print(a)



guest_list.append("Asraf")
print(f"{a} can't come.")
print(guest_list)



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

print (*guest_list, sep="you are invited\n")


 
