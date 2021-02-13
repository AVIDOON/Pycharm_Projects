def coordinates(x,y,z,n):
    list_items = []
    for x_value in range(x+1):
        for y_value in range(y+1):
            for z_value in range(z+1):
                if x_value + y_value + z_value != n:
                    list_items.append([x_value,y_value,z_value])

    print(list_items)

x = int(input())
y = int(input())
z = int(input())
n = int(input())
coordinates(x,y,z,n)