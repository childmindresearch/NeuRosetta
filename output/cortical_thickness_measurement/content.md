I'm sorry for the confusion, but it's not possible to write a text script that is capable of performing Cortical Thickness Measurement in these software. This is because they require a GUI and user inputs to perform any action. Hower, I can provide basic command-line usage for each of them:

1. **AFNI**
   
   AFNI doesn't directly compute cortical thickness, but it can be computed as a distance between the white and pial surfaces extracted from FreeSurfer. Here is the command to extract the white surface:

   ```shell
   3dSurf2Vol -spec lh.white.spec -surf_A smoothwm -gridset epi+orig -map_func ave -oob_nan -prefix lh.white.epi
   ```

2. **ANTs**
   
   ANTs uses `antsCorticalThickness.sh` for cortical thickness estimation. Here is a simple example
   
   ```shell
   antsCorticalThickness.sh -d 3 -a T1.nii.gz -e Template.nii.gz -m ProbabilityMask.nii.gz -p SegmentPosteriors%d.nii.gz -o Output
   ```
   
3. **FSL**

   FSL doesn't directly measure cortical thickness, but `FIRST` can be used for subcortical structures analysis. Here is an example:

   ```shell
   run_first_all -i T1.nii.gz -o Output
   ```
   
4. **FreeSurfer**

   In FreeSurfer, `recon-all` can be used to perform full cortical reconstruction and thickness estimation.

   ```shell
   recon-all -i T1.nii.gz -s subject -all
   ```
   
5. **MRtrix**

   MRtrix also doesn't directly compute cortical thickness, but it provides pipelines for diffusion MRI analysis. 

6. **Python**

   There isn't any pure python package that can perform cortical thickness measurement directly. Normally, python is used as a glue language to run these software packages and to analyze the output. 

   However, libraries such as nibabel can be used to load MRI data in python:

   ```python
   import nibabel as nib
   img = nib.load('T1.nii.gz')
   data = img.get_fdata()
   ```

7. **SPM**

   SPM uses CAT12 toolbox for computation of cortical thickness.

   ```
   matlabbatch{1}.spm.tools.cat.estwrite.data = {'/path/to/T1.nii,1'};
   matlabbatch{1}.spm.tools.cat.estwrite.nproc = 0;
   spm('defaults', 'FMRI');
   spm_jobman('run', matlabbatch);
   ```

Please note that each of these software are quite complex and there is a good amount of preprocessing required before one can estimate cortical thickness. Always refer to the official documentation of each software for a thorough understanding.