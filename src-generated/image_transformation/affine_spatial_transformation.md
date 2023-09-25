1. AFNI:
```sh
3dAllineate -source source_file.nii -master ref_file.nii -prefix out_file.nii
```

2. ANTs:
```sh
antsApplyTransforms -d 3 -i input.nii -r reference.nii -o output.nii -t transformation0GenericAffine.mat
```

3. FSL:
```sh
flirt -in source_file -ref ref_file -out output_file -omat affine_matrix -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp trilinear
```

4. FreeSurfer:
```sh
mri_robust_register --mov source_file.mgz --dst target_file.mgz --lta output.lta --satit --cost corratio
```

5. MRtrix:
```sh
mrtransform source_image.mif -linear transformation_matrix.txt -inverse output.mif
```

6. R:
```r
library(oro.nifti)
img <- readNIfTI("input.nii")
trans <- matrix(c(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0), 3, 4)
img2 <- imgApplyXform(img, trans)
writeNIfTI(img2, "transformed.nii.gz")
```

7. Workbench Command:
```sh
wb_command -volume-affine-resample source.nii transformation.mat reference.nii CUBIC output.nii
```

8. Pure Python (using nibabel and numpy):
```python
import nibabel as nib
import numpy as np

img = nib.load('source.nii.gz')
data = img.get_fdata()

affine = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
new_img = nib.Nifti1Image(data, affine)

nib.save(new_img, 'output.nii.gz')
```

9. SPM (via a MATLAB script):
```matlab
matlabbatch{1}.spm.spatial.coreg.estwrite.ref = {'ref_img.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.source = {'source_img.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estwrite.other = {''};
matlabbatch{1}.spm.spatial.coreg.estwrite.eoptions.cost_fun = 'nmi';
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```