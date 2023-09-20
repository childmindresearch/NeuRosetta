I'm sorry, but it's incorrect to create an ALFF script for all these tools as some of them are not designed to carry out the ALFF analysis. Therefore, there are no direct script examples for some of the mentioned tools like ANTs, FreeSurfer, and MRtrix. However, it's possible to attempt ALFF with AFNI, FSL, SPM, and Python through third-party packages like nilearn.

Here are some examples:

1. AFNI
```bash
3dFourier -lowpass 0.08 -highpass 0.01 -retrend -prefix sub-001.func.alff.nii.gz sub-001.func.nii.gz
```
2. FSL
FSL does not provide direct support for ALFF calculation. However, you can perform bandpass filtering and then calculate the standard deviation or variance over time, which is proportional to ALFF.
```bash
# Bandpass filtering
fslmaths sub-001.func.nii.gz -bptf 25 2.5 sub-001.func.filtered.nii.gz

# Calculate standard deviation
fslmaths sub-001.func.filtered.nii.gz -Tstd sub-001.func.alff.nii.gz
```
3. SPM
In SPM, the Resting-State fMRI Data Analysis Toolkit (REST) [1] can be used to perform ALFF and fALFF.

4. Python
Using nilearn package in Python,

```python
from nilearn import input_data, image
import numpy as np

masker = input_data.NiftiMasker(mask_img='your_mask.nii.gz', standardize=True)
time_series = masker.fit_transform('sub-001.func.nii.gz')

# Compute ALFF
alff = np.std(time_series, axis=0)

# Save ALFF image
alff_img = masker.inverse_transform(alff)
alff_img.to_filename('sub-001.func.alff.nii.gz')
```

Please note that the above codes are just sketchy and simplified examples to perform ALFF. Always cross-verify with the manual or official documentation for latest commands and options.

Reference:
[1] Song X-W, Dong Z-Y, Long X-Y, et al. REST: a toolkit for resting-state functional magnetic resonance imaging data processing. PLoS ONE 6(9):e25031, 2011.
