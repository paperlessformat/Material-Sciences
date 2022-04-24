function g = get_metric_tensor(a,b,c,alpha,beta,gamma) 

 

g = [a^2, a*b*cosd(gamma), a*c*cosd(beta); 

    a*b*cosd(gamma), b^2, b*c*cosd(alpha); 

    a*c*cosd(beta), b*c*cosd(alpha), c^2]; 