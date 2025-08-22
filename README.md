# 🚀 Moku VHDL Development Workspace

This is a **meta-repository** that brings together all the tools you need for Moku development:

## 🏷️ **Stable Release Tag - Recommended for Production Use**

**For the most reliable setup with all submodules working correctly, clone at this specific tag:**

```bash
# Clone the repository at the stable tag
git clone --recurse-submodules --depth 1 --branch v1.0.0-submodules-restored git@github.com:sealablab/moku-vhdl-dev-workspace.git

# Or if you prefer HTTPS:
git clone --recurse-submodules --depth 1 --branch v1.0.0-submodules-restored https://github.com/sealablab/moku-vhdl-dev-workspace.git

cd moku-vhdl-dev-workspace
```

**What this tag guarantees:**
- ✅ All 4 submodules successfully restored and working
- ✅ Clean working tree with no conflicts
- ✅ Full synchronization between local and remote repositories
- ✅ Stable development environment ready for use
- ✅ No submodule corruption or remote ref issues

**Alternative: Clone latest main branch (may have ongoing development changes)**
```bash
git clone --recurse-submodules --depth 1 git@github.com:sealablab/moku-vhdl-dev-workspace.git
cd moku-vhdl-dev-workspace
```

**Already have the repository? Switch to the stable tag:**
```bash
cd moku-vhdl-dev-workspace
git fetch origin
git checkout v1.0.0-submodules-restored
git submodule update --init --recursive
```

## 🏗️ Workspace Architecture

```
├── 📁 moku-dev-vhdl/          # Core VHDL modules and IP cores
├── 📁 moku-examples-miniml/   # minimial fork of Liquid Instruments examples
├── 📁 moku-vhdl-dev-knowledge/ # Knowledge base & Obsidian vault content
├── 📁 docs/                   # Moku specific documentation
└── 📁 scripts/                # Development and automation tools
```

## 🧠 **Knowledge Management & Obsidian Integration**

This workspace now serves as a **full Obsidian vault** with integrated knowledge management:

### **📚 Knowledge Base (`moku-vhdl-dev-knowledge/`)**
- **Git Submodule**: Independent version control for knowledge content
- **Structured Documentation**: Design decisions, component analysis, integration guides
- **Cross-References**: Direct links to VHDL files, documentation, and examples
- **Team Collaboration**: Shareable knowledge repository separate from implementation

### **🔗 Obsidian Vault Features**
- **Full File Access**: Link directly to any file in the workspace
- **Knowledge Integration**: Connect design decisions to actual implementations
- **Search & Navigation**: Obsidian can search through all linked content
- **Graph View**: Visualize relationships between components and concepts

### **🚀 Benefits**
- **Context Preservation**: Stay in Obsidian while accessing your codebase
- **Knowledge Evolution**: Track how design decisions evolve over time
- **Team Onboarding**: New members can quickly understand system architecture
- **Decision History**: Maintain institutional knowledge and rationale

### **🤝 AI Collaboration Zones**
- **Cursor Safe Areas**: Designated collaboration zones within the knowledge base
- **Controlled Boundaries**: AI assistance while respecting Obsidian's organizational domain
- **Daily Notes**: Automated note creation in controlled collaboration areas

## 🚀 Quick Start (2 Steps!)

### 1. Clone the Workspace

**Option A: Stable Release (Recommended)**
```bash
git clone --recurse-submodules --depth 1 --branch v1.0.0-submodules-restored git@github.com:sealablab/moku-vhdl-dev-workspace.git
cd moku-vhdl-dev-workspace
./runme.sh
```

