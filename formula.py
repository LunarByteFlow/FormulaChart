import math

"we shall be creating a formula chart having differenct formulas and it can be used by a student."
# define different formulas by functions.
# using an if else staement to acess the formulas.
# category 1 for area
#         1.1 --> area of square.
#         1.2 --> parimeter of square
#         1.3 --> area of circle.
#         1.4 --> perimeter of a square
#         1. --> area of triangle.
#         1. --> area of parallelogram.
# category 2 for formulas for gravity and work done.
#         2.1 --> force of gravity between two bodies
#         2.2 --> work done
#         2.3 --> power
#         2.4 --> force
#         2.5 --> formula for simple force (Newtons second law)
# category 3 for formulas related to current.
#         3.1 --> force between two charged bodies
#         3.2 --> resistance.
#         3.3 --> electric field
#         3.4 --> voltage
#         3.5 --> conductivity

#  CATEGORY 1 FORMULAS:
pi = 22 / 7


def angle_conversions():
    print("CONVERT BETWEEN DEGREES AND RADIANS:\n\n")
    print("for degree -> radian Enter [deg-rad]")
    print("for radian -> degree Enter [rad-deg]")
    print("Enter your value:  ")
    value = input()
    while (True):
        if value == "deg-rad":
            print("Enter Value in degree:  ")
            deg = float(input())
            rad = deg * (pi / 180)
            print("The value in RADIANS will be: pi/ ", rad, "\n")
        elif value == "rad-deg":
            print("Enter value in radian:  ")
            radd = float(input())
            degg = radd*(180/pi)
        else:
            print("Enter 0 to stop")
            print("for degree -> radian Enter [deg-rad]")
            print("for radian -> degree Enter [rad-deg]")
            print("Enter your value:  ")
            val = int(input())
            if val == 0:
                break


def area_parallelogram():
    print("    AREA OF PARALLELOGRAM :\n\n")
    print("Enter value for side a:   ")
    l = int(input())
    print("Enter value for side b:   ")
    b = int(input())
    area = l * b
    print("Lenght:  ", l)
    print("Breath:  ", b)
    print("The area of parallelogram with lenght = ", l, "and breath =  ", b, "will be ", area)
    return area


# area_parallelogram()

def area_circle():
    print("    AREA CIRCLE: \n\n")
    print("Enter radius of circle:  ")
    radius = int(input())
    area = (3.142) * (radius) * (radius)
    print("Enter value of Radius:   ", radius)
    print("The area of circle :  ", area, " units")
    return area


# area_circle()

def area_square():
    print("    AREA OF SQUARE:\n\n")
    print("Enter the value of a:   ")
    a = int(input())
    area = a * a
    print('Area of square is', area, " units")
    return area


# area_square()

def area_triangle():
    print("    AREA OF TRIANGLE:\n\n")
    print("Enter the lenght:  ")
    lenght = int(input())
    print("Enter the breath:  ")
    breath = int(input())
    area = (lenght * breath) * 1 / 2
    print("area of triangle:  ", area, " units")
    return area


def perimeter_square():
    print("    PERIMETER OF SQUARE :\n\n")
    print("Enter the lenght of side:  ")
    perimeter = 4 * lenght_side
    print("The perimeter of square is : ", perimeter, "units")
    return perimeter


def perimeter_rectangle():
    print("    PERIMETER OF RECTANGLE:\n\n")
    print("Enter value of lenght:  ")
    lenght = int(input())
    print("Enter value of width:   ")
    width = int(input())
    perimeter = 2 * (lenght + width)
    print("The value of parimeter is :  ", perimeter, "units")
    return perimeter


# area_triangle()

# CATEGORY 2:
G = 6.673 * (10 ** -11)


def momentum():
    print("    FORMULA FOR MOMENTUM:\n\n")
    print("Enter the value of mass:  ")
    mass = int(input())
    print("Enter the value of velocity:  ")
    velocity = int(input())
    momentum = mass * velocity
    print(" MASS:  ", mass)
    print(" VELOCITY:  ", velocity)
    print("The momentum will be:  ", momentum)
    return momentum


def force_gravity():
    print("FORCE OF GRAVITY:\n\n")
    print("Enter the mass of body A:  ")
    massA = int(input())
    print('Enter the mass of body B:  ')
    massB = int(input())
    print("Enter the distance between body A and B :  ")
    r = int(input())
    force = (6.673 * (10 ** -11) * (massA * massB) / (r * r))
    print(" Mass of body A :  ", massA)
    print(" Mass of body B :  ", massB)
    print(" Distance between bodyA and bodyB:  ", r)
    print(" The force of gravity will be:  ", force)
    return force


# force_gravity()


