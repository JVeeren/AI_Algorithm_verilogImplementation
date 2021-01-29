module Fulladdr(a,b,cin,sum,ca);
input a,b,cin;
output sum,ca;
	assign sum = a^b^cin;
	assign ca = (a&b)|(b&cin)|(a&cin);
endmodule