**Option B: Latest Development Version**
```bash
git clone --recurse-submodules --depth 1 git@github.com:sealablab/moku-vhdl-dev-workspace.git
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

### **🛠️ Troubleshooting Common Issues**

If you encounter git submodule errors during setup, here are the solutions in order of preference:

#### **Option 1: Update Submodule References (Recommended)**
```bash
cd moku-vhdl-dev-workspace
git submodule update --init --recursive --remote
```

#### **Option 2: Reset Submodules to Latest**
```bash
cd moku-vhdl-dev-workspace
git submodule foreach git checkout main
git submodule foreach git pull origin main
git add .
git commit -m "Update submodules to latest commits"
```

**Why This Happens**: Submodule references can become outdated when remote repositories are updated, force-pushed, or when commits are rewritten. This is common in active development repositories.

**Pro Tip**: For the most reliable setup, use `git clone --recurse-submodules --depth 1` which creates a shallow clone with properly initialized submodules. This avoids most submodule corruption issues.

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

## 🏛️ **Enhanced Global Requirements Architecture**

### **🎯 New Standard: Three Register Types with Equal Treatment**

We've established a **comprehensive VHDL architecture standard** that ensures all modules follow consistent design principles and maintain Verilog portability.

#### **📋 Three Register Types (All Equal Priority)**

| Register Type | Purpose | Characteristics | Implementation |
|---------------|---------|-----------------|----------------|
| **🔄 Control** | Runtime actions | Immediate effects, runtime accessible | VHDL records with std_logic types |
| **⚙️ Configuration** | Initialization parameters | Set during reset, stable during operation | VHDL records with std_logic_vector types |
| **📊 Status** | Operational state | Read-only, real-time updates | VHDL records with std_logic types |

#### **🏗️ Four-Layer Architecture**
```
┌─────────────────┐
│      TOP        │ ← System integration & platform features
├─────────────────┤
│   INTERFACE     │ ← External interface & register handling
├─────────────────┤
│      CORE       │ ← Pure algorithmic logic
├─────────────────┤
│     COMMON      │ ← Shared types, constants & utilities
└─────────────────┘
```

#### **🔑 Key Design Principles**
- **Equal Treatment**: All three register types receive equal documentation, implementation effort, and testing coverage
- **VHDL Records**: All register definitions use VHDL records for better organization and type safety
- **Verilog Portability**: Prefer std_logic types to minimize future conversion issues
- **Layered Separation**: Clear boundaries between layers with no cross-dependencies
- **Status Visibility**: Operational state is clearly visible and accessible through dedicated status registers

#### **📚 Documentation & Compliance**
- **Comprehensive Requirements**: Complete specification in `rework-try2/Global-Reqs/`
- **Validation Checklists**: Built-in compliance verification for all modules
- **Equal Implementation**: Mandates equal effort for all register types
- **Professional Standards**: Production-ready VHDL architecture guidelines

### **🚀 Benefits of the New Architecture**
- **Consistency**: All modules follow the same pattern
- **Maintainability**: Clear separation of concerns
- **Testability**: Core logic can be tested independently
- **Portability**: Better Verilog conversion path
- **Status Management**: Complete operational state visibility
- **Professional Quality**: Enterprise-grade VHDL standards

## 🔄 **Current Refactoring Status**

### **✅ Completed Work**
- **Enhanced Global Requirements**: Comprehensive architecture standards established
- **Equal Register Treatment**: StatusRegisters now have equal visibility and documentation
- **VHDL Records Mandate**: All register definitions must use VHDL records
- **Verilog Portability**: Prefer std_logic types for better conversion path
- **Four-Layer Architecture**: Clear separation of concerns defined

### **🚧 In Progress**
- **BasicBlock Refactoring**: Converting to new architecture (in `rework-try2/`)
- **ProbeDriver Refactoring**: Adapting existing production-ready module
- **SigGen Refactoring**: Updating signal generator to new standards

### **📋 Next Steps**
1. **Complete Module Migration**: Finish refactoring all three target modules
2. **Validation Testing**: Ensure all modules compile and meet new standards
3. **Documentation Updates**: Update individual module documentation
4. **Template Creation**: Generate reusable templates for new modules
5. **Training Materials**: Create guides for developers using the new architecture

### **🎯 Refactoring Goals**
- **Zero Compilation Errors**: All modules must compile with GHDL
- **Equal Register Implementation**: All three register types fully implemented
- **Layered Architecture**: Proper separation of concerns
- **Status Visibility**: Complete operational state tracking
- **Professional Quality**: Enterprise-grade VHDL standards

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



