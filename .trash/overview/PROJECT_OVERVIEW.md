# Moku VHDL Development Project Overview

## **Project Purpose**
This repository contains VHDL implementations for various Moku platform modules, including probe drivers, slot blinkers, and other custom functionality designed for fault injection and signal analysis applications.

## **Project Structure**

### **Core Modules**

#### **ProbeDriver** (`/ProbeDriver/`)
- **Purpose**: Fault injection probe driver with configurable intensity, timing, and status monitoring
- **Key Features**: 
  - Configurable pulse duration and cooldown periods
  - Intensity lookup table for precise control
  - Status LED indicators and monitoring
  - Clock divider support for various timing requirements
- **Status**: ✅ **Production Ready** - Fully tested and documented
- **Documentation**: Complete architecture docs, register specs, and user guides

#### **EnhancedSlotBlinker** (`/EnhancedSlotBlinker/`)
- **Purpose**: Advanced slot blinker with pattern generation and control register support
- **Key Features**:
  - Multiple pattern types (square, triangle, sine, custom)
  - Configurable frequency and phase
  - Control register interface for runtime configuration
- **Status**: ✅ **Production Ready** - Fully tested and documented
- **Documentation**: Enhancement summaries and control register documentation

#### **BestSlotBlinker** (`/BestSlotBlinker/`)
- **Purpose**: Optimized slot blinker with UART communication support
- **Key Features**:
  - UART interface for external control
  - Pattern generation and control
  - Optimized for performance and reliability
- **Status**: ✅ **Production Ready** - Fully tested and documented
- **Documentation**: Control register layout and UART driver documentation

#### **MokuModules** (`/MokuModules/`)
- **Purpose**: Template and example implementations for Moku platform
- **Key Features**:
  - CustomWrapper interface templates
  - Example implementations for various use cases
  - Platform-specific optimizations
- **Status**: 🔄 **In Development** - Templates and examples available
- **Documentation**: Implementation summaries and usage examples

### **Supporting Components**

#### **Clock Divider** (`/clk-divider/`)
- **Purpose**: Configurable clock divider for various timing requirements
- **Status**: ✅ **Production Ready** - Integrated into ProbeDriver

#### **Legacy Implementations** (Archived)
- **Purpose**: Historical development artifacts and troubleshooting reference
- **Status**: 📦 **Archived** - Preserved for historical reference
- **Location**: `docs/archive/` - Legacy Slot1 and Slot2 implementations
- **Note**: Current implementations are in their respective module directories

## **Development Status**

### **✅ Production Ready**
- ProbeDriver (v1.0 - Refactored)
- EnhancedSlotBlinker
- BestSlotBlinker
- Clock Divider

### **🔄 In Development**
- MokuModules templates
- Slot1/Slot2 implementations
- Additional pattern generators

### **📋 Planned**
- Advanced triggering systems
- Performance monitoring
- Additional probe types

## **Key Technologies**

### **VHDL Standards**
- IEEE Std_Logic_1164
- IEEE Numeric_Std
- VHDL-2008 compatible

### **Platform Support**
- **Moku Go**: Primary target platform
- **Moku Pro**: Extended functionality support
- **Moku Lab**: Development and testing

### **Build System**
- **GHDL**: Open-source VHDL simulator
- **Makefiles**: Automated build and test processes
- **Python**: Test automation and control

## **Getting Started**

### **Prerequisites**
```bash
# Install GHDL
brew install ghdl  # macOS
# or
sudo apt-get install ghdl  # Ubuntu/Debian

# Clone repository
git clone https://github.com/sealablab/moku-dev-vhdl.git
cd moku-dev-vhdl
```

### **Quick Start**
```bash
# Check syntax
cd ProbeDriver
make syntax_check

# Run tests
cd testbench
make all

# Build for MCC synthesis
make mcc_build
```

### **First Project**
1. **Start with ProbeDriver** - Most complete and well-documented
2. **Review register documentation** - Understand the control interface
3. **Run testbenches** - Verify functionality
4. **Modify parameters** - Experiment with different configurations

## **Documentation Structure**

### **High-Level Docs** (`/docs/`)
- **Overview**: This document and project-wide information
- **Requirements**: High-level requirements and specifications
- **Migration**: Migration guides and progress tracking

### **Module-Specific Docs** (with code)
- **README.md**: User guides and quick start
- **Architecture docs**: Implementation details and design decisions
- **Register specs**: Control interface documentation
- **Test documentation**: Testbench descriptions and usage

## **Contributing**

### **Development Workflow**
1. **Create feature branch** from main
2. **Implement changes** with corresponding documentation updates
3. **Run tests** to ensure functionality
4. **Update documentation** to reflect changes
5. **Submit pull request** with clear description

### **Documentation Standards**
- **Keep technical docs with code** during active development
- **Update high-level docs** when architecture changes
- **Include examples** for all new features
- **Maintain consistency** across all modules

## **Contact & Support**

- **Repository**: https://github.com/sealablab/moku-dev-vhdl
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Documentation**: All documentation is maintained in this repository

---

*Last Updated: 2025-01-27*
*Version: 1.0*
