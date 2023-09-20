It's important to note that performing surface visualization with these tools requires a preprocessed brain image data. The following scripts only provide some basic steps for surface generation or visualization:

**1. AFNI**

```bash
# Example on AFNI
3dVol2Surf -spec SUBJECTS_DIR/subject1/SUMA/subject1_lh.spec -surf_A smoothwm -grid_parent brain.nii -map_func ave -oob_index -1 -out_niml stdout | suma -spec SUBJECTS_DIR/subject1/SUMA/subject1_lh.spec -sv brain.nii
```

**2. ANTs**

```bash
# Example on ANTs. Here, ANTs is used to create the cortical thickness map - it itself does not have visualization tools.
antsCorticalThickness.sh -d 3 -a brain.nii -o output.nii
```

**3. FSL**

```bash
# Example on FSL
fslview_deprecated brain.nii -b 30,80 -r -Y 90 -x 0.5 -y 0.5 -z 0.5
```

**4. FreeSurfer**

```bash
# Example on FreeSurfer
recon-all -i brain.nii -s subject1 -all
tksurfer subject1 lh pial
```

**5. MRtrix**

```bash
# Example on MRtrix
mrview brain.nii -load tractogram.tck
```

**6. SPM (Matlab)**

```matlab
% Example on SPM (Matlab)
spm_surf('brain.nii',1,'brain_surface')
```

**7. Pure Python**

Python doesn't have a specific module for neuroimaging surface visualization by itself, but external libraries like `nilearn` can be used:

```python
# Example on Python with nilearn
from nilearn import plotting
plotting.plot_glass_brain("brain.nii")
```
Please modify the 'brain.nii', 'subject1' and other placeholders with your actual data.