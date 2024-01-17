[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/fmri_analysis/regional_homogeneity_reho_.md)
# Regional Homogeneity (ReHo)

I'm sorry for any misunderstanding, but it's not possible to provide example scripts for all the software you mentioned as some of them do not support ReHo (Regional Homogeneity) analysis directly. However, I can provide you examples for a few of them like AFNI and Python and point you to relevant resources for the others.

## <img src="../icons/afni.png" height="24px" /> AFNI
    
```
3dReHo -prefix ReHo.nii -inset RestingState.nii
```

This one-liner will conduct a ReHo analysis on a resting state time series dataset. 


2. **ANTs/Freesurfer/FSL/MRtrix/Workbench Command**

These packages don't provide direct methods or commands to conduct ReHo analysis. However, you can create permutations of existing functions to accomplish it. Consider using other software that directly support ReHo analysis like AFNI, DPARSF /REST, or using a language like R or Python. 

For example, in FSL you might first extract the time series the ROI using fslmeants, then run fslcc to compute cross-correlation coefficient, and then square that value to get Regional homogeneity.
     

## <img src="../icons/r.png" height="24px" /> R
    
Here is a minimal example with fslr package.
    
```R
library(fslr)
data <- fslr::readnii("RestingState.nii")
reho_map <- fslr::fslreho(data)
```
Notice that R might not be the most efficient tool for this task, especially with large datasets.

## <img src="../icons/python.png" height="24px" /> Python
  
```python
import numpy as np
from nilearn.input_data import NiftiSphereMasker
from nilearn import datasets, plotting

dataset = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm') 
atlas_filename = dataset.maps
labels = dataset.labels

coords = plotting.find_parcellation_cut_coords(labels_img=atlas_filename)
sphere_masker = NiftiSphereMasker(seeds=coords, radius=8,
                                   standardize=True, memory='nilearn_cache', verbose=5)
time_series = sphere_masker.fit_transform('subject_func_images.nii.gz', confounds='subject_confounds.csv')

n_regions = time_series.shape[1]
correlation_matrix = np.empty((n_regions, n_regions))
for i in range(n_regions):
    for j in range(i, n_regions):
        correlation_matrix[i, j] = np.corrcoef(time_series[:, i], time_series[:, j])[0, 1]

reho_map = np.repeat(correlation_matrix.mean(axis=0), n_regions, axis=0).reshape(correlation_matrix.shape)
```

This is a very simplified script for ReHo analysis in Python. It mainly focuses on depicting the main idea of computations and is probably missing some standard parameters like band-pass filtering or discarding first few volumes.


## <img src="../icons/spm.png" height="24px" /> SPM

For MATLAB, you can use toolbox such as DPABI/DPARSF which is developed based on SPM. Here is a simple example:

```matlab
addpath /path/to/DPABI_V4_3_190615;
DPABI_PATH = fileparts(which('DPABI.m'));
addpath ([DPABI_PATH,filesep,'RestingStateImage']);
addpath ([DPABI_PATH,filesep,'Subfunctions']);

[FileList, SubjectQuantity]=GetSubName('/path/to/sub_directory');
ReHoDir=['/path/to/save/ReHoResults'];

parfor i=1:SubjectQuantity
    InFile = FileList(i, :);
    [pathstr, name, ext] = fileparts(InFile); 
    OutName=[ReHoDir,'/','ReHo_',name];

    y_reho(InFile, OutName, '/path/to/BrainMask.nii');
end
```

Always remember to precisely adapt paths in scripts to your data and use parameters that are appropriate for your specific dataset. Scripts like these are often only starting points, it's usually necessary to customize them.