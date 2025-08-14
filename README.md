# [moku-vhdl-dev-workspace](https://github.com/sealablab/moku-vhdl-dev-workspace)
Top level developer workspace - simplify your Moku-Go VHDL lifestyle

Getting started.
``` git clone git@github.com:sealablab/moku-vhdl-dev-workspace.git```

# Submodules

## [pydantic-moku-models](https://github.com/sealablab/pydantic-moku-models) 
**02-pydantic-moku-models**: All data structures that are exposed for consumption to other services can and should have a clearly defined pydantic model. For example
``` python
from pydantic import BaseModel, field

class MokuDeviceConfig(BaseModel):
	name: str = Field(..., description="e.g. Lilo, Stitch")
	ip_address: str = Field(..., description="IP address of moku device")
	tcp_port: int = Field(27183, description="(TCP)Port:")
	serial_num: int = Field(22314)

```

## [Moku-Dev-VHDL](https://github.com/sealablab/moku-dev-vhdl)
**10-Moku-Dev**: This is a repo with the following structure.
Dependencies: None
__Note__: Limit this repo to VHDL for now. Smaller context window. Simpler cursor rules.
(VHDL-2008)

``` bash
./10-Moku-Dev-VHDL/
│   ./Blinkers/blink_b.vhd
│   ./Blinkers/blink_g.vhd
│   ./Blinkers/Top_blink_b.vhd
│   ./Blinkers/
```



