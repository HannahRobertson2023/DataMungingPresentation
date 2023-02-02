#### SERX94: Experimentation
#### TODO (title)
#### TODO (author)
#### TODO (date)


## Explainable Records
### Record 1
Population Density maps to Health Metric
{01023, AL, Choctaw County, AL, 9, 10, 0, 6226, 5815, 411, 6.6, 5907, 5481, 426, 7.2, 5749, 5239, 510, 8.9, 5672, 5107, 565, 10.0, 5465, 5002, 463, 8.5, 5285, 4940, 345, 6.5, 5335, 5038, 297, 5.6, 5197, 4882, 315, 6.1, 5076, 4638, 438, 8.6, 5106, 4474, 632, 12.4, 4857, 4225, 632, 13.0, 4760, 4140, 620, 13.0, 4798, 4292, 506, 10.5, 4701, 4261, 440, 9.4, 4501, 4098, 403, 9.0, 4369, 3969, 400, 9.2, 4292, 3926, 366, 8.5, 4460, 4172, 288, 6.5, 4800, 4539, 261, 5.4, 4722, 4490, 232, 4.9, 4699, 4351, 348, 7.4, 4591, 4391, 200, 4.4, 41649, 77.2}


Prediction Explanation:** A lot of problems with health rely heavily on access to health services. Health services are often more difficult to access in areas with low population density due to long travel distances and low funding to build new clinics. In Choctaw County, AL, which is incredibly rural, health metrics may be low. 

### Record 2
Median Household Income maps to Health Metric
example:
{01005, AL, Barbour County, AL, 6, 6, 0, 11449, 10812, 637, 5.6, 11324, 10468, 856, 7.6, 11006, 10154, 852, 7.7, 11019, 10241, 778, 7.1, 10639, 9884, 755, 7.1, 10730, 10114, 616, 5.7, 10713, 10110, 603, 5.6, 10363, 9698, 665, 6.4, 10175, 9249, 926, 9.1, 9944, 8635, 1309, 13.2, 10219, 8978, 1241, 12.1, 9843, 8716, 1127, 11.4, 9377, 8273, 1104, 11.8, 9096, 8152, 944, 10.4, 8859, 7930, 929, 10.5, 8590, 7823, 767, 8.9, 8334, 7638, 696, 8.4, 8415, 7914, 501, 6.0, 8505, 8071, 434, 5.1, 8637, 8292, 345, 4.0, 8680, 8004, 676, 7.8, 8197, 7728, 469, 5.7, 38866, 72.0}

Prediction Explanation:** In America income is heavily associated with health, especially with health metrics that can be skewed by attention to predictive care. Lower median household income might be associated with worse health metrics overall. In Barbour County's case, their health metrics are consistently low. 

## Interesting Features
### Feature A
**Feature:** Population Density/Health Metric Relation

**Justification:**  
My project structure was initially based on Urban Index. However, Urban Index is bad for linear regression, as it is a simple array of only nine integer values. To accomodate for this, I created a model which conists of nine separate regressions, one for each urban index, plotting income and health metrics against each other. I made three models with this format, based on least squares, lasso, and ridge regression respectively. 

Because I was using Urban Index as more of a qualitying factor instead of a input, I needed to find a new input. I had noticed a definite skew in the earlier part of this project, rural areas according to the Rural Urban Index tending to score lower in most health metrics. I decided to try to quantify that with a more direct indication of rural areas, population density. I plotted population density against my health metrics, hoping to find correlation.

I did not! Of the six main models I trained, the three population density models were the three lowest scoring with correlation.

### Feature B
**Feature:** Income/Health Metric Relation

**Justification:** 
My project structure was initially based on Urban Index. However, Urban Index is bad for linear regression, as it is a simple array of only nine integer values. To accomodate for this, I created a model which conists of nine separate regressions, one for each urban index, plotting income and health metrics against each other. I made three models with this format, based on least squares, lasso, and ridge regression respectively. 

I was going through my data doing checks when I realized that most of the rural areas that had poor metrics were also quite poor. I decided to do a rural-index-adjusted model check the relation between income and my health metrics. To my surprise, this mapped much better in all three of my main models based on it. 

This relation let to the best fit I found in my project. Of my six main models, the three with the main fit involved this relation. 

## Experiments 
### Varying A
**Prediction Trend Seen:** Income
	When income is varied, Population Density becomes the better predictor of Health Metric, going from about 10% to 30%. However, this is associated with sky high MSE and RSE.

### Varying B
**Prediction Trend Seen:** Population Density
	When population density is varied, income is the better fit most of the time, jumping from being best fit about 45% of the time to about 75%. Both MSE and RSE are high, though.

### Varying A and B together
**Prediction Trend Seen:** Income and Population Density
	When both trends are varied, Income becomes an even better fit oddly enough, jumping from 45% to 85% of the times as best fit. These data tend to have high MSE but low RSE.


### Varying A and B inversely
**Prediction Trend Seen:** Population Density and inverse Income
	The numbers are all over the board on this one! Some files have high MSE and low RSE, others vice versa, and some have both very high.