import math

#Q = Area * SQRT ( (2H) / (rho * (1 - beta ratio^4))
#not used but ... V = SQRT ( (2H) / (rho * (1 - beta ratio^4))
#verified om my trainer
#orifice is 0.25 inches
#pipe ID is 0.526
#I calculated an orifice discharge of 0.65 based on test data
#Water density assumed at 0.0361

#I had issues with one large formula so i broke it down into steps

dp_str = input("Enter differential pressure in inches of water: ")
dp_int = float(dp_str)
volumetric_flow_pt1 = math.pi * ((0.5 * 0.25)**2)
volumetric_flow_pt2 = (0.0361 *(1-((0.25 / 0.526)**4)))
volumetric_flow_pt3 = (2 * dp_int)
volumetric_flow_pt4 = volumetric_flow_pt3 / volumetric_flow_pt2
volumetric_flow_pt5 = math.sqrt(volumetric_flow_pt4)
volumetric_flow_pt6 = round(volumetric_flow_pt5 * volumetric_flow_pt1 * 0.65, 3) #0.65 is my orifice discharge coefficient



#print(volumetric_flow_pt1)
#print(volumetric_flow_pt2)
#print(volumetric_flow_pt3)
#print(volumetric_flow_pt4)
#print(volumetric_flow_pt5)
print("The flow rate is", volumetric_flow_pt6, "gallons per minute.")

input("Press ENTER to exit")
