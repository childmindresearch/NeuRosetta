I'm sorry, but I can't create scripts for all the platforms you listed because some of them, such as the Workbench command, do not support image registration directly. However, I can create scripts for some of the platforms. Here they are:

### AFNI
```bash
# AFNI Example
3dAllineate -base base_image.nii -input input_image.nii -prefix registered_image.nii -1Dfile translation.1D
```

### ANTs
```bash
# ANTs Example
antsRegistrationSyN.sh -d 3 -f fixed_image.nii -m moving_image.nii -o output_
```

### FSL
```bash
# FSL Example
flirt -in input_image.nii.gz -ref ref_image.nii.gz -omat out.mat -out output_image.nii.gz
```

### FreeSurfer
```bash
# FreeSurfer Example
bbregister --s subject --mov input_image.nii.gz --init-fsl --reg register.dat
```

### MRtrix
```bash
# MRtrix Example
mrregister fixed_image.nii.gz moving_image.nii.gz -transformed registered_image.nii.gz
```

### R (using ANTsR)
```R
# R ANTsR Example
library(ANTsR)
fixed_image <- antsImageRead('fixed_image.nii.gz')
moving_image <- antsImageRead('moving_image.nii.gz')
my_transformation <- antsRegistration(fixed_image, moving_image)
```

### Python (nipy)
```python
# Python Nipy Example
from nipy.algorithms.registration import HistogramRegistration
import nibabel as nib

fixed_image = nib.load('fixed_image.nii.gz')
moving_image = nib.load('moving_image.nii.gz')
registration = HistogramRegistration(moving_image, fixed_image)
transformed_image = registration.transform_image(moving_image)
nib.save(transformed_image, 'registered_image.nii.gz')
```

### SPM (via a MATLAB script)
```matlab
% SPM MATLAB Example
matlabbatch{1}.spm.spatial.coreg.estwrite.ref = {'fixed_image.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.source = {'moving_image.nii,1'};
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```
Please be sure to replace the placeholders (like 'fixed_image.nii.gz') with the actual paths to your data. These scripts may need further adjustments depending on the specific requirements of your data and analyses.