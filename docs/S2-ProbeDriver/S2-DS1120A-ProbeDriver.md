# DS1120A
The ***DS1120A** has the following specifications. Most of the behavior is defined in the [[S2-ProbeDriver]]

# See Also
[[S2-ProbeDriver-spec]]


All Probes will have the following (static) properties:
The DS1120A-Drv module should have the following (static) LUT's. 

* array IntensityLUT[16]; 
## ProbeProperties:

### IntensityLut
``` python
IntensityLut = array unsigned(16)
IntensityLut[100] = 3v3
IntensityLut[50] = 1v67
IntensityLuty[10] = 0.3v3
```
### CoolDown
**CoolDown** The number of clock cycles that must pass **after** firing before the probe can be re-armed. (This prevents f.ex, overheating or damaging equipment).
``` python
MinDuration__in_clks: 1
MaxDuration_in_clks: 32


```
### MinDuration
The minimal amount of clock cycles that the probe needs `trig_out` set high in order to fire correctly.

### MaxDuration
The maximum amount of clock cycles that `trig_out` can (safely) be set high.


