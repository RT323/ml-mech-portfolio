import numpy as np
import pandas as pd

def generate_dataset(n: int = 2000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    k = rng.uniform(0.1, 400.0, size=n)          
    L = rng.uniform(0.001, 0.2, size=n)          
    h1 = rng.uniform(5.0, 200.0, size=n)         
    h2 = rng.uniform(5.0, 200.0, size=n)
    Tinf1 = rng.uniform(20.0, 200.0, size=n)     
    Tinf2 = rng.uniform(-10.0, 100.0, size=n)   

    swap_mask = Tinf2 > Tinf1
    Tinf1[swap_mask], Tinf2[swap_mask] = Tinf2[swap_mask], Tinf1[swap_mask]

    R_total = (1.0 / h1) + (L / k) + (1.0 / h2)
    q_flux = (Tinf1 - Tinf2) / R_total           

    df = pd.DataFrame({
        "k_W_mK": k,
        "L_m": L,
        "h1_W_m2K": h1,
        "h2_W_m2K": h2,
        "Tinf1_C": Tinf1,
        "Tinf2_C": Tinf2,
        "q_flux_W_m2": q_flux
    })
    return df

if __name__ == "__main__":
    df = generate_dataset()
    df.to_csv("../data/raw/heat_transfer_dataset.csv", index=False)
    print("Saved dataset to data/raw/heat_transfer_dataset.csv")