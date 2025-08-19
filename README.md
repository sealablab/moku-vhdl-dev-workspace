# ProbeDriver - VHDL Fault Injection Laser System Controller

## Overview

The ProbeDriver is a VHDL-based controller for fault injection laser systems, designed to provide precise control over laser pulse timing, intensity, and safety features. It implements a state machine that manages the complete firing sequence with configurable parameters and automatic safety modes.

## Key Features

- **7-bit intensity control** with lookup table mapping
- **16-bit pulse duration** control (1-65535 clock cycles)
- **16-bit cooldown period** management
- **ZeroInit mode** for automatic demonstration and testing
- **Status register** for real-time monitoring
- **Safety interlocks** and minimum timing enforcement
- **Clean control register interface** with proper bit mapping

## Architecture

### Core Components

- **`ProbeDriver.vhd`** - Main state machine and control logic
- **`IntensityLut.vhd`** - Intensity lookup table package
- **`ProbeConfig.vhd`** - Configuration constants and timing parameters
- **`CustomWrapper.vhd`** - Interface wrapper for system integration

### Top-Level Interfaces

- **`top_probe_driver.vhd`** - Official interface with improved control register layout
- **`old/top_probe_driver_legacy.vhd`** - Legacy backward compatible interface (archived)

## Control Register Interface

### Control0 Register (32-bit)
```
CR0[31]:    Global Enable/Reset (1=Enable, 0=Reset)
CR0[23]:    Soft Trigger Input
CR0[22:16]: 7-bit Intensity Index (0-127)
CR0[15:0]:  16-bit Pulse Duration (1-65535)
```

### Control1 Register (32-bit)
```
CR1[31:16]: 16-bit Cooldown Period (1-65535)
CR1[15:0]:  Reserved for future use
```

### Signal Mapping
- **Reset**: `Control0[31]` (active low)
- **Enable**: `Control0[31]` (active high)
- **Trigger**: `Control0[23]` (rising edge)
- **Intensity**: `Control0[22:16]` (7-bit index)
- **Duration**: `Control0[15:0]` (16-bit value)
- **Cooldown**: `Control1[31:16]` (16-bit value)

## State Machine

The ProbeDriver operates through five main states:

1. **IDLE** - Waiting for enable signal or auto-advance in zeroinit mode
2. **ARMED** - Ready for trigger, initializing pulse counter
3. **FIRING** - Actively firing laser with duration control
4. **FIRED** - Pulse completed, transitioning to cooldown
5. **COOL_DOWN** - Safety cooldown period before next cycle

## ZeroInit Mode

ZeroInit mode automatically executes a demonstration cycle when all control registers are set to zero (default state). This feature:

- **Automatically detects** when all registers are 0x00
- **Uses safe default values** for timing and intensity
- **Executes one complete cycle** automatically
- **Clears itself** after triggering to prevent loops
- **Perfect for testing** and initial hardware validation

### ZeroInit Default Values
- **Intensity**: 0 (safe minimum)
- **Pulse Duration**: `PulseMinDuration` constant
- **Cooldown**: `ProbeCoolDownMin` constant

## Status Register

The status register provides real-time feedback on the current state:

```
Status[0]: ARMED state active
Status[1]: FIRING state active  
Status[2]: FIRED state active
Status[3]: COOL_DOWN state active
Status[4-31]: Reserved for future use
```

## Timing Parameters

### Minimum Values (enforced by hardware)
- **Pulse Duration**: 1 clock cycle minimum
- **Cooldown Period**: 1 clock cycle minimum
- **Intensity Index**: 0-127 (7-bit range)

### Clock Requirements
- **System Clock**: Configurable frequency
- **Timing Resolution**: 1 clock cycle precision
- **Maximum Duration**: 65,535 clock cycles

## Usage Examples

### Basic Operation
1. Set `Control0[31]` to 1 (Enable)
2. Configure `Control0[22:16]` with desired intensity (0-127)
3. Set `Control0[15:0]` with pulse duration (1-65535)
4. Configure `Control1[31:16]` with cooldown period (1-65535)
5. Pulse `Control0[23]` to trigger firing sequence

### ZeroInit Testing
1. Reset all control registers to 0x00
2. Enable the system (`Control0[31] = 1`)
3. System automatically executes one safe cycle
4. Monitor status register for state transitions

## Building and Testing

### Prerequisites
- GHDL VHDL compiler/simulator
- Make utility

### Build Commands
```bash
# Build all components
make

# Run unit tests
make test_unit

# Run integration tests  
make test_integration

# Clean build artifacts
make clean
```

### Testbench Structure
- **`probe_driver_tb.vhd`** - Unit tests for core ProbeDriver
- **`top_probe_driver_improved_tb.vhd`** - Integration tests for top-level interface

## Safety Features

- **Minimum timing enforcement** prevents unsafe short pulses
- **Cooldown protection** ensures proper thermal management
- **Intensity limits** prevent excessive laser power
- **State validation** ensures proper sequence execution
- **Reset protection** clears all states safely

## Future Enhancements

The design includes reserved bits in `Control1[15:0]` for future features:
- Advanced timing modes
- Burst firing capabilities
- External trigger synchronization
- Power management controls
- Diagnostic and calibration features

## Documentation

For detailed technical information, see the `old/` directory containing:
- Detailed register specifications
- Troubleshooting guides
- Organization documentation
- Historical development notes

## License

This project is licensed under the terms specified in the LICENSE file.



