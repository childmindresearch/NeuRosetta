[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/statistical_analysis/dynamic_connectivity_analysis.md)
# Dynamic Connectivity Analysis

Sorry for the misunderstanding, but creating scripts for Dynamic Connectivity Analysis in all of these platforms can't be reduced into a few short lines as such a task includes multiple complex steps and is highly dependent on the exact methods you'd like to employ, the desired outputs, and the image format you are starting with. However, as a starting point, I can provide minimal example scripts for time-series extraction which is generally the first step of any Connectivity Analysis. 

Let's assume we have preprocessed fMRI data and a mask/region of interest (ROI) for each of them.

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
3dmaskave -quiet -mask my_mask.nii.gz my_preprocessed_fmri_data.nii.gz > time_series.txt
```
## <img src="../icons/ants.png" height="24px" /> ANTs
ANTs doesn't include dedicated functionalities for time-series extraction. However, you can use it for image preprocessing before extracting the time-series using other tools.

## <img src="../icons/fsl.png" height="24px" /> FSL
```bash
fslmeants -i my_preprocessed_fmri_data.nii.gz -o time_series.txt -m my_mask.nii.gz
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
FreeSurfer doesn't directly support this functionality. It focuses on reconstruction and analysis of cortical surface. After completing these steps with FreeSurfer, you may use other tools to extract time-series.

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```bash
mrstats my_preprocessed_fmri_data.nii.gz -mask my_mask.nii.gz -output mean > time_series.txt
```

## <img src="../icons/r.png" height="24px" /> R
```R
library(fslr)
dat <- fslr::readnii("my_preprocessed_fmri_data.nii.gz")
mask <- fslr::readnii("my_mask.nii.gz")
time_series <- colMeans(dat[mask == 1, ])
write.table(time_series, file = "time_series.txt")
```
## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
Workbench Command is mainly for dealing data in particular formats (like CIFTI). Please use other tools for extracting time series. 

## <img src="../icons/python.png" height="24px" /> Python
```python
import nibabel as nib
import numpy as np
img = nib.load("my_preprocessed_fmri_data.nii.gz")
mask = nib.load("my_mask.nii.gz").get_fdata().astype(bool)
time_series = np.mean(img.get_fdata()[mask], axis=0)
np.savetxt("time_series.txt", time_series)
```
## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
Vf = spm_vol('my_preprocessed_fmri_data.nii.gz');
Vmask = spm_vol('my_mask.nii.gz');
mask = spm_read_vols(Vmask) > 0;
Y = spm_get_data(Vf,spm_find_xyzmat(Vf) * [find(mask); ones(1,sum(mask(:)))]);
time_series = mean(Y,2);
dlmwrite('time_series.txt',time_series,'delimiter','\t');
``` 
Remember, the resultant time-series files can be used as a starting point for Dynamic Connectivity Analysis. Dynamic Connectivity Analysis involves many steps like sliding-window or wavelet based analysis, statistical analysis, and possibly graph theoretical analysis, which requires additional code and additional libraries/packages.