# Graph Theory Analysis

it's not feasible to provide a complete script for each software package due to the complexity involved in Graph Theory Analysis. However, I can provide brief examples of the necessary commands.

## <img src="../../icons/afni.png" height="24px" /> AFNI

```bash
3dNetCorr -in_rois ROI_MASK -inset FUNC_DATA
```
In AFNI, `3dNetCorr` command is used to calculate correlations between different regions of interest defined in `ROI_MASK` on the functional data `FUNC_DATA`.

## <img src="../../icons/ants.png" height="24px" /> ANTs

ANTS doesn't directly generate graphs. But it is used to preprocess MRI images. For graph analysis, the outputs are used in other software like FSL or AFNI.

## <img src="../../icons/fsl.png" height="24px" /> FSL

```bash
fslmaths FUNC_DATA -Tmean MEAN_FUNC_DATA
fslmaths FUNC_DATA -bptf $(echo "scale=2; 2.8/$TR" | bc) -1 -add MEAN_FUNC_DATA NORM_FUNC_DATA
fslmeants -i NORM_FUNC_DATA -o ts.txt -m ROI_MASK
```
In FSL, preprocessing like normalizing and bandpass filtering is performed. Then mean time series `ts.txt` in the region of interest defined by `ROI_MASK` is computed.

## <img src="../../icons/freesurfer.png" height="24px" /> FreeSurfer

FreeSurfer itself does not contain Graph Theory Analysis tools but is used for preprocessing steps. Brain surfaces obtained from FreeSurfer can be used in connectome software like the Connectome Mapping Toolkit.

## <img src="../../icons/mrtrix.png" height="24px" /> MRtrix

In MRtrix, tck2connectome is used to generate a connectome from a tractogram.

```bash
tck2connectome tracks.tck nodes.mif connectome.csv
```

## <img src="../../icons/r.png" height="24px" /> R

```R
library(igraph)
edges <- read.table("edges.txt", header = TRUE)
graph <- graph_from_data_frame(edges)
centrality <- betweenness(graph)
print(centrality)
```
R's igraph package is used for the graph analysis where edges are defined in a text file.

## <img src="../../icons/workbench_command.png" height="24px" /> Workbench Command

Workbench mostly deals with surface analyses. It can use CIFTI files to generate graphs:

```bash
wb_command -cifti-correlation FUNC_DATA.dtseries.nii output.dconn.nii
```

## <img src="../../icons/python.png" height="24px" /> Python

```python
import networkx as nx
G = nx.read_edgelist('edges.txt')
centrality = nx.betweenness_centrality(G)
print(centrality)
```
In Python, the NetworkX package is often used for graph theory analysis.

## <img src="../../icons/spm.png" height="24px" /> SPM

SPM's CONN toolbox is used for the graph theoretical analysis:

```matlab
conn_batch('setup.conditions.name', 'rest');
conn_batch('Setup.rois.files', 'ROI_MASK');
conn_batch('Setup.covariates.names', 'white matter');
conn_batch('Run');
```