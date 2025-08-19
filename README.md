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

## 🚀 Quick Start (3 Steps!)

### 1. Clone the Workspace
```bash
git clone --recursive git@github.com:sealablab/moku-vhdl-dev-workspace.git
cd moku-vhdl-dev-workspace
git submodule update --init --recursive
```

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

### **Development Workflow**
- **Submodule management**: AI can help with dependency updates
- **Build automation**: Scripts for common development tasks
- **Testing framework**: Integrated testbenches for validation

## 🔧 Development Workflow

### **1. Design Your VHDL Module**
```bash
# Start with a template
cp moku-dev-vhdl/Template/Top.vhd my_new_module.vhd

# Let Cursor AI help you implement the logic
# "Help me implement a 16-bit counter with enable signal"
```

### **2. Test Your Design**
```bash
# Create a testbench
# Let Cursor AI help you write test cases
# "Help me create test vectors for this counter"
```

## 🛠️ Available Tools

### **Build & Simulation**
- **GHDL**: Open-source VHDL simulator
- **Makefiles**: Automated build processes
- **Testbenches**: Comprehensive verification

## 🔍 Troubleshooting

### **Submodule Issues**
```bash
# If submodules aren't loading
git submodule update --init --recursive

# If you need to update submodules
git submodule update --remote
```

### **Build Problems**
```bash
# Clean and rebuild
make clean && make

# Check GHDL installation
ghdl --version
```



