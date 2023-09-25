I'm sorry, but it would be challenging to show minimal example scripts of Tractography in each of the mentioned processing packages due to the complexity of the field. Tractography involves several preprocessing steps (like creating masks, estimating diffusion models, etc.), cannot be practically consolidated into minimal code snippets, and usually these piping steps are done through a GUI or its own scripting language. Here I will list some general commands and examples where feasible:

1. **AFNI**

AFNI doesn't do tractography itself but it can be used to preprocess data for tractography. 

2. **ANTs**

Similar to AFNI, ANTs is used primarily for image registration, and you would need to use another software for the tractography portion. Its usage could be like:

```bash
antsRegistrationSyN.sh -d 3 -f fixed.nii -m moving.nii -o output
```

3. **FSL**

The 'probtrackx' script in FSL is used for Tractography,

```bash
probtrackx --samples=dti --mask=mask --seed=seed --out=output
```

4. **FreeSurfer**

Same as AFNI and ANTs, FreeSurfer does not perform tractography itself, it can be used to preprocess data for tractography.

5. **MRtrix**

MRtrix3 has a tckgen command used for tractography,

```bash 
tckgen FOD.mif tracks.tck -act 5tt.mif -backtrack -crop_at_gmwmi -seed_image seeds.mif -select 1000
```

6. **R**

R does not support tractography directly. However, there is a package called 'tracter' which you can use in combination with FSL.

7. **Workbench Command**

```bash
wb_command -fiber-tractography <method-name> <input-diffusion> <output-tractography>
```

8. **Python** 

Python scripting with `DIPY` package:

```python
from dipy.reconst.dti import TensorModel
from dipy.reconst.csdeconv import CsdModel
from dipy.reconst.csdeconv import auto_response
from dipy.reconst.dti import fractional_anisotropy
from dipy.feature.mask import median_otsu
from dipy.io.streamline import save_tck
```

9. **SPM (MATLAB)**

SPM does not have direct support for tractography, but you can load MAT files produced by other software, and manipulate them in SPM environment.

Again, these are only brief examples, you would need more code for preprocessing, parameters' setup and the following steps.