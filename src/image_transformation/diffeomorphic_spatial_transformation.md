# Diffeomorphic Spatial Transformation

here's a brief overview with minimum examples. Please note that the specific commands and usage may vary depending on the version of the software and the specific images or data you're working with.

```bash
# AFNI (https://afni.nimh.nih.gov)
3dQwarp -source source.nii -base target.nii -prefix transformed.nii

# ANTs - Advanced Normalization Tools (https://stnava.github.io/ANTs)
antsRegistrationSyN.sh -d 3 -f fixed.nii -m moving.nii -o transformed.nii

# FSL - FMRIB Software Library (https://fsl.fmrib.ox.ac.uk)
flirt -in moving.nii -ref fixed.nii -out transformed.nii -omat affine.mat
fnirt --in=moving.nii --aff=affine.mat --cout=nonlinear_transf --iout=transformed.nii --ref=fixed.nii

# FreeSurfer (https://surfer.nmr.mgh.harvard.edu)
mri_normalize -mprage -i moving.nii -o transformed.nii 

# MRtrix (https://mrtrix.readthedocs.io)
mrregister moving.mif fixed.mif -type diff -nl_warp warp.mif transformed.mif

# R (https://www.r-project.org) with 'ANTsR' package
library(ANTsR)
fixed = antsImageRead("fixed.nii")
moving = antsImageRead("moving.nii")
mytx = antsRegistration(fixed, moving, typeofTransform="SyN")
transformed = antsApplyTransforms(fixed, moving, mytx$fwdtransforms)

# Workbench Command (https://www.humanconnectome.org/software/connectome-workbench)
wb_command -volume-affine-resample moving.nii affine.mat fixed.nii CUBIC transformed.nii

## <img src="../../icons/python.png" height="24px" /> Python
import nibabel as nib
import numpy as np
from dipy.align.imwarp import SymmetricDiffeomorphicRegistration
from dipy.align.metrics import SSDMetric, CCMetric
mov_img = nib.load('moving.nii')
static_img = nib.load('fixed.nii')
sdr = SymmetricDiffeomorphicRegistration(metric=CCMetric(3),step_length=0.25, level_iters=[10], inv_iter=5)
warped_img = sdr.optimize(static_img, mov_img)
nib.save(warped_img, 'transformed.nii')
```

```matlab
% SPM (https://www.fil.ion.ucl.ac.uk/spm)
spm('defaults', 'PET');
matlabbatch{1}.spm.spatial.normalise.write.subj.def = {'moving.nii'};
matlabbatch{1}.spm.spatial.normalise.write.subj.resample = {'fixed.nii'};
matlabbatch{1}.spm.spatial.normalise.write.woptions.bb = [-78 -112 -70
                                                           78 76 85];
matlabbatch{1}.spm.spatial.normalise.write.woptions.vox = [2 2 2];
matlabbatch{1}.spm.spatial.normalise.write.woptions.interp = 4;
matlabbatch{1}.spm.spatial.normalise.write.woptions.prefix = 'w';
spm_jobman('run', matlabbatch);
```
Please, do replace 'fixed.nii' and 'moving.nii' in the commands above with your image files. Also, always check official software documentation for the proper usage instructions.