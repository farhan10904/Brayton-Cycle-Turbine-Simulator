import numpy as np
import pandas as pd
from Brayton import calculate_cycle, calculate_cycle_real
import Config

def sensitivity_pressure_ratio(pr_min, pr_max, pr_step, cycle):
    results = []

    for Pr in np.arange(pr_min, pr_max +pr_step, pr_step):
        try:
            if cycle is calculate_cycle_real:
                cycle_results = calculate_cycle_real(
                    T1 = Config.T1,
                    P1 = Config.P1, 
                    pressure_ratio = Pr,
                    turbine_inlet_temperature = Config.turbine_inlet_temperature,
                    gamma = Config.gamma,
                    Cp = Config.Cp,
                    compressor_efficiency = Config.compressor_efficiency,
                    turbine_efficiency = Config.turbine_efficiency,
                    mass_flow_rate = Config.mass_flow_rate,
                    combustor_pressure_loss = Config.combustor_pressure_loss,
                    R = Config.R,
                    T_ambient = Config.T_ambient
                )
            else:
                cycle_results = calculate_cycle(
                    T1 = Config.T1,
                    P1 = Config.P1,
                    pressure_ratio = Pr,
                    turbine_inlet_temperature = Config.turbine_inlet_temperature,
                    gamma = Config.gamma,
                    Cp = Config.Cp,
                    mass_flow_rate = Config.mass_flow_rate,
                    combustor_pressure_loss = Config.combustor_pressure_loss,
                    R = Config.R,
                    T_ambient = Config.T_ambient
                )
            cycle_results["pressure_ratio"] = Pr
            results.append(cycle_results)
        except ValueError as e:
            print(f"Error for Pressure Ratio {Pr}: {e}")
    return pd.DataFrame(results) 


def sensitivity_turbine_inlet_temperature(tit_min, tit_max, tit_step, cycle):
    results = []

    for Tit in np.arange(tit_min, tit_max + tit_step, tit_step):
        try:
            if cycle is calculate_cycle_real:
                cycle_results = calculate_cycle_real(
                    T1 = Config.T1,
                    P1 = Config.P1,
                    pressure_ratio = Config.pressure_ratio,
                    turbine_inlet_temperature = Tit,
                    gamma = Config.gamma,
                    Cp = Config.Cp,
                    compressor_efficiency = Config.compressor_efficiency,
                    turbine_efficiency = Config.turbine_efficiency,
                    mass_flow_rate = Config.mass_flow_rate,
                    combustor_pressure_loss = Config.combustor_pressure_loss,
                    R = Config.R,
                    T_ambient = Config.T_ambient
                )
            else:
                cycle_results = calculate_cycle(
                    T1 = Config.T1,
                    P1 = Config.P1,
                    pressure_ratio = Config.pressure_ratio,
                    turbine_inlet_temperature = Tit,
                    gamma = Config.gamma,
                    Cp = Config.Cp,
                    mass_flow_rate = Config.mass_flow_rate,
                    combustor_pressure_loss = Config.combustor_pressure_loss,
                    R = Config.R,
                    T_ambient = Config.T_ambient
                )
            cycle_results["turbine_inlet_temperature"] = Tit
            results.append(cycle_results)
        except ValueError as e:
            print(f"Error for Turbine Inlet Temperature {Tit}: {e}")
    return pd.DataFrame(results) 

#print(df_ideal[["pressure_ratio","W_net","thermal_efficiency"]].head())
#print(df_real[["pressure_ratio","W_net","thermal_efficiency"]].head())