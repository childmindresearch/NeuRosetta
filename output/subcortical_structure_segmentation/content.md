I'm sorry for any misunderstanding but I cannot provide actual visual imaging or coding results. However, I can give you examples of code snippets used for subcortical structure segmentation in the mentioned software. Remember to handle path and file names accordingly because these will vary in your specific system.

**1. AFNI**:

```bash
3dSeg -anat struct.nii -mask AUTO
```

**2. ANTs**:

```bash
antsAtroposN4.sh -d 3 -a struct.nii -x mask.nii -c 2 -o output
```

**3. FSL**:

```bash
fast -t 1 -n 3 -H 0.1 -I 4 -l 20.0 -g -o output struct.nii
```

**4. FreeSurfer**:

```bash
recon-all -s subject1 -i struct.nii -all
```

**5. MRtrix**:

MRtrix doesn't directly have a functionality for subcortical structure segmentation, you will likely have to use it in combination with FreeSurfer.

```bash
5ttgen fsl struct.nii output.mif
```

**6. SPM (Matlab)**:

```matlab
clear matlabbatch;
matlabbatch{1}.spm.spatial.preproc.channel.vols = {'struct.nii,1'};
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 0];
matlabbatch{1}.spm.spatial.preproc.tissue(1).tpm = {'/path/to/tpm.nii,1'};
matlabbatch{1}.spm.spatial.preproc.tissue(1).ngaus = 1;
spm_jobman('run', matlabbatch);
```

**7. Pure Python**:

You may use Python packages like nibabel, nipype and nilearn, here's an example using nipype to wrap FSL's FAST tool.

```python
from nipype.interfaces import fsl

fast = fsl.FAST()
fast.inputs.in_files = 'struct.nii'
fast.inputs.segments = True
res = fast.run()
```

Among these packages, generally, FreeSurfer is well reputed for good subcortical structure segmentation, although each package has its strengths and weaknesses and many researchers use a mix of tools to get the best results.
  
These scripts should work provided the rest of the software (FSL, AFNI, FreeSurfer etc.) is correctly setup and installed, and the data files (in these examples 'struct.nii' etc.) are yours to substitute in. Keep in mind that, these are just simple example usage, actual use requires careful reading of each software's manual and tuning parameters accordingly.