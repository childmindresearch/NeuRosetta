[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/quality_control/outlier_detection.md)
# Outlier Detection

below are examples of scripts in each of the mentioned softwares and languages to perform Outlier Detection. Please take into account that these are minimal examples and might need to be adjusted based on your particular needs and datasets.

## <img src="../icons/afni.png" height="24px" /> AFNI
```bash
3dToutcount -automask -fraction -polort 4 -legendre func_srt.nii > outcount.1D
```

## <img src="../icons/ants.png" height="24px" /> ANTs
In ANTs there isn't a direct function for outlier detection, but you can use the ImageMath function and statistical methods to do so:
```bash
ImageMath 3 output.nii Kmeans image.nii 2
```

## <img src="../icons/fsl.png" height="24px" /> FSL
Here is an example using fsl_motion_outliers:
```bash
fsl_motion_outliers -i input.nii.gz -o confound_ev.txt -s output_metric_values.txt -p plot.png
```

## <img src="../icons/freesurfer.png" height="24px" /> FreeSurfer
```bash
mri_binarize --i input.mgz --o binary_vol.mgz --min .00001
```

## <img src="../icons/mrtrix.png" height="24px" /> MRtrix
MRtrix doesn't have specific command for outlier detection, but it can be done through certain steps in the diffusion processing pipeline such as dwidenoise, mrdegibbs and dwifslpreproc.

## <img src="../icons/r.png" height="24px" /> R
```R
data <- read.csv("data.csv")
boxplot.stats(data$column)$out
```

## <img src="../icons/workbench_command.png" height="24px" /> Workbench Command
```bash
wb_command -cifti-outlier-count my_data.dscalar.nii 2 2 count_outliers.dscalar.nii -above 1
```

## <img src="../icons/spm.png" height="24px" /> SPM
```python
import matplotlib.pyplot as plt
from scipy.io import loadmat
data = loadmat('data.mat')['data']
outliers = data[abs(data - np.mean(data)) > 2 * np.std(data)]
plt.plot(data)
plt.plot(outliers, 'ro')
plt.show()
```

Just make sure to replace "data.csv" with your own csv file and "column" with the column you want to detect for outliers in the R script; "my_data.dscalar.nii" with your own .nii file in the Workbench Command script; and 'data.mat' with your own .mat file in the Pure Python SPM script.