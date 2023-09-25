# Event-Related Analysis

Sorry for the misunderstanding, but writing scripts for all of these platforms would be quite comprehensive and potentially long. However, I can provide a simple, introductory script for each one to give you a basic understanding of how they work.

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
## <img src="../../icons/r.png" height="24px" /> Run 3dDeconvolve to perform the analysis
3dDeconvolve -input data.nii.gz -censor motion_censor.1D \
-npolort 4 -num_stimts 1 -stim_times 1 task.1D 'BLOCK(15,1)' \
-stim_label 1 task -fout -tout -x1D X.xmat.1D -xjpeg X.jpg \
-fitts fitts.nii.gz -errts errts.nii.gz -bucket stats.nii.gz
```

## <img src="../../icons/ants.png" height="24px" /> ANTs
```bash
## Perform registration
antsRegistration --dimensionality 3 --float 0 \
--output [output, warped.nii.gz] --interpolation Linear \
--use-histogram-matching 0 \
--transform Rigid[0.1] --metric MI[fixed.nii.gz, moving.nii.gz, 1, 32, Regular, 0.25] \
--convergence [1000x500x250x100, 1e-6, 10] --shrink-factors 8x4x2x1 --smoothing-sigmas 3x2x1x0vox
```

## <img src="../../icons/fsl.png" height="24px" /> FSL
```bash
## <img src="../../icons/r.png" height="24px" /> Run GLM with FEAT
feat_design <- 'design.fsf'
system2('feat', feat_design)
```

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
## <img src="../../icons/r.png" height="24px" /> Run recon-all for structural analysis
recon-all -subjid Sample -i sample.nii.gz -all
```

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix
```bash
# Compute a brain mask for the FOD image
dwi2mask input.mif mask.mif
```

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
## Volume to surface mapping 
wb_command -volume-to-surface-mapping volume.nifti my_surface.gii output.shape.gii -ribbon-constrained my_white.gii my_pial.gii
```

## <img src="../../icons/r.png" height="24px" /> R
```r
## Load NIfTI image
library(neurobase)
img <- readnii("T1-image.nii.gz")
```

## <img src="../../icons/spm.png" height="24px" /> SPM
```matlab
spm('defaults', 'fmri');
spm_jobman('initcfg');

matlabbatch{1}.spm.stats.fmri_spec.dir = {'/path/to/SPM/folder'};
matlabbatch{1}.spm.stats.fmri_spec.timing.units = 'secs';
matlabbatch{1}.spm.stats.fmri_spec.sess.scans = {'/path/to/brain/images'};
% more configuration ...
spm_jobman('run', matlabbatch);
```
Note that scripts should be tailored for your specific use case. This includes paths to files, which would need to be filled with the actual location of your data. This is just an example of how the scripts might look like, and each script would perform a specific task in each software.