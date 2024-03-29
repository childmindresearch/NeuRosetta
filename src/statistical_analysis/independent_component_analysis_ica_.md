[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/statistical_analysis/independent_component_analysis_ica_.md)
# Independent Component Analysis (ICA)

Here are minimal example scripts to perform Independent Component Analysis (ICA) using different neuroimaging analysis software and programming languages. These scripts work with already preprocessed and input data:

## <img src="../icons/afni.png" height="24px" /> AFNI

AFNI doesn't contain direct ICA functionality. However, it can work with the MELODIC outputs which are generated by FSL.

```sh
3dcalc -a melodic_IC.nii.gz[0] -expr 'a' -prefix IC0.nii
```

## <img src="../icons/ants.png" height="24px" /> ANTs

ANTs also does not have direct ICA functionality, but just like AFNI it can handle MELODIC outputs of FSL.

```sh
ImageMath 3 melodic_IC.nii.gz TimeSeriesDisassemble melodic_IC.nii.gz
```

## <img src="../icons/fsl.png" height="24px" /> FSL

```sh
melodic -i preprocessed_fMRI.nii.gz -o output --nobet --bgthreshold=10 --tr=2.0 --mmthresh=0.5 --Oall
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer

FreeSurfer does not possess independent native ICA tools, but it can be used interconnectedly with other tools mentioned here like FSL's MELODIC and MATLAB's SPM.

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix

MRtrix does not have a direct ICA function. It focuses on diffusion MRI, tractography, and quantitative structural connectivity analysis.

## <img src="../icons/r.png" height="24px" /> R

Here is a simple example using the `fastICA` package in R:

```R
library(fastICA)

# Assuming 'data' is your matrix with fMRI data.
s <- fastICA(data, n.comp = 20, algorithm = "parallel")

# The independent components estimates are stored in s$S
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command

Workbench Command (wb_command) does not contain direct ICA functionality. It's primarily used for exploring and visualising neuroimaging data, particularly surface-based data.

## <img src="../icons/python.png" height="24px" /> Python

Python's `scikit-learn` library contains an implementation of ICA. 

```python
from sklearn.decomposition import FastICA

ica = FastICA(n_components=20)
S_ = ica.fit_transform(X)  # Reconstruct signals

# Assuming 'X' is your matrix with fMRI data. The ICA components are stored in 'S_'.
```

## <img src="../icons/spm.png" height="24px" /> SPM

```matlab
matlabbatch{1}.spm.tools.gift.group_ica.fmri_data = '<YOUR_NIFTI_FILES_HERE>';
matlabbatch{1}.spm.tools.gift.group_ica.param_mask = '<YOUR_MASK_HERE>';
matlabbatch{1}.spm.tools.gift.group_ica.num_ica_comp = 20;
matlabbatch{1}.spm.tools.gift.group_ica.algorithm = 'Infomax';
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```

Replace `<YOUR_NIFTI_FILES_HERE>` with the names of your nifti files (each nifti file is a string in a cell array). Replace `<YOUR_MASK_HERE>` with the filename of your mask.

Please note that the output and the behavior of these tools(C-PAC, Group ICA of fMRI Toolbox (GIFT)) can often be subject to different options and settings. These scripts may not work if your files are not preprocessed or organized in the specified way. Always check the documentation of each software to ensure correct usage.
