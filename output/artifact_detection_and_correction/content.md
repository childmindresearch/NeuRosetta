Unfortunately, writing a minimal script for each software in this context would be quite extensive and cannot be compressed into a concise format due to the complexity and variable usage of each package. However, I can outline the general approach and key commands used in each tool for artifact detection and correction. Please refer to the official documentation and tutorials for detailed scripting information. 

**1. AFNI**

- The main function used in AFNI for artifact detection is the `3dDespike` which is used to remove 'spikes' from the 3D+time input dataset. 

```bash
3dDespike -prefix output_dataset input_dataset
```

**2. ANTs**

- In ANTs, you can use the `N4BiasFieldCorrection` to correct for intensity non-uniformity artifacts.

```bash
N4BiasFieldCorrection -d 3 -i input.nii.gz -o output.nii.gz
```

**3. FSL**

- FSL's `FAST` (FMRIB's Automated Segmentation Tool) can be used for bias field correction.

```bash
fast -B -v -o output input.nii.gz
```

- `topup` and `eddy` are used to correct for susceptibility and eddy current artifacts:

```bash
topup --imain=my_images --datain=my_parameters.txt --config=b02b0.cnf --out=topup_results

eddy_openmp --imain=my_images --mask=brain_mask --acqp=my_parameters.txt --index=index.txt --out=eddy_results
```

**4. FreeSurfer**

- `mri_nu_correct.mni` and `mri_normalize` are the commands used to correct intensity non-uniformity artifacts:

```bash
mri_nu_correct.mni --i input.mgz --o output.mgz

mri_normalize -g 1 input.mgz output.mgz
```
    
**5. MRtrix**

- MRtrix provides dwidenoise for denoising raw diffusion data and mrdegibbs for Gibbs ringing artifact correction.

```bash
dwidenoise input.mif output.mif 

mrdegibbs input.mif output.mif
```

**6. SPM (Matlab-based, not pure Python)**

- SPM doesn't have a specific artifact detection and correction script. It's usually combined with other packages like ART (Artifact Detection Tools) for this purpose. SPM's `spm_smooth` function is commonly used in preprocessing:

```matlab
spm_smooth('input.nii', 'smoothed_input.nii', [8 8 8])
```
      
Please be aware that all commands depend on the correct previous steps which may include converting data into the correct format, applying masks correctly and setting the appropriate parameters.