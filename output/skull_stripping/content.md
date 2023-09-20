Sure, here are some script examples for doing brain skull stripping with different neuroimaging tools. In each of these examples, `input.nii` is the name and extension of the input MRI and `output.nii` is the name and extension of the output after skull stripping.

1. AFNI:

```bash
# AFNI
3dSkullStrip -input input.nii -output output.nii
```

2. ANTs:

```bash
# ANTs
antsBrainExtraction.sh -d 3 -a input.nii -e template.nii -m probability_mask.nii -o output
```

3. FSL:

```bash
# FSL
bet input.nii output.nii
```

4. FreeSurfer:

```bash
# FreeSurfer
mri_convert input.nii input.mgz
mri_watershed -h 40 input.mgz output.mgz
mri_convert output.mgz output.nii
```

5. MRtrix:

```bash
# MRtrix
5ttgen fsl input.nii output.nii
```

6. Pure Python:

```python
# pure Python using nibabel and nilearn libraries
import nibabel as nib
from nilearn.masking import compute_brain_mask

input_img = nib.load('input.nii')
brain_mask = compute_brain_mask(input_img)

# Save the mask
output_img = nib.Nifti1Image(brain_mask.astype(float), input_img.affine)
nib.save(output_img, 'output.nii')
```

7. SPM:

```matlab
% SPM
matlabbatch{1}.spm.tools.oldseg.data = {'input.nii'};
matlabbatch{1}.spm.tools.oldseg.output.GM = [0 0 1];
matlabbatch{1}.spm.tools.oldseg.output.WM = [0 0 1];
matlabbatch{1}.spm.tools.oldseg.output.CSF = [0 0 0];
spm_jobman('run',matlabbatch);

GM = spm_read_vols(spm_vol('c1input.nii'));
WM = spm_read_vols(spm_vol('c2input.nii'));
brain_mask = GM + WM > 0.2;
spm_write_vol(spm_vol(input.nii), brain_mask.*spm_read_vols(spm_vol(input.nii)));
```

**Note:** Make sure the input image is in the same directory as the scripts or specify absolute path. For example: `/Users/[yourusername]/Desktop/input.nii`. Also, some scripts generate brain tissue probability maps, white matter maps, or partial volume estimations along with skull-stripped brain.