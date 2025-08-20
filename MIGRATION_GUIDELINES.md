# Direct Entity Instantiation Migration Guidelines

## Overview
This document provides step-by-step guidelines for migrating VHDL modules from component declarations to direct entity instantiation.

## Migration Pattern

### Before (Component Declaration)
```vhdl
-- Component declaration
component entity_name is
    port (
        clk : in std_logic;
        rst : in std_logic;
        data_in : in std_logic_vector(7 downto 0);
        data_out : out std_logic_vector(7 downto 0)
    );
end component;

-- Component instantiation
entity_inst : entity_name
    port map (
        clk => clk,
        rst => rst,
        data_in => data_in,
        data_out => data_out
    );
```

### After (Direct Entity Instantiation)
```vhdl
-- Direct entity instantiation
entity_inst : entity work.entity_name
    port map (
        clk => clk,
        rst => rst,
        data_in => data_in,
        data_out => data_out
    );
```

## Step-by-Step Migration Process

### 1. Identify Component Declarations
- Search for `component` keywords in VHDL files
- Look for component declarations in wrapper files
- Check testbench files for component usage

### 2. Verify Entity Existence
- Ensure the entity file exists in the same directory or accessible path
- Check that entity name matches component name exactly
- Verify port definitions are identical

### 3. Replace Component Declaration
- Remove the entire `component ... end component;` block
- Replace component instantiation with `entity work.entity_name`

### 4. Update Port Mapping
- Ensure all ports are mapped using named port mapping
- Verify signal names match exactly
- Check for any generic mappings if present

### 5. Test the Migration
- Run the module's testbench to verify functionality
- Check that the module builds successfully
- Verify synthesis still works (if applicable)

## Common Issues and Solutions

### Issue: Entity Not Found
**Error**: `Entity "entity_name" is not declared`
**Solution**: 
- Check file path and library inclusion
- Ensure entity file is compiled before use
- Verify entity name spelling

### Issue: Port Mismatch
**Error**: `Port "port_name" not found in entity`
**Solution**:
- Use named port mapping to catch mismatches early
- Compare port definitions between component and entity
- Check for typos in port names

### Issue: Generic Mismatch
**Error**: `Generic "generic_name" not found in entity`
**Solution**:
- Map generics explicitly using named generic mapping
- Verify generic default values match expectations

## Migration Checklist

For each module:
- [ ] Identify all component declarations
- [ ] Verify entity files exist and are accessible
- [ ] Replace component declarations with direct instantiation
- [ ] Update port mappings to use named mapping
- [ ] Test functionality with existing testbenches
- [ ] Verify build process still works
- [ ] Update documentation if needed

## Testing Strategy

### Immediate Testing
- Run existing testbenches
- Verify "ALL TESTS PASSED" output
- Check for any new warnings or errors

### Build Testing
- Ensure `make` commands still work
- Verify GHDL compilation succeeds
- Check that work libraries are created correctly

### Integration Testing
- Test module integration with other modules
- Verify no regressions in functionality
- Check that synthesis constraints still apply

## Rollback Plan

If issues arise:
1. **Git revert**: `git revert <commit-hash>`
2. **File restoration**: Restore from backup files
3. **Test verification**: Ensure functionality is restored
4. **Issue analysis**: Document what went wrong

## Success Criteria

- [ ] All component declarations replaced with direct entity instantiation
- [ ] All testbenches pass without modification
- [ ] All modules build successfully
- [ ] No functionality regression
- [ ] Code is cleaner and more maintainable
