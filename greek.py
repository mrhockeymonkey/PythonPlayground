

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta',
         'Iota','Kappa','Lamda','Mu','Nu','Xi','Omicron','Pi','Rho',
         'Final Sigma','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']
         
#Format required:
#    The hex value of the character
#    The character name (cname), left justified, maximum 12 characters
#    A colon separator
#    The lowercase Greek character
#    The uppercase Greek character

for pos, cname in enumerate(greek, start=0x03B1):
    try:
        char = chr(pos)  
        print('{0:#x} {1:<12}: {2} {3}'.format(pos, cname, char, char.upper()))
        #print(cname,":",char)
    except UnicodeEncodeError as err:
        print (cname, 'unknown')
