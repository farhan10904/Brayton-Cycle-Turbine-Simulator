import matplotlib.pyplot as plt

# def plot_efficiency_vs_pressure_ratio(df):
#     plt.figure(figsize=(8, 5))
#     plt.plot(df["pressure_ratio"], df["thermal_efficiency"]*100, marker='o')
#     plt.xlabel("Pressure Ratio")
#     plt.ylabel("Thermal Efficiency (%)")
#     plt.title("Thermal Efficiency vs Pressure Ratio")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig("Efficiency_vs_Pressure_Ratio.png")
#     plt.show()

# def plot_efficiency_vs_net_work(df):
#     plt.figure(figsize=(8, 5))
#     plt.plot(df["W_net"], df["thermal_efficiency"]*100, marker='o')
#     plt.xlabel("Net Work Output (W_net) (J/kg)")
#     plt.ylabel("Thermal Efficiency (%)")
#     plt.title("Thermal Efficiency vs Net Work Output")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig("Efficiency_vs_Net_Work.png")
#     plt.show()

# def plot_net_work_vs_pressure_ratio(df):
#     plt.figure(figsize=(8, 5))
#     plt.plot(df["pressure_ratio"], df["W_net"], marker='o')
#     plt.xlabel("Pressure Ratio")
#     plt.ylabel("Net Work Output (W_net) (J/kg)")
#     plt.title("Net Work Output vs Pressure Ratio")
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig("Net_Work_vs_Pressure_Ratio.png")
#     plt.show()

def plot_net_work_vs_pressure_ratio_comparison(df_ideal, df_real):
    plt.figure(figsize=(8, 5))
    plt.plot(df_ideal["pressure_ratio"], df_ideal["W_net"], marker='o', label="Ideal Cycle")
    plt.plot(df_real["pressure_ratio"], df_real["W_net"], marker='x', label="Real Cycle")
    plt.xlabel("Pressure Ratio")
    plt.ylabel("Net Work Output (W_net) (J/kg)")
    plt.title("Net Work Output vs Pressure Ratio (Ideal vs Real)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("Net_Work_vs_Pressure_Ratio_Comparison.png")
    plt.show()