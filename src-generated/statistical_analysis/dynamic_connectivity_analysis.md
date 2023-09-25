Sorry for the misunderstanding, but creating scripts for Dynamic Connectivity Analysis in all of these platforms can't be reduced into a few short lines as such a task includes multiple complex steps and is highly dependent on the exact methods you'd like to employ, the desired outputs, and the image format you are starting with. However, as a starting point, I can provide minimal example scripts for time-series extraction which is generally the first step of any Connectivity Analysis. 

Let's assume we have preprocessed fMRI data and a mask/region of interest (ROI) for each of them.

1. **AFNI**
```bash
3dmaskave -quiet -mask my_mask.nii.gz my_preprocessed_fmri_data.nii.gz > time_series.txt
```
2. **ANTs**
ANTs doesn't include dedicated functionalities for time-series extraction. However, you can use it for image preprocessing before extracting the time-series using other tools.

3. **FSL**
```bash
fslmeants -i my_preprocessed_fmri_data.nii.gz -o time_series.txt -m my_mask.nii.gz
```

4. **FreeSurfer**
FreeSurfer doesn't directly support this functionality. It focuses on reconstruction and analysis of cortical surface. After completing these steps with FreeSurfer, you may use other tools to extract time-series.

5. **MRtrix**
```bash
mrstats my_preprocessed_fmri_data.nii.gz -mask my_mask.nii.gz -output mean > time_series.txt
```

6. **R**
```R
library(fslr)
dat <- fslr::readnii("my_preprocessed_fmri_data.nii.gz")
mask <- fslr::readnii("my_mask.nii.gz")
time_series <- colMeans(dat[mask == 1, ])
write.table(time_series, file = "time_series.txt")
```
7. **Workbench Command**
Workbench Command is mainly for dealing data in particular formats (like CIFTI). Please use other tools for extracting time series. 

8. **Python**
```python
import nibabel as nib
import numpy as np
img = nib.load("my_preprocessed_fmri_data.nii.gz")
mask = nib.load("my_mask.nii.gz").get_fdata().astype(bool)
time_series = np.mean(img.get_fdata()[mask], axis=0)
np.savetxt("time_series.txt", time_series)
```
9. **SPM (via a MATLAB script)**
```matlab
Vf = spm_vol('my_preprocessed_fmri_data.nii.gz');
Vmask = spm_vol('my_mask.nii.gz');
mask = spm_read_vols(Vmask) > 0;
Y = spm_get_data(Vf,spm_find_xyzmat(Vf) * [find(mask); ones(1,sum(mask(:)))]);
time_series = mean(Y,2);
dlmwrite('time_series.txt',time_series,'delimiter','\t');
``` 
Remember, the resultant time-series files can be used as a starting point for Dynamic Connectivity Analysis. Dynamic Connectivity Analysis involves many steps like sliding-window or wavelet based analysis, statistical analysis, and possibly graph theoretical analysis, which requires additional code and additional libraries/packages.