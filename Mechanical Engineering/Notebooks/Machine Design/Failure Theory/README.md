# Failure Theory

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kelinio/Snakepit/blob/main/Mechanical%20Engineering/Notebooks/Machine%20Design/Failure%20Theory/Failure%20Theory.ipynb)

## Description

This notebook visualises two yield criteria for ductile materials — **Von Mises** and **Tresca** — in principal stress space. It computes the Von Mises stress $S_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$ and plots the yield envelope for a material of yield strength $S_{yt}$: an ellipse for Von Mises and a hexagon for Tresca. Stress points $(\sigma_1, \sigma_2)$ are overlaid so you can see at a glance whether a given stress state falls inside the safe region.

## Practical uses

- **Design validation** — check whether a stress state $(\sigma_1, \sigma_2)$ lies inside the safe envelope.
- **Material selection** — compare failure envelopes against operating stresses to pick a suitable material.
- **Stress analysis** — see how the two criteria differ, and where Tresca is the more conservative of the two.

## Key equations

Von Mises stress (plane stress):

$$S_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$$

Semi-axes of the Von Mises ellipse:

$$a = \sqrt{2}\, S_{yt}, \qquad b = \sqrt{\tfrac{2}{3}}\, S_{yt}$$

## Running it

From the repository root:

```bash
pip install -r requirements.txt
jupyter lab "Mechanical Engineering/Notebooks/Machine Design/Failure Theory/Failure Theory.ipynb"
```
