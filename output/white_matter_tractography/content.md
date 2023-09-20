I'm sorry but creating scripts for all of the mentioned software would be quite long and complex due to the vital differences each one has and the prerequisites needed such as specific input data formats and toolbox calls. However, I'm glad to provide sample pseudocode or individual command lines for some of the platforms:

**1. AFNI**

AFNI wouldn't be my first choice for tractography specifically, but here is a basic 3dDWItoDT + 3dTrackID pipeline:

```bash
3dDWItoDT -prefix dt -evec_prefix evec -eval_prefix eval -sep_dsets prefix DwEff.evec1 DwEff.evec2 DwEff.evec3
3dTrackID -mode DET -dti_in dt+orig. -prefix DetPTrack -uncert DwEff.UNCERT+orig -netrois ROI_ICMAP+orig
```

**2. ANTs**

ANTs doesn't really perform tractography, rather it is used for image registration, and normalization. You can however use it in combination with other software, for example: FSL, MRtrix, Dipy.

**3. FSL (using FDT and BEDPOST)**

```bash
# Run DTIFit to get tensor model
dtifit --data=data.nii.gz --out=dtifit --mask=mask.nii.gz --bvecs=bvecs --bvals=bvals

# Run BEDPOSTX to estimate diffusion parameters
bedpostx data_directory

# Run probtrackx for tractography
probtrackx --samples=bedpostx/diff_slices/data --mask=mask.nii.gz --seed=seed.nii.gz --out=probtrackx
```

**4. FreeSurfer**

FreeSurfer also doesn't perform tractography itself. It is mainly used for cortical surface reconstructions. However, you can use the output from FreeSurfer (like white matter segmentation) for tractography in other softwares.

**5. MRtrix (preprocessing, tensor fitting, and streamline tractography)**

```bash
# Preprocessing
dwidenoise dwi.mif dwi_denoised.mif
dwipreproc dwi_denoised.mif dwi_preprocessed.mif -rpe_none -pe_dir PA

# Create mask
dwi2mask dwi_preprocessed.mif mask.mif

# Calculate tensors
dwi2tensor dwi_preprocessed.mif -mask mask.mif dt.mif

# Calculate FA map
tensor2metric dt.mif -fa fa.mif

# Whole brain tractography
tckgen -algorithm iFOD2 -backtrack -crop_at_gmwmi -maxlength 250 -power 1.0 CSD.mif tracks.tck
```

**6. DIPY (Python package for diffusion MRI)**

```python
import numpy as np
import nibabel as nib
from dipy.reconst.dti import TensorModel
from dipy.reconst.dti import fractional_anisotropy
from dipy.reconst.csdeconv import ConstrainedSphericalDeconvModel
from dipy.tracking.local_tracking import LocalTracking
from dipy.tracking.stopping_criterion import ThresholdStoppingCriterion
from dipy.direction import peaks_from_model
from dipy.io.streamline import save_trk

# Load your Diffusion Weighted data
data, affine = nib.load("data.nii.gz").get_data()

# Load your gradients tables
bvals = np.loadtxt("bvals.txt")
bvecs = np.loadtxt("bvecs.txt")

# Fit tensor model and compute FA map
dti_model = TensorModel(gtab)
dti_fit = dti_model.fit(data, mask)
FA = fractional_anisotropy(dti_fit.evals)

# Perform CSD
csd_model = ConstrainedSphericalDeconvModel(gtab, response)
csd_fit = csd_model.fit(data, mask=FA > 0.7)

# Perform tractography
stopping_criterion = ThresholdStoppingCriterion(FA, 0.25)
streamlines_generator = LocalTracking(csd_fit.peak_dirs, stopping_criterion, seeds, affine, step_size=.5)
save_trk("tractography.trk", streamlines_generator, affine, FA.shape)
```

However, the required processing steps (e.g., denoising, eddy current correction, etc.) and actual command can vary based on your data and research question.

Please notice that the sample scripts may not result in meaningful results because they lack critical pre- and post-processing steps, which depend on the specifics of your data and study design. Always consult software-specific documentation or expert guidance when setting up new methods.