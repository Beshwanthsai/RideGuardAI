import random
import pandas as pd

rides = []

for i in range(10000):

    estimated_fare = random.randint(100, 1000)

    estimated_distance = round(
        random.uniform(1, 20),
        2
    )

    otp_verified = random.choice(
        [True, True, True, False]
    )

    fraud = random.choice(
        [0, 0, 0, 1]
    )

    if fraud:

        actual_fare = round(
            estimated_fare
            * random.uniform(1.4, 2.2),
            2
        )

        actual_distance = round(
            estimated_distance
            * random.uniform(1.3, 2),
            2
        )

        complaint = 1

    else:

        actual_fare = round(
            estimated_fare
            * random.uniform(0.9, 1.15),
            2
        )

        actual_distance = round(
            estimated_distance
            * random.uniform(0.95, 1.1),
            2
        )

        complaint = random.choice(
            [0, 0, 0, 1]
        )

    rides.append(
        {
            "ride_id": f"RIDE{i}",
            "driver_id": f"DRV{random.randint(1,100)}",
            "estimated_fare": estimated_fare,
            "actual_fare": actual_fare,
            "estimated_distance": estimated_distance,
            "actual_distance": actual_distance,
            "otp_verified": otp_verified,
            "complaint": complaint,
            "fraud_label": fraud,
        }
    )

df = pd.DataFrame(rides)

df.to_csv(
    "data/rides.csv",
    index=False
)

print(
    "Dataset Generated Successfully"
)