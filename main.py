def drawPyramid(heigth):
    if heigth == 1:
        print("#")
        return None
    # I have to count how much spaces there are before printing the ascii
    spaceNumber = heigth - 1
    # Printing the first ascii
    for i in range(0, spaceNumber):
        print(" ", end='')
    print("#")
    # asciiNumber count the number of ascii that I have to print in the next line
    asciiNumber = 3
    # Every line I have to print one less space before the ascii
    spaceNumber -= 1
# Already printed the first line
    for h in range(1,heigth):
        # Printing the spaces
        for space in range(0, spaceNumber):
            print(" ", end='')
        # Printing the ascii
        for ascii in range(0,asciiNumber):
            print("#", end='')
        # Printing newline because I finished to print the current line
        print("\n", end='')
        # Update the number of ascii ad spaces
        asciiNumber += 2
        spaceNumber -= 1

drawPyramid(8)