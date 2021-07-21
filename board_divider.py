#6/19/2021
#board divider

def board_divider(length,divisions):
    total = (length / divisions)
    return total


print("\nWelcome to the Board Divider Program.")


length = float(input("What is the length of the board to be divided?(inches): "))
inset = float(input("How far from the edge is the hardware inset?(inches): "))
width = float(input("Whats it the width if the board?(inches): "))
divisions= float(input("Enter the number of divisions you want?:(whole numbers only) "))
hardware =int(input("How many pieces of hardware are you using?: "))

length2 = length - (inset *2)
calc=round(board_divider(length2,(divisions+1.15)),3)
print(f"The board divisions are: {calc} inches.")

centerfinder = (length/2,  width/2,) 
print(f"The board center is:{centerfinder}inches from the edge.")