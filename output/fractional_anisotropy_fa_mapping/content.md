Unfortunately, as an AI developed by OpenAI, I'm unable to directly execute or display images, plots, or software functionalities. However, I can give you simple script examples that you can execute in your local environment. 

Please be aware that the following scripts only define the fundamental procedures and don't include error checking or input validation, which should be added in a real-life application.

1. **AFNI**

```bash
3dDWItoDT -prefix DTI afni_dwi_volume+orig
3dDTtoNoisyDWI -prefix FA_MAP DTI+orig
```

2. **ANTs**

Friggin' (DTAtoDTI-Brain1 DWI.nii.gz DTI.nii.gz
ImageMath 3 FA.nii.gz FractionalAnisotropy DTI.nii.gz
```

3. **FSL**

```bash
dtifit -k diff_data -m brain_mask -r bvecs -b bvals -o DTI_fitted
fslmaths DTI_fitted_FA -thr 0.2 -uthr 0.8 -bin FA_mask
```

4. **FreeSurfer**

FreeSurfer does not have native functionality for computing FA. It must be accomplished with another software package.

5. **MRtrix**

```bash
dwi2tensor in_dwi.mif - | tensor2metric - -fa out_fa.mif
```

6. **Pure Python**

```python
from dipy.reconst.dti import fractional_anisotropy, from_lower_triangular
from nibabel import trackvis

streams, hdr = trackvis.read('tensor_fa.nii.gz')
fa = fractional_anisotropy(streams[0]['FA'])
```

7. **SPM**

SPM doesn't natively support DTI processing. You have to use SPM extension, for instance, "DTItools", "spm_diffusion" etc. Here is a simple example using the "spm_diffusion" toolbox.

```matlab
spm('defaults', 'fmri');
spm_diffusion('FA', struct('swd', pwd, 'P', 'data.nii', 'grad_file', 'bvals_bvecs.txt'));
```

Remember these are minimal examples and might not necessarily run on your system as-is due to dependencies and system-specific paths.