Sure, here are minimal examples of volume visualization using different packages:

**AFNI**
```bash
# Display an image
afni anat+orig
```

**ANTs**
```bash
# Visualize the anatomic image
antsSliceRegularizedIsotropicWavelet ants_anatomic.nii
```

**FSL**
```bash
# Visualize the anatomic image
fslview anat.nii.gz
```

**FreeSurfer**
```bash
# Displaying the subject's brain with tksurfer
tksurfer subject lh inflated
```

**MRtrix**
```bash
# Visualize the anatomic image
mrview anat.mif
```

**R**
```r
# Using neurobase package to view brain image
library(neurobase)
ortho2(oro.nifti::readNIfTI("anat.nii.gz"))
```

**Workbench Command**
```bash
# View surfaces and volumes
wb_command -volume-view anat.nii.gz
```

**Pure Python (nilearn package)**
```python
from nilearn import plotting

# Visualize the anatomic image
plotting.plot_img("anat.nii.gz")
plotting.show()
```

**SPM (via a MATLAB script)**
```matlab
% Load MRI data
V = spm_vol('anat.nii');
img = spm_read_vols(V);

% Display image
imagesc(img(:,:,50)); axis off; colormap gray;
```
Please replace "anat.nii", "anat.nii.gz", "anat+orig" and "anat.mif" with your actual file paths.