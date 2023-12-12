line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position_line = int(input("Please enter the line number (1, 2, 3) you want to hide the treasure in:\n"))-1

position_row_b = input("Please enter the row letter (A, B, C) you want to hide the treasure in:\n")

if position_row_b.casefold() == "a":
    position_row = 0
elif position_row_b.casefold() == "b":
    position_row = 1
elif position_row_b.casefold() == "c":
    position_row = 2

map[position_line][position_row] = "X"

print(f"{line1}\n{line2}\n{line3}")
