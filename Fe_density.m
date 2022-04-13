%%From Fe.cif file
a = 2.86640; %in unit of Amstrong
b = 2.86640;
c = 2.86640;

alpha = 90.00000; %in unit of degrees
beta = 90.00000;
gamma = 90.00000;

%Fe.cif is Body-Center-Cubic with 2 atoms

%%Calculate Unit-Cell Volume
a = a*(1*10^-8); %converting Amstrong to cm
V = a^3;

%%Calculate mass of the 2 Fe atoms 
M = 55.845; %in unit of g/mol

m = M/(6.022*10^23) * 2; %coverting Fe to g/atoms with Avogadro's number, then multiple by 2 atoms, the final unit is grams

%%Calculate density of Fe
rho = m/V;