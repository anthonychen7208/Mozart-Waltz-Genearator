import stdaudio
import stdio
import sys

# reads waltz into 1D list
x = stdio.readAllInts()
# first half of list is minuet measures
m = x[0:16]
# second half of the list is trio measures
t = x[16:]

# checks if list is 32 measures
if len(x) != 32:
    sys.exit("A waltz must contain exactly 32 measures.")

# checks if minuet measures are between 1 and 176
for i in range(len(m)):
    if 1 <= m[i] <= 176:
        # plays first 16 minuet measure
        stdaudio.playFile("data/M" + str(m[i]))
    else:
        sys.exit("A minuet measure must be from [1, 176]")

# checks if trio measures are between 1 and 96
for i in range(len(t)):
    if 1 <= t[i] <= 96:
        # plays last 16 trio measures
        stdaudio.playFile("data/T" + str(t[i]))
    else:
        sys.exit("A trio measure must be from [1, 96]")
