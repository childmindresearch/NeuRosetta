Sure, let's see a short minimal example for Artifact Detection and Correction in these popular neuroimaging packages. Please understand that most of these packages may not provide a standalone solution to artifact detection and correction. 

These codes are for demonstration purposes -- contexts in which these codes were used, necessary assumptions, and detailed explanations are not shown.

**AFNI**
```bash
3dDespike -prefix output.nii -ignore 5 input.nii
```

**ANTs**
ANTs doesn't specifically have artifact detection and correction but you can use N4 for bias field correction.
```bash
N4BiasFieldCorrection -d 3 -i input.nii -o output.nii 
```

**FSL**
```bash
fsl_motion_outliers -i input.nii -o output.nii -s output_metric.txt
```

**FreeSurfer**
```bash
mri_robust_template --mov input1.nii input2.nii --template output.nii
```

**MRtrix**
```bash
dwidenoise input.nii output.nii
```

**R**
There is no direct function for artifact detection and correction in R. Instead, fslr package can be used to incorporate FSL's functionalities into R. Here is an example of doing this with fslr:

```r
library(fslr)
img <- readnii("input.nii")
img_despike <- fsl_motion_outliers(img)
```

**Workbench Command**
```
wb_command -cifti-outlier-replace -cifti input.dscalar.nii -replace NAN -column 1 
```

**pure Python**
Nilearn package in python can be used for artifact detection and correction.
```python
from nilearn.image import clean_img
cleaned_img = clean_img("input.nii", standardize=True, detrend=True)
```

**SPM (via a MATLAB script)**
```matlab
spm('defaults', 'FMRI');
spm_jobman('initcfg');

matlabbatch{1}.spm.spatial.preproc.despike.data = {'/path/to/input.nii,1'};
matlabbatch{1}.spm.spatial.preproc.despike.mask = {'/path/to/mask.img,1'};

spm('run', matlabbatch);
```
Since SPM doesn't directly do artifact correction, we use here preprocessing method. Also, a path to a mask image is needed.

Please remember that artifact detection and correction are complex tasks with many potential strategies. The code above provides very basic examples of typical procedures. Each of these software packages provides many options that can be adjusted to suit specific experimental conditions and research questions.