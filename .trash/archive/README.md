# Archive Directory

This directory contains legacy development artifacts that are no longer part of the current project workflow but are preserved for historical reference.

## **What's Archived and Why**

### **Slot1** (`/Slot1/`)
- **Content**: Basic slot implementation (`Slot1-S1.vhd`)
- **Status**: Early development prototype
- **Why Archived**: Superseded by current modular architecture
- **Current Equivalent**: Integrated into main project structure

### **Slot2** (`/Slot2/`)
- **Content**: Legacy ProbeDriver implementation with testbenches
- **Status**: Development version before refactoring
- **Why Archived**: Replaced by current clean ProbeDriver implementation
- **Current Equivalent**: `ProbeDriver/` directory with refactored architecture

## **Archive Contents**

### **Slot1 Legacy**
```
Slot1/
└── Slot1-S1.vhd          # Early slot implementation prototype
```

### **Slot2 Legacy**
```
Slot2/
├── ProbeDriver.vhd        # Legacy implementation
├── IntensityLut.vhd       # Legacy intensity lookup
├── ProbeConfig.vhd        # Legacy configuration
├── top_probe_driver.vhd   # Legacy top-level interface
├── CustomWrapper.vhd       # Legacy wrapper
├── testbench/             # Legacy testbenches
├── TROUBLESHOOTING_SUMMARY.md
├── README_Organization.md
├── README_ProbeDriver_Reset.md
└── REGISTER_REFERENCE.md
```

## **When to Reference This Archive**

### **Historical Context**
- Understanding the evolution of the project
- Seeing how the architecture has improved
- Reference for troubleshooting approaches

### **Development History**
- How the refactoring improved the codebase
- What problems were solved
- Evolution of the design patterns

### **Troubleshooting Reference**
- Historical solutions to specific problems
- Alternative approaches that were considered
- Lessons learned from previous implementations

## **Current Project Structure**

The current project has moved to a clean, modular architecture:

```
moku-dev-vhdl/
├── ProbeDriver/           # Current, refactored implementation
├── EnhancedSlotBlinker/   # Current slot blinker implementation
├── BestSlotBlinker/       # Current UART-enabled implementation
├── MokuModules/           # Current template system
└── docs/                  # Current documentation structure
```

## **Migration Path**

### **From Slot2 to Current ProbeDriver**
- **Legacy**: Mixed responsibilities in single files
- **Current**: Clean separation of concerns (core, wrapper, package)
- **Legacy**: Inconsistent signal naming
- **Current**: Standardized naming conventions
- **Legacy**: Monolithic testbenches
- **Current**: Modular, focused test suites

### **From Slot1 to Current Architecture**
- **Legacy**: Basic slot implementation
- **Current**: Full-featured slot blinker with pattern generation
- **Legacy**: Limited functionality
- **Current**: Configurable, extensible design

## **Important Notes**

- **Do not use archived code** for new development
- **Current implementations** are in their respective directories
- **Archive is read-only** - no updates or modifications
- **Git history** preserves all development evolution
- **Current docs** provide up-to-date information

---

*This archive preserves development history while maintaining a clean, current project structure.*
