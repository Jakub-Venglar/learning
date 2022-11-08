#! python3
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'supergoose'],
             ['fork', 'pot', 'spoooon', 'knife']]

def table_printer (table):
#nejprve zjistim nejdelsi slovo pro kazdy podseznam a ulozim ho do listu spolu s rezervou abych mel sirku sloupce
    colWidths = [0] * len(tableData)
    for indx, lists in enumerate(table):
        length = 0
        for items in lists:
            newLength = len(items)
            if newLength > length:
                length = newLength
        colWidths[indx] = length+4
#z kazdeho podseznamu vezmu odpovidajici slovo podle radku a tisknu
    rows = len(table[0])
    rowsCounter = 0
    while True:
        for indx, lists in enumerate(table):
            print(lists[rowsCounter].rjust(colWidths[indx]),end='')
        rowsCounter+=1
        print()
        if rowsCounter == rows:
            break

table_printer(tableData)

