`include "fbit.v"

module bit8(a,b,cin,sum,cout);

input [7:0] a,b;
	input cin;
	output[7:0] sum;
	output cout;
	wire c,c1,c2;
	
	fbitAdder fbit0(a[3:0],b[3:0],cin,sum[3:0],c);

	fbitAdder fbit1(a[7:4],b[7:4],c,sum[7:4],cout);


endmodule
