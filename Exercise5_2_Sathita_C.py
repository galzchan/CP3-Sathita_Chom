distance = 0
while distance < 1:
    distance = int(input("distance (kilometer) : "))
    if distance < 1 :
        print("Error : Please enter a number more than or equal 1.")

deltaTime = 0
while deltaTime < 1:
    deltaTime =  int(input(" time (hr) : "))
    if deltaTime < 1:
        print("Error : Please enter a number more than or equal one.")

averageSpeed = (distance/deltaTime)
print("%.0f km/hr" % averageSpeed)