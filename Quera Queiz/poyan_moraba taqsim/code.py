# gets the string of pieces and turns it into a list (each item splitted by `space`)
chess_pieces = input().split(' ')

# creates a variable containing the ideal amount of chess pieces needed in said order
ideal_pieces = [1, 1, 2, 2, 2, 8]

# creates an empty list in order to save the amount needed to add or substract in order to reach the ideal amount of pieces
needed_pieces = []

# loops through each piece in `chess_pieces` and saves it's index into `i`
for i, piece in enumerate(chess_pieces):
    # calculates the needed amount to substract or add and saves it into the `needed_pieces` list
    needed_pieces.append(str(ideal_pieces[i] - int(piece)))
    
# creates and prints a string containing each item of `needed_pieces`, seperating them by 1 space
print(' '.join(needed_pieces))