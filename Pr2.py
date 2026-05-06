location = input("Enter current location (A/B): ").upper()
A = input("Enter status of A (Dirty/Clean): ").upper()
B = input("Enter status of B (Dirty/Clean): ").upper()

if location == "A":
    if A == "DIRTY":
        print("Action: Suck dirt at A")
        A = "CLEAN"
    else:
        print("Action: Move Right to B")
        location = "B"

elif location == "B":
    if B == "DIRTY":
        print("Action: Suck dirt at B")
        B = "CLEAN"
    else:
        print("Action: Move Left to A")
        location = "A"

print("\nFinal State:")
print("Location:", location)
print("A:", A)
print("B:", B)
print("\nJayant75")
