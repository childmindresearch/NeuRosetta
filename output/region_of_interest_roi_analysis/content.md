Sure, below are simplified example scripts for ROI analysis for each of the mentioned software. Please replace "mypath", "mydata", "myroi", etc with the correct path/filename on your system.

**1. AFNI:**

```bash
# AFNI
3dmaskave -mask mypath/myroi.nii -quiet mypath/mydata.nii > output.txt
```

**2. ANTs:**

```bash
# ANTs
ImageMath 3 output.txt m mean mypath/mydata.nii mypath/myroi.nii
```

**3. FSL:**
 
```bash
# FSL
fslstats mypath/mydata.nii -k mypath/myroi.nii -M > output.txt
```

**4. FreeSurfer:**

```bash
# FreeSurfer
mri_segstats --seg mypath/mysegmentation.nii --i mypath/mydata.nii --avgwf output.txt
```

**5. MRtrix:**

```bash
# MRtrix
maskdump mypath/myroi.mif output.csv
```

**6. Pure Python (using nibabel and numpy):**

```python
# Pure Python
import nibabel as nib
import numpy as np

# load your data and roi
data_img = nib.load('mypath/mydata.nii')
roi_img = nib.load('mypath/myroi.nii')

# apply the roi mask to the data
masked_data = data_img.get_fdata() * roi_img.get_fdata()

# calculate the mean in the roi
mean_roi = np.mean(masked_data)

# output to a text file
with open('output.txt', 'w') as f:
    f.write(str(mean_roi))
```

**7. SPM (Matlab):**

```matlab
% SPM
mask = 'mypath/myroi.nii';
V = spm_vol(mask);
roi = spm_read_vols(V);

data = 'mypath/mydata.nii';
V = spm_vol(data);
Y = spm_read_vols(V);

masked_data = Y .* roi;

mean_roi = mean(masked_data(:));

dlmwrite('output.txt', mean_roi)
```
Please note that the nature of the ROI operation will depend on your specific application and data, and you might need to perform additional steps (such as smoothing, normalization, etc.) before or after the ROI analysis.