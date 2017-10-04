
import turtle, random
DIST = 100
turtle.speed(10)
colors = ["red", "green","blue","orange","purple","indigo","yellow"]
turtle.width(20)
for x in range(0,7):
    
    print "x", x
    for y in range(1,40):
        turtle.color(random.choice(colors))
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(150)
        # advance according to set distance
        turtle.forward(DIST)
        DIST += 3
    # add to set distance
    