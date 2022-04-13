%%can be editted to desired lengths
a=3;
b=4;
c=6;

%%can be editted to desired angles
alpha=90;
beta=120;
gamma=90;

g=[a^2, a*b*cosd(gamma), a*c*cosd(beta);
    a*b*cosd(gamma), b^2, b*c*cosd(alpha);
    a*c*cosd(beta), b*c*cosd(alpha), c^2]

%%get p and q
p=[1 1 1]
q=[0 0 0]

%%distance from any two points
D=sqrt((q-p)*g*(q-p)')