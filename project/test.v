`include "Fulladder.v"

module test(a,b,cin,sum,cout);

	input [3:0] a,b;
	input cin;
	output[3:0] sum;
	output cout;
	wire c,c1,c2;
	Fulladder fa0(a[0],b[0],cin,sum[0],c);

	Fulladder fa1(a[1],b[1],c,sum[1],c1);


	Fulladder fa2(a[2],b[2],c1,sum[2],c2);

	Fulladder fa3(a[3],b[3],c2,sum[3],cout);


endmodule
