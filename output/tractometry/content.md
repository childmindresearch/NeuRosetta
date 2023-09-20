I'm sorry, but it wouldn't be possible or practical to provide a fully functioning script for each of the software packages you've listed. However, I can share the basic concepts or commands needed for performing Tractometry using those software packages.

1. AFNI:
AFNI doesn't directly support Tractometry, but you can use it in combination with other libraries like 3dTrackID and FATCAT.

```bash
3dTrackID -mode DET -dti_in dti_values.niml.dset -netrois mask_ROI.niml.dset -prefix TrackID
```

2. ANTs:
ANTs also doesn't have direct support for Tractometry, but you can perform registration and normalization steps with it.

```bash
antsRegistrationSyN.sh -d 3 -f fixed.nii.gz -m moving.nii.gz -o output
```

3. FSL:
Tractometry can be performed by combining several steps in FSL, like BEDPOST and PROBTRACKX

```bash
# Run BedPostX
bedpostx InputData
# Run ProbTrackX
probtrackx2 --samples=InputData.bedpostX/merged --mask=InputData.bedpostX/nodif_brain_mask --seed=Seed --out=OutputName
```

4. FreeSurfer:
FreeSurfer is not typically used for tractometry, but for cortical thickness and volume analysis. However, it can still be used to prepare data for other software like tract_querier.

5. MRtrix:
Again, tractometry itself involves various steps, but to get streamlines in MRtrix you can use the following command:

```bash
tckgen FOD.mif tracks.tck -act 5TT.mif -backtrack -seed_sphere seed.nii.gz 5 -select 10000 -cutoff 0.06
```

6. pure Python | Dipy:
Dipy is a Python library for performing different steps of diffusion imaging analysis, including tractometry. Here is a very minimal example:

```python
import numpy as np
from dipy.io.streamline import load_tractogram
from dipy.tracking.utils import length

tractogram = load_tractogram('AF.left.trk', 'same')
streamlines = tractogram.streamlines
lengths = list(length(streamlines))

print(np.median(lengths))
```

7. SPM:
SPM is primarily used for statistical analysis of fMRI and PET data, and does not directly support tractometry.

Please note that Tractometry involves a large pipeline including preprocessing of MRI scans, tractography to get streamlines, and then sectioning these streamlines based on a parcellation scheme. You will need to design a full pipeline based on your specific needs in real-life scenarios.