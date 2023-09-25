# Spatial Smoothing

I can provide a small example for each, assuming the necessary software is installed and data is available.

## <img src="../../icons/afni.png" height="24px" /> AFNI
```bash
3dBlurInMask -input run1.nii -FWHM 4 -prefix run1_smooth.nii
```

## <img src="../../icons/ants.png" height="24px" /> ANTs
```bash
SmoothImage 3 input.nii 1 output.nii
```

## <img src="../../icons/fsl.png" height="24px" /> FSL
```bash
fslmaths run1.nii -s 2.548 run1_smooth.nii
```

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
mris_fwhm --i run1.nii --fwhm 5 --o run1_smooth.nii
```

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix
```bash
mrfilter run1.nii smooth -fwhm 4 - | mrconvert - run1_smooth.nii
```

## <img src="../../icons/r.png" height="24px" /> R
```r
library(fslr)
img = readnii('run1.nii')
smooth_img = fslsmooth(img, sigma = 2)
writenii(smooth_img, 'run1_smooth.nii')
```

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
wb_command -volume-smoothing run1.nii 4 run1_smooth.nii
```

## <img src="../../icons/python.png" height="24px" /> Python
```python
import nibabel as nib
import scipy.ndimage

img = nib.load('run1.nii')
data = img.get_fdata()
smooth_data = scipy.ndimage.filters.gaussian_filter(data, sigma=2)
smooth_img = nib.Nifti1Image(smooth_data, img.affine)
nib.save(smooth_img, 'run1_smooth.nii')
```

## <img src="../../icons/spm.png" height="24px" /> SPM
```matlab
matlabbatch{1}.spm.spatial.smooth.data = {'run1.nii'};
matlabbatch{1}.spm.spatial.smooth.fwhm = [8 8 8];
matlabbatch{1}.spm.spatial.smooth.dtype = 0;
matlabbatch{1}.spm.spatial.smooth.im = 0;
matlabbatch{1}.spm.spatial.smooth.prefix = 's';
spm_jobman('run', matlabbatch);
```
Please replace `'run1.nii'` in all the scripts with your actual input file name. Also, note that the degree of smoothing (set by the FWHM value or sigma value in some scripts) will need to be adjusted as per your requirements. Be aware that smoothing can biases the data if it's not done properly; consult appropriate documentation or a statistician.

Also please note not all commands, especially SPM, FreeSurfer, MRtrix, and Workbench Command, are not able to be run outside of their respective environments.