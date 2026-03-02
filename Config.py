
# initial Conditions
T1 = 298.15 # K
P1 = 100000.0 # Pa

# Pressure Ratio
pressure_ratio = 5.0 

# Turbine Inlet Temperature
turbine_inlet_temperature = 1400.0 # K

# Mass Flow Rate
mass_flow_rate = 1.0 # kg/s

# Gas Properties
gamma = 1.4  # Specific heat ratio
R = 287.0    # Gas constant (J/kg*K)
Cp = 1005.0 # Specific heat at constant pressure (J/kg*K)    

# Efficiency
compressor_efficiency = 0.85
turbine_efficiency = 0.9
combustion_efficiency = 0.98

# Ambient Conditions
T_ambient = 300.0 # K

#Pr range for sensitivity analysis
pr_min = 2.0
pr_max = 50.0
pr_step = 1

#Tit range for sensitivity analysis
tit_min = 1400
tit_max = 1800
tit_step = 50