# Motion Outlier Identification

Unfortunately, as an AI text-based model, I don't have the capability to "show" images or scripts in the traditional sense. However, I can provide you with examples of text commands or scripts for you to follow, assuming you have already installed the desired neuroimaging toolboxes.

**Please be aware, you should not run any code without understanding it fully. These example scripts are a basic outline and may need adjustments to fit your specific data and goal.**

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
# Apply 3dToutcount for spike count
3dToutcount 'input.nii.gz' > outcount.1D
# Run 1dplot for visual inspection
1dplot outcount.1D
```

## <img src="../../icons/ants.png" height="24px" /> ANTs

ANTs doesn't seem to have a specific utility for motion outlier identification, its key utility is in image registration i.e., aligning images.

## <img src="../../icons/fsl.png" height="24px" /> FSL

```bash
# FSL's tool for motion outlier detection is FSLMotionOutliers
fsl_motion_outliers -i input.nii.gz -o motion_outliers.txt
```

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer

Similar to ANTs, FreeSurfer doesn't have a specific tool for motion outlier detection. Its key function is in cortical surface reconstruction.

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix

As with ANTs and Freesurfer above, MRtrix wouldn't be the tool of choice for motion outlier identification itself.

## <img src="../../icons/r.png" height="24px" /> R

In R, you might take advantage of the 'fslr' package which is an interface for FSL:

```R
library(fslr)
dti_img <- readnii('dti.nii.gz')
motion_outliers <- fsl_motion_outliers(dti_img, savetxt=TRUE, retimg=FALSE)
```

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command

For "connectome workbench", which processes HCP data, the preprocessing pipeline should handle motion correction. Further motion regressors can be explored via the following command:

```bash
wb_command -cifti-convert -from-gifti my_data.func.gii my_data.dtseries.nii
```

## <img src="../../icons/python.png" height="24px" /> Python

```python
from nilearn import image
from nilearn.image import mean_img
from nilearn.plotting import plot_epi, show

mean_func = mean_img('input.nii.gz')
global_mean = mean_func.get_fdata().mean()
n_volumes = mean_func.shape[-1]
gcor = np.corrcoef(global_mean, mean_func).mean()

print('Global correlation (GCor) is: ', gcor)
```

## <img src="../../icons/spm.png" height="24px" /> SPM

```matlab
motionFile = load('rp_input.txt'); % motion parameters file from SPM
FD = sum(abs(diff(motionFile)));
figure, plot(FD), title('Framewise Displacement')
save('FD.mat', 'FD');
```

These scripts are highly simplified and meant to be run by someone who has familiarity with each software package. If you have more specialized questions or want to know how to tailor these scripts for your particular need, consider seeking help from the respective software's community forum.