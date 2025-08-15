# [moku-vhdl-dev-workspace](https://github.com/sealablab/moku-vhdl-dev-workspace)
Top level developer workspace - simplify your Moku-Go VHDL lifestyle

Getting started.
``` bash 
git clone git@github.com:sealablab/moku-vhdl-dev-workspace.git
cd moku-vhdl-dev-workspace
git submodule init
git submodule update --recursive
```

# [.cursor/rules](https://github.com/sealablab/moku-vhdl-dev-workspace/blob/main/.cursor/rules)
The `.cursor/rules` file is intended to make extensive use of the latest [cursor project rules](https://docs.cursor.com/en/context/rules). 
This allows you to keep the context window tight, and focus cursor on language specific goals

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

## 4) [Moku-bsl](https://github.com/sealablab/moku-bsl)
#### Dependencies: `pydantic-moku-models`
**moku-bsl** loads bitstreams (usually in multi-instrument mode) onto a moku device over the network.
> [!NOTE]  You will need to ByOB (bring your own bitstream)

``` shell
./moku-bsl/
./moku-bsl/__init__.py
./moku-bsl/cli.py
./moku-bsl/device.py
```
**moku-bsl** is based on my previous worth with the [moku-go](https://github.com/sealablab/Moku-Go) module



