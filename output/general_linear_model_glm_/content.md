I'm sorry but it's not possible to provide scripts for each software package you mentioned as they all have different functionalities and use cases. However, below you can find examples of GLM applications for some of these neuroimaging software. These examples will use hypothetical data as input: they may not run as-is and might need to be adapted to fit into your specific use-cases and data.

1. **AFNI:**

AFNI provides an integrated approach for GLM through 3dDeconvolve or 3dREMLfit commands:

```bash
3dDeconvolve -input data.nii \
    -nodata 30 0 \
    -polort 5 \
    -num_stimts 1 \
    -stim_file 1 'GAM' \
    -fout \
    -iresp 1 HRF.nii \
    -bucket stats.nii
```

2. **FSL:**

FSL uses 'fsl_glm' for GLM:

```bash
# Design matrix (X.mat) and contrast (X.con) files need created prior
fsl_glm -i input_data.nii.gz -d X.mat -c X.con --out_t=stat_out.nii.gz
```

3. **FreeSurfer:**

FreeSurfer includes mri_glmfit for GLM application:

```bash
mri_glmfit \
--y input.mgh \
--fsgd design.fsgd \
--C contrast.mtx \
--glmdir glm_results
```

4. **SPM (MATLAB):**

SPM is largely MATLAB-based and GLM is applied as a part of SPM.mat:

```MATLAB
matlabbatch{1}.spm.stats.fmri_spec.sess.cond.name = 'condition_name';
matlabbatch{1}.spm.stats.fmri_spec.sess.cond.onset = condition_onset;
matlabbatch{1}.spm.stats.fmri_spec.sess.cond.duration = condition_duration;
```

There's no direct approach to apply GLM in ANTS, MRtrix, and direct Python is not defined (although you can use nibabel in Python to perform similar tasks.). Usually, Python is used as a strategy for calling functions from toolboxes such as AFNI, ANTs, FSL, etc.

5. **nilearn (Python library):**

Nilearn, a Python module for neuroimaging computation, enables GLM at the level of the whole brain:

```python
from nilearn.glm.first_level import FirstLevelModel

first_level_model = FirstLevelModel(t_r)
first_level_model = first_level_model.fit('path_to_imaging_data', events='path_to_events.tsv')
```

**Note:** These scripts are provided as an illustrative guide to demonstrate the usage of GLM in different neuroimaging software. For actual use-cases, the scripts may need to be modified or enhanced as per your objective and requirements. Familiarity with neuroimaging data format, structures, software, and GLM is assumed. Always refer to the software's own documentation for accurate details.