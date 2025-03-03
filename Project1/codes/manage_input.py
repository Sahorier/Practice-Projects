category = None
# global category
def manage_input():
    global category
    print("input 1(electronics), 2(clothing), 3(Home), 4(Footwear), 5(Accessories), 6(Health), 7(Sports)")
    choice = input(">> ")
    if choice == "1":
        category = "Electronics"
    elif choice == "2":
        category = "Clothing"
    elif choice == "3":
        category = "Home"
    elif choice == "4":
        category = "Footwear"
    elif choice == "5":
        category = "Accessories"
    elif choice == "6":
        category = "Health"
    elif choice == "7":
        category = "Sports"
manage_input()
# print(category)