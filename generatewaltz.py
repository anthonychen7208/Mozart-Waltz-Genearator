import stdarray
import stdrandom
import stdio

# declare rows and column count for minuet and trio arrays
M_ROW = 11
T_ROW = 6
COL = 16

# read minuet measures into 2d list with dimensions 11X16
minuet = stdarray.create2D(M_ROW, COL, 0)
for i in range(M_ROW):
    for j in range(COL):
        minuet[i][j] = stdio.readInt()

# read trio measures into 2d list with dimensions 6X16
trio = stdarray.create2D(T_ROW, COL, 0)
for i in range(T_ROW):
    for j in range(COL):
        trio[i][j] = stdio.readInt()

for i in range(16):
    # simulate 2 die rolls
    die1 = stdrandom.uniformInt(1, 7)
    die2 = stdrandom.uniformInt(1, 7)
    die3 = die1 + die2
    # return 16 minuet measures with with column as value from 1-15 and
    # row as sum of 2 die rolls
    stdio.write(str(minuet[die3 - 2][i]) + " ")

for i in range(16):
    # simulate 1 die roll
    die = stdrandom.uniformInt(1, 7)
    # return 16 minuet measures with with column as value from 1-15 and
    # row as 1 die roll
    stdio.write(str(trio[die - 1][i]) + " ")
stdio.writeln()
