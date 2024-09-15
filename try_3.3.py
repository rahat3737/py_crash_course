favorite_motorcycle =["Honda CBR600RR", "Yamaha YZF-R1", "Ducati Panigale V4", "Kawasaki Ninja ZX-10R", "Suzuki GSX-R1000"]

a = (f"I would like to own a {(favorite_motorcycle[0])} motorcycle.")
b = (f"I would like to own a {(favorite_motorcycle[1])} motorcycle.")
c = (f"I would like to own a {(favorite_motorcycle[2])} motorcycle.")
d = (f"I would like to own a {(favorite_motorcycle[3])} motorcycle.")
e = (f"I would like to own a {(favorite_motorcycle[4])} motorcycle.")


print(a)
print(b)
print(c)
print(d)
print(e)


# this is another system with for loop
for motorcycle in favorite_motorcycle:
    print(f"I would like to own a {motorcycle} motorcycle.")