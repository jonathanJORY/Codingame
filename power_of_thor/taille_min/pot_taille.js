for([l,m,o,p]=readline().split(' ').map(Number);;){readline();d=(p<m?'S':p>m?'N':'')+(o<l?'E':o>l?'W':'');console.log(d);o+=(l>o)-(l<o);p+=(m>p)-(m<p);}
