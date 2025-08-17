---
created: 2025-08-16
modified: 2025-08-16
---
# ProbeDriverMonitor
This note describes a **ProbeMonitor** setup that leverages a second moku go to validate the functioning of the first. We call this second device the `DriverMonitor` - and it can be incredibly useful when troubleshooting.

The following document describes how the devices should be configured. 

It is intended to accompany an (as of yet written) python test script `ProbeDriverMonitorTester` [[ProbeDriverMonitorTester]]




In short, 
* `Stitch(⚫️)` is setup to generate a lot of noise 
* Lilo (⚪️) is supposed to baby-sit Stich and make sure he doesn't exceed his boundaries.

## Photo [[imgs/LiloStitchDriverMonitorPhysicalWiringExampl]]

![[imgs/LiloStitchDriverMonitorPhysicalWiringExample.png]]


## Diagram [[Lilo-Stich-Driver_Monitor-Sketch]]
![[Lilo-Stitch-Stacked-Sketch]]

Additionally, the DIO's have been wired thusly

### Driver-Monitor: DIO settings

| Moku    | IN  | OUT |
| ------- | --- | --- |
| Driver  |  0  | 4-7 |
| Monitor | 0-3 |   14  |

## ProbeStatusRegister
Each ProbeDriver has a 4-bit status register that contains the folllwing bits:

| BIT   |                |
| ----- | -------------- |
| 0(🟢) | Armed          |
| 1(🟡) | Firing!        |
| 2(🔴) | Fired          |
| 3(🔵) | Cooldown       |
| 4(🟣) | Err (optional) |

The ProbeDriver is / should be configured such that **OuputC** is connected to the DIO[OUT] pins


These pins can then be routed down to the **ProbeMonitor**.


# Setup

## Lilo: `192.168.127.107` : ProbeDriver

### DIO Configuration: (ProbeDriver)
``` python

```

> [!NOTE] We are going to connect the ProbeDrivers **status register** to the following four (or five) DIO-outs. 
> That way we can observe them on some LEDs!

![[imgs/Pasted image 20250816201520.png]]

### Stitch: 192.168.127.145 : ProbeDriver Monitor
The ProbeDriver **Monitor** will use DIO's[0:3] to monitor the probe transitions through the correct states.

![[imgs/Pasted image 20250816201645.png]]


# Triggering options

There are two different approaches we could pursue for triggering the ProbeDriver:

### Option 1: set registers across the network 
### Option 2: manually connect a DIO and drive the ProbeDriver like it was intended.





# See Also
## [[ProbeDriverMonitorTester]]

