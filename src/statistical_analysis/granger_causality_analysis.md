[Edit on GitHub](https://github.com/cmi-dair/NeuRosetta/edit/main/src/statistical_analysis/granger_causality_analysis.md)
# Granger Causality Analysis

it's quite a complex task to write scripts for Granger causality Analysis for all these different frameworks as they each have different methods and procedures for doing such analyses. Here are limited examples for a couple of the mentioned frameworks:

## <img src="../icons/afni.png" height="24px" /> AFNI

AFNI does not natively support Granger Causality Analysis. We typically need to use another software like R or Python's scipy library and then import the results back into AFNI for further analysis. 

## <img src="../icons/fsl.png" height="24px" /> FSL

Like AFNI, FSL does not directly support Granger Causality Analysis. A similar approach must be taken with substituting sections of the analysis with Python or R scripts.

## <img src="../icons/r.png" height="24px" /> R

The `lmtest` library in R can be used to perform Granger Causality Analysis.
```R
# Assume time series x and y are _already_ loaded (e.g., via read.csv())
library(lmtest)

fit <- lm(y ~ lag(y, -1) + lag(x, -1))  # Fit a linear regression model
summary(fit)  # Review the fit

grangertest(y ~ x, order=1)  # Perform the Granger causality test
```
## <img src="../icons/python.png" height="24px" /> Python

The `statsmodels` Python library can also be used for performing Granger causality tests.
```python
import numpy as np
from statsmodels.tsa.stattools import grangercausalitytests

# Assume x and y are already loaded, e.g., via numpy.loadtxt or pandas.read_csv

# Reshape to 2D arrays, needed for the function input
x = np.atleast_2d(x).T
y = np.atleast_2d(y).T

# Stack and do the test 
xy = np.hstack([x, y])
result = grangercausalitytests(xy, maxlag=2, verbose=False) 
```
For the other software like ANTs, FreeSurfer, MRtrix, SPM (via a MATLAB script), and Workbench Command, it's the same case as with AFNI and FSL. They do not natively support Granger causality analysis and would require integration with Python, R or possibly MATLAB scripts. Generally, Granger causality analyses are typically conducted in R or MATLAB due to the relatively simpler syntax and inbuilt libraries specifically designed for such analysis. Python has also become a popular choice due to the presence of the scipy and statsmodels packages.