---
author: Bryce Bartlett
title: Overview of IE model for APC
date: 9/25/2014
---

#Overview#

This outlines mathematical issues related to APC form Land and Yang's book to assist in building data.

#Summary#

The classical general linear regression model (equation 4.1, p.61) is written as follows:

$$ R_{ij} = \mu + \alpha_i + \beta_j + \gamma_k + \epsilon_{ij}  $$

Alternatives include a log-linear or binomial model (specified in the same area).

Where $R$ represents the rate (incidence divided by population at risk), $i$ indexes age, $j$ indexes period, and $k$ indexes cohort.

#Final Thoughts#

What I need is a matrix (by country) which includes a vector of exposures outcomes, any exposure variables (x), age, and period for *each* cause of death I'm interested in. There are three sets: (1) general COD, (2) Communicable/Acute/Chronic, and (3) Heart Disease/CVD.

