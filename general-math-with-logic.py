import math

line = '='*40
print(line)
print("The Picasso Paint Company")
print("Paint cost calculator")
print(line)
print("\nAvailable Colors")
print("1. Cloud White \t\t$27.50/gal")
print("2. Swiss Coffee \t$48.98/gal")
print("3. Hale Navy \t\t$49.99/gal")
print("4. Colonial Aqua \t$25.97/gal")
print("5. Orange Blossom \t$25.97/gal")
choice = int(input("\nPlease select a paint color: "))
cost = 0.0
if choice == 1:
    color = "Cloud White"
    cost = 27.5
elif choice == 2:
    color = "Swiss Coffee"
    cost = 48.98
elif choice == 3:
    color = "Hale Navy"
    cost = 49.99
elif choice == 4:
    color = "Colonial Aqua"
    cost = 25.97
else:
    color = "Orange Blossom"
    cost = 25.97

wall1height = float(input("Please enter the height of the first wall: "))
wall1length = float(input("Please enter the length of the first wall: "))
wall2height = float(input("Please enter the height of the second wall: "))
wall2length = float(input("Please enter the length of the second wall: "))

windowarea = 0.0
doorarea = 0.0

numwindows = int(input("Please enter the number of windows in the room: "))
if numwindows > 0:
    count = 1
    windows = []
    while count <= numwindows:
        height = float(input("Please enter the height of window #%d: " % count))
        length = float(input("Please enter the length of window #%d: " % count))
        area = height * length
        windows.append(area)
        count = count + 1
    windowarea = sum(windows)

numdoors = int(input("Please enter the number of doors in the room: "))
if numdoors > 0:
    count = 1
    doors = []
    while count <= numdoors:
        height = float(input("Please enter the height of door #%d: " % count))
        length = float(input("Please enter the length of door #%d: " % count))
        area = height * length
        doors.append(area)
        count = count + 1
    doorarea = sum(doors)
avoidarea = windowarea + doorarea

coats = int(input("Please enter the number of coats needed: "))

wall1 = wall1height * wall1length
wall2 = wall2height * wall2length
totalarea = (2 * wall1) + (2 * wall2)

areatopaint = totalarea - avoidarea

#assumtion that 1 paintcan covers approximately 400 sq ft
numgallons = areatopaint / 400
numgallons = int(math.ceil(numgallons))
price = (numgallons * cost) * coats

print("")
print(line)
print("Estimate of cost of painting a room by\nThe Picasso Paint Company")
print(line)
print("\nRoom Dimensions:")
print("   Wall #1:\t\t%.2f by %.2f square feet." % (wall1height, wall1length))
print("   Wall #2:\t\t%.2f by %.2f square feet." % (wall2height, wall2length))
print("   Area to be Painted: \t%.3f square feet." % areatopaint)
print("\nPaint Information:")
print("   Paint color: \t%s at $%.2f per gallon." % (color, cost))
print("   Gallons needed:\t%d gallons for 1 coat." % numgallons)
if coats>1:
    print("\t\t\t%d gallons for %d coats." % ((numgallons * coats), coats))
print("")
print(line)
print("Total cost: \t\t$%.2f" % price)
print(line)
