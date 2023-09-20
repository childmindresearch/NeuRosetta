Sure, here are some simple code snippets for performing intensity normalization in several brain imaging software packages:

**1. AFNI**
```bash
3dTstat -mean -prefix mean_volume.nii input_volume.nii
3dcalc -a input_volume.nii -b mean_volume.nii -expr 'a/b' -prefix normalized_volume.nii
```

**2. ANTs**

You can use "N4BiasFieldCorrection" from ANTs for intensity normalization.
```bash
N4BiasFieldCorrection -d 3 -i input_volume.nii -o normalized_volume.nii 
```

**3. FSL**
```bash
fslmaths input_volume.nii -Tmean mean_volume.nii 
fslmaths input_volume.nii -div mean_volume.nii normalized_volume.nii
```

**4. FreeSurfer**
```bash
mri_normalize -mprage input_volume.nii normalized_volume.nii
```

**5. MRtrix**

In the Mrtrix, there is not a specific command for intensity normalization, but intensity scaling can be accomplished through the mathematical operations provided by the 'mrcalc' command.

```bash
mrcalc input_volume.mif -mean mean_volume.mif
mrcalc input_volume.mif mean_volume.mif -div normalized_volume.mif
```

**6. SPM (Matlab)**

Load the SPM GUI, then:

```matlab
matlabbatch{1}.spm.spatial.normalise.write.subj.def = {'/path/to/y_input_volume.nii'};
matlabbatch{1}.spm.spatial.normalise.write.subj.resample = {'/path/to/input_volume.nii'};
matlabbatch{1}.spm.spatial.normalise.write.woptions.vox  = [2 2 2];
spm_jobman('run',matlabbatch);
```

**7. Pure Python (nibabel and numpy example)**

```python
import nibabel as nib
import numpy as np

img = nib.load('input_volume.nii')
data = img.get_fdata()
mean_intensity = np.mean(data)
normalized_data = data / mean_intensity
normalized_img = nib.Nifti1Image(normalized_data, img.affine)
nib.save(normalized_img, 'normalized_volume.nii')
```

These scripts assume filenames and may need to be adapted to your specific database structure or preprocessing procedure. Always thoroughly check the output of each processing step.