# Image Coregistration

I'm sorry for the confusion, but I cannot provide visual content or script files as I'm a text-based AI model developed by OpenAI. However, I can still help you generate those example scripts in text form. Here they are:

## <img src="../icons/afni.png" height="24px" /> AFNI
```Shell
# Example: Coregister anat to epi
3dAllineate -base epi.nii -input anat.nii -prefix anat2epi
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```Shell
# Example: Register T2 to T1 image
antsRegistration --dimensionality 3 --float 0 \
    --output [transform,warpedImage] \
    --interpolation Linear \
    --use-histogram-matching 0 \
    --initial-moving-transform [t1.nii, t2.nii, 1] \
    --transform Rigid[0.1] \
    --metric MI[t1.nii, t2.nii, 1, 32, Regular, 0.25] \
    --convergence [1000x500x250x100,1e-6,10] \
    --shrink-factors 8x4x2x1 \
    --smoothing-sigmas 3x2x1x0vox
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```Shell
# Example: Register T1 to MNI space
flirt -in T1.nii -ref $FSLDIR/data/standard/MNI152_T1_2mm_brain -out T1_MNI -omat T1_to_MNI.mat
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```Shell
# Example: BBR cost function coregistration
bbregister --s subject --mov bold.nii --init-fsl --bold --reg bold_to_fs.dat
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```Shell
# Example: Register T2 to T1 image
mrregister T1.mif T2.mif -type rigid -mask1 T1_mask.mif -mask2 T2_mask.mif -nl_warp T12Warp.mif T21Warp.mif
```

## <img src="../icons/r.png" height="24px" /> R
```R
# Example using R's 'oro.nifti' and 'RNifti' libraries
library(oro.nifti)
library(RNifti)
t1 <- niftiR('T1.nii')
t2 <- niftiR('T2.nii')
t1affineparams <- flirt(t1, t2, method="affine")
t1warped <- applyTransform(t1affineparams, t1)
writeNifti(t1warped, 'T1_coreg.nii')
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```Shell
# Example: Apply CIFTI standard-space registration
wb_command -cifti-resample input.dconn.nii COLUMN target.dtseries.nii COLUMN ADAP_BARY_AREA input_to_target.dconn.nii -area-metrics input.area.surf.gii target.area.surf.gii
```

## <img src="../icons/spm.png" height="24px" /> SPM
```MATLAB
% Example: Coregister T2 to T1 image
matlabbatch{1}.spm.spatial.coreg.estwrite.ref = {'T1.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.source = {'T2.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.other = {''};
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```