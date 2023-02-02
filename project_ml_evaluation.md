#### SERX94: Machine Learning Evaluation
#### TODO Rural Vs. Urban Quality of Life
#### TODO Hannah Robertson
#### TODO 11-21-2022

## Evaluation Metrics
### Metric 1
**Name:** MSE

**Choice Justification:** MSE is a easily calculable way to measure error in a linear regression, which I already happen to know how to do. 

Interpretation:** Error is crucial in the measurement of the fit of any given line. 

### Metric 2
**Name:** RSS  

**Choice Justification:** RSS is a way to smooth out some of the outliers I had.

## Alternative Models
### Alternative 1
**Construction:** Model set 1 is set on the least squares computation from HW 5. I have 3 subtypes: the first is Urban Index vs. health indicator; the second is Population Density vs health indicator (with a different set of coefficients for each urban index); the third is Income vs health (with a different set of coefficients for each urban index). 

**Evaluation:** The Urban Index - adjusted Income/Health Measurements model was my second most accurate model to date. 


### Alternative 2
**Construction:** Model set 1 is sklearn ridge regression. I have 3 subtypes: the first is Urban Index vs. health indicator; the second is Population Density vs health indicator (with a different set of coefficients for each urban index); the third is Income vs health (with a different set of coefficients for each urban index). 

**Evaluation:** This model was not as accurate as other models in any of the permutations I used. 


### Alternative 3
**Construction:** Model set 1 is sklearn lasso regression. I have 3 subtypes: the first is Urban Index vs. health indicator; the second is Population Density vs health indicator (with a different set of coefficients for each urban index); the third is Income vs health (with a different set of coefficients for each urban index). 

**Evaluation:** The Urban Index - adjusted Income/Health Measurements model was my most accurate model to date, scoring most accurate about half the time.


### Best Model:
Urban Index adjusted Income-based lasso regression consistently scored most accurate. 