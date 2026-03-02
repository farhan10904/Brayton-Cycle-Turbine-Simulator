
def calculate_cycle(T1, P1, pressure_ratio, turbine_inlet_temperature, gamma, Cp,):
    T3 = turbine_inlet_temperature
    # Compressor Outlet Pressure
    P2 = P1 * pressure_ratio
    # Compressor Outlet Temperature (Isentropic)
    T2 = T1 * (pressure_ratio) ** ((gamma - 1) / gamma)
    if T3 <= T2:
        raise ValueError("Turbine inlet temperature (T3) must be greater than compressor outlet temperature (T2).")
    #Turbine Inlet Pressure (Assuming no pressure loss in combustion chamber)
    P3 = P2
    #Turbine exit pressure (Assuming expansion back to ambient pressure)
    P4 = P1
    #Turbine exit temperature (Isentropic)
    T4 = T3 * (pressure_ratio) ** (-(gamma - 1) / gamma)
    # Compressor work (Isentropic)
    Wc = Cp * (T2 - T1)
    #Turbine work (Isentropic)
    Wt = Cp * (T3 - T4)
    #Net work output of the cycle
    W_net = Wt - Wc
    if W_net <= 0:
        raise ValueError("Net work output (W_net) must be greater than zero.")
    #Heat Added to the cycle   
    Qin = Cp * (T3 - T2)
    if Qin <= 0:
        raise ValueError("Heat added (Qin) must be greater than zero.")
    #Thermal Efficiency of the cycle
    thermal_efficiency = W_net / Qin
    
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
        "Qin": Qin,
        "thermal_efficiency": thermal_efficiency
    }

def calculate_cycle_real(T1, P1, pressure_ratio, turbine_inlet_temperature, gamma, Cp, compressor_efficiency, turbine_efficiency):
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
    P3 = P2
    #Turbine exit pressure (Assuming expansion back to ambient pressure)
    P4 = P1
    #Turbine exit temperature 
    T4s = T3 * (pressure_ratio) ** (-(gamma - 1) / gamma)
    # Actual Turbine Exit Temperature (Considering turbine efficiency)
    T4 = T3 - (T3 - T4s) * turbine_efficiency
    # Compressor work 
    Wc = Cp * (T2 - T1)
    #Turbine work 
    Wt = Cp * (T3 - T4)
    #Net work output of the cycle
    W_net = Wt - Wc
    if W_net <= 0:
        raise ValueError("Net work output (W_net) must be greater than zero.")
    #Heat Added to the cycle   
    Qin = Cp * (T3 - T2)
    if Qin <= 0:
        raise ValueError("Heat added (Qin) must be greater than zero.")
    #Thermal Efficiency of the cycle
    thermal_efficiency = W_net / Qin
    
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
        "Qin": Qin,
        "thermal_efficiency": thermal_efficiency
    }