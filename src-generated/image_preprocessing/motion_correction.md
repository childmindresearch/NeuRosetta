I'm an AI and I can't execute these scripts for you, but I can certainly provide some simplified examples.

1. AFNI:

This is how you would do linear motion correction in AFNI using 3dvolreg:

```bash
3dvolreg -verbose -Fourier -zpad 1 -prefix output.nii.gz -base 'input.nii.gz[0]' input.nii.gz
```

2. ANTs:
```bash
antsMotionCorr -d 3 -a input.nii.gz -o output.nii.gz
```

3. FSL:

This is an example of a motion correction script in FSL using MCFLIRT:
```bash
mcflirt -in input.nii.gz -out output.nii.gz -plots
```

4. FreeSurfer:
```bash
mri_motion_correct.fsl --i input.nii.gz --o output.nii.gz --use-gradient
```

5. MRtrix:
```bash
mrregister input.nii.gz -type rigid -datatype float32 - - | mrtransform input.nii.gz -linear - -template input.nii.gz output.nii.gz
```

6. R:

Motion correction in R would typically involve preprocessing steps using specific imaging packages like fmri or oro.nifti. Here is a very rough pseudo-code type example:
```R
library(fslr)
data <- readNIfTI("input.nii.gz", reorient = FALSE)
output <- fsl_motion_correct(data)
```

7. Workbench Command:
```bash
wb_command -volume-mc input.nii.gz output.nii.gz -method FLIRT
```

8. Pure Python (using Nipy):

```python
from nipy.algorithms.registration import register, aff2rigid, resample
from nipy import load_image, save_image

moving_img = load_image("input.nii.gz")
static_img = load_image("reference.nii.gz")
affine_map = register(static_img, moving_img)
T = aff2rigid(affine_map)
resampled = resample(moving_img, static_img.coordmap, T.inv(), static_img.shape)
save_image(resampled, "output.nii.gz")
```

9. SPM (via a MATLAB script):
```MATLAB
spm('defaults', 'fmri');
spm_jobman('initcfg');

matlabbatch{1}.spm.spatial.realign.estwrite.data{1} = {'/path/to/scan/*'};
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.sep = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.fwhm = 5;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.rtm = 1;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.interp = 2;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.weight = '';

spm_jobman('run', matlabbatch);
```

Please note that these scripts are representative and should be modified to adapt to specific use-cases. The data paths and parameters used in the scripts might need to be changed depending on your data and its specifications. Additionally, make sure all dependencies are installed and paths are set appropriately.