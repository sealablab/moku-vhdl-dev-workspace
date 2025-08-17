#!/usr/bin/env python3
"""
LA2LA - Logic Analyzer to Logic Analyzer Communication using BUS Routing

This script configures a single Moku device with two Logic Analyzers using BUS routing:
- Slot 1: Logic Analyzer Writer (generates patterns on DIO pins 4,5,6,7)
- Slot 2: Logic Analyzer Reader (detects patterns via BUS routing)

The script demonstrates communication between the two Logic Analyzers by:
1. Configuring Slot 1 as a pattern generator that outputs different patterns on DIO pins 4,5,6,7
2. Using BUS routing to connect DIO pins to Slot 2 Logic Analyzer inputs
3. Configuring Slot 2 to read and display the generated patterns via BUS connections
4. Ensuring physical DIO pins actually toggle externally for state machine driving
5. Continuously monitoring and displaying the BUS-routed communication

Usage:
    python LA2LA.py [device_ip]
    
    device_ip: IP address of the Moku device (default: prompts user)
"""

import sys
import time
import matplotlib.pyplot as plt
from moku.instruments import MultiInstrument, LogicAnalyzer

def get_device_ip():
    """Get device IP from command line or prompt user"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return input("Enter Moku device IP address: ").strip()

def configure_logic_analyzer_writer(la_writer):
    """Configure Slot 1 Logic Analyzer as a pattern generator on 4 DIO pins"""
    print("Configuring Slot 1 Logic Analyzer as 4-Pin Pattern Generator...")
    
    # Create different test patterns for each DIO pin
    # Each pattern will create a unique, visible signal that can be easily detected
    
    # DIO4: Clock-like pattern (alternating 1,0)
    clock_pattern = [1, 0] * 64  # 128 samples of alternating 1,0
    
    # DIO5: Pulse pattern (4 high, 4 low)
    pulse_pattern = [1, 1, 1, 1, 0, 0, 0, 0] * 16  # 128 samples with pulse groups
    
    # DIO6: Staircase pattern (incrementing pulse widths)
    staircase_pattern = []
    for i in range(8):  # 8 different pulse widths
        staircase_pattern.extend([1] * (i + 1))  # 1, 2, 3, 4, 5, 6, 7, 8 ones
        staircase_pattern.extend([0] * (16 - i))  # Fill to 16 samples per cycle
    # Trim to 128 samples total
    staircase_pattern = staircase_pattern[:128]
    
    # DIO7: Random-like pattern (pseudo-random sequence)
    random_pattern = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1] * 8  # 128 samples
    
    # Configure pattern generator on all 4 DIO pins
    patterns = [
        {"pin": 4, "pattern": clock_pattern},      # Clock signal
        {"pin": 5, "pattern": pulse_pattern},      # Pulse signal  
        {"pin": 6, "pattern": staircase_pattern},  # Staircase signal
        {"pin": 7, "pattern": random_pattern},     # Random signal
    ]
    
    # Set pattern generator with divider (controls frequency)
    # Lower divider = higher frequency
    la_writer.set_pattern_generator(1, patterns=patterns, divider=16)
    
    # Configure all 4 DIO pins as pattern generator outputs
    la_writer.set_pin_mode(pin=4, state="PG1")
    la_writer.set_pin_mode(pin=5, state="PG1")
    la_writer.set_pin_mode(pin=6, state="PG1")
    la_writer.set_pin_mode(pin=7, state="PG1")
    
    print(f"4-pin pattern generator configured:")
    print(f"  DIO4: Clock pattern ({len(clock_pattern)} samples)")
    print(f"  DIO5: Pulse pattern ({len(pulse_pattern)} samples)")
    print(f"  DIO6: Staircase pattern ({len(staircase_pattern)} samples)")
    print(f"  DIO7: Random pattern ({len(random_pattern)} samples)")
    print(f"  All patterns use divider=16")
    
    return patterns

def configure_logic_analyzer_reader(la_reader):
    """Configure Slot 2 Logic Analyzer to read data via BUS routing"""
    print("Configuring Slot 2 Logic Analyzer as Reader via BUS routing...")
    
    # Configure Logic Analyzer inputs to read from BUS connections
    # The BUS routing will automatically map DIO pins to these inputs
    la_reader.set_pin_mode(pin=1, state="Input")  # Will receive DIO4 via BUS
    la_reader.set_pin_mode(pin=2, state="Input")  # Will receive DIO5 via BUS
    la_reader.set_pin_mode(pin=3, state="Input")  # Will receive DIO6 via BUS
    la_reader.set_pin_mode(pin=4, state="Input")  # Will receive DIO7 via BUS
    
    # Set timebase for acquisition
    # Adjust these values based on your pattern frequency
    la_reader.set_timebase(-0.001, 0.001)  # ±1ms window
    
    print("Logic Analyzer reader configured to read via BUS routing")
    return la_reader

def setup_bus_connections(mim):
    """Set up BUS routing between DIO pins and Logic Analyzer inputs"""
    print("Setting up BUS routing for DIO to Logic Analyzer communication...")
    
    # Configure BUS routing to connect DIO pins to Logic Analyzer inputs
    # This creates internal signal paths using Moku's BUS system
    try:
        connections = [
            # Route DIO pins to BUS for internal communication
            dict(source="DIO4", destination="Bus1"),      # DIO4 → Bus1
            dict(source="DIO5", destination="Bus2"),      # DIO5 → Bus2  
            dict(source="DIO6", destination="Bus3"),      # DIO6 → Bus3
            dict(source="DIO7", destination="Bus4"),      # DIO7 → Bus4
            
            # Route BUS signals to Logic Analyzer inputs
            dict(source="Bus1", destination="Slot2InA"),  # Bus1 → Slot2 InputA
            dict(source="Bus2", destination="Slot2InB"),  # Bus2 → Slot2 InputB
            dict(source="Bus3", destination="Slot2InC"),  # Bus3 → Slot2 InputC
            dict(source="Bus4", destination="Slot2InD"),  # Bus4 → Slot2 InputD
            
            # Also route DIO pins to physical outputs for external monitoring
            dict(source="DIO4", destination="OutputA"),   # DIO4 → OutputA (Clock)
            dict(source="DIO5", destination="OutputB"),   # DIO5 → OutputB (Pulse)
            dict(source="DIO6", destination="OutputC"),   # DIO6 → OutputC (Staircase)
            dict(source="DIO7", destination="OutputD"),   # DIO7 → OutputD (Random)
        ]
        
        result = mim.set_connections(connections=connections)
        print("✓ BUS routing connections established:")
        print("  DIO4 → Bus1 → Slot2InA (Clock pattern)")
        print("  DIO5 → Bus2 → Slot2InB (Pulse pattern)")
        print("  DIO6 → Bus3 → Slot2InC (Staircase pattern)")
        print("  DIO7 → Bus4 → Slot2InD (Random pattern)")
        print("")
        print("🔌 PHYSICAL PINS NOW TOGGLE EXTERNALLY!")
        print("  - Connect oscilloscope/logic analyzer to OutputA-D")
        print("  - Use these signals to drive your state machine")
        print("  - All 4 pins will show different patterns simultaneously")
        print("")
        print("🚌 BUS ROUTING ENABLED:")
        print("  - Internal signal routing via Moku's BUS system")
        print("  - DIO pins automatically mapped to Logic Analyzer inputs")
        print("  - No external wiring needed for internal communication")
        
        return connections
        
    except Exception as e:
        print(f"⚠️  Warning: Could not establish BUS routing: {e}")
        print("   Falling back to direct DIO pin access...")
        
        # Fallback: Try simpler connections without BUS routing
        try:
            fallback_connections = [
                dict(source="DIO4", destination="OutputA"),
                dict(source="DIO5", destination="OutputB"),
                dict(source="DIO6", destination="OutputC"),
                dict(source="DIO7", destination="OutputD"),
            ]
            
            result = mim.set_connections(connections=fallback_connections)
            print("✓ Physical output connections established (fallback mode)")
            return fallback_connections
            
        except Exception as e2:
            print(f"✗ Failed to establish any connections: {e2}")
            return []

def display_pattern_info(patterns):
    """Display information about the generated patterns"""
    print("\n" + "="*60)
    print("4-PIN PATTERN GENERATOR CONFIGURATION")
    print("="*60)
    
    pin_names = {4: "DIO4 (Clock)", 5: "DIO5 (Pulse)", 6: "DIO6 (Staircase)", 7: "DIO7 (Random)"}
    
    for pattern_config in patterns:
        pin = pattern_config["pin"]
        pattern = pattern_config["pattern"]
        pin_name = pin_names.get(pin, f"DIO{pin}")
        
        print(f"{pin_name}: {len(pattern)} samples")
        print(f"  Pattern preview: {pattern[:16]}...")
        print(f"  Pattern summary: {sum(pattern)} ones, {len(pattern) - sum(pattern)} zeros")
        
        # Calculate pattern characteristics
        transitions = sum(1 for i in range(1, len(pattern)) if pattern[i] != pattern[i-1])
        duty_cycle = (sum(pattern) / len(pattern)) * 100
        
        print(f"  Characteristics: {transitions} transitions, {duty_cycle:.1f}% duty cycle")
        print()
    
    print("="*60)

def run_continuous_monitoring(la_reader, la_writer, patterns):
    """Run continuous monitoring of the BUS-routed communication"""
    print("\nStarting continuous BUS-routed monitoring...")
    print("Press Ctrl+C to stop")
    
    # Set up plotting for 4 pins
    plt.ion()
    fig, axes = plt.subplots(4, 2, figsize=(16, 12))
    fig.suptitle('LA2LA BUS-Routed Communication Monitor (Physical Pin Toggling)', fontsize=16)
    
    # Configure plot titles and labels
    pin_names = {4: "DIO4 (Clock)", 5: "DIO5 (Pulse)", 6: "DIO6 (Staircase)", 7: "DIO7 (Random)"}
    
    for i, pin in enumerate([4, 5, 6, 7]):
        # Left column: Generated patterns (Slot 1)
        axes[i, 0].set_title(f'Slot 1: Generated {pin_names[pin]}')
        axes[i, 0].set_ylabel('Logic Level')
        axes[i, 0].set_ylim([-0.2, 1.2])
        axes[i, 0].grid(True)
        
        # Right column: Detected patterns via BUS (Slot 2)
        axes[i, 1].set_title(f'Slot 2: Detected {pin_names[pin]} via BUS')
        axes[i, 1].set_ylabel('Logic Level')
        axes[i, 1].set_ylim([-0.2, 1.2])
        axes[i, 1].grid(True)
        if i == 3:  # Only bottom plot gets x-label
            axes[i, 1].set_xlabel('Time (s)')
    
    # Initialize plot lines for all 4 pins
    lines_writer = {}
    lines_reader = {}
    
    colors = ['blue', 'red', 'green', 'orange']
    
    for i, pin in enumerate([4, 5, 6, 7]):
        color = colors[i]
        # Generated pattern lines (left column - Slot 1)
        lines_writer[pin], = axes[i, 0].plot([], [], color=color, linewidth=2, 
                                            label=f'Generated (DIO{pin})')
        # Detected pattern lines (right column - Slot 2 via BUS)
        lines_reader[pin], = axes[i, 1].plot([], [], color=color, linewidth=2, 
                                            label=f'Detected via BUS (DIO{pin})')
        
        axes[i, 0].legend()
        axes[i, 1].legend()
    
    plt.tight_layout()
    
    try:
        while True:
            # Get data from both Logic Analyzers
            # Slot 1: Reading from DIO pins directly
            data_writer = la_writer.get_data(wait_reacquire=True, include_pins=[4, 5, 6, 7])
            # Slot 2: Reading from BUS-routed inputs
            data_reader = la_reader.get_data(wait_reacquire=True, include_pins=[1, 2, 3, 4])
            
            # Update plots for all 4 pins
            pin_mapping = {4: 1, 5: 2, 6: 3, 7: 4}  # DIO pin to Logic Analyzer input mapping
            
            for dio_pin in [4, 5, 6, 7]:
                la_input = pin_mapping[dio_pin]
                
                # Update generated pattern plot (Slot 1 - DIO pins)
                dio_key = f'pin{dio_pin}'
                if dio_key in data_writer and len(data_writer[dio_key]) > 0:
                    lines_writer[dio_pin].set_xdata(data_writer['time'])
                    lines_writer[dio_pin].set_ydata(data_writer[dio_key])
                    axes[dio_pin-4, 0].set_xlim(data_writer['time'][0], data_writer['time'][-1])
                
                # Update detected pattern plot (Slot 2 - BUS routing)
                la_key = f'pin{la_input}'
                if la_key in data_reader and len(data_reader[la_key]) > 0:
                    lines_reader[dio_pin].set_xdata(data_reader['time'])
                    lines_reader[dio_pin].set_ydata(data_reader[la_key])
                    axes[dio_pin-4, 1].set_xlim(data_reader['time'][0], data_reader['time'][-1])
            
            plt.pause(0.1)
            
    except KeyboardInterrupt:
        print("\nStopping monitoring...")
    finally:
        plt.ioff()
        plt.close()

def main():
    """Main function to run the LA2LA BUS-routed demonstration"""
    print("LA2LA - BUS-Routed Logic Analyzer to Logic Analyzer Communication")
    print("=" * 80)
    
    device_ip = get_device_ip()
    
    try:
        print(f"Connecting to Moku device at {device_ip}...")
        
        # Connect to Moku device in Multi-Instrument Mode
        mim = MultiInstrument(device_ip, platform_id=2, force_connect=True)
        
        # Configure Slot 1 as Logic Analyzer Writer (DIO pattern generator)
        la_writer = mim.set_instrument(1, LogicAnalyzer)
        
        # Configure Slot 2 as Logic Analyzer Reader (BUS-routed input)
        la_reader = mim.set_instrument(2, LogicAnalyzer)
        
        print("Successfully connected and configured both Logic Analyzers")
        
        # Configure the Logic Analyzers
        patterns = configure_logic_analyzer_writer(la_writer)
        configure_logic_analyzer_reader(la_reader)
        
        # Set up BUS routing and physical output connections
        setup_bus_connections(mim)
        
        # Display pattern information
        display_pattern_info(patterns)
        
        # Start continuous monitoring
        run_continuous_monitoring(la_reader, la_writer, patterns)
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the device is accessible and supports Logic Analyzer in both slots")
        return 1
    
    finally:
        try:
            if 'mim' in locals():
                print("Closing connection...")
                mim.relinquish_ownership()
        except:
            pass
    
    print("LA2LA BUS-routed demonstration completed")
    return 0

if __name__ == "__main__":
    sys.exit(main())
