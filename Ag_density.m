%%From Ag.cif file
a =  4.08570; %in unit of Amstrong
b =  4.08570;
c =  4.08570;

alpha = 90.00000; %in unit of degrees
beta = 90.00000;
gamma = 90.00000;

%Fe.cif is Face-Center-Cubic with 4 atoms

%%Calculate Unit-Cell Volume
a = a*(1*10^-8); %converting Amstrong to cm
V = a^3;

%%Calculate mass of the 4 Ag atoms 
M = 107.8682; %in unit of g/mol

m = M/(6.022*10^23) * 4; %coverting Fe to g/atoms with Avogadro's number, then multiple by 4 atoms, the final unit is grams

%%Calculate density of Ag
rho = m/V;