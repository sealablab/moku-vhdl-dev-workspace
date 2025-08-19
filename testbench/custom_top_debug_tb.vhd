-- CustomWrapper Debug Testbench
-- Tests the complete CustomWrapper interface and monitors OutputA, OutputB, OutputC
-- Designed to help troubleshoot initialization and reset issues

library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.Numeric_Std.all;
use work.IntensityLut_pkg.all;
use work.ProbeConfig_pkg.all;

entity custom_top_debug_tb is
end entity custom_top_debug_tb;

architecture testbench of custom_top_debug_tb is
    -- Clock period definition
    constant CLK_PERIOD : time := 10 ns;  -- 100MHz clock
    
    -- Test parameters
    constant TEST_RESET_DURATION : time := 100 ns;
    constant TEST_ENABLE_DELAY : time := 50 ns;
    constant TEST_TRIGGER_DELAY : time := 100 ns;
    constant TEST_OBSERVATION_TIME : time := 2000 ns;
    
    -- Clock and reset signals
    signal Clk : std_logic := '0';
    signal Reset : std_logic := '1';
    
    -- Control register signals
    signal Control0 : std_logic_vector(31 downto 0) := (others => '0');
    signal Control1 : std_logic_vector(31 downto 0) := (others => '0');
    
    -- Output signals to monitor
    signal OutputA : signed(15 downto 0);
    signal OutputB : signed(15 downto 0);
    signal OutputC : signed(15 downto 0);
    
    -- Internal monitoring signals
    signal OutputA_prev : signed(15 downto 0);
    signal OutputB_prev : signed(15 downto 0);
    signal OutputC_prev : signed(15 downto 0);
    
    -- Test state tracking
    signal test_phase : string(1 to 20) := "INITIALIZATION    ";
    signal test_step : integer := 0;
    
begin
    -- =============================================================================
    -- CLOCK GENERATION
    -- =============================================================================
    Clk <= not Clk after CLK_PERIOD / 2;
    
    -- =============================================================================
    -- DUT INSTANTIATION
    -- =============================================================================
    u_custom_wrapper: entity work.CustomWrapper
        port map (
            Clk => Clk,
            Reset => Reset,
            Control0 => Control0,
            Control1 => Control1,
            OutputA => OutputA,
            OutputB => OutputB,
            OutputC => OutputC
        );
    
    -- =============================================================================
    -- OUTPUT MONITORING
    -- =============================================================================
    process(Clk)
    begin
        if rising_edge(Clk) then
            -- Store previous values for change detection
            OutputA_prev <= OutputA;
            OutputB_prev <= OutputB;
            OutputC_prev <= OutputC;
            
            -- Report any output changes
            if OutputA /= OutputA_prev then
                report "OutputA changed: " & to_string(OutputA_prev) & " -> " & to_string(OutputA) & 
                       " (Phase: " & test_phase & ", Step: " & integer'image(test_step) & ")";
            end if;
            
            if OutputB /= OutputB_prev then
                report "OutputB changed: " & to_string(OutputB_prev) & " -> " & to_string(OutputB) & 
                       " (Phase: " & test_phase & ", Step: " & integer'image(test_step) & ")";
            end if;
            
            if OutputC /= OutputC_prev then
                report "OutputC changed: " & to_string(OutputC_prev) & " -> " & to_string(OutputC) & 
                       " (Phase: " & test_phase & ", Step: " & integer'image(test_step) & ")";
            end if;
        end if;
    end process;
    
    -- =============================================================================
    -- TEST STIMULUS
    -- =============================================================================
    process
    begin
        -- Initialize
        report "========================================";
        report "Starting CustomWrapper Debug Testbench";
        report "========================================";
        report "This testbench will help debug initialization and reset issues";
        report "========================================";
        
        -- Phase 1: Initial Reset State
        test_phase <= "RESET_STATE      ";
        test_step <= 1;
        report "Phase 1: Testing initial reset state";
        report "Reset = '1', Control0 = 0x00000000, Control1 = 0x00000000";
        
        Reset <= '1';
        Control0 <= x"00000000";
        Control1 <= x"00000000";
        wait for TEST_RESET_DURATION;
        
        -- Report initial output state
        report "Initial Output State:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Phase 2: Release Reset (Auto-fire should trigger)
        test_phase <= "AUTO_FIRE        ";
        test_step <= 2;
        report "Phase 2: Releasing reset - auto-fire should trigger";
        report "Reset = '0', Control0 = 0x00000000 (enabled with safe defaults)";
        
        Reset <= '0';
        wait for TEST_ENABLE_DELAY;
        
        -- Report state after reset release
        report "After Reset Release:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Phase 3: Wait for Auto-fire Completion
        test_phase <= "AUTO_FIRE_WAIT  ";
        test_step <= 3;
        report "Phase 3: Waiting for auto-fire completion";
        report "Monitoring outputs during auto-fire cycle...";
        
        wait for TEST_OBSERVATION_TIME;
        
        -- Report final auto-fire state
        report "Auto-fire Completion:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Phase 4: Test Manual Trigger
        test_phase <= "MANUAL_TRIGGER   ";
        test_step <= 4;
        report "Phase 4: Testing manual trigger";
        report "Setting Control0(23) = '1' to trigger manually";
        
        Control0(23) <= '1';
        wait for TEST_TRIGGER_DELAY;
        Control0(23) <= '0';
        
        -- Report manual trigger state
        report "Manual Trigger State:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Phase 5: Wait for Manual Trigger Completion
        test_phase <= "MANUAL_WAIT      ";
        test_step <= 5;
        report "Phase 5: Waiting for manual trigger completion";
        
        wait for TEST_OBSERVATION_TIME;
        
        -- Report final manual trigger state
        report "Manual Trigger Completion:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Phase 6: Test Disable Mode
        test_phase <= "DISABLE_MODE     ";
        test_step <= 6;
        report "Phase 6: Testing disable mode";
        report "Setting Control0(31) = '1' to disable system";
        
        Control0(31) <= '1';
        wait for TEST_ENABLE_DELAY;
        
        -- Report disable mode state
        report "Disable Mode State:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Phase 7: Test Re-enable
        test_phase <= "RE_ENABLE        ";
        test_step <= 7;
        report "Phase 7: Testing re-enable";
        report "Setting Control0(31) = '0' to re-enable system";
        
        Control0(31) <= '0';
        wait for TEST_ENABLE_DELAY;
        
        -- Report re-enable state
        report "Re-enable State:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        
        -- Final wait and completion
        wait for TEST_OBSERVATION_TIME;
        
        report "========================================";
        report "CustomWrapper Debug Testbench Complete";
        report "========================================";
        report "Final Output State:";
        report "  OutputA = " & to_string(OutputA) & " (Status Register)";
        report "  OutputB = " & to_string(OutputB) & " (Trigger Output)";
        report "  OutputC = " & to_string(OutputC) & " (Intensity Output)";
        report "========================================";
        
        -- End simulation
        wait;
    end process;
    
    -- =============================================================================
    -- TIMEOUT PROTECTION
    -- =============================================================================
    process
    begin
        wait for 10000 ns;  -- 10 microseconds timeout
        report "Simulation timeout reached - ending testbench";
        wait;
    end process;
    
end architecture testbench;
