I'm sorry, but providing complete scripts for each of these tools would be beyond the capabilities due to their complexity. However, let me give you a general idea of how to do Motion Outlier Identification with each of them:

1) AFNI:

```sh
3dToutcount -automask -fraction -polort 4 -legendre pb00.r01.tshift+orig > outcount.1D
```
This command saves the 'fraction of voxel time series points that are outliers' for each volume in the dataset.

2) ANTs: 

ANTs itself doesn't have a specific tool for motion outlier detection. But you can use basic image similarity metrics functions here: [ANTs](https://github.com/ANTsX/ANTs)

3) FSL:

```sh
fsl_motion_outliers -i input_data -o motion_outliers
```
This command searches through the specified input data for volumes that are outliers in terms of their head-motion estimates or their global mean intensity.

4) FreeSurfer:

FreeSurfer primarily focuses on structural MRI data and does not directly handle motion correction or motion outlier identification. However, it can use motion correction parameters provided by other software like FSL or AFNI.

5) MRtrix:

In MRtrix, outlier detection in the context of motion is embedded into tools that perform motion correction such as `dwipreproc` which uses the `eddy` tool from FSL.

6) pure Python/SPM:

SPM also doesn't directly handle motion outlier identification, However, you can use spm_realign or spm_regress in SPM to estimate motion and then use a tool like the Artifact Detection Tools (ART) toolbox to identify outliers. For Python, you can use the nipype library to do it.
    
Note: Codes above are minimal and may require a proper setup and additional arguments. This is just to give a rough idea and is not a comprehensive guide for motion outlier identification using these software packages.