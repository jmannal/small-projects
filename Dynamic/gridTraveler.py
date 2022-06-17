rows = int(input("Enter Rows: "))
cols = int(input("Enter Cols: "))

def gridTraveler(rows, cols, memo = {}):
    if (rows, cols) in memo:
        return memo[(rows, cols)]

    # Reflected grid will have same value
    if (cols, rows) in memo:
        return memo[(cols, rows)]

    if cols == 0 or rows == 0:
        return 0
    if cols == 1 or rows == 1:
        return 1

    memo[(rows, cols)] = gridTraveler(rows - 1, cols, memo) + gridTraveler(rows, cols - 1, memo)
    return memo[(rows, cols)]

print(gridTraveler(rows, cols))