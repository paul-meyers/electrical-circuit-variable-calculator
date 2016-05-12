#import the math module so math.sqrt works
import math

#the following inputs are the necessary info for solving the circuit
et_str = input("What is the source voltage:")
et = float(et_str)  #we have to convert the input from a "string" to a "float".
hz_str = input("What is the frequency:")
hz = float(hz_str)
res_str = input("What is the resistance:")
res = float(res_str)
l_str = input("What is the Henries:")
l = float(l_str)
c_str = input("What is the microfarads:")
c_micro = float(c_str)
c = c_micro / 1000000

#this is a parallel circuit, so voltage stays the same across all branches.
er = et
el = et
ec = et

#solve for xl and xc and round to 3 decimal places
xl = round(2 * 3.14 * hz * l, 3)
xc = round(1 / (2 * 3.14 * hz * c), 3)

#use ohm's law to solve for I through each branch
ir = er / res
il = el / xl
ic = ec / xc
it = math.sqrt(ir**2 + (il - ic)**2)

#simple ohm's law
z = et / it

#simple ohm's law
pt = et * it
pr = er * ir
pl = el * il
pc = ec * ic

#power factor is easy to solve
pf = (pr / pt) * 100

#this looks weird, python uses "acos" to solve in radians.  We need to then convert to degrees and round
angle_theta = round(math.degrees(math.acos(pr/pt)), 2)

#now we print the results of our program.  We rounded the values to 2 decimal places.  Everything in "" will be shown as text.
print("E total is", et, "volts")
print("I total is", round(it, 2), "amps")
print("Z total is", round(z, 2), "Ω")
print("Volt amps is", round(pt, 2), "VA")
print("Power factor is", round(pf, 2), "%")
print("Angle theta is", round(angle_theta, 2), "°")
print("The resistor has", round(er,2), "volt drop and a current of", round(ir, 2), "amps. \n The watts, or true power, equal", round(pr, 2))
print("The inductor has", round(el, 2), "volt drop and a current of", round(il, 2), "amps. \n The vars, or inductive reactive power, equal", round(pl, 2))
print("The capacitor has", round(ec, 2), "volt drop and a current of", round(ic, 2), "amps. \n The vars , or capacitive reactive  power, equal", round(pc, 2))


input("Press enter to quit")
