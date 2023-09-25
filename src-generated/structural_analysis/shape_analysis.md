1. AFNI

```bash
3dSkullStrip -input /path/to/input.nii -prefix /path/to/output.nii
```

2. ANTs

```bash
antsRegistrationSyN.sh -d 3 -f /path/to/fixedImage.nii -m /path/to/movingImage.nii -o /path/to/output
```

3. FSL

```bash
bet /path/to/input.nii /path/to/output.nii
```

4. FreeSurfer

```bash
recon-all -s subject1 -i /path/to/input.nii -all
```

5. MRtrix

```bash
dwibiascorrect ants -input /path/to/input.mif -output /path/to/output.mif
```

6. R

```R
library(neurobase)
volume <- readnii("/path/to/input.nii")
len.volume <- length(volume)
```

7. Workbench Command

```bash
wb_command -volume-smoothing /path/to/input.nii 4 /path/to/output.nii
```

8. Pure Python (Using nibabel)

```python
import nibabel as nib

# Load nifti image
img = nib.load('/path/to/input.nii')

# Get data from image
img_data = img.get_fdata()

# Print shape of the image
print(img_data.shape)

# Save new image
new_img = nib.Nifti1Image(img_data, img.affine)
nib.save(new_img, "/path/to/output.nii")
```

9. SPM (via a MATLAB script)

```matlab
spm('defaults', 'fmri');
spm_jobman('initcfg');
matlabbatch{1}.spm.spatial.preproc.channel.vols = {'/path/to/input.nii'};
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 0];
spm('run', matlabbatch);
```

Note: Always replace "/path/to/input.nii" with the path to your actual NIfTI file and "output.nii" to the desired output file. In the MATLAB example, the SPM MATLAB Toolbox should be in your MATLAB path.