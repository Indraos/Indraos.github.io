---
layout: post
title:  "Thesis on a Data Application of Graphon Theory: Literature"
date:   2018-03-25 08:00:00 +0100
categories: learn
---
Graph Kernels are heavily used in network classification. This is a short commented literature review for my [Master Thesis in Mathematics](/assets/papers/thesis_msc_math.pdf).
<!--more-->
## Graph comparisons
### via embeddings
 - arxiv:1006.5169 fits graphs to points sampled from a hyperbolic space, just as arxiv:1411.1350

### via graph kernels
 - doi:101007/978354045167911 shows that the complete kernel is NP-hard to compute, presents the walk kernel as efficient kernel (that is spectrally computed).
 - issn:1532-4435 shows that many graph kernels can be computed efficiently using spectral methods. They give a very general overview of graph kernels.
 - [This](http://proceedings.mlr.press/v5/shervashidze09a.html) uses homomorphism densities of small graphs as features. 
 - [This](http://papers.nips.cc/paper/3813-fast-subtree-kernels-on-graphs.pdf) uses trees. 
 - issn:1532-4435 studies Graph kernels using tree homomorphism densities with additional information on node labels.
 - doi:101007/978364233460330 is the first approach I found that tries to leverage ideas that work for unweighted graphs to weighted graphs. 
 - doi:101145/10140521014072 gives a graph kernel that is unfortunately not efficiently computable.

## Graphon Theory
 - arxix:math/0408173 is the initial paper on dense graphon theory.
 - arxiv:1212.1247v7 is the only efficient estimation method for graphs from a sample: In fact, it is a low-rank approximation (from one observed graph)
 - arxiv:1007.1684v3 motivated 1212.1247v7 with spectral clustering results for block models with many blocks.
 - arxiv:1309.5936 show under strong assumptions on the graph density error bounds for a maximum likelihood estimator.
 - arxiv:1010.5155 is the main paper for limits of **weighted** undirected graphs. They show that one can characterise the limit objects with a countable family of homomorphism densities.
 - doi:101007/354033700818 has among many other things the results on the spectrum of the graphon operator and identities that connect cycle homomorphism numbers to spectral powers.

## Neuroscience with Graphs
 - doi:101109/msp20122233865 is a survey paper on graph-based techniques in neuroscience. It discusses mostly ad-hoc measures of similarity (clustering, similarity)
 - doi:101038/nrn2575 studies the differences between functional and structural connectome. 

## Tools
 - doi:101073/pnas0907096106 introduces the study of network modularity.
 - doi:101007/s1020801090606 gives a stability result. They do not connect it to classification performance.