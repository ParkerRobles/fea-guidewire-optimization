import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import io

# 1. Load the data
data_str = """Run	MPa	SN_thick	Si3N4_midZ	maxZ(mm)	maxMag(mm)	Full cool	Status
1	0	5.000e-04	1.5000e-03	2.6592e-01	2.7037e-01	yes	ok
2	300	5.000e-04	1.5000e-03	3.6902e-01	3.8067e-01	yes	ok
3	-300	5.000e-04	1.5000e-03	1.5128e-01	1.5234e-01	yes	ok
4	-600	5.000e-04	1.5000e-03	5.6672e-02	5.6921e-02	yes	ok
5	-900	5.000e-04	1.5000e-03	-5.1036e-02	-5.9119e-02	yes	ok
6	-1000	5.000e-04	1.5000e-03	-6.8920e-02	-7.9554e-02	yes	ok
7	-900	6.500e-04	1.5750e-03	-1.3574e-01	-1.4710e-01	yes	ok
8	-900	3.500e-04	1.4250e-03	-1.0931e-01	-1.1059e-01	yes	ok
9	-750	5.000e-04	1.5000e-03	3.4661e-02	3.4743e-02	yes	ok
10	-750	5.750e-04	1.5375e-03	6.9644e-02	7.4597e-02	yes	ok
11	-750	4.250e-04	1.4625e-03	8.0424e-02	8.1072e-02	yes	ok
12	-675	5.000e-04	1.5000e-03	4.3461e-02	4.3602e-02	yes	ok
13	-825	5.000e-04	1.5000e-03	-3.6407e-02	-4.2950e-02	yes	ok
14	-750	5.375e-04	1.5188e-03	4.5435e-02	5.0159e-02	yes	ok
15	-750	4.625e-04	1.4812e-03	5.6606e-02	5.6896e-02	yes	ok
16	-712	5.000e-04	1.5000e-03	3.8382e-02	3.8486e-02	yes	ok
17	-788	5.000e-04	1.5000e-03	3.1933e-02	3.4325e-02	yes	ok
18	-788	5.188e-04	1.5094e-03	4.1404e-02	4.6960e-02	yes	ok
19	-788	4.813e-04	1.4906e-03	4.1098e-02	4.1222e-02	yes	ok
20	-769	5.000e-04	1.5000e-03	3.2869e-02	3.2947e-02	yes	ok
21	-806	5.000e-04	1.5000e-03	-3.2840e-02	-3.9015e-02	yes	ok
22	-788	5.094e-04	1.5047e-03	3.4988e-02	4.0634e-02	yes	ok
23	-788	4.906e-04	1.4953e-03	3.6223e-02	3.6317e-02	yes	ok"""

df = pd.read_csv(io.StringIO(data_str), sep='\t')
x, y = df['MPa'].values, df['SN_thick'].values

# Create grid
xi = np.linspace(x.min(), x.max(), 500)
yi = np.linspace(y.min(), y.max(), 500)
X, Y = np.meshgrid(xi, yi)

# Interpolate both targets
Z_z = griddata((x, y), df['maxZ(mm)'].values, (X, Y), method='cubic')
Z_mag = griddata((x, y), df['maxMag(mm)'].values, (X, Y), method='cubic')

# Get contours
fig, ax = plt.subplots()
c1 = ax.contour(X, Y, Z_z, levels=[0.0])
c2 = ax.contour(X, Y, Z_mag, levels=[0.0])

paths1 = c1.allsegs[0]
paths2 = c2.allsegs[0]

print("\nSearching for intersection where Z=0 and Mag=0:")
print("===============================================")

found = False
# Compare paths to find points that are very close to each other
if len(paths1) > 0 and len(paths2) > 0:
    p1 = paths1[0]
    p2 = paths2[0]
    
    # Calculate distance matrix (simple search for nearest points)
    for pt1 in p1[::10]: # Sample every 10th point for speed
        for pt2 in p2[::10]:
            dist = np.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
            if dist < 5.0: # Threshold for "intersection"
                print(f"Intersection found near:")
                print(f"  MPa: {pt1[0]:.2f}")
                print(f"  SN_thick: {pt1[1]:.6e}")
                found = True
                break
        if found: break

if not found:
    print("No direct intersection found. The zero-lines may not cross in this range.")

plt.close(fig)