import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

days = 60
lines = ["Line_A", "Line_B", "Line_C"]
shifts = ["Shift_1", "Shift_2", "Shift_3"]

data = []

start_date = datetime(2024, 1, 1)

for i in range(days):
    for line in lines:
        for shift in shifts:
            units = np.random.randint(400, 800)
            defects = np.random.randint(5, 40)
            downtime = np.random.randint(10, 120)
            inventory = np.random.randint(1000, 5000)

            data.append([
                start_date + timedelta(days=i),
                line,
                shift,
                units,
                defects,
                downtime,
                inventory
            ])

df = pd.DataFrame(data, columns=[
    "Date",
    "Production_Line",
    "Shift",
    "Units_Produced",
    "Defective_Units",
    "Downtime_Minutes",
    "Inventory_Level"
])

df.to_csv("data/production_data.csv", index=False)

print("Manufacturing dataset created.")
