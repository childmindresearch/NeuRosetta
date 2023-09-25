# Diffeomorphic Spatial Transformation

Here are examples of scripts that perform the Diffeomorphic Spatial Transformation task using different neuroimaging and scientific computing software. Note that the syntax and structure can be different for each software. 

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
3dAllineate -1Dmatrix_apply diffeo.example.aff12.1D -base template.nii -source example.nii -prefix example_diffeo_afni.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```bash
antsRegistration --dimensionality 3 --float 0 --output [ diffeo , diffeoWarped.nii.gz ] --interpolation Linear --use-histogram-matching 0 --winsorize-image-intensities [ 0.005, 0.995 ] --initial-moving-transform [ template.nii.gz , example.nii.gz , 1 ] --transform SyN[ 0.1, 3, 0 ] --metric CC[ template.nii.gz , example.nii.gz , 1, 4 ] --convergence [ 100x100x70x50x20 , 1e-6, 10 ] --shrink-factors 8x4x2x1x1 --smoothing-sigmas 3x2x1x0x0vox
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```bash
fnirt --in=example.nii --ref=template.nii --iout=example_diffeo_fsl.nii --warpres=10,10,10
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
mri_robust_register --mov example.nii --dst template.nii --lta diffeo.lta --mapmov example_diffeo_freesurfer.nii
```
  
## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```bash
Notably, MRtrix does not include a standalone tool for performing diffeomorphic registration.

## <img src="../icons/r.png" height="24px" /> R
```R
library(ANTsR)
fixed <- antsImageRead("template.nii")
moving <- antsImageRead("example.nii")
mytx <- antsRegistration(fixed, moving, typeofTransform = "SyN")
WarpedImage <- antsApplyTransforms(fixed, moving, mytx$forwardTransforms)
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
matlabbatch{1}.spm.spatial.normalise.estwrite.subj.vol = {'example.nii'};
matlabbatch{1}.spm.spatial.normalise.estwrite.subj.resample = {'example.nii'};
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.biasreg = 0.0001;
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.biasfwhm = 60;
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.tpm = {'TPM.nii'};
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.affreg = 'mni';
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.reg = [0 0.001 0.5 0.05 0.2];
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.fwhm = 0;
matlabbatch{1}.spm.spatial.normalise.estwrite.eoptions.samp = 3;
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.bb = [-78 -112 -70; 78 76 85];
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.vox = [2 2 2];
matlabbatch{1}.spm.spatial.normalise.estwrite.woptions.interp = 4;
spm_jobman('run', matlabbatch);
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
wb_command -volume-affine-resample example.nii diffeo.warpfield.nii TEMPLATE VolumeAffineResampleMethod::CUBIC example_diffeo_wb.nii -flirt template.nii example.nii
```

## <img src="../icons/python.png" height="24px" /> Python
```python
import ants
fixed = ants.image_read("template.nii")
moving = ants.image_read("example.nii")
mytx = ants.registration(fixed, moving, 'SyN')
warped_moving = ants.apply_transforms(fixed, moving, mytx['fwdtransforms'])
```
It's important to note that some platforms do not have built-in commands to perform Diffeomorphic Spatial Transformation like MRtrix. Similarly, some of these scripts like those for PYTHON and MATLAB (SPM) need an environment in which to be executed.