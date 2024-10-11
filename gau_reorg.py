#Variants.
Flag1=False
Flag2=False
freq=[]
huangrhys=[]
f=0
counter=0
fulllines=0
resline=0
hr=''
hrconver=''
str1=''
str2=''
lambdai=0

import sys
filename=sys.argv[1]

orderdecomp=input('Output decomposition of reorganization energy? Yes, 1; No, 0.\n')
orderhr=input('Output Huang-Rhys factor diagram? Yes, 1; No, 0.\n')
ordermat=input('Output Duschinsky matrix? Yes, 1; No, 0.\n')

#Function 1: Calculate Internal Reorganization Energy based on Huang-Rhys Factors.
if int(orderdecomp)!=0:
    logf = open(filename,'r')
    for l in logf.readlines():
        L = l.split()
        if len(L)==4 and L[0]=='Deg.' and L[1]=='of' and L[2]=='freedom':
            f=int(L[3])
            fulllines=int(f/3)
        if len(L)==3 and L[0]=='and' and L[1]=='normal' and 'coordinates:':
            Flag1=True
        if Flag1:
            if counter < fulllines and len(L) > 4 and L[0]=='Frequencies' and L[1]=='--':
                freq.append(L[2])
                freq.append(L[3])
                freq.append(L[4])
                counter += 1
            elif counter == fulllines and len(L) > 2 and L[0]=='Frequencies' and L[1]=='--':
                resline=f-3*fulllines
                for i in range(1,resline+1):
                    freq.append(L[i+1])
        if len(L)==2 and L[0]=='Huang-Rhys' and L[1]=='Factors':
            Flag2=True
        if Flag1:
            if len(L)==6 and L[0]=='Mode' and L[1]=='num.' and L[3]=='-' and L[4]=='Factor:':
                hr=L[5]
                str1=hr[0:8]
                str2=hr[-3:]
                hr=str1+'E'+str2
                huangrhys.append(hr)
    print('No.\tFrequencies/cm^-1\tHuang-Rhys Factors\tlambda_i/kJ*mol^-1\tlambda_i/eV')
    reorg1=0
    reorg2=0
    for i in range(1,len(freq)+1):
        print(i,end='\t')
        print(freq[i-1],end='\t')
        print(huangrhys[i-1],end='\t')
        lambdai=float(huangrhys[i-1])*6.62606896*10**-34*float(freq[i-1])*100*3*10**8*6.02214076*10**23/1000
        reorg1=reorg1+lambdai
        print(lambdai,end='\t')
        lambdai=lambdai/2625.5*27.2114
        reorg2=reorg2+lambdai
        print(lambdai)
    print('Internal Reorganization Energy:',reorg1,'kJ*mol^-1;',reorg2,'eV')

#Function 2: Generate Curve Line for Plotting Huang-Rhys Diagram in Origin.
if int(orderhr)!=0:
    curvefile = filename + '.hr.txt'
    file = open(curvefile,'w')
    file.write('0\t0\n')
    for i in range(1,len(freq)+1):
        bot = str(freq[i-1]) + '\t0\n'
        top = str(freq[i-1]) + '\t' + str(huangrhys[i-1]) + '\n'
        file.write(bot)
        file.write(top)
        file.write(bot)
    file.write('4000\t0\n')

#Function 3: Generate Matrix Data for Countor Plotting Duschinsky Matrix in Origin.
Flag3=False
Flag4=False
mat=[]
counter=0
matnum=''
if int(ordermat)!=0:
    fulllines=int(f/5)
    resline=f-5*fulllines
    matfile = filename + '.mat.txt'
    file = open(matfile,'w')
    for i in range(1,f+1):
        logf = open(filename,'r')
        for l in logf.readlines():
            L = l.split()
            if len(L)==2 and L[0]=='Duschinsky' and L[1]=='Transformation':
                Flag3=True
            if Flag3 and len(L)==6:
                Flag4=True
            if Flag4:
                if L[0]==str(i):
                    counter+=1
                    for j in range(1,6):
                        matnum=L[j]
                        if matnum[0:1] == '-':
                            str1=matnum[0:9]
                            str2=matnum[-3:]
                            matnum=str1+'E'+str2
                        elif matnum[0:1] != '-':
                            str1=matnum[0:8]
                            str2=matnum[-3:]
                            matnum=str1+'E'+str2
                        mat.append(matnum)
            elif Flag3 and counter==fulllines and resline!=0:
                if len(L)==resline+1 and L[0]==str(i):
                    for j in range(1,resline+1):
                        matnum=L[j]
                        if matnum[0:1] == '-':
                            str1=matnum[0:9]
                            str2=matnum[-3:]
                            matnum=str1+'E'+str2
                        elif matnum[0:1] != '-':
                            str1=matnum[0:8]
                            str2=matnum[-3:]
                            matnum=str1+'E'+str2
                        mat.append(matnum)
            Flag4=False
            if len(L)==2 and L[0]=='Shift' and L[1]=='Vector':
                Flag3=False
        for j in range(1,f+1):
            matrow = str(mat[j-1]) + '\t'
            file.write(matrow)
        file.write('\n')
        mat=[]
        counter=0

print('Successful Work!')
print('Code Written by Kalinite.')