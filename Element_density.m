%%Calculating an element's density 
a =  1; %in unit of Amstrong
b =  1;
c =  1;

alpha = 90.00000; %in unit of degrees
beta = 90.00000;
gamma = 90.00000;

%Determine how many n atoms is in the unit-cell

%%Calculate Unit-Cell Volume
a = a*(1*10^-8); %converting Amstrong to cm
V = a^3;

%%Calculate mass of the n atoms
M = 100; %in unit of g/mol for that particular element

m = M/(6.022*10^23) * n; %coverting g/mol to g/atoms with Avogadro's number, then multiple by n atoms, the final unit is grams

%%Calculate density of the element
rho = m/V;