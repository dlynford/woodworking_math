#6/19/2021
#Board foot calculator: attempt1
#Board Foot Calculation informs a woodworker how much wood they need to purchase for a project
#and how much the raw materials will cost.

def board_foot_calc(length,width,thickness):
    board_feet = ((length * width * thickness)/144)
    return board_feet 

print("\nWelcome to the board foot calculator program.")
#number_of_boards = input(int("How many boards do you want to purchase?: "))
species = input("What wood species are you purchasing?: ")
species_cost = float(input(f"How much does {species} cost per board/foot?: "))
length = float(input("Enter the board length (inches): "))
width = float(input("Enter the board width (inches): "))
thickness = float(input("Enter the board thickness (inches): "))

bf_calc = round(board_foot_calc(length,width,thickness),2)
cost = bf_calc * species_cost
cost = round(cost,2)
print(f"Total board feet = {bf_calc} \nThe cost is = ${cost}")





