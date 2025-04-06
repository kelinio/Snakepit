# Projetile Motion

## Description
This Python notebook simulates projectile motion for two launch angles ($$\theta_1 = 45^\circ$$, $$\theta_2 = 30^\circ$$) with initial velocity $$u_0 = 40 \, \text{m/s}$$ under gravity $$g = 9.81 \, \text{m/s}^2$$. It calculates horizontal ($$s_x = u_x t$$) and vertical ($$s_y = u_y t - \frac{1}{2} g t^2$$) positions over time, plotting trajectories for each angle.

## Practical Uses
- Trajectory Analysis: Predict projectile paths for given launch angles and velocities.
- Optimization: Determine optimal angles for maximum range or height in engineering designs (e.g., ballistics, sports equipment).
- Education: Visualize the effect of launch angle on projectile motion for teaching purposes.

## Key Equations
- Horizontal velocity: $$u_x = u_0 \cos(\theta)$$  
- Vertical velocity: $$u_y = u_0 \sin(\theta)$$  
- Horizontal position: $$s_x = u_x t$$  
- Vertical position: $$s_y = u_y t - \frac{1}{2} g t^2$$  
- Total flight time: $$t_{total} = \frac{2 u_y}{g}$$  

![Projectile Trajectory](../Images/projectile_main.png)

