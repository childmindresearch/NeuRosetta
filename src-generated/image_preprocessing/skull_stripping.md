Sure, here's an example of running Skull Stripping on different neuroimaging software. However, each tool has a slightly different approach or method for performing Skull Stripping:

1. **AFNI**
```bash
3dSkullStrip -input <input_brain.nii.gz> -prefix <output_brain.nii.gz>
```

2. **ANTs**
```bash
antsBrainExtraction.sh -d 3 -a <input_brain.nii.gz> -e <brain_template.nii.gz> -m <probability_mask.nii.gz> -o <output_brain>
```

3. **FSL**
```bash
bet <input_brain> <output_brain> -R -f 0.5 -g 0 -m
```

4. **FreeSurfer**
```bash
mri_convert <input_volume> <input_volume.mgz>
mri_watershed -T1 <preSkullStripped.mgz> <skullStripped.mgz>
mri_convert <skullStripped.mgz> <output_volume>
```

5. **MRtrix**
```bash
5ttgen fsl <input_brain.nii.gz> <5tt.mif> -premasked
mrconvert <5tt.mif> <output_brain.nii.gz>
```

6. **R**
```R
library(neurobase)
output_brain <- fslbet(input_brain, retimg=TRUE, opts="-R -f 0.5 -g 0")
```

7. **Workbench Command**
```bash
wb_command -volume-remove-islands <input_brain.nii.gz> <output_brain.nii.gz>
```

8. **pure Python (with nibabel and nilearn)**
```python
from nilearn import masking
import nibabel as nib

img = nib.load('brain.nii.gz')
mask_img = masking.compute_epi_mask(img)
mask_img.to_filename('brain_mask.nii.gz')
```

9. **SPM (via a MATLAB script)**
```matlab
matlabbatch{1}.spm.tools.oldseg.data = {'<input_brain.nii,gz>'};
matlabbatch{1}.spm.tools.oldseg.output.GM = [0 0 1];
matlabbatch{1}.spm.tools.oldseg.output.WM = [0 0 1];
matlabbatch{1}.spm.tools.oldseg.output.CSF = [0 0 1];
spm_jobman('run', matlabbatch);
```
Please replace the placeholders \<input_brain\>, \<brain_template\>, \<probability_mask\>, \<output_brain\> and \<output_volume\> with actual file names. Also note that usage may differ depending on data types and specific needs of the experiment. Do ensure to check the documentation for each toolkit to fully understand how they function.