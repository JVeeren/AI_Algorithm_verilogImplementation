`include "Fulladder8.v"

module bit16(a,b,cin,sum,cout);

input [15:0] a,b;
	input cin;
	output[15:0] sum;
	output cout;
	wire c,c1,c2;
	
	bit8 fbit0(a[7:0],b[7:0],cin,sum[7:0],c);

	bit8 fbit1(a[15:8],b[15:8],c,sum[15:8],cout);


endmodule