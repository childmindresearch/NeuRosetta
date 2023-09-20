I'm sorry, but I'm not able to provide complete scripts for all these packages directly as a text-based AI assistant, I can provide brief pseudo-code references that could be done using these packages:

1. AFNI
```bash
3dDWItoDT -prefix DTI afni_diffusion_data
3dwrite DTI.f* afni_diffusion_tensor
```

2. ANTs
```bash
N/A - ANTs does not directly support diffusion tensor imaging calculations.
```

3. FSL
```bash
# Assumed you've done eddy correction prior and the data is corrected_dwi.nii.gz
dtifit -k corrected_dwi -o dti -m brain_mask -r bvecs -b bvals
```

4. FreeSurfer
```bash
# Assuming you have a DTI volume dti.nii and a brain mask brain_mask.mgz
mri_convert dti.nii dti.mgz
mri_mask dti.mgz brain_mask.mgz masked_dti.mgz
dt_recon --i masked_dti.mgz --b bvals --r bvecs --o dtrecon_output
```

5. MRtrix
```bash
dwidenoise dwi.mif dwi_den.mif
dwipreproc dwi_den.mif dwi_preproc.mif
dwi2tensor dwi_preproc.mif dt.mif
```

6. pure Python
```python
# Assumed you're using Dipy for the processing
from dipy.reconst import dti
from dipy.data import fetch_stanford_hardi, read_stanford_hardi

fetch_stanford_hardi()
img, gtab = read_stanford_hardi()
data = img.get_data()

dti_model = dti.TensorModel(gtab)
dti_fit = dti_model.fit(data)

FA = dti_fit.fa
```

7. SPM
```matlab
% Assumed you're using SPM12 for DTI analysis
matlabbatch{1}.spm.tools.dti.run_dti.data = {'DTI.nii,1'};
matlabbatch{1}.spm.tools.dti.run_dti.outdir = {'C:\outpath\'};
spm('defaults', 'FMRI');
spm_jobman('run', matlabbatch);
```

Please note that you might need to modify these codes according to your needs like file paths and file names.