def force():
    print("SIMPLE FORCE:\n\n")
    print("Enter the value of mass:  ")
    mass = int(input())
    print("Enter the value of acceleration")
    acceleration = int(input())
    force = mass * acceleration
    print("The force will be: ", force)
    return force


# force()

# CATEGORY 3 FOR CURRENT AND RELATED
k = 9 * (10 ** 9)


def power():
    print("    FORMULA FOR POWER:\n\n")
    print("Enter value of work done:   ")
    work = int(input())
    print("Enter the time elapse for work done:  ")
    time = int(input())
    power = work * time
    print("work done  :  ", work)
    print("Time lapse :  ", time)
    print("The work done will be: ", power)
    return power


def force_charged():
    print("FORCE BETWEEN TWO CHARGED BODIES:\n\n")
    print("Enter charge of body A:")
    chargeA = int(input())
    print("Enter charge of body B:")
    chargeB = int(input())
    print("Enter distance between two bodies:  ")
    radius = int(input())
    k = 9 * (10 ** 9)
    force = ((k) * (chargeA) * (chargeB)) / (radius * radius)
    print("\n")
    print("Charge in body A:", chargeA)
    print("Charge in body B:", chargeB)
    print("Distance between two charged bodies: ", radius)
    print("Coloumbs constant: ", k)
    print("The force between two charged bodies :  ", force)
    return force


# force_charged()

def resistance():
    print("FORMULA FOR RESISTANCE:\n\n")
    print("Enter value for voltage:  ")
    voltage = int(input())
    print("Enter value for current:  ")
    current = int(input())
    resistance = voltage / current
    print("voltage:  ")
    print("current:  ")
    print("\n")
    print("The resistance will be: ", resistance)
    return resistance


# resistance()
def work():
    print("FORMULA FOR WORK DONE:\n\n")
    print("Enter value for mass of the body:  ")
    mass = int(input())
    print("Enter value for height:  ")
    height = int(input())
    g = 9.8
    work_done = mass * g * height
    print(" MASS of the body   :  ", mass, "\n")
    print(" HEIGHT of the body :", height, "\n")
    print("The work done by the body is:  ", work_done)
    return work_done


def electric_field():
    print("FORMULA FOR ELECTRIC FIELD:\n\n")
    print("Enter the value for charge:  ")
    charge = int(input())
    print("Enter the value for force:   ")
    force = int(input())
    field = force / charge
    print("The value for force:   ", force)
    print("The value for charge:  ", charge)
    print("The value of electric field is:  ", field)
    return field


# electric_field()

def voltage():
    print("FORMULA FOR VOLTAGE:\n\n")
    print("Enter value for current:  ")
    current = int(input())
    print("Enter value for Resistance:  ")
    resistance = int(input())
    voltage = current * resistance
    print("Value for current:  ", current)
    print("Value for Resistance:  ", resistance)
    print("The voltage will be:  ", voltage)
    return voltage


print("\t\t\tFORMULA CHART:\n\n\n")
print("\t\t Welcome to the formula chart:\n\n")
print("We have 2 types of formulas:")
print(" Category A:  simple math.  \n")
print(" Category B:  simple physics.\n")
print("\tEnter [ area_square       ]    -->   for calculating area of square.")
print("\tEnter [ perimeter_square  ]    -->   for calculating perimeter of square.")
print("\tEnter [ area_triangle     ]    -->   for calculating area of triangle.")
print("\tEnter [ area_parallelogram]    -->   for calculating area of parallelogram.")
print("\tEnter [ area_parallelogram]    -->   for calculating perimeter of parallelogram.")
print("\tEnter [ angle_conversions ]    -->   for conversion between radian and degrees.")

print("category B: physics")
print("\t Enter [ momentum ]         --> For calculating Momentum.")
print("\t Enter [ force_gravity ]    --> for calculating force of gravity. ")
print("\t Enter [ force ]            --> for calculating force. ")
print("\t Enter [ power ]            --> for calculating power.")
print("\t Enter [ force_charged ]    --> for calculating force between gharged bodies. ")
print("\t Enter [ resistance ]       --> for calculating resistance.")
print("\t Enter [ voltage ]          --> for calculating voltage.")
print("\t Enter [ power ]            --> for calculating power.")
print("\t Enter [ electric_field ]   --> for calculating electric field")
print("\t Enter [ work ]             --> for calculating work done")

