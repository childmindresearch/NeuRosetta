Sure, below is a basic example script to perform bias field correction in the mentioned software. Remember, the example here assumes that the original image is named "input.nii" and the corrected image will be "output.nii".

1. AFNI:
```shell
3dUnifize -input input.nii -prefix output.nii
```

2. ANTs:
```shell
N4BiasFieldCorrection -d 3 -i input.nii -o output.nii
```

3. FSL:
```shell
fast -B -v -o output input.nii
```

4. FreeSurfer:
```shell
mri_nu_correct.mni --i input.nii --o output.nii
```

5. MRtrix:
```shell
dwibiascorrect -ants input.mif output.mif
```

6. SPM (MATLAB):
```Matlab
spm('defaults','fmri');
spm_jobman('initcfg');
matlabbatch{1}.spm.spatial.preproc.channel(1).vols = {'input.nii'};
matlabbatch{1}.spm.spatial.preproc.channel(1).biasreg = 0.001;
matlabbatch{1}.spm.spatial.preproc.channel(1).biasfwhm = 60;
matlabbatch{1}.spm.spatial.preproc.channel(1).write = [0 1];
spm_jobman('run',matlabbatch);
```
Please replace 'spm' with your installed SPM-version number if needed. 

7. Pure Python (using N4ITK - needs SimpleITK):
```python
import SimpleITK as sitk

image = sitk.ReadImage('input.nii')
corrector = sitk.N4BiasFieldCorrectionImageFilter() 
output = corrector.Execute(image)

sitk.WriteImage(output, 'output.nii')
```

Please ensure to replace 'input.nii' and 'output.nii' with your actual file paths.