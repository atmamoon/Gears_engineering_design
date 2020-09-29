


try:
    import numpy as np

    while True:
        P=float(input("enter power to be transmitted: "))
        r=float(input("velocity ratio: "))
        pi=np.pi
        z1=0
        if r>30:
            z1=1
        elif r>16 and r<25:
            z1=2
        else:
            z1=4
        Np=float(input("worm rpm: "))
        x=float(input("centre distace: "))

        Ng=Np/r
        lamda=np.arctan(1/np.power(r,1/3))
        ln=x*2*pi/(1/np.sin(lamda)+r/np.cos(lamda))
        l=ln/np.cos(lamda)
        pa=l/z1
        m=pa/pi

        while True:
            m=float(input("enter the closest standard value of module\n \
            greater than {} ".format(m)))

            pa=pi*m
            l=pa*z1
            ln=l*np.cos(lamda)
            x=ln*(1/np.sin(lamda)+r/np.cos(lamda))/(2*pi)
            Dw=l/(pi*np.tan(lamda))
            z2=r*z1
            pc=pa
            Lw=pc*(4.5+0.02*z1)
            Lw=round(Lw+27)
            h=0.623*pc
            a=0.286*pc
            Dow=Dw+2*a

            Dg=m*z2
            Dog=Dg+0.8903*pc
            Dt=Dg+0.572*pc
            b=2.15*pc+5
            T=P*60/(2*pi*Ng)
            Wt=2*T/Dg
            v=pi*Dg*Ng/60
            Cv=6/(6+v)
            y=0.154-0.912/z2
            sigma_2=float(input("enter allowable static stress for gear: "))
            Wt=sigma_2*Cv*b*pi*m*y
            Wd=Wt/Cv
            sigma_e=float(input("flexural endurance limit for gear material: "))
            Ws=sigma_e*b*pi*m*y
            K=float(input("load stress factor for gear material: "))
            Ww=Dg*b*K
            if Ws>Wt and Ww>Wt:
                break
            else:
                m=m+0.5
                continue

        vr=pi*Dw*Ng/(1000*np.cos(lamda))
        nu=0.025+vr/18000
        phi1=np.arctan(nu)
        eeta=np.tan(lamda)/np.tan(lamda+phi1)
        Qg=125*P*(1-eeta)
        Aw=pi*np.square(Dw)/4
        Ag=pi*np.square(Dg)/4
        A=Ag+Aw
        k=float(input("coefficient of convective heat transfer of the\
    cooling fluid: "))
        delta_T=Qg/(A*k)
        if delta_T>38:
            print("WARNING_overheating detected\nselect different parameter\
            or change material")
            continue
        print("Worm")
        print("module {}".format(round(m,3)))
        print("axial pitch {}".format(round(pa,3)))
        print("lead angle of worm {}".format(round(lamda)))
        print("gear teeth {}".format(int(z2)))
        print("face length {}".format(round(Lw,3)))
        print("depth of tooth {}".format(round(h,3)))
        print("addendum {}".format(round(a,3)))
        print("Outside diameter of worm {}".format(round(Dow,3)))

        print("\n\nWorm Gear")
        print("face width {}".format(round(b,3)))
        print("pitch circle diameter {}".format(round(Dg,3)))
        print("Outside diameter of worm gear {}".format(round(Dog,3)))
        print("Throat diameter {}".format(round(Dt,3)))
        print("efficiency {}%".format(round(eeta*100)))
        break

except ValueError:
    print("ENTERED ILLEGAL VALUE.")
