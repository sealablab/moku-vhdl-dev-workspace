# Direct Entity Instantiation Migration Plan
## moku-vhdl-dev-workspace

**Version**: 1.0  
**Date**: 2025-01-27  
**Goal**: Migrate all VHDL modules from component declarations to direct entity instantiation while maintaining 100% testbench functionality.

---

## Executive Summary

This plan migrates the entire `moku-vhdl` codebase from traditional component declaration + instantiation patterns to modern direct entity instantiation (`entity work.entity_name`). This change will:

- **Reduce code duplication** by ~30-40%
- **Eliminate synchronization issues** between component declarations and entity definitions
- **Improve maintainability** and reduce maintenance overhead
- **Align with modern VHDL best practices** and industry standards
- **Maintain 100% testbench functionality** throughout the migration

---

## Current State Analysis

### Component Declaration Usage (Found 25+ instances)
- **BasicBlock**: `basicblock_core` component in wrapper
- **SigGen**: `siggen_wrapper` and `siggen_core` components
- **ProbeDriver**: Multiple testbench components
- **SlotBlinker**: Testbench components
- **MokuModules**: Package-based component declarations

### Direct Entity Instantiation Usage (Found 10+ instances)
- **BasicBlock**: `clock_divider` already migrated
- **Examples**: Multiple Moku examples using direct instantiation
- **Mixed approach**: Some modules use both patterns

---

## Migration Strategy

### Phase 1: Foundation & Rules Update (Week 1)
1. **Update `.cursor/rules`** with new VHDL conventions
2. **Create migration guidelines** document
3. **Establish backup strategy** for rollback capability

### Phase 2: Core Module Migration (Week 2)
1. **BasicBlock** module (already partially migrated)
2. **SigGen** module
3. **ProbeDriver** module
4. **SlotBlinker** module

### Phase 3: Testbench Migration (Week 3)
1. **Critical testbenches** (ensure no functionality loss)
2. **Secondary testbenches**
3. **Integration testbenches**

### Phase 4: Validation & Cleanup (Week 4)
1. **Full build verification**
2. **Testbench validation**
3. **Documentation updates**

---

## Detailed Migration Steps

### Step 1: Update `.cursor/rules` File

Add the following section to your `.cursor/rules` file:

```markdown
### VHDL Instantiation Conventions

- **Direct Entity Instantiation**: Use `entity work.entity_name` instead of component declarations
- **Component Declarations**: Only use when:
  - Testbenches require component override behavior
  - Multiple instantiations with different configurations
  - Legacy compatibility requirements
- **Port Mapping**: Always use named port mapping for clarity
- **Generic Mapping**: Use named generic mapping when generics are present
```

### Step 2: Module-by-Module Migration

#### BasicBlock Module
**Files to Update**:
- `BasicBlock/wrapper/basicblock_wrapper.vhd` (lines 96-125)

**Current Pattern**:
```vhdl
component basicblock_core is
    port (
        -- port declarations
    );
end component;

basicblock_core_inst : basicblock_core
    port map (
        -- port mappings
    );
```

**New Pattern**:
```vhdl
basicblock_core_inst : entity work.basicblock_core
    port map (
        -- port mappings
    );
```

#### SigGen Module
**Files to Update**:
- `SigGen/SigGen.vhd` (lines 16-40)
- `SigGen/wrapper/siggen_wrapper.vhd` (lines 48-70)

**Migration Pattern**: Same as BasicBlock

#### ProbeDriver Module
**Files to Update**:
- All testbench files with component declarations
- Core module files if they exist

#### SlotBlinker Module
**Files to Update**:
- `SlotBlinker/testbench/SlotBlinker_tb.vhd`
- `EnhancedSlotBlinker/testbench/SlotBlinker_tb.vhd`

### Step 3: Testbench Migration Strategy

#### Critical Testbenches (Migrate First)
1. **BasicBlock testbenches** - Core functionality
2. **SigGen testbenches** - Signal generation
3. **ProbeDriver testbenches** - Fault injection

