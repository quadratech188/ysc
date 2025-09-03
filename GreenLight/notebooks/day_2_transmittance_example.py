import greenlight
import os
import datetime

log_file_path = os.path.join(os.path.dirname(__file__), "callback_log.txt")
if os.path.exists(log_file_path):
    os.remove(log_file_path)

# 1. Define a callback function for dynamic parameter updates.
def transmittance_callback(t, current_vars):
    """
    Dynamically adjusts the transmittance of the greenhouse cover.

    Args:
        t (float): The current simulation time in seconds.
        current_vars (dict): A dictionary of all current model variables.
                             This can be modified in-place by the callback.
    """
    with open(log_file_path, "a") as f:
        f.write(f"Current simulation time: {t}\n")
    # After 2 days, set the transmittance of the cover to 0.
    if t >= 172800:
        with open(log_file_path, "a") as f:
            f.write("Setting transmittance to 0\n")
        current_vars['tauCovPar'] = 0

# 2. Initialize the GreenLight model.
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
model_file = os.path.join("models", "katzin_2021", "definition", "main_katzin_2021.json")

options = {
    "options": {
        "t_end": str(5 * 24 * 3600),
        "solving_method": "solve_ivp"
    }
}

input_prompt = [model_file, options]

model = greenlight.GreenLight(
    base_path=base_path,
    input_prompt=input_prompt,
    param_callback=transmittance_callback
)

# 4. Load the model definitions and run the simulation.
model.load()
model.solve()

