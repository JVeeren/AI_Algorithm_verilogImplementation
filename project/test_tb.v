`include "test.v"
module top;
    integer f;
    integer cfgtype;
    integer cfgtype1;
    initial begin    
		if ($value$plusargs("CFGTYPE=%d", cfgtype)) begin
    		$display("Configuring DUT to config = %d", cfgtype);
		end
		if ($value$plusargs("CFGTYPE1=%d", cfgtype1)) begin
    		$display("Configuring DUT to config = %d", cfgtype1);
		end	
	end

reg [3:0]a,b;
reg cin;

wire [3:0] sum;
wire cout;

test fBit(a,b,cin,sum,cout);

initial
begin
	f=$fopen("output.txt","w");
	a=cfgtype;
	b=cfgtype1;
	cin=0;
    #1
    $fwrite(f,"%d",sum);
    $fclose(f);
	$monitor("sum = %d",sum);
	$dumpfile("test.vcd");
	$dumpvars;
end

endmodule
