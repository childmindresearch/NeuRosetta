Although fully functional scripts for each of these software packages would require a complex and lengthy setup, I will give basic examples of scripts you could use to achieve White Matter Fiber Bundle Analysis in each. Note that these scripts assume you have properly installed the software and that you have already preprocessed your data appropriately.

1. AFNI
------
AFNI doesn't directly support Fiber Bundle Analysis. However, it is commonly used alongside other packages such as FreeSurfer or FSL to visualize and analyze fiber tracts. Here, I'll provide a script for visualization:

```bash
3dTrackID -input DTI_FIT.nii -prefix TRACK -alg FACT
```

2. ANTs
------
ANTs also does not directly perform diffusion tensor tractography but can be used for preprocessing. It can register and normalize diffusion images before fiber analysis using tools like FSL and MRtrix.

```bash
antsRegistrationSyN.sh -d 3 -f fixedImage.nii -m movingImage.nii -o outputName
```

3. FSL
------
FSL's `probtrackx2` tool is used to perform probabilistic tracking.

```bash
probtrackx2 --samples=bvecs --mask=mask.nii --seed=seed.nii --out=FD --forcedir --opd --os2t --s2tastext
```

4. FreeSurfer
--------------
FreeSurfer includes a utility called `trac-all` that can be used for tractography.

```bash
trac-all -s subjectid -c dti/aparc+aseg -l lh-cingulum-hippocampus
```

5. MRtrix
---------
MRtrix includes a tool called `tckgen` for fiber tracking.

```bash
tckgen FOD.mif tracks.tck -act 5TT.mif -backtrack -crop_at_gmwmi -seed_image seed.mif -select 10000
```

6. Pure Python SPM
------------------
While SPM is a MATLAB-based toolset, it does not directly offer tractography or fiber bundle analysis methods. However, Python tools like NiBabel and Dipy can be implemented for these tasks.

```python
from dipy.tracking.local import LocalTracking
from dipy.tracking.streamline import Streamlines
    
subprocess.call(['bet', 'input.nii', 'output_brain.nii'])
img = nib.load('output_brain.nii')
maskdata = img.get_data()
streamline_generator = LocalTracking(prob_dg, classifier, seeds, affine, step_size=.5)
streamlines = Streamlines(streamline_generator)
```

Remember that these brief examples represent small snippets of what the whole analysis pipeline would include. Completing these tasks in practice involves numerous additional steps including data import, pre-processing, post-processing, and statistical analysis. I recommend studying the detailed documentation for each software package to implement them properly in your research.