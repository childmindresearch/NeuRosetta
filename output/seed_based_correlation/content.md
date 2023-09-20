Sure. Here are the very basic examples of seed-based correlation for each software you mentioned. Note that a comprehensive explanation for each line is omitted in these examples, and you might need to adjust the code for use with your own data and conditions.

### 1. AFNI:
```
3dROIstats -mask seed.nii -quiet -nzmean func.nii > seed.1D
3dDetrend -polort 5 -prefix detrend.nii func.nii
3dpc -vmean -mask brain_mask.nii -prefix PC detrend.nii
3dTproject -input detrend.nii -ort PC+orig -prefix proj.nii
3dfim+ -input proj.nii -ideal_file seed.1D -out Correlation -bucket stats.nii
```

### 2. ANTs:
ANTs doesn't have a seed-based correlation function, but ANTsR, its R-based counterpart does:
```
library(ANTsR)
image<-antsImageRead("image.nii")
mask<-antsImageRead("mask.nii")
out<-getMaskedMean(image, mask)
```

### 3. FSL:

```
fslmeants -i func.nii -o seed.txt -m seed.nii 
fsl_glm -i func.nii -d seed.txt -o betas.nii --out_z=zstat.nii -m mask.nii
```

### 4. FreeSurfer:

```
mri_segstats --seg seed.nii --i func.nii --avgwf seed.txt
mri_glmfit --y func.nii --fsgd design.fsgd --C seed.txt --seed 12345 --glmdir glm_output
```

### 5. MRtrix:
```
maskfilter seed.nii mean mean_seed.nii
for_each + "-/%p.nii.gz:l" dwi2response_hollander mean_seed.nii %r.nii.gz -mask mask.nii
mrcalc %r.nii.gz %a.nii.gz -mult seed.nii.gz 
```

### 6. SPM (through MATLAB):
```
matlabbatch{1}.spm.util.imcalc.input = {
                                        'func.nii,1'
                                        'seed.nii,1'
                                       };
matlabbatch{1}.spm.util.imcalc.output = 'seed_ts';
matlabbatch{1}.spm.util.imcalc.outdir = {''};
matlabbatch{1}.spm.util.imcalc.expression = 'i1.*i2';
spm_jobman('run', matlabbatch);

matlabbatch{1}.spm.stats.factorial_design.dir = {'/path/to/output_directory'};
matlabbatch{1}.spm.stats.factorial_design.des.t1.scans = {'seed_ts.nii,1'};
spm_jobman('run',matlabbatch);
```

### 7. Pure Python (Nilearn as Brain imaging library in python)

```
from nilearn import input_data, image, plotting

seed_masker = input_data.NiftiMasker(mask_img='seed.nii').fit()
brain_masker = input_data.NiftiMasker(mask_img='brain_mask.nii').fit()

seed_time_series = seed_masker.transform('func.nii')
brain_time_series = brain_masker.transform('func.nii')

correlation_matrix = image.corrcoef(seed_time_series, brain_time_series)

plotting.plot_matrix(correlation_matrix)
```
Please note that you need to provide the full path for the files in the script and replace path and file names according to your actual situation. Make sure to understand what each command is doing before running the scripts on your own data. Not all commands are equivalent between software. In addition, necessary pre-processing steps (brain extraction, motion correction, spatial smoothing, etc) are not included.


