# dynamic viscosity and kinematic viscosity
# area
# thickness of oil film
# velocity of plate (upper or lower) change of velocity
# force need to maintain the speed

# input type of viscosity to be found
def dynamic_viscosity():

    #input for type of plate
    top = input("Type of Plate has been Used (1.Square , 2.Rectangular ) : ")
    if top == "1" or top == "Square" or top == "square":

        #input area or side of plate
        toi=input("Side or Area (1.Side , 2. Area ) : ")
        if toi == "1" or toi =="Side" or toi == "side":

            #input for side
            side_input=float(input("Enter the side in centimeters : "))
            area=(side_input*0.01)*(side_input*0.01)
            print("Area of the Plates : ",area)
        else:
            area_input=float(input("Enter the area in meters : "))
            area=area_input
            print("Area of the Plates : ",area)
    else:

        #input area or side of plate
        toi=input("Sides or Area (1.Sides , 2. Area ) : ")
        if toi == "1" or toi =="Sides" or toi == "sides":

            #input for side
            length_input=float(input("Enter the length in centimeters : "))
            breath_input=float(input("Enter the breath in centimeters : "))
            area=(length_input*0.01)*(breath_input*0.01)
            print("Area of the Plates : ",area)

    #input for thickness of oil film
    thickness_of_oil=float(input("Enter Thickness of oil film in millimeters : "))

    #input for velocity of the plates
    velocity_of_plates=float(input("Enter Velocity of Plates in meter/sec : "))
    
    #force required to maintain the speed
    force = float(input("Enter the force in Newtons : "))
    shear_stress = force/area
    dynamic_viscosity = shear_stress * ((thickness_of_oil*(10**-3))/velocity_of_plates)
    print("Dynamic Vicosity of oil is :",dynamic_viscosity*10,"poise")
    return dynamic_viscosity
def continue_check():
    coninput=str(input("you wanna continue (1.Yes , 2.No ) : "))
    if coninput == "1" or coninput =="yes":
        print("Redirecting to the Program...")
        viscosity()
    else:
        print("Terminating Sequence...")
        print("Terminated")
        quit
def viscosity():
    tov= input("Type of Viscosity to be Found (1.Dynamic viscosity , 2.Kinematic Viscosity ) : ")
    area=0
    if tov == "1" or tov =="dynamic" or tov=="Dynamic":
        dynamic_viscosity()
        continue_check()
    else:
        #input for dynamic viscosity
        density=0
        check_for_dynamic = input("Do you Have Dynamic Viscosity Value ? : (1.yes , 2. No ) : ")
        if check_for_dynamic=="1" or check_for_dynamic=="yes" or check_for_dynamic=="Yes":
            dynamic_input=float(input("Enter the Dynamic Viscosity Value in poise : "))
            density_input = str(input("Enter the Density of the oil (Don't know the Density means type '0') : "))
            if density_input == "0":
                #input for density
                specific_gravity = float(input("Enter the Specific Gravity of oil : "))
                density= specific_gravity*1000
            else:
                density=float(density_input)
                kinematic_viscosity=dynamic_input/density
                print("Kinematic Viscosity of Oil is " , kinematic_viscosity*(10**4),"strokes")
                continue_check()
        else:
            dynamic_input=dynamic_viscosity()
            density_input = str(input("Enter the Density of the oil (Don't know the Density means type '0') : "))
            if density_input == "0":
                specific_gravity = float(input("Enter the Specific Gravity of oil : "))
                density= specific_gravity*1000
            else:
                density=float(density_input)
                kinematic_viscosity=dynamic_input/density
                print("Kinematic Viscosity of Oil is " , kinematic_viscosity*(10**4),"strokes")
                continue_check()
viscosity()
