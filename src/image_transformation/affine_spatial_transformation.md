# Affine Spatial Transformation

## <img src="../icons/afni.png" height="24px" /> AFNI
```sh
3dAllineate -source source_file.nii -master ref_file.nii -prefix out_file.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```sh
antsApplyTransforms -d 3 -i input.nii -r reference.nii -o output.nii -t transformation0GenericAffine.mat
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```sh
flirt -in source_file -ref ref_file -out output_file -omat affine_matrix -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp trilinear
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```sh
mri_robust_register --mov source_file.mgz --dst target_file.mgz --lta output.lta --satit --cost corratio
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```sh
mrtransform source_image.mif -linear transformation_matrix.txt -inverse output.mif
```

## <img src="../icons/r.png" height="24px" /> R
```r
library(oro.nifti)
img <- readNIfTI("input.nii")
trans <- matrix(c(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0), 3, 4)
img2 <- imgApplyXform(img, trans)
writeNIfTI(img2, "transformed.nii.gz")
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```sh
wb_command -volume-affine-resample source.nii transformation.mat reference.nii CUBIC output.nii
```

## <img src="../icons/python.png" height="24px" /> Python
```python
import nibabel as nib
import numpy as np

img = nib.load('source.nii.gz')
data = img.get_fdata()

affine = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
new_img = nib.Nifti1Image(data, affine)

nib.save(new_img, 'output.nii.gz')
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
matlabbatch{1}.spm.spatial.coreg.estwrite.ref = {'ref_img.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.source = {'source_img.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.other = {''};
matlabbatch{1}.spm.spatial.coreg.estwrite.eoptions.cost_fun = 'nmi';
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```