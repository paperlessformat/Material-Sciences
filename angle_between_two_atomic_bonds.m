%%Compute angles between atomic bonds
g = get_metric_tensor(a, b, c, alpha, beta, gamma); %Assume already have the function in another file

%add your own vectors
s = [s1, s2, s3];
t = [t1, t2, t3];

s_length = sqrt(s*g*s');
t_length = sqrt(t*g*t');

theta = acosd(s*g*t'/(s_length*t_length));


