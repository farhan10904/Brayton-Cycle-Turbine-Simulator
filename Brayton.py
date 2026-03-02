import numpy as np

def calculate_cycle(T1, P1, pressure_ratio, turbine_inlet_temperature, gamma, Cp, 
mass_flow_rate, combustor_pressure_loss, R, T_ambient):
    
    T3 = turbine_inlet_temperature
    # Compressor Outlet Pressure
    P2 = P1 * pressure_ratio
    # Compressor Outlet Temperature (Isentropic)
    T2 = T1 * (pressure_ratio) ** ((gamma - 1) / gamma)
    if T3 <= T2:
        raise ValueError("Turbine inlet temperature (T3) must be greater than compressor outlet temperature (T2).")
    #Turbine Inlet Pressure (Assuming no pressure loss in combustion chamber)
    if combustor_pressure_loss == 0:
        P3 = P2 # No pressure loss in combustor
    else:
        P3 = P2 * (1 - combustor_pressure_loss) # Account for pressure loss in combustor
    #Turbine exit pressure (Assuming expansion back to ambient pressure)
    P4 = P1
    #Turbine exit temperature (Isentropic)
    T4 = T3 * (P4/P3) ** ((gamma - 1) / gamma)
    #Compressor entropy generation
    s_gen_compressor = Cp * np.log(T2/T1) - R * np.log(P2/P1)
    s_gen_compressor = max(0.0, s_gen_compressor) # Ensure non-negative entropy generation
    # Turbine entropy generation
    s_gen_turbine = Cp * np.log(T4/T3) - R * np.log(P4/P3)
    s_gen_turbine = max(0.0, s_gen_turbine) # Ensure non-negative entropy generation
    #Exergy destruction in compressor
    exergy_destruction_compressor = mass_flow_rate * T_ambient * s_gen_compressor # Exergy destruction in compressor (W)
    #Exergy destruction in turbine
    exergy_destruction_turbine = mass_flow_rate * T_ambient * s_gen_turbine # Exergy destruction in turbine (W)
    #Exergy rate total
    exergy_rate_destruction_total = exergy_destruction_compressor + exergy_destruction_turbine
    #Exergy specific total
    exergy_specific_destruction_total = exergy_rate_destruction_total / mass_flow_rate
    # Compressor work (Isentropic)
    Wc = Cp * (T2 - T1)
    #Turbine work (Isentropic)
    Wt = Cp * (T3 - T4)
    #Net work output of the cycle
    W_net = Wt - Wc
    if W_net <= 0:
        raise ValueError("Net work output (W_net) must be greater than zero.")
    power_net = mass_flow_rate * W_net # Net power output of the cycle (J/s)
    #Heat Added to the cycle   
    Qin = Cp * (T3 - T2)
    if Qin <= 0:
        raise ValueError("Heat added (Qin) must be greater than zero.")
    #Thermal Efficiency of the cycle
    thermal_efficiency = W_net / Qin
    #Second law efficiency (Exergy efficiency)
    exergy_input = Qin * (1 - T_ambient / T3) # Exergy input to the cycle (J/Kg)
    second_law_efficiency = W_net / exergy_input if exergy_input > 0 else 0 # Second law efficiency (Exergy efficiency)
    
    return {
        "T1": T1,
        "P1": P1,
        "T2": T2,
        "P2": P2,
        "T3": T3,
        "P3": P3,
        "T4": T4,
        "P4": P4,
        "Wc": Wc,
        "Wt": Wt,
        "W_net": W_net,
        "power_net": power_net,
        "Qin": Qin,
        "thermal_efficiency": thermal_efficiency,
        "exergy_destruction_compressor": exergy_destruction_compressor,
        "exergy_destruction_turbine": exergy_destruction_turbine,
        "exergy_destruction_compressor_specific": exergy_destruction_compressor / mass_flow_rate,
        "exergy_destruction_turbine_specific": exergy_destruction_turbine / mass_flow_rate,
        "exergy_rate_destruction_total": exergy_rate_destruction_total,
        "exergy_specific_destruction_total": exergy_specific_destruction_total,
        "second_law_efficiency": second_law_efficiency,
        "entropy_generation_compressor": s_gen_compressor,
        "entropy_generation_turbine": s_gen_turbine
    }

