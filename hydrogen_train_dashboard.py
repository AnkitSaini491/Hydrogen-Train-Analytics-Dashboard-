import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# HYDROGEN TRAIN DATA
# ==========================================

train = {

    "Month":[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "Distance":[
        4200,4500,4700,5000,5300,5600,
        5900,6200,6500,6800,7100,7400
    ],

    "Hydrogen_Used":[
        850,880,910,950,980,1010,
        1050,1090,1130,1170,1210,1250
    ],

    "CO2_Saved":[
        180,195,210,230,245,260,
        280,300,320,340,360,380
    ],

    "Passengers":[
        4200,4500,4700,5100,5500,5900,
        6200,6500,6900,7200,7600,8000
    ],

    "Speed":[
        110,112,114,116,118,120,
        121,123,124,126,128,130
    ],

    "Efficiency":[
        82,83,84,85,86,87,
        88,89,90,91,92,93
    ],

    "Maintenance":[
        15000,14800,14500,14300,14100,13900,
        13700,13500,13300,13100,12900,12700
    ]
}

df = pd.DataFrame(train)

# ==========================================
# KPI VALUES
# ==========================================

total_distance = df["Distance"].sum()

total_hydrogen = df["Hydrogen_Used"].sum()

total_co2 = df["CO2_Saved"].sum()

total_passengers = df["Passengers"].sum()

avg_speed = df["Speed"].mean()

avg_efficiency = df["Efficiency"].mean()

# ==========================================
# DASHBOARD STYLE
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20,12))

fig.patch.set_facecolor("#0f172a")

fig.suptitle(
    "HYDROGEN TRAIN ANALYTICS DASHBOARD",
    fontsize=28,
    fontweight="bold",
    color="white"
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
    0.02,0.90,
    f"Distance\n{total_distance:,} km",
    fontsize=14,
    bbox=dict(facecolor="#2563eb",boxstyle="round,pad=0.8")
)

plt.figtext(
    0.18,0.90,
    f"Hydrogen\n{total_hydrogen:,} kg",
    fontsize=14,
    bbox=dict(facecolor="#0ea5e9",boxstyle="round,pad=0.8")
)

plt.figtext(
    0.35,0.90,
    f"CO₂ Saved\n{total_co2:,} Tons",
    fontsize=14,
    bbox=dict(facecolor="#16a34a",boxstyle="round,pad=0.8")
)

plt.figtext(
    0.52,0.90,
    f"Passengers\n{total_passengers:,}",
    fontsize=14,
    bbox=dict(facecolor="#f59e0b",boxstyle="round,pad=0.8")
)

plt.figtext(
    0.69,0.90,
    f"Avg Speed\n{avg_speed:.1f} km/h",
    fontsize=14,
    bbox=dict(facecolor="#9333ea",boxstyle="round,pad=0.8")
)

plt.figtext(
    0.85,0.90,
    f"Efficiency\n{avg_efficiency:.1f}%",
    fontsize=14,
    bbox=dict(facecolor="#dc2626",boxstyle="round,pad=0.8")
)

# ==========================================
# CHART 1 - DISTANCE TREND
# ==========================================

ax1 = plt.subplot(3,2,1)

ax1.plot(
    df["Month"],
    df["Distance"],
    marker="o",
    linewidth=3,
    color="cyan"
)

ax1.fill_between(
    df["Month"],
    df["Distance"],
    color="cyan",
    alpha=0.30
)

ax1.set_title("Monthly Distance Covered")
ax1.set_ylabel("Distance (km)")
ax1.grid(alpha=0.3)
ax1.tick_params(axis="x", rotation=45)

# ==========================================
# CHART 2 - HYDROGEN FUEL CONSUMPTION
# ==========================================

ax2 = plt.subplot(3,2,2)

ax2.plot(
    df["Month"],
    df["Hydrogen_Used"],
    marker="o",
    linewidth=3,
    color="deepskyblue"
)

ax2.fill_between(
    df["Month"],
    df["Hydrogen_Used"],
    color="deepskyblue",
    alpha=0.30
)

ax2.set_title("Hydrogen Fuel Consumption")
ax2.set_ylabel("Hydrogen (kg)")
ax2.grid(alpha=0.3)
ax2.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 3 - CO₂ EMISSIONS SAVED
# ==========================================

ax3 = plt.subplot(3,2,3)

ax3.bar(
    df["Month"],
    df["CO2_Saved"],
    color="limegreen"
)

ax3.set_title("CO₂ Emissions Saved")
ax3.set_ylabel("CO₂ Saved (Tons)")
ax3.grid(alpha=0.3)
ax3.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 4 - PASSENGER GROWTH
# ==========================================

ax4 = plt.subplot(3,2,4)

