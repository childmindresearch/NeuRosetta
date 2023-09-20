I'm sorry for the confusion, but creating full code examples for each of the mentioned software packages would be quite extensive and may not be practical in this context. However, I can certainly provide a general guideline for how one could approach Mean Diffusivity (MD) mapping in each case, though please note that the exact execution will depend heavily on individual dataset characteristics and specific project needs.

1. AFNI:

AFNI is primarily used for functional imaging, but it can also extract diffusion parameters such as MD.

```bash
3dDWItoDT -prefix DTI -eig_vec_prefix EVEC DTI.nii
3dcalc -a 'DTI_MD+orig' -expr 'a' -prefix MD_map.nii
```
Mostly AFNI follows command-line functions. You can use 3dDWItoDT to calculate DTI parametric maps and then extract the MD map.

2. ANTs:

ANTs doesn't directly calculate MD, but it's possible by using its image arithmetic capabilities after calculating tensor images with other processing tool.

```bash
ImageMath 3 dtMD.nii TensorToVectorMD dt.nii
```
After you calculate the tensor image, you can use ImageMath.

3. FSL:

FSL uses DTIFIT for tensor model fitting.

```bash
dtifit --data=diffusion_data.nii.gz --mask=mask.nii.gz --bvecs=bvecs.txt --bvals=bvals.txt --out=dtifit_output
fslmaths dtifit_output_MD -mul 1000 dtifit_output_MD
```
The output of DTIFIT generates several images, including the MD map.

4. FreeSurfer:

Freesurfer isn't primarily used for diffusion imaging, and as such, it doesn't have built-in tools for MD mapping. For that, it's recommended to use tools like FSL or MRtrix and then register the results to freesurfer anatomical space if necessary.

5. MRtrix:

MRtrix includes a command named `dwi2tensor` to calculate diffusion tensor images (DTI) from a DWI image.

```bash
dwi2tensor dwi.mif dt.mif -mask mask.mif
tensor2metric dt.mif -md md.mif
```
You can use `tensor2metric` to create the MD map as an output.

6. SPM:

You can use the DTI Tool (which is an SPM extension) to process DTI data, including calculating MD maps. It is GUI based and doesn't support scripting.

7. Pure Python:

In pure python, you can use Dipy.

```python
from dipy.reconst.dti import from_lower_triangular
from dipy.io import read_bvals_bvecs
from dipy.core.gradients import gradient_table

bvals, bvecs = read_bvals_bvecs('bvals.txt', 'bvecs.txt')
gtab = gradient_table(bvals, bvecs)
tenmodel = dti.TensorModel(gtab)
tenfit = tenmodel.fit(data)
MD = tenfit.md
```
This script loads in b-values and b-vectors, sets up a gradient table, fits a tensor model, and calculates MD. Note that 'data' here refers to your diffusion data.