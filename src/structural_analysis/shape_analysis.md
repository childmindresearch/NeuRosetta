# Shape Analysis

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
3dSkullStrip -input /path/to/input.nii -prefix /path/to/output.nii
```

## <img src="../../icons/ants.png" height="24px" /> ANTs

```bash
antsRegistrationSyN.sh -d 3 -f /path/to/fixedImage.nii -m /path/to/movingImage.nii -o /path/to/output
```

## <img src="../../icons/fsl.png" height="24px" /> FSL

```bash
bet /path/to/input.nii /path/to/output.nii
```

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer

```bash
recon-all -s subject1 -i /path/to/input.nii -all
```

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix

```bash
dwibiascorrect ants -input /path/to/input.mif -output /path/to/output.mif
```

## <img src="../../icons/r.png" height="24px" /> R

```R
library(neurobase)
volume <- readnii("/path/to/input.nii")
len.volume <- length(volume)
```

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command

```bash
wb_command -volume-smoothing /path/to/input.nii 4 /path/to/output.nii
```

## <img src="../../icons/python.png" height="24px" /> Python

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

## <img src="../../icons/spm.png" height="24px" /> SPM

```matlab
spm('defaults', 'fmri');
spm_jobman('initcfg');
matlabbatch{1}.spm.spatial.preproc.channel.vols = {'/path/to/input.nii'};
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 0];
spm('run', matlabbatch);
```

Note: Always replace "/path/to/input.nii" with the path to your actual NIfTI file and "output.nii" to the desired output file. In the MATLAB example, the SPM MATLAB Toolbox should be in your MATLAB path.