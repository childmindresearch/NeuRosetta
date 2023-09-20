Sure, below are some basic examples of Image Quality Assessment scripts for different neuroimaging software platforms and Python. Please adjust these scripts according to your actual need and data manipulation requirements. 

**1. AFNI**

```bash
3dFWHMx -mask yourMask -input yourFunctional -acf > output.txt
}
```
This example uses 3dFWHMx for spatial smoothness estimation. It outputs the estimates to output.txt file.

**2. ANTs**

```bash
N4BiasFieldCorrection -d 3 -i input.nii.gz -o output.nii.gz
```
This example uses ANTs' N4BiasFieldCorrection which is an improved N3 bias correction. 

**3. FSL**

```bash
fslstats image.nii.gz -R -P 10 -P 90
```
Here fslstats is used to calculate image statistics. This will calculate and print the range of intensity values across the whole image (option -R) as well as the 10th and 90th percentiles (options -P).

**4. FreeSurfer**

```bash
mri_quality --i input_volume.mgz --vol-fwhm --o quality.log
```
mri_quality is a freesurfer command-line tool which calculates the Full Width Half Maximum (FWHM) to assess image quality. 

**5. MRtrix**

```bash
dwidenoise input_image.mif output_image.mif
```
The dwidenoise command performs a denoising operation on diffusion-weighted MRI datasets to assess the quality. 

**6. SPM (Matlab)**

```Matlab
Vol = spm_vol('image.nii');
Img = spm_read_vols(Vol);
Img_Quality = QualityEstimate(Img);
```
This snippet reads the volume data from an image and performs a quality estimation operation on it via a hypothetical QualityEstimate function.

**7. Pure Python**

```Python
from skimage import io, img_as_ubyte
from skimage.measure import shannon_entropy

image_path = '/path/to/your/image.nii'
image = io.imread(image_path, as_gray=True)
image = img_as_ubyte(image)

quality = shannon_entropy(image)
print(f'Quality (Shannon Entropy): {quality}')
```
This script uses the skimage library to read the image and evaluate its quality using the Shannon Entropy. 

Remember that these are very simple examples; assessing the quality of neuroimaging data is a complex process that involves multiple steps, and may include not only the inspection of individual images, but also registration quality, temporal variance, and other factors.