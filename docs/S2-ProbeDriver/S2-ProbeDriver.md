This note defines the basic ProbeDriver architecture.

It serves as the foundation for the [[S2-DS1120A-ProbeDriver]]


The following document describes the shared design of all Slot2-ProbeDrivers. 

## ProbeDriver: Physical-Inputs:
The bare minimum number of inputs to a ProbeDriver (excluding configuration values passed via controlRegisters) is precisely **one**. 

### Trig-in: 


## ProbeDriver: Physical-Outputs:
The bare minimum number of physical outputs **from** a ProbeDriver (again, excluding status / debugging registers) is also precisely **two**:
* Trig-out: Literally drives the 
### Trig-out:

For now, we will treat **trig_out** as a single DIO. 

##




All probe drivers will have the following (syncronous) inputs connected:
### `trig_in` 
**trig_in**: self-explanatory: This will likely be connected to DIO[0], but maybe will be an analog input..🤔

## Probe-Outputs
All probes will have the following three outputs:
* **trig_out**: self-explanatory
* ***intensity_out**: self-explanatory 
* ***pbus_out**: (Optional) 4-wire [[P-Bus]] status output. (Suitable for monitoring LEDS)


> [!NOTE] It is __Expected__ that these output will be connected to **OutputA** **OutputB** and **OuptutC** by the moku platform!

### Trig_out: 
**trig-out**: self-explanatory
## Intensity_out
**intensity-out**: Simiilar to spider.V_OUT

### pbus_out
**pbus_out**: (Optional) 4-wire 'Probe-Bus' connection for debugging and feedback. (Also good for driving LEDs)




## Probe-Static:
All Probes will have the following (static) properties:
The DS1120A-Drv module should have the following (static) LUT's. 
* array IntensityLUT[16]; 
### IntensityLut
**IntensityLut** is a look up table that maps a base-10 percentage (i.e, 0-100) to a 16-bit value suitable for driving the Riscure DS11210A HP-EM probe. The table should  linearly extrapolate between  0v0 3v3 (100% power)

### CoolDown
**CoolDown** The number of clock cycles that must pass **after** firing before the probe can be re-armed. (This prevents f.ex, overheating or damaging equipment).

### MinDuration
The minimal amount of clock cycles that the probe needs `trig_out` set high in order to fire correctly.

### MaxDuration
The maximum amount of clock cycles that `trig_out` can (safely) be set high.




