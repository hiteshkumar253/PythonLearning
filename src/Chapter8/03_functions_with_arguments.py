def goodDay(name, ending):
    print(f"Have a good day!, " + name)
    print(ending)

goodDay("Hitesh", "Thank you")
goodDay("Heyansh", "Thank you")
goodDay("Kalu", "Thank you")

# Another version with return value

def goodDay(name, ending):
    print(f"Have a good day!, " + name)
    print(ending)
    return "ok"

a = goodDay("Hitesh", "Thank you")
print(a)
b = goodDay("Heyansh", "Thank you")
print(b)
c = goodDay("Kalu", "Thanks")
print(c)
