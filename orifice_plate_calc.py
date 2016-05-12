import math

#Q = Area * SQRT ( (2H) / (rho * (1 - beta ratio^4))
#not used but ... V = SQRT ( (2H) / (rho * (1 - beta ratio^4))
#verified om my trainer
#orifice is 0.25 inches
#pipe ID is 0.526
#I calculated an orifice discharge of 0.65 based on test data
#Water density at 0.0361


orifice_str = input("Enter orifice diameter in inches: ")
orifice_int = float(orifice_str)
pipe_str = input("Enter pipe inside diameter in inches: ")
pipe_int = float(pipe_str)
density_str = input("Enter density in pounds per cubic inch: ")
density_int = float(density_str)
dp_str = input("Enter differential pressure in inches of water: ")
dp_int = float(dp_str)
volumetric_flow_pt1 = math.pi * ((0.5 * orifice_int)**2)
volumetric_flow_pt2 = (density_int*(1-((orifice_int / pipe_int)**4)))
volumetric_flow_pt3 = (2*dp_int)
volumetric_flow_pt4 = volumetric_flow_pt3 / volumetric_flow_pt2
volumetric_flow_pt5 = math.sqrt(volumetric_flow_pt4)
volumetric_flow_pt6 = round(volumetric_flow_pt5 * volumetric_flow_pt1 * 0.65, 3) #orifice discharge coefficient



#print(volumetric_flow_pt1)
#print(volumetric_flow_pt2)
#print(volumetric_flow_pt3)
#print(volumetric_flow_pt4)
#print(volumetric_flow_pt5)
print("The flow rate is", volumetric_flow_pt6, "gallons per minute.")
