# Piezoelectric Guidewire FEA Optimization

Python-based finite-element data analysis and design-space optimization
developed during undergraduate research at Stevens Institute of Technology.

## Project Overview

This project investigates a multilayer piezoelectric bending actuator for
potential use in an active thrombectomy guidewire.

Fabrication cool-down can introduce residual stresses that cause the
multilayer actuator to bend before activation. The objective of the research
was to identify design parameters that minimize this unwanted deformation
while maintaining a crack-free piezoelectric structure.

## Computational Approach

Finite-element models were created using HyperMesh and solved using Radioss.

The design study varied two primary parameters:

- Si3N4 residual stress
- Si3N4 layer thickness

Python was used to analyze the resulting finite-element simulation data and
search the design space for combinations associated with minimal
out-of-plane deformation.

The analysis uses interpolation to construct continuous response surfaces
from discrete simulation results and examines zero-displacement contours
to identify candidate design conditions.

## Technologies

- Python
- NumPy
- pandas
- SciPy
- Matplotlib
- HyperMesh
- Radioss
- SolidWorks
- Finite Element Analysis (FEA)
- Numerical data analysis

## Repository Contents

### `find_zero.py`

Analyzes finite-element simulation results across residual-stress and
layer-thickness parameters.

The script:

1. Loads simulation results into a pandas DataFrame.
2. Constructs a two-dimensional parameter grid.
3. Uses SciPy interpolation to estimate responses between simulated designs.
4. Generates zero-level contours for displacement metrics.
5. Searches the contours for candidate intersections corresponding to
   near-zero deformation.

## Research Results

The broader finite-element study found that residual stress strongly
controls the direction of actuator bending and that changing the Si3N4
layer thickness shifts the flat-design condition.

At a Si3N4 thickness of 0.5 µm, the finite-element study identified a
near-flat configuration around -787.5 MPa residual stress, with a peak
out-of-plane displacement magnitude of approximately 0.032 mm.

A separate interpolated design-space analysis was also used to investigate
conditions where multiple displacement measures approach zero.

## Research Context

This work was conducted in the Department of Mechanical Engineering at
Stevens Institute of Technology under the guidance of Prof. Yong Shi, with
Dr. Sundeep Mangla, M.D. serving as industrial mentor.

The project explores computational design methods for a multilayer
piezoelectric actuator intended for future active-guidewire applications.

## Future Work

Future development includes combining the optimized flat, crack-free
configuration with piezoelectric activation in a two-stage
cool-down/activation simulation and eventual device fabrication.

## Author

Parker Robles  
Biomedical Engineering | Computer Science Minor  
Stevens Institute of Technology