ax4.plot(
    df["Month"],
    df["Passengers"],
    marker="o",
    linewidth=3,
    color="gold"
)

ax4.fill_between(
    df["Month"],
    df["Passengers"],
    color="gold",
    alpha=0.30
)

ax4.set_title("Passenger Growth")
ax4.set_ylabel("Passengers")
ax4.grid(alpha=0.3)
ax4.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 5 - ENERGY EFFICIENCY
# ==========================================

ax5 = plt.subplot(3,2,5)

ax5.plot(
    df["Month"],
    df["Efficiency"],
    marker="o",
    linewidth=3,
    color="orange"
)

ax5.fill_between(
    df["Month"],
    df["Efficiency"],
    color="orange",
    alpha=0.30
)

ax5.set_title("Energy Efficiency")
ax5.set_ylabel("Efficiency (%)")
ax5.grid(alpha=0.3)
ax5.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 6 - MAINTENANCE COST
# ==========================================

ax6 = plt.subplot(3,2,6)

ax6.bar(
    df["Month"],
    df["Maintenance"],
    color="tomato"
)

ax6.set_title("Maintenance Cost")
ax6.set_ylabel("Cost ($)")
ax6.grid(alpha=0.3)
ax6.tick_params(axis="x", rotation=45)

plt.tight_layout(rect=[0,0,1,0.88])

# ==========================================
# CHART 7 - TRAIN SPEED TREND
# ==========================================

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.plot(
    df["Month"],
    df["Speed"],
    marker="o",
    linewidth=3,
    color="cyan"
)

plt.fill_between(
    df["Month"],
    df["Speed"],
    color="cyan",
    alpha=0.30
)

plt.title("Average Train Speed Trend")
plt.xlabel("Month")
plt.ylabel("Speed (km/h)")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 8 - ROUTE PERFORMANCE
# ==========================================

route = pd.DataFrame({

    "Route":[
        "Delhi-Chandigarh",
        "Delhi-Jaipur",
        "Mumbai-Pune",
        "Ahmedabad-Surat",
        "Chennai-Bengaluru"
    ],

    "Performance":[
        96,
        94,
        92,
        95,
        93
    ]
})

plt.figure(figsize=(9,5))
plt.style.use("dark_background")

plt.bar(
    route["Route"],
    route["Performance"],
    color="limegreen"
)

plt.title("Route Performance")
plt.ylabel("Performance (%)")
plt.xticks(rotation=15)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# CHART 9 - PASSENGER DISTRIBUTION
# ==========================================

plt.figure(figsize=(7,7))
plt.style.use("dark_background")

labels = [
    "Business",
    "Regular",
    "Tourists",
    "Students"
]

sizes = [
    30,
    40,
    18,
    12
]

colors = [
    "#3498db",
    "#2ecc71",
    "#f39c12",
    "#9b59b6"
]

plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Passenger Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# CHART 10 - DISTANCE VS HYDROGEN
# ==========================================

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.scatter(
    df["Distance"],
    df["Hydrogen_Used"],
    s=120,
    color="red"
)

for i in range(len(df)):
    plt.text(
        df["Distance"][i] + 30,
        df["Hydrogen_Used"][i],
        df["Month"][i],
        fontsize=9
    )

plt.title("Distance vs Hydrogen Consumption")
plt.xlabel("Distance (km)")
plt.ylabel("Hydrogen Used (kg)")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# SUMMARY REPORT
# ==========================================

best_month = df.loc[df["Distance"].idxmax()]

print("="*65)
print("HYDROGEN TRAIN ANALYTICS SUMMARY")
print("="*65)

print(f"Total Distance Covered : {total_distance:,} km")
print(f"Hydrogen Consumed      : {total_hydrogen:,} kg")
print(f"CO₂ Emissions Saved    : {total_co2:,} Tons")
print(f"Total Passengers       : {total_passengers:,}")
print(f"Average Speed          : {avg_speed:.2f} km/h")
print(f"Energy Efficiency      : {avg_efficiency:.2f}%")

print(f"\nBest Performing Month : {best_month['Month']}")
print(f"Distance Covered      : {best_month['Distance']} km")

print("="*65)


# ==========================================
# SAVE DASHBOARD
# ==========================================

fig.savefig(
    "hydrogen_train_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard saved as hydrogen_train_dashboard.png")


# ==========================================
# PROJECT DETAILS
# ==========================================

print("\nProject Name : Hydrogen Train Analytics Dashboard")
print("Technology   : Python | Pandas | Matplotlib")
print("Domain       : Transportation & Sustainability")
print("Status       : Dashboard Generated Successfully")


# ==========================================
# FOOTER
# ==========================================

plt.figtext(
    0.28,
    0.02,
    "Developed using Python | Pandas | Matplotlib",
    fontsize=11,
    color="white"
)

plt.show()
