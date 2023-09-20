Sure, let's go over an example script that performs volume visualization in each of these programs.

1. AFNI:

```bash
afni my_volume_file.nii
```

This simple command will open the AFNI GUI and allow you to visualize the volume.

2. ANTs:

```bash
ThresholdImage 3 input.nii.gz output.nii.gz 2 5
```

This command thresholds an image, keeping only intensities between 2 and 5. ANTs is more about processing rather than viewing, so then use your favorite viewer to visualize `output.nii.gz`.

3. FSL: 

```bash
fslview my_volume_file.nii.gz
```

This command will open your volume nifti file with FSL's viewer.

4. FreeSurfer:

```bash
freeview -v 
    /usr/local/freesurfer/subjects/bert/mri/T1.mgz:colormap=grayscale: 
    /usr/local/freesurfer/subjects/bert/mri/wm.mgz:colormap=lut:opacity=0.2 
    -f /usr/local/freesurfer/subjects/bert/surf/lh.pial:edgecolor=yellow 
    /usr/local/freesurfer/subjects/bert/surf/rh.pial:edgecolor=yellow 
    /usr/local/freesurfer/subjects/bert/surf/lh.white:edgecolor=green 
    /usr/local/freesurfer/subjects/bert/surf/rh.white:edgecolor=green 
    /usr/local/freesurfer/subjects/bert/surf/lh.inflated:edgecolor=red 
    /usr/local/freesurfer/subjects/bert/surf/rh.inflated:edgecolor=red
```

This command will open T1 and white matter volumes and pial, white, and inflated surfaces in Freesurfer's viewer.

5. MRtrix:

```bash
mrview my_volume.mif
```

This command will open your volume file with MRtrix viewer.

6. pure Python:

```python
import matplotlib.pyplot as plt
import nibabel as nib

img = nib.load("my_volume_file.nii.gz")
data = img.get_fdata()

plt.figure()
plt.imshow(data[:, :, data.shape[2] // 2])
plt.show()
```

This script will load your volume file and display a slice in the middle axis using matplotlib and nibabel.

Please note that all the examples require the respective software (AFNI, ANTs, FSL, FreeSurfer, MRtrix3 and Python with nibabel, matplotlib libraries) and access to the files in the examples. Replace "my_volume_file.nii" and other related file paths with your actual data file path. 

7. SPM (Matlab/Octave):

```matlab
spm('createintwin');
spm('display','my_volume_file.nii');
```

This script will create an interactive window using SPM and display the specified volume image.

Note that this is very basic usage of visualization tools. All of these software applications have advanced options to inspect your images in detail, apply transformations, adjust color maps, and many other operations. For more advanced usage, please refer to the documentation provided by the developers of the software. 
In the case of pure Python, there are many different libraries to handle and inspect neuroimaging data.