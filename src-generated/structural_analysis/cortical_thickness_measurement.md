1. AFNI
```bash
3dSkullStrip -input INPUT.nii -o_ply OUTPUT.ply
```
2. ANTs
```bash
antsCorticalThickness.sh -d 3 -a T1.nii -e TEMPLATE -o OUTPUT
```
3. FSL
```bash
fast -t 1 -n 3 -H 0.1 -I 4 -l 20.0 -g -B -b OUTPUT.nii
```
4. FreeSurfer
```bash
recon-all -i INPUT.nii -s SUBJECT -all
```
5. MRtrix
```bash
5ttgen fsl INPUT.nii OUTPUT.nii
```
6. R
```R
library(oro.nifti)
nii <- readNIfTI("INPUT.nii", reorient=FALSE)
ct.measure(nii)
```
7. Workbench Command
```bash
wb_command -volume-to-surface-mapping INPUT.nii OUTPUT.surf.gii -trilinear
wb_command -surface-smoothing OUTPUT.surf.gii 5 OUTPUT_SMOOTH.surf.gii
wb_command -surface-to-volume-mapping OUTPUT_SMOOTH.surf.gii INPUT.nii OUTPUT.nii
```
8. Pure Python
```python
import nibabel as nib
from nipype.interfaces import ants

image = nib.load('INPUT.nii')

seg = ants.AntsCorticalThickness()
seg.inputs.dimension = 3
seg.inputs.anatomical_images = 'INPUT.nii'
seg.inputs.brain_template = 'TEMPLATE.nii'
# ... More options here
seg.run()
```
9. SPM (via a MATLAB script)
```matlab
spm('Defaults', 'FMRI');
spm_jobman('initcfg');
matlabbatch{1}.spm.tools.cat.estwrite.data = {'/path/to/your/nifti.nii,1'};
matlabbatch{1}.spm.tools.cat.estwrite.output.surface = true;
spm('run', matlabbatch);
```

Please note that these are very basic examples and you would likely need to adjust parameters to get acceptable results in each toolkit. You would also need to check that images are in the right space, voxel size, orientation, and so on for the given method. Also, actual use would require that you set up your environment variables correctly for each package.

Lastly, you might need to preprocess (like N4BiasFieldCorrection, Registration, etc.) or postprocess (like Laplacian, ROI Extraction, etc.) the data depending on your actual application scenario.