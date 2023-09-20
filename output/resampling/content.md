Sure, here are some examples. Please bear in mind that these are very basic examples, and actual application in a real-world scenario may need additional scripting.

**1. AFNI**

The AFNI (Analysis of Functional NeuroImages) has a function `3dresample`.

```bash
3dresample -dxyz 1.0 1.0 1.0 -prefix resampled.nii -input original.nii
```

**2. ANTs**

The ANTs (Advanced Normalization Tools) toolset includes `ResampleImage`.

```bash
ResampleImage 3 input.nii output.nii 1x1x1
```

**3. FSL**

FSL (FMRIB Software Library) provides the `flirt` utility for re-sampling.

```bash
flirt -in input.nii -ref input.nii -out output.nii -applyisoxfm 1.0
```

**4. FreeSurfer**

FreeSurfer's `mri_convert` utility allows re-sampling.

```bash
mri_convert --voxsize 1 1 1 input.mgz output.mgz
```

**5. MRtrix**

MRtrix's `mrresize` utility takes care of re-sampling.

```bash
mrresize input.mif output.mif -scale 1
```

**6. SPM (Matlab)**

SPM (Statistical Parametric Mapping) in Matlab uses `spm_sample_vol`.

```MATLAB
V = spm_vol('input.nii');
X = spm_read_vols(V);
Vout = V;
Vout.dt(1) = 4; % data type float32
Vout.fname = 'output.nii';
spm_write_vol(Vout, X);
```

**7. Python (Nilearn)**

In Python, nilearn's `resample_to_img` function is straightforward for re-sampling.

```python
from nilearn.image import resample_to_img

resampled_img = resample_to_img(img_to_resample, reference_img)
```
Here, `img_to_resample` and `reference_img` are nifti image objects.

Remember that these are simplistic examples, and actual brain imaging data requires more complex processing and tailor-made scripts.