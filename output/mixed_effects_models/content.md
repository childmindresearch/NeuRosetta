Mixed-Effects Models is a statistical technique that is popular in brain imaging for taking into account both fixed and random effects.

Below are minimal example scripts for applying Mixed-Effects Models in different neuroimaging software packages. Please note that these are the scripts for the purpose of illustration and may require modification according to your specific use-case.

### AFNI (Analysis of Functional NeuroImages)
```bash
3dLME -prefix LME -jobs 4 -model 'Time*Group' -qVars 'Age,Sex' -ranEff '~1' -num_glt 3 \
-gltLabel 1 'GrpXtime' -gltCode  1 'Group : 1*Control -1*Experimental Time :' \
-gltLabel 2 'Control' -gltCode  2 'Group : 1*Control' \
-gltLabel 3 'Experimental' -gltCode  3 'Group : 1*Experimental' \
-residual Z_RES -dataTable @file_list.txt
```

### ANTs (Advanced Normalization Tools)
Currently, ANTs does not support Mixed-Effects Models directly. Typically, the images are preprocessed and normalized in ANTs, then the statistical analysis is done in another software like R.

### FSL (FMRIB's Software Library)
```bash
fsl_glm -i inputfile -d designmatrix -c contrasts -m mask --out_filedir=./output
```

### FreeSurfer
FreeSurfer does not directly support Mixed-Effects Models. However, you can integrate your preprocessed FreeSurfer data into other statistical software like R or Python to apply mixed-effects models.

### MRtrix
MRtrix does not directly support Mixed-Effects Models. You may need to use other specialized statistical software, such as R or Python, to run these models.

### Python: using statsmodels for Mixed-Effects Modelling
```python
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = sm.datasets.get_rdataset("dietox", "geepack").data
md = smf.mixedlm("Gain ~ Age*Group", data, groups=data["Pig"])
mdf = md.fit()
print(mdf.summary())
```

### SPM (Statistical Parametric Mapping)
In the context of SPM, one would typically build a GLM model first and then apply contrasts. SPM does not directly support Mixed-Effects Models. Nevertheless, one can create a design matrix that allows for a similar effect by using the multiple conditions field when setting up the model. Afterward, statistics could be calculated in Matlab or R.