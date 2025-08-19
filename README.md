# 🚀 Moku VHDL Development Workspace

This is a **meta-repository** that brings together all the tools you need for Moku development:

This workspace is designed to be the ultimate starting point for Moku platform VHDL development. Clone it once, get everything you need, and let Cursor AI help you build amazing fault injection and signal analysis tools.

## 🏗️ Workspace Architecture

```
moku-vhdl-dev-workspace/
├── 📁 moku-dev-vhdl/          # Core VHDL modules and IP cores
├── 📁 moku-examples/          # Official Liquid Instruments examples
├── 📁 docs/                   # Moku specific documentation
└── 📁 scripts/                # Development and automation tools
```

## 🚀 Quick Start (2 Steps!)

### 1. Clone the Workspace
```bash
git clone --recursive git@github.com:sealablab/moku-vhdl-dev-workspace.git
cd moku-vhdl-dev-workspace
./runme.sh
```


`runme.sh` will automatically:
- Initialize and update all git submodules
- Configure sparse-checkout for moku-examples (VHDL + Python only)
- Verify the setup and show you what's available
- Guide you through next steps

### **What `runme.sh` Does**
The setup script handles all the complexity of:
- **Git submodule management**: Clones and updates all dependencies
- **Sparse-checkout configuration**: Ensures only VHDL and Python examples are included

## 🎯 What You Get Out of the Box

### **VHDL Development (`moku-dev-vhdl/`)**
- **ProbeDriver**: Fault injection laser controller with precise timing
- **SlotBlinkers**: Advanced pattern generators for testing and demonstration
- **IP Cores**: FFT, FIR filters, CORDIC, and more
- **Templates**: Ready-to-use VHDL module templates


### **Examples & Templates (`moku-examples/`)**
- **Python APIs**: Complete examples for every Moku instrument
- **VHDL Templates**: IP core templates and example implementations
- **Cloud Compile**: Examples for cloud-based VHDL compilation

## 🤖 Why This Workspace Loves Cursor

### **Perfect File Organization**
- **Semantic grouping**: Related files are logically organized
- **Clear naming**: Files and directories have descriptive names
- **Consistent structure**: Predictable layout across all modules

### **Rich Context for AI**
- **Comprehensive examples**: AI can learn from real implementations
- **Documentation**: Extensive docs help AI understand your goals
- **Testbenches**: AI can help with verification and testing


```



