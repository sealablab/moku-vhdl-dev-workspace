# Documentation Directory

This directory contains high-level documentation for the moku-dev-vhdl project. Technical implementation details remain with their respective code modules for easier maintenance during active development.

## **Directory Structure**

### **`overview/`**
- **PROJECT_OVERVIEW.md**: Comprehensive project overview, module status, and getting started guide
- High-level architecture and project structure information

### **`requirements/`**
- **ProbeDriver requirements**: Architecture refactor requirements and specifications
- **CustomWrapper requirements**: Interface and wrapper specifications
- **General requirements**: LED drivers, state machines, and other component specs

### **`migration/`**
- **MIGRATION_PROGRESS.md**: Progress tracking for major architectural changes
- Migration guides and upgrade paths

## **Documentation Philosophy**

### **High-Level Docs** (in `/docs/`)
- Project-wide overview and architecture
- Requirements and specifications
- Migration and upgrade guides
- Getting started and contribution guidelines

### **Technical Docs** (with code)
- Implementation details and architecture
- Register specifications and interfaces
- User guides and quick start instructions
- Test documentation and examples

## **Why This Structure?**

During active development, keeping technical documentation close to the code it describes:
- **Maintains consistency** between code and docs
- **Easier to update** when implementation changes
- **Reduces documentation drift** during rapid iterations
- **Better developer experience** when working on specific modules

## **Finding Information**

### **For New Users**
1. Start with `overview/PROJECT_OVERVIEW.md`
2. Navigate to specific module directories
3. Read module README.md files
4. Review architecture documentation

### **For Developers**
1. Check module-specific docs in code directories
2. Review requirements in `docs/requirements/`
3. Check migration guides for breaking changes
4. Update both code docs and high-level docs as needed

### **For Contributors**
1. Follow documentation standards outlined in overview
2. Keep technical docs with code during development
3. Update high-level docs when architecture changes
4. Include examples and usage instructions

---

*This structure balances organization with maintainability during active development.*
