
while True:
    try:

        import numpy as nmp

        print("HELICAL GEAR DESIGN FOR 20 DEGREE INVOLUTE PROFILE TEETH\
         UNITS AS USED IN DESIGN DATA BOOK")
        pi=nmp.pi
        rad=pi/180

        np=float(input("rpm of pinion: "))
        zp=0#int(2/(nmp.square(nmp.sin(20*pi/180))))
        psi=float(input("enter helix angle: "))*rad
        alphat=float(input("transverse pressure angle: "))*rad

        P=float(input("enter rated power: "))
        r=float(input("enter gear reduction ratio: "))
        d_p=float(input("pinion diameter: "))
        d_g=float(input("wheel diameter: "))
        fs=float(input("factor of safety: "))
        Cs=float(input("service factor: "))
        Sut_p=float(input("allowabe tensile strength of pinion: "))
        Sut_g=float(input("allowabe tensile strength of wheel: "))
        if Sut_g<Sut_p:
            Sut_p=Sut_g
            d_p=d_g+d_p
            d_g=d_p-d_g
            d_p=d_p-d_g
            r=1/r

        zg=0
        m=0
        mn=0
        dpv=0
        BHN=0
        Peff=0
        Peff=0
        Sb=0
        Mt=0
        R_P=0

        alphan=nmp.arctan(nmp.tan(alphat)*nmp.cos(psi))
        dpv=d_p/nmp.square(nmp.cos(psi))
        b=pi*1/nmp.sin(psi)
        b=int(b+2)
        zpv=2/(nmp.square(nmp.sin(alphan)))
        zpv=int(zpv+1)
        Y=float(input("enter lewis form factor for z={} ".format(zpv)))
        v=np*d_p*2*pi/(2*1000*60)

        i=0

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
            Sigma_b=Sut_p/1
            return [m*b*Sigma_b*Y,nmp.sqrt(fs*Peff/(b*Sigma_b*Y))]

        def velocity(d,n):
            return pi*d*n/(60000)

        def Hardness(f):
            Q=2*zg/(zp+zg)
            Sw=f*Peff
            bhn=100*nmp.sqrt(Sw/(b*Q*d_p*0.16))
            return bhn

        def WearCheck():
            Q=2*zg/(zp+zg)

            Ses=float(input("enter endurance strength: "))
            Ep=float(input("modulus of elasticity for pinion: "))
            Eg=float(input("modulus of elasticity for wheel: "))
            K=nmp.square(Ses)*nmp.sin(alphan)*nmp.cos(alphan)*(1/Ep+1/Eg)/1.4

            return b*Q*d_p*K/nmp.square(nmp.cos(psi))


        while True:
            Cv=VelocityFactor(v)

            L=P_effective(d_p,Cv)
            Peff=L[0]

            L=BeamStrength(mn)

            if mn==0:
                mn=(int(L[1])+int(L[1]+1))/2+i*0.3
                i+=1
                b=b*mn
                zpv=int(dpv/mn+0.9)
                Y=float(input("lewis form factor for z={} ".format(zpv)))


                continue
            else:
                Sb=L[0]
                if (Sb/Peff)>(fs):

                    zp=int(zpv*nmp.power(nmp.cos(psi),3)+0.9)
                    zg=r*zp

                    Sw=WearCheck()
                    if (Sb/Peff)>(fs):
                        BHN=Hardness(Sb/Peff)
                        break
                    else:
                        continue


                else:
                    mn=(int(L[1])+int(L[1]+1))/2+i*0.3
                    i+=1
                    continue



        print("\n\nThe design output parameters are:")
        print("normal module={}".format(round(mn,3)))
        print("face width={}".format(round(b,3)))
        print("Peff={}".format(round(Peff,3)))
        print("Hardness={} BHN".format(int(BHN)))
        print("\nAddendum {}".format(round(mn,3)))
        print("Dedendum {}".format(round(1.25*mn,3)))
        print("Clearance {}".format(round(0.25*mn,3)))

        break

    except ValueError:
        print("please enter valid design data ")
        continue
