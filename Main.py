from Sensitivity import sensitivity_pressure_ratio
from Brayton import calculate_cycle_real, calculate_cycle
from Plots import plot_LossBreakdown_comparison, plot_second_law_efficiency_comparison, plot_specific_exergy_destruction_comparison, plot_exergy_destruction_comparison, plot_efficiency_vs_pressure_ratio_comparison, plot_efficiency_vs_net_work_comparison, plot_net_work_vs_pressure_ratio_comparison, plot_power_vs_pressure_ratio_comparison, plot_net_power_vs_pressure_ratio_real_cpl_5, plot_net_power_vs_pressure_ratio_real_cpl_0, plot_efficiency_vs_pressure_ratio, plot_efficiency_vs_net_work, plot_net_work_vs_pressure_ratio
import pandas as pd
import Config

df_ideal = sensitivity_pressure_ratio(
    Config.pr_min,
    Config.pr_max,
    Config.pr_step,
    cycle = calculate_cycle
)

df_real = sensitivity_pressure_ratio(
    Config.pr_min,
    Config.pr_max,
    Config.pr_step,
    cycle = calculate_cycle_real
)

df_real.to_csv("Results/results_real.csv", index=False)
df_ideal.to_csv("Results/results_ideal.csv", index=False)

def build_optima_summary(df, case_name):
    return pd.DataFrame({
        "case": [case_name, case_name, case_name],
        "objective": [
            "max_net_power",
            "max_thermal_efficiency",
            "max_second_law_efficiency"
        ],
        "pressure_ratio": [
            df.loc[df["power_net"].idxmax(), "pressure_ratio"],
            df.loc[df["thermal_efficiency"].idxmax(), "pressure_ratio"],
            df.loc[df["second_law_efficiency"].idxmax(), "pressure_ratio"],
        ],
        "net_power_kW": [
            df.loc[df["power_net"].idxmax(), "power_net"] / 1000,
            df.loc[df["thermal_efficiency"].idxmax(), "power_net"] / 1000,
            df.loc[df["second_law_efficiency"].idxmax(), "power_net"] / 1000,
        ],
        "thermal_efficiency_percent": [
            df.loc[df["power_net"].idxmax(), "thermal_efficiency"] * 100,
            df.loc[df["thermal_efficiency"].idxmax(), "thermal_efficiency"] * 100,
            df.loc[df["second_law_efficiency"].idxmax(), "thermal_efficiency"] * 100,
        ],
        "second_law_efficiency_percent": [
            df.loc[df["power_net"].idxmax(), "second_law_efficiency"] * 100,
            df.loc[df["thermal_efficiency"].idxmax(), "second_law_efficiency"] * 100,
            df.loc[df["second_law_efficiency"].idxmax(), "second_law_efficiency"] * 100,
        ]
    })

summary = pd.concat([
    build_optima_summary(df_ideal, "ideal_cycle"),
    build_optima_summary(df_real, "real_cycle")
], ignore_index=True)

summary.to_csv("Results/cycle_optima_summary.csv", index=False)


plot_efficiency_vs_pressure_ratio(df_ideal)
plot_efficiency_vs_net_work(df_ideal)
plot_net_work_vs_pressure_ratio(df_ideal)
plot_net_work_vs_pressure_ratio_comparison(df_ideal, df_real)
plot_power_vs_pressure_ratio_comparison(df_ideal, df_real)
plot_net_power_vs_pressure_ratio_real_cpl_5(df_real)
plot_net_power_vs_pressure_ratio_real_cpl_0(df_real)
plot_efficiency_vs_pressure_ratio_comparison(df_ideal, df_real)
plot_efficiency_vs_net_work_comparison(df_ideal, df_real)
plot_exergy_destruction_comparison(df_ideal, df_real)
plot_second_law_efficiency_comparison(df_ideal, df_real)
plot_LossBreakdown_comparison(df_ideal, df_real)
plot_specific_exergy_destruction_comparison(df_ideal, df_real)
