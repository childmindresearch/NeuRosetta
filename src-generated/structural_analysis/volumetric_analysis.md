Of course. Here are minimal examples of volumetric analysis scripts for each of the requested neuroimaging and programming softwares and packages. Please, remember that these are only basic examples and make sure to modify them according to the specific requirements of your analysis.

#### AFNI
```bash
3dvolreg -prefix registered_data -base master_image.nii.gz input_data.nii.gz
```
#### ANTs
```bash
AntsMotionCorr -d 3 -a input_data.nii.gz -o registered_data.nii.gz -m MI[background.nii.gz, input_data.nii.gz, 1, 32]
```
#### FSL
```bash
fslmaths input_data.nii.gz -Tmean output_volume.nii.gz
```
#### FreeSurfer
```bash
recon-all -i input_data.nii.gz -all -subject subject1
asegstats2table --subjectsfile sub_list.txt --meas volume --tablefile output_table.txt
```
#### MRtrix
```bash
mrconvert dwi.mif dwi.nii.gz
dwi2response dhollander dwi.nii.gz RF_WM.txt RF_GM.txt RF_CSF.txt
```
#### R
```R
library(neurobase)
vol_data <- readnii("input_data.nii.gz")
vol_mean <- apply(vol_data, c(1:3), mean)
```
#### Workbench Command
```bash
wb_command -volume-math "(x > 0) * x" mask.nii.gz -var x input_data.nii.gz
```
#### Pure Python
```python
import nibabel as nib
img = nib.load('input_data.nii.gz')
data = img.get_fdata()
mean_volume = data.mean(axis=(0, 1, 2))
```
#### SPM (via a MATLAB script)
```MATLAB
spm('defaults', 'FMRI');
matlabbatch{1}.spm.spatial.preproc.channel.vols = {'input_data.nii,1'};
matlabbatch{1}.spm.spatial.preproc.channel.write = [0 1];
spm_jobman('run', matlabbatch);
```
Remember, these are highly simplified examples. The specifics of the analyses could be complex and may require additional steps or parameters. Ensure to verify and match your work with the official documentation or reach out to the community forum/support for help with these software.