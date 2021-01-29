`include "eight.v"

module sixteen(A,B,cin,sum,ca);
	input [15:0]A,B;
	input cin;
	output [15:0]sum;
	output ca;
	wire w0;
	
	eight e1(A[7:0],B[7:0],cin,sum[7:0],w0);
	eight e2(A[15:8],B[15:8],cin,sum[15:8],ca);
endmodule