#### Migration Pattern for Testbenches
**Before**:
```vhdl
component CustomWrapper is
    port (
        Clk : in std_logic;
        -- ... other ports
    );
end component;

uut: CustomWrapper
    port map (
        -- port mappings
    );
```

**After**:
```vhdl
uut: entity work.CustomWrapper
    port map (
        -- port mappings
    );
```

### Step 4: MokuModules Package Update

**File**: `MokuModules/MokuModules_pkg.vhd`

**Decision**: Keep component declarations in this package as they serve a specific purpose for testbench standardization across multiple projects.

**Rationale**: This package provides reusable component definitions that eliminate duplication across testbenches. It's a different use case than internal module instantiation.

---

## Risk Mitigation

### Backup Strategy
1. **Git branches**: Create `migration/direct-instantiation` branch
2. **File backups**: Keep original files with `.backup` extension
3. **Rollback plan**: Document exact steps to revert changes

### Testing Strategy
1. **Incremental testing**: Test each module after migration
2. **Build verification**: Ensure all Makefiles still work
3. **Simulation validation**: Run existing testbenches to verify functionality

### Common Issues & Solutions
1. **Port mismatch**: Use named port mapping to catch errors early
2. **Generic issues**: Ensure generic values are correctly mapped
3. **Library issues**: Verify `work` library is properly configured

---

## Success Criteria

### Functional Requirements
- [ ] All existing testbenches pass without modification
- [ ] All modules build successfully with GHDL
- [ ] All modules synthesize successfully with Vivado 2022.2
- [ ] No regression in functionality

### Code Quality Requirements
- [ ] 100% of internal module instantiations use direct entity instantiation
- [ ] Component declarations only exist where specifically needed
- [ ] Consistent naming conventions across all modules
- [ ] Updated documentation reflects new conventions

### Performance Requirements
- [ ] No degradation in synthesis timing
- [ ] No increase in resource utilization
- [ ] Maintained or improved build times

---

## Implementation Checklist

### Phase 1: Foundation
- [ ] Update `.cursor/rules` file
- [ ] Create migration guidelines document
- [ ] Establish git branch for migration
- [ ] Create backup strategy

### Phase 2: Core Modules
- [ ] Migrate BasicBlock module
- [ ] Migrate SigGen module
- [ ] Migrate ProbeDriver module
- [ ] Migrate SlotBlinker module
- [ ] Test each module individually

### Phase 3: Testbenches
- [ ] Migrate critical testbenches
- [ ] Migrate secondary testbenches
- [ ] Migrate integration testbenches
- [ ] Validate all testbench functionality

### Phase 4: Validation
- [ ] Full build verification
- [ ] Testbench validation
- [ ] Documentation updates
- [ ] Final review and cleanup

---

## Post-Migration Benefits

### Immediate Benefits
- **Reduced code duplication**: ~30-40% reduction in component declarations
- **Eliminated sync issues**: Port definitions always match entity definitions
- **Cleaner code**: More readable and maintainable VHDL

### Long-term Benefits
- **Easier maintenance**: No need to update component declarations when entities change
- **Better tool support**: Modern synthesis tools optimize direct instantiation better
- **Industry alignment**: Follows current VHDL best practices
- **Reduced errors**: Fewer opportunities for port mismatch errors

---

## Rollback Plan

If issues arise during migration:

1. **Git revert**: `git revert <migration-commit>`
2. **File restoration**: Restore from `.backup` files
3. **Test verification**: Ensure all functionality is restored
4. **Issue analysis**: Document what went wrong for future attempts

---

## Conclusion

This migration represents a significant improvement in code quality and maintainability while maintaining 100% backward compatibility. The phased approach ensures minimal risk and allows for thorough testing at each stage.

The benefits of direct entity instantiation far outweigh the migration effort, and this change will position your codebase for better long-term maintainability and industry alignment.

---

**Next Steps**:
1. Review and approve this migration plan
2. Create the migration git branch
3. Begin Phase 1 implementation
4. Schedule regular progress reviews

**Estimated Timeline**: 4 weeks  
**Risk Level**: Low (with proper testing)  
**ROI**: High (immediate and long-term benefits)
