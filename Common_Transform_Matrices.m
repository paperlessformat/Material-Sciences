%Transform Matrix, Conventional to Primitive (FCC)
T = [0.5, 0.5, 0;
    0, 0.5, 0.5;
    0.5, 0, 0.5]   
inv_T = inv(T) %for Primi. to Conv.

%Transform Matrix, Conventional to Primitive (BCC)
W = [0.5, 0.5, -0.5;
    -0.5, 0.5, 0.5;
    0.5, -0.5, 0.5]
inv_W = inv(W) %for Primi. to Conv.

%Transform Matrix, Conventional to Primitive (RHL)
R = [2/3, -1/3, -1/3;
    1/3, 1/3, -2/3;
    1/3, 1/3, 1/3]
inv_R = inv(R) %for Primi. to Conv.