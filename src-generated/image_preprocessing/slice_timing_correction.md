In many brain imaging software contexts, Slice Timing Correction is quite a complicated process that includes complex script lines and requires understanding of the related terminologies and methods. However, I can give short basic examples of command lines for some of the software you mentioned. Please note that the actual scripts will differ and are more complex depending on which options and parameters you are using in each case.

1. AFNI:
```bash
3dTshift -prefix output.nii -tpattern alt+z -TR 2s input.nii
```

2. ANTs:
ANTs does not directly support slice timing correction. Instead, you would typically use it within the framework of another software (like SPM, FSL, AFNI, etc.), or use an external library like nipy.

3. FSL:
```bash
slicetimer --in=input.nii --out=output.nii --TR=2.5 --direction=z --odd
```

4. FreeSurfer:
FreeSurfer does not have direct support for Slice Timing Correction.

5. MRtrix:
MRtrix does not have built-in slice timing correction, it generally relies on the results obtained from other packages (FSL, SPM, etc.).

6. R:
```R
library(RNifti)
image <- readNifti("input.nii")
imageCorrected <- slicetiming(image,tr=2,direction=3)
writeNifti(imageCorrected, "output.nii")
```

7. Workbench Command:
Workbench does not provide a direct command for slice timing correction.

8. Pure Python (Nipy):
```python
from nipy.algorithms.slicetimer.api import space_time_realign
volume = load('input.nii')
corrected_volume = space_time_realign(volume, tr=2.5, slice_order='ascending')
save(corrected_volume, 'output.nii')
```

9. SPM (via MATLAB script):
```matlab
spm('Defaults','fMRI');
spm_jobman('initcfg');
matlabbatch{1}.spm.temporal.st.scans = {'input.nii,1'};
matlabbatch{1}.spm.temporal.st.nslices = 32;
matlabbatch{1}.spm.temporal.st.tr = 2.5;
matlabbatch{1}.spm.temporal.st.ta = 2.4375;
matlabbatch{1}.spm.temporal.st.so = [1:1:32];
matlabbatch{1}.spm.temporal.st.refslice = 1;
spm('run', matlabbatch);
```
Remember to replace 'input.nii', 'output.nii' and other parameters with your actual input file, output file, and actual parameters.