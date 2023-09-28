[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/fmri_analysis/seed_based_correlation.md)
# Seed-Based Correlation

here are some minimal example scripts to perform seed-based correlation analysis in some of the programs you've mentioned. Please note that these are incredibly simplified snippets and might not be functional without some adjustments to fit your specific pipelines and data.

## <img src="../icons/afni.png" height="24px" /> AFNI
```shell
# Assuming your seed ROI is already defined in 'seed.nii.gz'
3dmaskave -mask seed.nii.gz -quiet rsfMRI.nii.gz > seed.1D
3dDetrend -polort 5 -prefix rsfMRI_detrend.nii.gz rsfMRI.nii.gz
3dTproject -input rsfMRI_detrend.nii.gz -ort seed.1D -prefix rsfMRI_proj.nii.gz
3dcalc -a 'rsfMRI_proj.nii.gz' -b seed.nii.gz -expr 'a*b' -prefix seedCorr.nii.gz
```

## <img src="../icons/ants.png" height="24px" /> ANTs
ANTs doesn't really have a seed-based correlation function. You might have to use ANTs to pre-process the fMRI image and then use another software package like FSL or AFNI to conduct the seed-based correlation.

## <img src="../icons/fsl.png" height="24px" /> FSL
```shell
# Assuming your seed ROI is defined in 'seed.nii.gz'
fslmeants -i rsfMRI.nii.gz -o seed_ts.txt -m seed.nii.gz 
fsl_glm -i rsfMRI.nii.gz -d seed_ts.txt -o seedCorr 
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```shell
# Assuming your seed vertex is at 40
mri_segstats --i rsfMRI.nii.gz --id 40 --avgwf seed_ts.txt
mri_glmfit --y rsfMRI.nii.gz --fsgd seed_ts.txt --glmdir seedCorr
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```shell
# Again assuming 'seed.nii.gz' as your seed
seedmean=`fslstats seed.nii.gz -M`
fslmaths rsfMRI.nii.gz -sub $seedmean seedCorr.nii.gz
```

## <img src="../icons/r.png" height="24px" /> R
R doesn't have native functions for neuroimaging data processing. You might use other packages like RNifti for reading nifti images and then process it like a matrix.

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```shell
# Assuming your are using CIFTI files
wb_command -cifti-correlation rsfMRI.dtseries.nii seed.dtseries.nii 
wb_command -cifti-separate seed.dtseries.nii COLUMN -volume-all seed.nii.gz
```

## <img src="../icons/python.png" height="24px" /> Python
```python
import nibabel as nib
import numpy as np

img = nib.load('rsfMRI.nii.gz')
seed = nib.load('seed.nii.gz')

seed_data = seed.get_fdata()
img_data = img.get_fdata()

seed_ts = np.mean(img_data[seed_data > 0], axis=0)

corr = np.empty_like(img_data[..., 0])
for i in range(img_data.shape[-1]):
    corr = np.corrcoef(img_data[..., i].ravel(), seed_ts.ravel())[0, 1]

corr_img = nib.Nifti1Image(corr, img.affine)
nib.save(corr_img, 'seedCorr.nii.gz')
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
% Assuming you have your seed time series in 'seed_ts.mat', 
% and your image data in 'rsfMRI.nii'
spm_imcalc('rsfMRI.nii', 'seedCorr.nii', 'i1.*mean(seed_ts)', {seed_ts});
```

Remember to replace 'rsfMRI.nii.gz' and 'seed.nii.gz' with your functional image and seed region (or timecourse) paths, respectively. This is very much an oversimplification: you'll usually want to add more steps in your pipeline like motion correction, normalizing, smoothing, etc.