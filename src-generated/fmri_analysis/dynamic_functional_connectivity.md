Creating an exhaustive script that covers Dynamic Functional Connectivity in each of the mentioned neuroimaging software goes beyond the purposes of this platform and my capabilities as AI. Moreover, flexibility and usability of an MRI pipeline depend greatly on the specific data and goals of the analysis. 

However, I can provide some brief examples of how such scripts might look in each of these tools, in a general sense:

1. **AFNI**

Here's a basic script for dynamic correlation with a seed ROI in AFNI:

```bash
3dmaskave -quiet -mask seed_roi.nii time_series.nii > seed_roi.1D
3dfim+ -input time_series.nii -ideal_file seed_roi.1D -out Correlation
```

2. **ANTs**

ANTs doesn't directly perform fMRI analysis, but it's typically used for image registration. An important step in functional connectivity analysis is to register (align) the images, which could be done by antsRegistration.

3. **FSL**

Here is an example using FSL's fslmeants tool to extract mean time series of a seed ROI, and FSL's fslcc to compute correlation:

```bash
fslmeants -i input.nii -o mean_ts.txt -m seed_roi.nii
fslcc -i input.nii -r mean_ts.txt > output.txt
```

4. **FreeSurfer** 

FreecSurfer is primarily used for structural brain imaging, and wouldn't typically be used for dynamic functional connectivity itself. However, you might use it to extract surfaces or ROIs, which can then be used in other tools.

5. **MRtrix**

MRtrix focuses more on diffusion MRI analyses, so doesn't directly deal with functional connectivity.

6. **R**

The "neuroim" package in R can perform functional connectivity analysis:

```r
library(neuroim)
fmri_data <- fmri_data('fmri.nii')
seed_ts <- extract_ts(fmri_data, 'seed_roi.nii')
connectivity_map <- correlate(fmri_data, seed_ts)
```
   
7. **Workbench Command (HCP Workbench)** 

Workbench Command can be used to manipulate data and compute connectivity, but requires Connetome Workbench.

8. **Python**

For pure Python, nilearn can be used:

```python
from nilearn.input_data import NiftiSpheresMasker
from nilearn.connectome import ConnectivityMeasure

masker = NiftiSpheresMasker(seeds='seed_roi.nii', standardize=True)
time_series = masker.fit_transform('fmri.nii')

correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]
```

9. **SPM (via a MATLAB script)**

Here's an example MATLAB script for performing seed-based correlation with SPM:

```matlab
matlabbatch{1}.spm.util.voi.roi{1}.sphere.centre = [x,y,z];
matlabbatch{1}.spm.util.voi.roi{1}.sphere.radius = r;
matlabbatch{1}.spm.util.voi.roi{1}.sphere.move.fixed = 1;

conn_batch;
conn_module('evabatch', matlabbatch);
```

These scripts are very generalized and may not work for specific needs. You should adjust them according to your targets.