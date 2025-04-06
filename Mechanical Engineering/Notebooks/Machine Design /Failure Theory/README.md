# Failure Theory

## Description
This Python notebook visualizes failure theories for mechanical engineering, focusing on Von Mises and Tresca criteria. It calculates the Von Mises stress ($$S_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$$) and plots yield envelopes for a material with yield strength $$S_yt$$. The code generates an ellipse for Von Mises ($$sigma_1,sigma_2$$) and a hexagon for Tresca, with stress points () overlaid to assess failure.

#Practical Uses
Design Validation: Check if stress states ($$sigma_1,sigma_2$$) lie within safe regions for ductile materials.
Material Selection: Compare failure envelopes against operating stresses to choose suitable materials.
Stress Analysis: Visualize how principal stresses interact under Von Mises and Tresca theories for component safety.

#Key Equations
Von Mises stress: $$S_v = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$$ 
Ellipse axes: $$a = \sqrt{2} S_{yt}, b = \sqrt{\frac{2}{3}} S_{yt}$$
