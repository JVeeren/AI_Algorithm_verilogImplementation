`include "FullAdder16.v"

module test;
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

reg [15:0] a,b;
reg cin;

wire [15:0] sum;
wire cout;

bit16 fBit(a,b,cin,sum,cout);

initial
begin
		f=$fopen("output.txt","w");
		a=cfgtype;
		b=cfgtype1;
		cin=0;
		#1
    	$fwrite(f,"%d",sum);
    	$fclose(f);
		//$monitor("sum = %d A= %b B= %b",sum,a,b);
		//$dumpfile("test.vcd");
		//$dumpvars;
	
end

endmodule