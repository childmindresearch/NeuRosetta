# AFNI

AFNI uses 3dAllineate for affine transformations:

```bash
3dAllineate -base base_image.nii -input input_image.nii -prefix output_image.nii -1Dparam_apply '1D: 12@0'\''
```

# ANTs

ANTs uses antsApplyTransforms for applying transformations:

```bash
antsApplyTransforms -d 3 -i input.nii -r reference.nii -o output.nii -t [ transformMatrix.txt , 1 ]
```

# FSL

FSL uses flirt for affine transformations:

```bash
flirt -in input_image.nii -ref ref_image.nii -out output_image.nii -omat transform_matrix.mat
```

# FreeSurfer

FreeSurfer uses mri_convert for transforms:

```bash
mri_convert --in_type nii --out_type nii --apply_transform transform.m3z --out_orientation RAS input_image.nii.gz output_image.nii.gz
```

# MRtrix

MRtrix uses mrtransform for affine transformations:

```bash
mrtransform input.mif -linear transform.txt -inverse output.mif
```

# Python

Python can leverage the `nipy` package for affine transformations:

```python
from nipy.algorithms.registration import resample
from nipy import load_image, save_image

# Load the images
target_img = load_image('target_image.nii')
source_img = load_image('input_image.nii')

# Specify the affine transformation
affine_transform = np.eye(4)

# Apply the transform
resampled_img = resample(source_img, target_img.coordmap, target_img.shape, target_img.affine)

# Save the image
save_image(resampled_img, 'output_image.nii')
```

# SPM

SPM can do affine transformations using its `spm_matrix` and `spm_slice_vol` functions:

```matlab
% Load image
V = spm_vol('input_image.nii');

% Define affine transformation matrix
M = spm_matrix([0 0 0 0 0 0 1 1 1 0 0 0]);

% Reslice the image
new_vol = spm_create_vol(spm_vol(V.fname), V.private);
for i = 1:V.dim(3),
    M_ = inv(spm_matrix([0 0 -i])*inv(new_vol.mat)*M);
    new_vol = spm_slice_vol(V, M_, V.dim(1:2), 1);

    % Save the slice to a new image
    spm_write_vol(new_vol, slice);
end;
``` 

Please replace 'input_image.nii', 'output_image.nii', and 'transform_matrix.mat' with your own filenames and parameters as necessary.