print("")
print("Enter your choice [1 for Math] And  [2 for physics] :  ")
choice = int(input())
while (True):
    if choice == 1:
        print("\tCATEGORY MATH:\n")
        print("The the formula you would like to use:  ")
        math_choice = input()
        if math_choice == "area_square":
            area_square()
        elif math_choice == "perimeter_square":
            perimeter_square()
        elif math_choice == "area_triangle":
            area_triangle()
        elif math_choice == "area_parallelogram":
            area_parallelogram()
        elif math_choice == "perimeter_rectangle":
            perimeter_rectangle()
        elif math_choice == "angle_conversions":
            angle_conversions()
        else:
            print("You entered wrong keywords!!")
            print("\tEnter [ area_square ]        -->   for finding  area of square.")
            print("\tEnter [ perimeter_square ]   -->   for finding perimeter of square.")
            print("\tEnter [area_triangle ]       -->   for finding area of triangle.")
            print("\tEnter [area_parallelogram]   -->   for finding area of parallelogram.")
            print("\tEnter [ area_parallelogram ] --> for finding perimeter of parallelogram.")
            print("\tEnter [angle_conversions]    -->   for conversion between radian and degrees")

    elif choice == 2:
        print("\tCATEGORY PHYSICS:\n  ")
        print("The the formula you would like to use:  ")
        phy_choice = input()
        if phy_choice == "momentum":
            momentum()
        elif phy_choice == "force_gravity":
            force_gravity()
        elif phy_choice == "force":
            force()
        elif phy_choice == "power":
            power()
        elif phy_choice == "force_charged":
            force_charged()
        elif phy_choice == "resistance":
            resistance()
        elif phy_choice == "electric_field":
            electric_field()
        elif phy_choice == "work":
            work()
        else:
            print("You Entered wrong keywords.!!")
            print("category B: physics")
            print("\t Enter [ force_gravity ]  --> for force of gravity. ")
            print("\t Enter [ momentum ]       --> For Momentum.")
            print("\t Enter [ force ]          --> for force. ")
            print("\t Enter [ power ]          --> for power.")
            print("\t Enter [ force_charged ]  --> for force between gharged bodies. ")
            print("\t Enter [ resistance ]     --> for finding resistance.")
            print("\t Enter [ voltage ]        --> for finding voltage.")
            print("\t Enter [ power ]          --> for finding power.")
            print("\t Enter [ electric_field ] --> for finding electric field")
            print("\t Enter [ work ]           --> for finding work done")
    else:
        print("Sorry wrong keywords!!")
        print("Try 1-> for math and 2-> for simple physics")
        print("Enter 123 if you want to quit")
        print("Enter your value:  ")
        vall = int(input())

        if vall == 1:
            print("\tCATEGORY MATH:\n")
            print("The the formula you would like to use:  ")
            math_choice = input()
            if math_choice == "area_square":
                area_square()
            elif math_choice == "perimeter_square":
                perimeter_square()
            elif math_choice == "area_triangle":
                area_triangle()
            elif math_choice == "area_parallelogram":
                area_parallelogram()
            elif math_choice == "perimeter_rectangle":
                perimeter_rectangle()
            elif math_choice == "angle_conversions":
                angle_conversions()
            else:
                print("You entered wrong keywords!!")
                print("\tEnter [ area_square ]        -->   for finding  area of square.")
                print("\tEnter [ perimeter_square ]   -->   for finding perimeter of square.")
                print("\tEnter [area_triangle ]       -->   for finding area of triangle.")
                print("\tEnter [area_parallelogram]   -->   for finding area of parallelogram.")
                print("\tEnter [ area_parallelogram ] --> for finding perimeter of parallelogram.")
                print("\tEnter [angle_conversions]    -->   for conversion between radian and degrees")
        elif vall == 2:
            print("\tCATEGORY PHYSICS:\n  ")
            print("The the formula you would like to use:  ")
            phy_choice = input()
            if phy_choice == "momentum":
                momentum()
            elif phy_choice == "force_gravity":
                force_gravity()
            elif phy_choice == "force":
                force()
            elif phy_choice == "power":
                power()
            elif phy_choice == "force_charged":
                force_charged()
            elif phy_choice == "resistance":
                resistance()
            elif phy_choice == "electric_field":
                electric_field()
            elif phy_choice == "work":
                work()
            else:
                print("You Entered wrong keywords.!!")
                print("category B: physics")
                print("\t Enter [ force_gravity ]  --> for force of gravity. ")
                print("\t Enter [ momentum ]       --> For Momentum.")
                print("\t Enter [ force ]          --> for force. ")
                print("\t Enter [ power ]          --> for power.")
                print("\t Enter [ force_charged ]  --> for force between gharged bodies. ")
                print("\t Enter [ resistance ]     --> for finding resistance.")
                print("\t Enter [ voltage ]        --> for finding voltage.")
                print("\t Enter [ power ]          --> for finding power.")
                print("\t Enter [ electric_field ] --> for finding electric field")
                print("\t Enter [ work ]           --> for finding work done")
        elif vall == 123:
            print("Thankyou for using our service ")
            print("\t\t\tGOOD BYE\n\n")

print("Enter first number: ")
var1 = int(input())
print("Enter second number: ")
var2 = int(input())
print(var1+var2)