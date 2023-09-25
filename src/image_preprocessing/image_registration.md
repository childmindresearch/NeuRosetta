# Image Registration

I can't create scripts for all the platforms you listed because some of them, such as the Workbench command, do not support image registration directly. However, I can create scripts for some of the platforms. Here they are:

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
## <img src="../icons/afni.png" height="24px" /> AFNI
3dAllineate -base base_image.nii -input input_image.nii -prefix registered_image.nii -1Dfile translation.1D
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```bash
## <img src="../icons/ants.png" height="24px" /> ANTs
antsRegistrationSyN.sh -d 3 -f fixed_image.nii -m moving_image.nii -o output_
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```bash
## <img src="../icons/fsl.png" height="24px" /> FSL
flirt -in input_image.nii.gz -ref ref_image.nii.gz -omat out.mat -out output_image.nii.gz
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
bbregister --s subject --mov input_image.nii.gz --init-fsl --reg register.dat
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```bash
## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
mrregister fixed_image.nii.gz moving_image.nii.gz -transformed registered_image.nii.gz
```

## <img src="../icons/r.png" height="24px" /> R
```R
## <img src="../icons/r.png" height="24px" /> R
library(ANTsR)
fixed_image <- antsImageRead('fixed_image.nii.gz')
moving_image <- antsImageRead('moving_image.nii.gz')
my_transformation <- antsRegistration(fixed_image, moving_image)
```

## <img src="../icons/python.png" height="24px" /> Python
```python
## <img src="../icons/python.png" height="24px" /> Python
from nipy.algorithms.registration import HistogramRegistration
import nibabel as nib

fixed_image = nib.load('fixed_image.nii.gz')
moving_image = nib.load('moving_image.nii.gz')
registration = HistogramRegistration(moving_image, fixed_image)
transformed_image = registration.transform_image(moving_image)
nib.save(transformed_image, 'registered_image.nii.gz')
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
% SPM MATLAB Example
matlabbatch{1}.spm.spatial.coreg.estwrite.ref = {'fixed_image.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.source = {'moving_image.nii,1'};
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```
Please be sure to replace the placeholders (like 'fixed_image.nii.gz') with the actual paths to your data. These scripts may need further adjustments depending on the specific requirements of your data and analyses.