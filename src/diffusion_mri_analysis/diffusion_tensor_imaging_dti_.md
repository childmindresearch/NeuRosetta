# Diffusion Tensor Imaging (DTI)

Unfortunately, it would be very complex and space-consuming to provide examples of how to conduct Diffusion Tensor Imaging (DTI) across all the different software you mentioned, as the processes are quite detailed. Additionally, some of these technologies (like Workbench Command) don't easily allow for DTI processing.

However, I can show short examples in FSL, MRtrix, and a Python-based tool named Dipy. These examples will be minimal and will need to be adjusted based on your specific dataset and research question.

## <img src="../../icons/fsl.png" height="24px" /> FSL
```bash
## <img src="../../icons/fsl.png" height="24px" /> FSL
# Preprocessing (eddy correct and brain extraction) omitted
dtifit --data=yourdata --out=youroutput --mask=yourmask --bvecs=bvecs --bvals=bvals
```

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix

```bash
# MRtrix3 tensor fitting
# Preprocessing (denoise, unring, dwi2mask, biascorrect) is omitted
dwi2tensor input - | tensor2metric - -fa output_FA.mif -adc output_MD.mif -rd output_RD.mif -ad output_AD.mif
```

## <img src="../../icons/python.png" height="24px" /> Python

```python
from dipy.reconst.dti import TensorModel
from dipy.data import fetch_stanford_hardi, read_stanford_hardi

# Download/load data
fetch_stanford_hardi()
img, gtab = read_stanford_hardi()

# Fit model and compute DTI metrics
tensor_model = TensorModel(gtab)
tensor_fit = tensor_model.fit(data, mask)
FA = tensor_fit.fa
```
For the usage of AFNI, ANTs, FreeSurfer, R, Workbench Command, or SPM (via a MATLAB script), you would need to look at their specific manuals or tutorials as DTI analysis procedures can be quite involved across different software.