def calculate_cycle_real(T1, P1, pressure_ratio, turbine_inlet_temperature, gamma, 
Cp, compressor_efficiency, turbine_efficiency, 
mass_flow_rate, combustor_pressure_loss, R, T_ambient):
    
    if compressor_efficiency <= 0 or compressor_efficiency > 1:
        raise ValueError("Compressor efficiency must be between 0 and 1.")
    if turbine_efficiency <= 0 or turbine_efficiency > 1:
        raise ValueError("Turbine efficiency must be between 0 and 1.")
    if pressure_ratio < 1:
        raise ValueError("Pressure ratio must be greater than 1.")
    T3 = turbine_inlet_temperature
    # Compressor Outlet Pressure
    P2 = P1 * pressure_ratio
    # Compressor Outlet Temperature 
    T2s = T1 * (pressure_ratio) ** ((gamma - 1) / gamma)
    # Actual Compressor Outlet Temperature (Considering compressor efficiency)
    T2 = T1 + (T2s - T1) / compressor_efficiency
    if T3 <= T2:
        raise ValueError("Turbine inlet temperature (T3) must be greater than compressor outlet temperature (T2).")
    #Turbine Inlet Pressure (Assuming no pressure loss in combustion chamber)
    if combustor_pressure_loss == 0:
        P3 = P2 # No pressure loss in combustor
    else:
        P3 = P2 * (1 - combustor_pressure_loss) # Account for pressure loss in combustor
    #Turbine exit pressure (Assuming expansion back to ambient pressure)
    P4 = P1
    #Turbine exit temperature 
    T4s = T3 * (P4/P3) ** ((gamma - 1) / gamma)
    # Actual Turbine Exit Temperature (Considering turbine efficiency)
    T4 = T3 - (T3 - T4s) * turbine_efficiency
    #Compressor entropy generation
    s_gen_compressor = Cp * np.log(T2/T1) - R * np.log(P2/P1)
    s_gen_compressor = max(0.0, s_gen_compressor) # Ensure non-negative entropy generation
    # Turbine entropy generation
    s_gen_turbine = Cp * np.log(T4/T3) - R * np.log(P4/P3)
    s_gen_turbine = max(0.0, s_gen_turbine) # Ensure non-negative entropy generation
    #Exergy destruction in compressor
    exergy_destruction_compressor = mass_flow_rate * T_ambient * s_gen_compressor
    #Exergy destruction in turbine
    exergy_destruction_turbine = mass_flow_rate * T_ambient * s_gen_turbine
    #Exergy rate total
    exergy_rate_destruction_total = exergy_destruction_compressor + exergy_destruction_turbine
    #Exergy specific total
    exergy_specific_destruction_total = exergy_rate_destruction_total / mass_flow_rate
    # Compressor work 
    Wc = Cp * (T2 - T1)
    #Turbine work 
    Wt = Cp * (T3 - T4)
    #Net work output of the cycle
    W_net = Wt - Wc
    if W_net <= 0:
        raise ValueError("Net work output (W_net) must be greater than zero.")
    power_net = mass_flow_rate * W_net # Net power output of the cycle (J/s)
    #Heat Added to the cycle   
    Qin = Cp * (T3 - T2)
    if Qin <= 0:
        raise ValueError("Heat added (Qin) must be greater than zero.")
    #Thermal Efficiency of the cycle
    thermal_efficiency = W_net / Qin
    #Second law efficiency (Exergy efficiency)
    exergy_input = Qin * (1 - T_ambient / T3) # Exergy input to the cycle (J/Kg)
    if exergy_input <= 0:
        raise ValueError("Exergy input must be greater than zero.")
    else:
        second_law_efficiency = W_net / exergy_input  # Second law efficiency (Exergy efficiency)
    
    return {
        "T1": T1,
        "P1": P1,
        "T2": T2,
        "T2s": T2s,
        "P2": P2,
        "T3": T3,
        "P3": P3,
        "T4": T4,
        "T4s": T4s,
        "P4": P4,
        "Wc": Wc,
        "Wt": Wt,
        "W_net": W_net,
        "power_net": power_net,
        "Qin": Qin,
        "thermal_efficiency": thermal_efficiency,
        "exergy_destruction_compressor": exergy_destruction_compressor,
        "exergy_destruction_turbine": exergy_destruction_turbine,
        "exergy_destruction_compressor_specific": exergy_destruction_compressor / mass_flow_rate,
        "exergy_destruction_turbine_specific": exergy_destruction_turbine / mass_flow_rate,
        "exergy_rate_destruction_total": exergy_rate_destruction_total,
        "exergy_specific_destruction_total": exergy_specific_destruction_total,
        "second_law_efficiency": second_law_efficiency,
        "entropy_generation_compressor": s_gen_compressor,
        "entropy_generation_turbine": s_gen_turbine

    }