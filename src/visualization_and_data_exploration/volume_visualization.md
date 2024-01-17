[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/visualization_and_data_exploration/volume_visualization.md)
# Volume Visualization

here are minimal examples of volume visualization using different packages:

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
# Display an image
afni anat+orig
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```bash
# Visualize the anatomic image
antsSliceRegularizedIsotropicWavelet ants_anatomic.nii
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```bash
# Visualize the anatomic image
fslview anat.nii.gz
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
# Displaying the subject's brain with tksurfer
tksurfer subject lh inflated
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```bash
# Visualize the anatomic image
mrview anat.mif
```

## <img src="../icons/r.png" height="24px" /> R
```r
# Using neurobase package to view brain image
library(neurobase)
ortho2(oro.nifti::readNIfTI("anat.nii.gz"))
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
# View surfaces and volumes
wb_command -volume-view anat.nii.gz
```

## <img src="../icons/python.png" height="24px" /> Python
```python
from nilearn import plotting

# Visualize the anatomic image
plotting.plot_img("anat.nii.gz")
plotting.show()
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
% Load MRI data
V = spm_vol('anat.nii');
img = spm_read_vols(V);

% Display image
imagesc(img(:,:,50)); axis off; colormap gray;
```
Please replace "anat.nii", "anat.nii.gz", "anat+orig" and "anat.mif" with your actual file paths.