`include "eight.v"

module top;
    integer f;
    integer cfgtype;
    integer cfgtype1;
    initial begin    
		if ($value$plusargs("CFGTYPE=%d", cfgtype)) begin
    		//$display("Configuring DUT to config = %d", cfgtype);
		end
		if ($value$plusargs("CFGTYPE1=%d", cfgtype1)) begin
    		//$display("Configuring DUT to config = %d", cfgtype1);
		end	
	end

	reg [7:0]A,B; reg cin;
	wire [7:0]sum; wire ca;
	
	eight f1(A,B,cin,sum,ca);
	
	initial
	begin
		f=$fopen("output.txt","w");
		A=cfgtype;
		B=cfgtype1;
		cin=0;
		#1
    	$fwrite(f,"%d",sum);
    	$fclose(f);
		//$monitor("sum = %d A= %b B= %b",sum,A,B);
		//$dumpfile("test.vcd");
		//$dumpvars;
	end

endmodule
