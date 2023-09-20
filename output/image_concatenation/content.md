Though I can't perform any actual code execution or show any images, here's a simple script example for each software package (given that all required datasets are already loaded and all dependencies are installed):

1. **AFNI**
```bash
3dTcat -prefix concatenated_image.nii first_image.nii second_image.nii
```

2. **ANTs**
```bash
N4BiasFieldCorrection -d 3 -i input.nii -o output.nii
```
2.1 Image concatenation is not directly supported in ANTs, but transformation matrices can be concatenated.

3. **FSL**
```bash
fslmerge -t output.nii first_image.nii second_image.nii
```

4. **FreeSurfer**
```bash
mri_concat --i first_image.nii --i second_image.nii --o concatenated_image.mgz
```

5. **MRtrix**
```bash
mrcat first_image.mif second_image.mif concatenated_image.mif
```

6. **Python**
```python
import nibabel as nib
import numpy as np

img1 = nib.load('first_image.nii')
img2 = nib.load('second_image.nii')

data1 = img1.get_fdata()
data2 = img2.get_fdata()

concatenated_data = np.concatenate((data1, data2), axis=None)

new_img = nib.Nifti1Image(concatenated_data, img1.affine)
nib.save(new_img, 'concatenated_image.nii')
```

7. **SPM**
```matlab
matlabbatch{1}.spm.util.cat.vols = {'first_image.nii,1', 'second_image.nii,1'};
matlabbatch{1}.spm.util.cat.name = 'concatenated_image.nii';
matlabbatch{1}.spm.util.cat.dtype = 4;
spm_jobman('run', matlabbatch);
```

Please make sure to replace `'first_image.nii'`, `'second_image.nii'`, and `'output.nii'` or `'concatenated_image.nii'` with the actual paths to your images.