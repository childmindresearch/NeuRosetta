I'm sorry but it's not possible to provide full scripts for each of these softwares, especially since conducting MVPA includes steps like preprocessing, feature extraction, training a model, and testing it, which can not be encapsulated in a few lines of codes. However, I can definitely provide you with basic syntax and commands used in each software.

1. AFNI

In AFNI, you can use the 3dsvm function to perform Multivariate Pattern Analysis. The typical usage is:

```sh
3dsvm -bucket stats -mask mask+orig -trainvol training+orig -trainlabels training_labels.1D -testvol testing+orig -testlabels testing_labels.1D
```

2. ANTs

ANTs is typically used for registration and normalization. It doesn't directly support MVPA from command line, but you can load the image into python or any other tool to perform MVPA.

3. FSL

FSL has a tool called PyMVPA which can be used for Multivariate Pattern Analysis. The sample usage can be like this:

```sh
fsl_sub python mvpa2.suite.Classifier filename.nii.gz
```

4. FreeSurfer

Like ANTs, FreeSurfer is used mostly for segmentation and registration but it doesn't directly support MVPA.

5. MRtrix

MRtrix is used more for diffusion imaging analysis. For MVPA, you would typically export the imaging data after preprocessing and perform the analysis with another tool like python or R.

6. R

In R, you can use the nnet or e1071 libraries to perform MVPA. Here is a short example:

```R
library(e1071)
svm_model <- svm(label~., data=train_data)
predictions <- predict(svm_model, newdata=test_data)
```

7. Workbench Command

The Connectome Workbench doesn't directly support MVPA as its primarily a visualization tool. You would need to export your data to another tool for statistical learning.

8. pure Python (nilearn)

Here's how you might use nilearn to perform MVPA:

```python
from nilearn.input_data import NiftiMasker
from sklearn.svm import SVC
from sklearn.model_selection import LeaveOneOut

masker = NiftiMasker(mask_img='mask.nii.gz')
X = masker.fit_transform('images.nii.gz')
y = ['label1', 'label2', ...]

svm = SVC(kernel='linear')
cv = LeaveOneOut()

for train, test in cv.split(X):
    svm.fit(X[train], y[train])
    predictions = svm.predict(X[test])
```

9. SPM (via a MATLAB script)

SPM doesn't directly support MVPA; typically one would use the CoSMoMVPA toolbox in conjunction with SPM. An example script might look like this:

```matlab
cosmo_config();
data_path=cosmo_config().tutorial_data_path;
mask_fn=fullfile(data_path,'ak6','s01','glm_T_stats_perrun.nii');
ds = cosmo_fmri_dataset(mask_fn,'mask',mask_fn);
clf = cosmo_classify_svm(ds.samples, ds.sa.chunks);
```

Remember to fit the MVPA task to your specific needs in terms of preprocessing, model training, testing and validation.