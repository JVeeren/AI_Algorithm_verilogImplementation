`include "wallace.v"

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
reg [7:0]a;
reg [7:0]b;
wire [15:0]result;

wallace W(a,b,result);

initial
begin
		f=$fopen("outputmult.txt","w");
    	a=cfgtype;   b=cfgtype1;
    	#1
    	$fwrite(f,"%d",result);
    	$fclose(f);
		//$monitor("mult = %d",result);
		//$dumpfile("testmult.vcd");
		//$dumpvars;
end

endmodule
