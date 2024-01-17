[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/statistical_analysis/general_linear_model_glm_.md)
# General Linear Model (GLM)

here are the minimal example scripts for GLM (General Linear Model) in each mentioned software:

## <img src="../icons/afni.png" height="24px" /> AFNI

```bash
3dDeconvolve -input dataX.nii -polort 2 -num_stimts 1 -stim_file 1 dataY.1D -fout -tout -bucket result.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs

Note: ANTs does not specialize in statistical analysis, but it is possible to use ANTs for image registration, then use another tool for the GLM (such as FSL, which is next).

## <img src="../icons/fsl.png" height="24px" /> FSL

```fsl
#! /bin/sh
fmri=fmri
design=design.mat
contrasts=contrasts.con
fsl_glm -i $fmri -d $design -c $contrasts -o betas
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
mri_glmfit --y y.mgh --fsgd dods.fsgd --C contrast.c.dat --glmdir glmresults
```
## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

MRtrix does not directly support GLM, but you could utilize its underlying libraries in a custom script.

## <img src="../icons/r.png" height="24px" /> R

```R
data <- read.csv("data.csv")
model <- lm(y ~ x1 + x2, data = data)
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

```bash
wb_command -cifti-stats file.dtseries.nii -reduce MEAN > output.txt
```

## <img src="../icons/python.png" height="24px" /> Python

```python
import numpy as np
import statsmodels.api as sm

X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = np.array([1, 2, 3, 4])

model = sm.OLS(y, X)
results = model.fit()
```

## <img src="../icons/spm.png" height="24px" /> SPM

```matlab
matlabbatch{1}.spm.stats.factorial_design.dir = {'/data'};
matlabbatch{1}.spm.stats.factorial_design.des.t1.scans = {'/data/subj1.nii,1'};
..
spm_jobman('run', matlabbatch);
```
Note that you will need to individualize these templates to your specific analysis, file-naming conventions, and directory structure. It may also be necessary to preprocess the data prior to analysis. These scripts do not include data checking, preprocessing, multiple comparison correction, diagnostics, or the generation of any results' reports.