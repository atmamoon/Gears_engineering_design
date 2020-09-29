

import numpy as nmp

print("SPUR GEAR DESIGN FOR 20 DEGREE INVOLUTE PROFILE TEETH\
 UNITS AS USED IN DESIGN DATA BOOK")
pi=nmp.pi
np=float(input("rpm of pinion: "))
zp=int(2/(nmp.square(nmp.sin(20*pi/180))))
zg=0
P=float(input("enter rated power: "))
r=float(input("enter gear reduction ratio: "))
m=0
d_p=0
d_g=0.2
ng=np*d_p/d_g
b=10*m
fs=float(input("factor of safety: "))
Cs=float(input("service factor: "))
Sut_p=float(input("ultimate tensile strength of pinion: "))
Sut_g=float(input("ultimate tensile strength of gear: "))
Y=0.308
BHN=0
Peff=0
Peff=0
Sb=0
Mt=0
R_P=0
v=6
d_p=2*v*1000*60/(2*pi*np)
i=2

def VelocityFactor(v):
    if v>20:
        return 5.6/(5.6+nmp.sqrt(v))
    elif v<20 and v>10:
        return 6/(6+v)
    else:
        return 3/(3+v)

def P_effective(d,Cv):
    Mt=60000000*P/(2*pi*np)

    Pt=2*Mt/d
    Peff=Cs*Pt/Cv
    return [Peff,Pt,Mt]

def BeamStrength(m):
    Sigma_b=Sut_p/3
    return [m*b*Sigma_b*Y,nmp.sqrt(fs*Peff/(10*Sigma_b*Y))]

def velocity(d,n):
    return pi*d*n/(60000)

def Hardness():
    Q=2*zg/(zp+zg)
    Sw=fs*Peff
    bhn=100*nmp.sqrt(Sw/(b*Q*d_p*0.16))
    return bhn


while True:
    Cv=VelocityFactor(v)

    L=P_effective(d_p,Cv)
    Peff=L[0]

    L=BeamStrength(m)

    if m==0:
        m=L[1]+i*0.3
        b=10*m
        d_p=m*zp
        v=velocity(d_p,np)

        continue
    else:
        Sb=L[0]
        if (Sb/Peff)>(fs):
            b=10*m
            zg=r*zp
            BHN=Hardness()

            break
        else:
            v=v+0.3
            continue

print("\n\nThe design output parameters are:")
print("module={}".format(round(m,3)))
print("Peff={}".format(round(Peff,3)))
print("Hardness of gear {} BHN".format(int(BHN)))
print("\n Addendum {}".format(round(m,3)))
print("Dedendum {}".format(round(1.25*m,3)))
print("Clearance {}".format(round(0.25*m,3)))
print("Working depth {}".format(round(2*m,3)))
print("Whole depth {}".format(round(2.25*m,3)))
print("Tooth thickness {}".format(round(1.5708*m,3)))
print("Tooth space {}".format(round(1.5708*m,3)))
print("Fillet radius {}".format(round(0.4*m,3)))
