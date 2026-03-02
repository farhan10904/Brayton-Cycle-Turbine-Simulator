from Sensitivity import sensitivity_pressure_ratio
from Brayton import calculate_cycle_real, calculate_cycle
from Plots import plot_net_work_vs_pressure_ratio_comparison
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

#df = df.sort_values("Pressure_Ratio")
#print(df)
#print(df.head())
#print(df.columns)
#plot_efficiency_vs_pressure_ratio(df)
#plot_efficiency_vs_net_work(df)
#plot_net_work_vs_pressure_ratio(df)
plot_net_work_vs_pressure_ratio_comparison(df_ideal, df_real)
