Here are simple scripts for tractography in AFNI, ANTs, FSL, FreeSurfer, MRtrix, and a Python implementation using Dipy. Please keep in mind that these scripts will need to be adapted to your specific needs and datasets.

1. AFNI:

```bash
3dDWItoDT -prefix DTI afni_dwi.nii.gz
3dTrackID -mode DET -dti_in DTI.nii.gz -prefix tracks
```

2. ANTs:

```bash
export ANTSPATH=/path/to/ants/bin/
ANTs_path=/path/to/ants/bin/
${ANTSPATH}/DTIProcess --dti_image dti.nii --ref_image ref.nii --idwi_image idwi.nii 
```

3. FSL:

```bash
bedpostx bpx_input_dir
probtrackx2 --samples=bpx_input_dir/merged --mask=bpx_input_dir/nodif_brain_mask --seed=masks.nii.gz --out=probtrackx_output
```

4. FreeSurfer:

```bash
mri_convert input.nii.gz output.mgz
mri_glmfit --y DTI.mgz --fsgd design.fsgd --out betas.mgh
```

5. MRtrix

```bash
# Compute FOD
dwi2fod csd dwi.mif response.txt fod.mif 

# Compute whole-brain tractogram
tckgen fod.mif tracks.tck -seed_image seed.mif -mask mask
```

6. Python using Dipy:

```python
import numpy as np
from dipy.tracking.local import LocalTracking
from dipy.tracking.stopping_criterion import ThresholdStoppingCriterion
from dipy.tracking import utils
from dipy.data import fetch_stanford_hardi, read_stanford_hardi
from dipy.reconst.shm import CsaOdfModel

fetch_stanford_hardi()
img, gtab = read_stanford_hardi()

model = CsaOdfModel(gtab, sh_order=6)
data = img.get_data()
affine = img.affine

seeds = utils.seeds_from_mask(data, affine, density=2)
stopping_criterion = ThresholdStoppingCriterion(model, .2)

local_tracking_gen = LocalTracking(model, stopping_criterion, seeds, affine, step_size=.5)
tractogram = utils.array_sequence_to_generator(local_tracking_gen)

nex,  = next(tractogram)
```

Please note that tractography is a complex processes and these scripts are oversimplifications. For detailed analyses, please refer to the respective software's guidance.