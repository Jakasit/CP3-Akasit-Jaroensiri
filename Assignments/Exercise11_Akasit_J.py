KeyInput = int(input())
x= KeyInput
y=""
z="*"
for i in range(KeyInput) :
    x = x - 1
    for j in range(x) :
        y = y + " "
    print(y+z)
    z=z+"**"
    y=""