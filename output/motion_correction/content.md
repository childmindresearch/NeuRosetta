Sure, here are the basic scripts for motion correction in different neuroimaging software packages. Please replace the placeholders `<input_file>` and `<output_file>` with your actual file names. 

1. **AFNI**:

```bash
#!/bin/bash
3dvolreg -twopass -1Dfile <motion.1D> -prefix <output_file> -base 0 <input_file>
```

2. **ANTs**:

```bash
#!/bin/bash
antsMotionCorr -d 3 -a <input_file> -o <output_file>
```

3. **FSL**:

```bash
#!/bin/bash
mcflirt -in <input_file> -out <output_file> -mats -plots -reffile <reference_vol> -rmsrel -rmsabs
```

4. **FreeSurfer**:

```bash
#!/bin/bash
mri_motion_correct.fsl --i <input_file> --o <output_file> --use-gradient --meanvol
```

5. **MRtrix**:

```bash
#!/usr/bin/env bash
mrregister <input_file> -type rigid -mask1 <mask_image> <reference_image> <output_file>
```

6. **SPM (in MATLAB)**:

```matlab
spm('defaults','fmri');
matlabbatch{1}.spm.spatial.realign.estwrite.data = {'<input_file>,1'};
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.sep = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.fwhm = 5;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.rtm = 1;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.interp = 2;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.weight = '';
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.which = [2 1];
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.interp = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.mask = 1;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.prefix = 'r';
spm_jobman('run',matlabbatch);
```

7. **Python (using Nipype)**:

```python
from nipype.interfaces import spm

realign = spm.Realign()
realign.inputs.in_files = '<input_file>'
realign.inputs.register_to_mean = True
realign.run() 
```

Please note that all of these are basic scripts and some options might need to be adjusted to fit your specific use-case. Nipype in Python can wrap modules from other software tools like FSL, AFNI, and SPM, making it a versatile option for many neuroimaging processing pipelines.