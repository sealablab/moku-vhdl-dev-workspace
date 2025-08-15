# quickload.py: 
# **quickload.py**: derived from https://github.com/liquidinstruments/moku-examples/blob/main/python-api/cloud_compile_adder.py 
#  This example demonstrates how you can configure Cloud Compile, using
# Multi-Instrument mode, to add and subtract two input signals together and
# output the result to the OscillLope.

from moku.instruments import MultiInstrument, CloudCompile, LogicAnalyzer

# Connect to your Moku by its ip address using
# MultiInstrument('192.168.###.###')
# force_connect will overtake an existing connection
m = MultiInstrument('192.168.127.106', platform_id=2, force_connect=True)

try: 
    # Set the instruments and upload C loud Compile bitstreams from your device
    # to your Moku
    bitstream = "./moku-dev-vhdl/bin/blink_b.tar"

    mcc = m.set_instrument(1, CloudCompile, bitstream=bitstream)
    print(mcc)
    L = m.set_instrument(2, LogicAnalyzer)
    print(L)

    # Configure the connections
    connections = [dict(source="Slot1OutA", destination="Slot2InA")]
    print(connections)

    m.set_connections(connections=connections)
    print("Connections established.")
    # Set up the plotting parameters

except Exception as e:
    m.relinquish_ownership()
    raise e
finally:
    m.relinquish_ownership()
