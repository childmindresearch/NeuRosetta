While applying ICA to neuroimaging data can be extensive, I can provide rudimentary examples to get you started with Independent Component Analysis in each of the requested libraries. Please note proper pre-processing steps are needed before performing ICA which have been omitted for brevity.

1. **AFNI**

Here is a simple command you might use with AFNI's `3dICA`:

```bash
3dICA -input your_4D_data.nii -prefix ica_output -num_components 20
```

2. **ANTs**

ANTs itself does not perform ICA, rather it's used for registration, segmentation, and bias field correction. You would typically use another software like FSL or AFNI for this.

3. **FSL**

Performing ICA with FSL is generally done through `MELODIC`. Here's an example:

```bash
melodic -i your_4D_data.nii -o ica_output --nobet --bgthreshold=10 --tr=2.0 --mmthresh=0.5 --Oall 
```

4. **FreeSurfer**

FreeSurfer does not provide a built-in function for performing ICA. It is primarily used for cortical surface reconstruction and analysis.

5. **MRtrix**

MRtrix3 does not have a direct ICA function, rather focuses on advanced tractography methodologies and quantitative analysis of diffusion MRI data.

6. **pure Python**

Python's `sklearn` library has an ICA implementation. Here is a basic example:

```python
from sklearn.decomposition import FastICA

# Assume "data" is a 2D numpy array where each row is a single time-point of your fMRI data.
# transpose it to make each column a time series (FastICA requires this).
data_T = data.T

# Initialize and run the ICA
ica = FastICA(n_components=20)
ica_components = ica.fit_transform(data_T)

# `ica_components` now holds the independent components of your data.
```

7. **SPM**

In SPM you could use the `spm_run_fmri_est` function to estimate models and run ICA. Here's an example:

```matlab
matlabbatch{1}.spm.stats.fmri_est.spmmat = {'/path/SPM.mat'};
matlabbatch{1}.spm.stats.fmri_est.write_residuals = 0;
matlabbatch{1}.spm.stats.fmri_est.method.Classical = 1;
spm_jobman('run', matlabbatch);
```

Please note this is a simplified overview, the parameters need to be adjusted based on your specific dataset and research question. Always consult the documentation or user manual to understand the full capabilities and parameters involved for each program/library!