---
layout: post
title:  "Information-Restricted Voting"
date:   2018-01-26 00:26:05 +0100
categories: decide
---
Voting is often done separately on separate issues: In parliament, the issues are defined by laws that people pass, in (German) university, representatives for the student parliament and the faculty council are voted in separate votes.
<!--more-->
This can lead to inefficiencies and non-sincere voting: If one issue influences the other and two issues are strong complements, I might would like to vote against both instead of just letting pass only one [^1]. Efficiency is hard to reach if persons cannot tell about their complete preferences. Therefore, inefficiencies and non-sincere voting might arise. 

The economist might argue that there is an easy remedy to this: Just take the "product ballot": Instead of voting on separate issues, vote on all combinations of possible votes. Votes are then tuples, e.g. a vote \((A, K)\) meaning candidate A into the student parliament, candidate K into the faculty council. The product ballot, however, is huge. 

If one took the product ballot with $k$ separate issues and two possible choices each, then one would have $2^k$ -- exponentially many -- choices. This is too large of a ballot to be evaluated by hand. 

One hence has a payoff of complexity of messages people send and the properties and performance the mechanism with which decisions are made. Let us set this up as an optimisation problem.

## Beyond the Revelation Principle
We start with a baby problem that we will show has some similarities to the above: There are $n$ agents that have iid real types according to distribution function $F$. Given type $\theta$, they are assumed to each have the single-peaked utility function $u_\theta (x) = -(x-\theta)^2$, which is standard to assume[^2]. We consider a message space 
$$\tabularnewline
M = \{a, b, c\}
$$
and mechanisms
$$\tabularnewline
\phi\colon M^n \to \R. 
$$
Let $\mathbf{\theta} = (\theta_1, \theta_2, \dots, \theta_n)$.We would like to select a mechanism that maximises ex-ante total welfare
$$\tabularnewline
\E_F [\sum_{i=1}^n u_{\theta_i}\phi(s(\theta_1), s(\theta_2), \dots, s(\theta_n))],
$$
such that the strategies $s$ constitute a Bayesian equilibrium.

## Connection to Moulin's result
Moulin showed a result similar to this:



[^1]: This has been further explored in [Combinatorial Voting]().
[^2]: Mussa, Rosen.