
print("=== RESISTOR COLOR CODE GAME ===")
print("Hi Francheska! Hulaan mo yung value:")
print("")

print("Tanong: Brown - Black - Red - Gold")
print("A. 1000 ohms")
print("B. 100 ohms") 
print("C. 10 ohms")
print("")

sagot = input("Type mo sagot mo A/B/C: ")

if sagot == "A" or sagot == "a":
    print("TAMA! 🔥 1k ohms nga!")
    print("Brown=1, Black=0, Red=x100, Gold=±5%")
    print("Future TI Clark engineer ka na talaga!")
else:
    print("Mali 😅 Ang sagot: A. 1000 ohms")
    print("Brown=1, Black=0, Red=x100 = 10 x 100 = 1000")
    
print("")
print("Game Over. Galingan mo next time!")