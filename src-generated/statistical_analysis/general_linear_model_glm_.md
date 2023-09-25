Sure, here are the minimal example scripts for GLM (General Linear Model) in each mentioned software:

1. AFNI

```bash
3dDeconvolve -input dataX.nii -polort 2 -num_stimts 1 -stim_file 1 dataY.1D -fout -tout -bucket result.nii
```

2. ANTs

Note: ANTs does not specialize in statistical analysis, but it is possible to use ANTs for image registration, then use another tool for the GLM (such as FSL, which is next).

3. FSL

```fsl
#! /bin/sh
fmri=fmri
design=design.mat
contrasts=contrasts.con
fsl_glm -i $fmri -d $design -c $contrasts -o betas
```

4. FreeSurfer

```bash
mri_glmfit --y y.mgh --fsgd dods.fsgd --C contrast.c.dat --glmdir glmresults
```
5. MRtrix

MRtrix does not directly support GLM, but you could utilize its underlying libraries in a custom script.

6. R

```R
data <- read.csv("data.csv")
model <- lm(y ~ x1 + x2, data = data)
```

7. Workbench Command

```bash
wb_command -cifti-stats file.dtseries.nii -reduce MEAN > output.txt
```

8. Python

```python
import numpy as np
import statsmodels.api as sm

X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = np.array([1, 2, 3, 4])

model = sm.OLS(y, X)
results = model.fit()
```

9. SPM (MATLAB)

```matlab
matlabbatch{1}.spm.stats.factorial_design.dir = {'/data'};
matlabbatch{1}.spm.stats.factorial_design.des.t1.scans = {'/data/subj1.nii,1'};
..
spm_jobman('run', matlabbatch);
```
Note that you will need to individualize these templates to your specific analysis, file-naming conventions, and directory structure. It may also be necessary to preprocess the data prior to analysis. These scripts do not include data checking, preprocessing, multiple comparison correction, diagnostics, or the generation of any results' reports.