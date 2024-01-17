[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/visualization_and_data_exploration/surface_visualization.md)
# Surface Visualization

here are some minimal example scripts for surface visualization in each mentioned tool:

1. **AFNI**:
```bash
## <img src="../icons/afni.png" height="24px" /> AFNI
suma -i example_surf.gii
```

2. **ANTs**:
*ANTs doesn't provide explicit surface visualization. Nevertheless, you can convert your data to a format that can be visualized using other tools with a script like this*:
```bash
# Convert a nifti Image to a surface
ImageMath 3 output.nii.gz ConvertToMesh input.nii.gz
```

3. **FSL**:
*FSL also doesn't provide explicit surface visualization, but you can view the data in a GUI tools*:
```bash
# Open a GUI viewer
fslview example_data.nii.gz -m ortho
```

4. **FreeSurfer**:
```bash
## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
freeview -f $SUBJECTS_DIR/freesurfer/subjects/subject/surf/lh.pial:color=255,0,0
```

5. **MRtrix**:
```bash
## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
mrview example_diffusion.mif -tractography.load example_tract.tck
```

6. **R**:
*R doesn't provide explicit surface visualization for brain imaging, but you can utilize additional libraries*:
```R
# Load library
library(rgl)
# Generate data
x <- rnorm(10000)
y <- rnorm(10000)
z <- rnorm(10000)
# Plot points cloud
plot3d(x, y, z)
```

7. **Workbench Command**:
```bash
# View a HCP MMP 1.0 surface
wb_view -surface $HCP_REFERENCE/MNINonLinear/fsaverage_LR32k/subject.L.midthickness.32k_fs_LR.surf.gii
```

8. **pure Python**:
*You can use matplotlib for 3D plotting*:
```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs)
plt.show()
```
*Or `nilearn` for brain imaging*:
```python
from nilearn import plotting
plotting.plot_stat_map("/path/to/my_stat_map.nii.gz")
plotting.show()
```

9. **SPM (via a MATLAB script)**:
```MATLAB
% Load data
V = spm_vol('example.nii');
% Plot surface
spm_surface(V);
```

Please note that these scripts are very simplified and you might need to adjust them according to your actual data and processing chain. Also, some libraries require pre-processing and post-processing to achieve meaningful results.