Shape analysis in brain imaging is a complex process that often involves several steps like preprocessing, segmentation, and statistical analysis. To keep things minimal yet informative, I'll provide short examples of scripts often used as a part of these steps. However, please keep in mind that these examples might not conduct full "shape analysis" but rather reflect important steps used as part of these processes. 

1. **AFNI**
AFNI (Analysis of Functional NeuroImages) is a set of software libraries designed for analyzing 4D Time-Series images.

```bash
#!/bin/bash
#Run spatial normalization with 3dQwarp
3dQwarp -source $brain -base MNI152_T1_2mm_brain.nii.gz -prefix $outnorm -blur 0 3
```

2. **ANTs**
ANTs (Advanced Normalization Tools) is a state-of-the-art medical image registration and segmentation toolkit.

```bash
#!/bin/bash
#Run registration
antsRegistrationSyN.sh -d 3 -f fixed.nii.gz -m moving.nii.gz -o output
```

3. **FSL**
FSL (FMRIB Software Library) is a comprehensive library of analysis tools for FMRI, MRI and DTI brain imaging data. 

```bash
#!/bin/bash
#Run brain extraction
bet input.nii.gz output.nii.gz -R
```

4. **FreeSurfer**
FreeSurfer is a set of tools for analysis and visualization of structural and functional brain imaging data.

```bash
#!/bin/bash
#Run cortical reconstruction
recon-all -i input.nii.gz -subject output -all
```

5. **MRtrix**
MRtrix provides a large suite of tools for image processing, particularly of diffusion-weighted MRI datasets.

```bash
#!/bin/bash
# Run dwi preprocessing
dwipreproc input_dwi.mif output_dwi_preproc.mif -rpe_none -pe_dir AP -eddy_options " --slm=linear ".
```

6. **SPM**
SPM (Statistical Parametric Mapping) is a statistical technique for examining differences in brain activity recorded during fMRI.

```python
# This is not pure Python. It is a mix of Matlab (which SPM uses) and Python
# which serves only as a demonstration.

# In Matlab
spm('defaults', 'FMRI');
spm_jobman('initcfg');
matlabbatch{1}.spm.spatial.preproc.channel.vols = {'<UNDEFINED>'};
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 1];
...
...
save('myjob', 'matlabbatch');

# In Python
import subprocess
subprocess.call(["matlab", "-nodesktop", "-nosplash", "-r", "run('myjob.m');exit;"])
```

Keep in mind links into full scripts for shape analysis may provide more useful information than presented here because it's a process that spans usually multiple steps (preprocessing, segmentation, statistical analysis, etc).