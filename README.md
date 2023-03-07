# liver_lineage_test
Small model to analyze liver lineage tracing model from Ober paper.

# Lineage tracing identifies heterogeneous hepatoblast contribution to cell lineages and postembryonic organ growth dynamics

In [this paper](https://www.biorxiv.org/content/10.1101/2023.01.18.524321v1), a simple model is used to analyze the ratio of cell types during liver development in Zebrafish. The aim here is to generate a similar model, in a simpler way. I will go for some deterministic modeling instead of stochastic. The results should be the same for the mean behaviour but we won't have the variance. We could then try some agent-based modeling if we wanted to get the variance or add some other functionalities... or just for the sake of it.

You can use this to start trying out different parameters, or, in the end, making parameters time dependent. It would be really nice to fit the data points and use Bayesian inference to discover the confidence interval for the parameters.

Good hunting!

Click the icon to open the notebook in Binder and test it out. Bear in mind it might take a while...

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/acorbat/liver_lineage_test/main?filepath=simple_model.ipynb)