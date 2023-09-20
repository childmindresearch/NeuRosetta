Sure, here are small script segments for applying spatial smoothing using different neuroimaging software. Note: This assumes the image are in the appropriate format for each software.

1. **AFNI**:
```bash
3dBlurInMask -prefix smoothed_file -input original_file.nii -FWHM 8 -mask brain_mask.nii
```

2. **ANTs**:
```bash
SmoothImage 3 original_file.nii 4 smoothed_file.nii 1 0
```

3. **FSL**:
```bash
fslmaths original_file.nii -s 2 smoothed_file.nii
```

4. **FreeSurfer**:
```bash
mri_fwhm --i original_file.nii --o smoothed_file.nii --fwhm 4.5 --smooth-only
```

5. **MRtrix**:
```sh
mrfilter original_file.nii smooth - -fwhm 5.0 | mrconvert - smoothed_file.nii
```

6. **SPM (via a MATLAB script)**:
```matlab
matlabbatch{1}.spm.spatial.smooth.data = {'/path/to/original_file.nii,1'};
matlabbatch{1}.spm.spatial.smooth.fwhm = [8 8 8];
matlabbatch{1}.spm.spatial.smooth.dtype = 0;
matlabbatch{1}.spm.spatial.smooth.im = 0;
matlabbatch{1}.spm.spatial.smooth.prefix = 'smoothed_';
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```

7. **Pure Python (using nibabel and scipy)**:
```python
import nibabel as nib
import scipy.ndimage

img = nib.load('original_file.nii')
data = img.get_fdata()
smoothed = scipy.ndimage.filters.gaussian_filter(data, 2)
smoothed_img = nib.Nifti1Image(smoothed, img.affine, img.header)
nib.save(smoothed_img, 'smoothed_file.nii')
```

Each script will take an original image file called "original_file.nii" and create a spatially smoothed image file. The degree of smoothing applied is somewhat arbitrarily chosen to demonstrate the syntax for each software package: you should adjust the values according to your specific research needs. Also, note that smoothing parameters are often specified in mm, though sometimes it is specified in terms of voxels: make sure to check the documentation for each specific software package.