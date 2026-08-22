# Mechanical Engineering

Engineering calculations and physics simulations written up as notebooks, using NumPy for the maths and Matplotlib for the plots. These come out of my mechanical engineering background — problems I already knew how to solve on paper, rebuilt in Python.

## What's here

| Notebook | What it does |
|---|---|
| [Projectile Motion](./Notebooks/Machine%20Design/Projectile%20Motion/) | Simulates and plots projectile trajectories for two launch angles under gravity, neglecting drag. |
| [Failure Theory](./Notebooks/Machine%20Design/Failure%20Theory/) | Plots Von Mises and Tresca yield envelopes in principal stress space and overlays stress points to check them against the safe region. |

Each folder has its own README with the description, the governing equations, and the practical uses.

## Running these

From the repository root:

```bash
pip install -r requirements.txt
jupyter lab
```

These are pure NumPy and Matplotlib — no GPU, no downloads, no dataset. They run anywhere in a few seconds.
