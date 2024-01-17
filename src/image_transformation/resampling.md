[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/image_transformation/resampling.md)
# Resampling

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
3dresample -dxyz 1.0 1.0 1.0 -prefix resampled.nii -input input.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```bash
antsApplyTransforms -d 3 -i input.nii -r reference.nii -o resampled.nii --use-NN
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```bash
flirt -in input.nii -ref reference.nii -out resampled.nii -applyisoxfm 1.0
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
mri_convert --resample_type nearest --voxsize 1.0 1.0 1.0 -i input.nii -o resampled.nii
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```bash
mrresize input.nii -scale 1.0 -interp nearest -datatype uint8 resampled.nii
```

## <img src="../icons/r.png" height="24px" /> R
```r
library(oro.nifti)
img <- readNIfTI("input.nii", reorient = FALSE)
resampled <- resampleImage(img, c(1, 1, 1), method="nearest")
writeNIfTI(resampled, filename="resampled.nii")
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
wb_command -volume-resample input.nii template.nii NEAREST resampled.nii
```

## <img src="../icons/python.png" height="24px" /> Python
```python
import nibabel as nib
from scipy.ndimage import affine_transform

img = nib.load('input.nii')
data = img.get_fdata()
affine = img.affine

resampled_data = affine_transform(data, affine)
resampled_img = nib.Nifti1Image(resampled_data, affine)

nib.save(resampled_img, 'resampled.nii')
```

## <img src="../icons/spm.png" height="24px" /> SPM
```Matlab
spm('defaults', 'fmri');
matlabbatch{1}.spm.spatial.coreg.write.ref = {'input.nii'};
matlabbatch{1}.spm.spatial.coreg.write.source = {'reference.nii'};
matlabbatch{1}.spm.spatial.coreg.write.roptions.interp = 4;
matlabbatch{1}.spm.spatial.coreg.write.roptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.coreg.write.roptions.mask = 0;
matlabbatch{1}.spm.spatial.coreg.write.roptions.prefix = 'r';
spm_jobman('run', matlabbatch);
```
In all these scripts, replace "input.nii" with the name of your input nifti file, and "resampled.nii" with the name you want for your output nifti file. Note that in some scripts a "reference.nii" image was used: you would also need to replace this with the filename of your reference image. The resampling has been done to voxels of size 1x1x1, using nearest neighbor interpolation.