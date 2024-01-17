[Edit on GitHub](https://github.com/childmindresearch/NeuRosetta/edit/main/src/quality_control/image_quality_assessment.md)
# Image Quality Assessment

Here are scripts for each software package you mentioned. These scripts do a basic image quality assessment by displaying image information, calculating image statistics, and checking for corruption or errors in the image file. The exact nature of the image quality assessment will vary depending on the capabilities of each software package. 

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
3dinfo -verb image.nii.gz
3dBrickStat -mean -var -max -min image.nii.gz
```

## <img src="../icons/ants.png" height="24px" /> ANTs
```bash
PrintHeader image.nii.gz
ImageMath 3 OutImage.nii.gz Normalize image.nii.gz
```

## <img src="../icons/fsl.png" height="24px" /> FSL
```bash
fslinfo image.nii.gz
fslstats image.nii.gz -R -m
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
mri_info image.mgz
mri_segstats --i image.mgz
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
```bash
mrinfo image.mif
mrstats image.mif
```

## <img src="../icons/r.png" height="24px" /> R
```R
library(oro.nifti)
nii <- readNIfTI("image.nii.gz", reorient = FALSE)
summary(nii)
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
wb_command -file-information image.nii.gz
wb_command -volume-stats image.nii.gz
```

## <img src="../icons/python.png" height="24px" /> Python
```python
import nibabel as nib

img = nib.load('image.nii.gz')
print(img.header)
print('Data shape:', img.shape)
print('Data type:', img.get_data_dtype())
```

## <img src="../icons/spm.png" height="24px" /> SPM
```matlab
V = spm_vol('image.nii');
data = spm_read_vols(V);
fprintf('Dimensions: %d %d %d\n', V.dim);
meanVal = mean(data(:));
stdDevVal = std(data(:));
fprintf('Mean and deviation: %f %f\n', meanVal, stdDevVal);
```

Please note that in actual practice, comprehensive Image Quality Assessment usually involves more complex methods and metrics. These scripts just represent a simple first inspection of the data.