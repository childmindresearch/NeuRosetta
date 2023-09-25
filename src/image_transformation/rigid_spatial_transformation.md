# Rigid Spatial Transformation

Here are examples of scripts that perform rigid spatial transformations in each package asked.

## <img src="../../icons/afni.png" height="24px" /> AFNI
```bash
3dAllineate -base base_image.nii -input input_image.nii -prefix output_image.nii -1Dmatrix_save rigid_mat.1D
```
  
## <img src="../../icons/ants.png" height="24px" /> ANTs
```bash
antsRegistrationSyNQuick.sh -d 3 -f fixed.nii -m moving.nii -o output.nii -t r
```
  
## <img src="../../icons/fsl.png" height="24px" /> FSL
```bash
flirt -in input_image.nii -ref reference_image.nii -out output_image.nii -omat rigid_mat.mat -dof 6
```
  
## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
mri_coreg --s subject --mov input_image.nii --reg output.mgz
```
    
## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix
```bash
mrregister fixed.nii moving.nii -rigid output.mif
```
    
6. **R** (with the 'RNifti' package)
```R
library(RNifti)
image <- readNifti("input_image.nii")
transformed <- rotate(image, theta = c(0,0,pi/4))
writeNifti(transformed, "transformed_image.nii")
```
  
## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
wb_command -volume-affine-resample input.nii affine.mat mm cubic output.nii
```
  
## <img src="../../icons/spm.png" height="24px" /> SPM
```python
import matlab.engine
eng = matlab.engine.start_matlab()

matlab_code = """
spm('defaults', 'PET');
spm_jobman('initcfg');
matlabbatch{1}.cfg_basicio.file_dir.file_ops.file_fplist.dir = {'/path_to/input'};
matlabbatch{1}.cfg_basicio.file_dir.file_ops.file_fplist.filter = '.*\.nii$';
matlabbatch{1}.cfg_basicio.file_dir.file_ops.file_fplist.rec = 'FPList';
matlabbatch{1}.spm.spatial.coreg.estimate.ref = {'/path_to/reference_image.nii,1'};
matlabbatch{1}.spm.spatial.coreg.estimate.source(1) = cfg_dep('File Selector (Batch Mode): Selected Files (^.*\.nii$)', substruct('.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','files'));
matlabbatch{1}.spm.spatial.coreg.estimate.other = {''};
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.cost_fun = 'nmi';
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.sep = [4 2];
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.tol = 
           [0.02 0.02 0.02 0.001 0.001 0.001 0.01 0.01 0.01 0.001 0.001 0.001];
matlabbatch{1}.spm.spatial.coreg.estimate.eoptions.fwhm = [7 7];

spm_jobman('run', matlabbatch);
"""
eng.eval(matlab_code, nargout=0)
```

Please replace paths and specific function parameters according to your requirements.

Also, please note that these are simple and basic examples only. More complex operations may require additional commands or options. Be aware that every single software has a different kind of batch processing command system and different capabilities. Therefore, it's important to dig into the official documentation of each of them to deeply understand how they work and how you can adapt them to your needs.