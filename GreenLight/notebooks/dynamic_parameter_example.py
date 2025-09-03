import greenlight
import matplotlib.pyplot as plt

# 1. Define a callback function for dynamic parameter updates.
# This function acts as a thermostat for the greenhouse.
def thermostat_callback(t, current_vars):
    """
    Dynamically adjusts the heating setpoint based on air temperature.

    Args:
        t (float): The current simulation time in seconds.
        current_vars (dict): A dictionary of all current model variables.
                             This can be modified in-place by the callback.
    """
    # If the air temperature drops below 18°C, turn heating on.
    if current_vars['tAir'] < 18:
        current_vars['uBoil'] = 1
        current_vars['uBoilGro'] = 1
    # If the air temperature rises above 22°C, turn heating off.
    elif current_vars['tAir'] > 22:
        current_vars['uBoil'] = 0
        current_vars['uBoilGro'] = 0

# 2. Initialize the GreenLight model.
# We pass our `thermostat_callback` function during initialization.
# We also use an absolute path for `base_path`.
import os
base_path = '/mnt/c/학업/대전과학고 2-2/YSC/GreenLight/models/katzin_2021/definition'
model = greenlight.GreenLight(
    input_prompt='main_katzin_2021.json',
    base_path=base_path,
    param_callback=thermostat_callback
)

# 3. Load the model definitions and run the simulation.
model.load()
model.solve()

# 4. Plot the results to visualize the effect of the callback.
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot the greenhouse air temperature on the primary y-axis.
color = 'tab:blue'
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Air Temperature (°C)', color=color)
ax1.plot(model.full_sol['Time'] / 3600, model.full_sol['tAir'], color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

# Create a second y-axis to show the heating setpoint changes.
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Heating Control Signal', color=color)
ax2.plot(model.full_sol['Time'] / 3600, model.full_sol['uBoil'], color=color, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Greenhouse Temperature Control Using a Dynamic Callback')
fig.tight_layout()
plt.show()
