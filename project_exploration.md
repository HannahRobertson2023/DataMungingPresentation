#### SERX94: Exploratory Data Munging and Visualization
#### Rural Vs. Urban Quality of Life
#### Hannah Robertson
#### 10-21-2022

## Basic Questions
**Dataset Author(s):** CDC.gov, USDA, Census.gov, compiled by myself

**Dataset Construction Date:** 2010, 2013, compiled in 2022

**Dataset Record Count:** 187657 + 

**Dataset Field Meanings:** 
For brevity I am only including the fields I am using in my project. 

PLACES__Local_Data_for_Better_Health__County_Data_2021_release
StateAbbr		State abbreviation
StateDesc		Full state name
LocationName		County or city name
Category		What category is this data
Measure			What is the data measuring
Data_Value		data value
MeasureId		Code for measure

LND01
Areaname		Name of county
LND010200D		Area of county

NCHSURCodes2013
State Abr. 		State abbreviation
County name		Name of county
2013 code		Urban index code

POP01
Area_name		Name of area
POP010210D		Population of county

U.S._Life_Expectancy_at_Birth_by_State_and_Census_Tract_-_2010-2015
Area_name		Name of area
VST210207D		Life Expectancy at birth
		
Unemployment
Area_name			Name of area
Median_Household_Income_2020	Median household income

VST01
areaname		Name of area
VST210207D		Death rate

COMPILED SET
data_processed\USA\_allData.csv
ST_ABV				State Abbreviation
Name				Name of are
TEETHLOST			What is the rate of teeth lost?
TEETHLOSTCategory		Category of teethlost metric
ARTHRITIS			What is rate of arthiritis?
ARTHRITISCategory		category of arthiritis metric
CANCER				what is rate of cancer
CANCERCategory			category of canter metric
KIDNEY				What is rate of kidney failure
KIDNEYCategory			category of previous metric
COPD				what is rate of copd
COPDCategory			category of previous metric
CHD				what is rate of chd
CHDCategory			category of previous metric
CASTHMA				what is rate of athsma
CASTHMACategory			category of previous metric
DEPRESSION			what is rate of depression
DEPRESSIONCategory		category of previous metric
DIABETES			what is rate of diabetes
DIABETESCategory		category of previous metric
BPHIGH				what is rate of high blood pressure
BPHIGHCategory			category of previous metric
HIGHCHOL			what is rate of high cholesterol
HIGHCHOLCategory		category of previous metric
OBESITY				what is rate of obesity
OBESITYCategory			category of previous metric
STROKE				what is rate of stroke
STROKECategory			category of previous metric
BINGE				what is rate of binge eating
BINGECategory			category of previous metric
CSMOKING			what is rate of smoking
CSMOKINGCategory		category of previous metric
LPA				what is rate of lpa
LPACategory			category of previous metric
SLEEP				what is rate of sleep disorders
SLEEPCategory			category of previous metric
GHLTH				what is rate of general health
GHLTHCategory			category of previous metric
MHLTH				what is rate of mental health
MHLTHCategory			category of previous metric
PHLTH				what is rate of physical health
PHLTHCategory			category of previous metric
CERVICAL			what is rate of cervical screening
CERVICALCategory		category of previous metric
CHOLSCREEN			what is rate of high cholesterol
CHOLSCREENCategory		category of previous metric
ACCESS2				what is rate of good access to health
ACCESS2Category			category of previous metric
COLON_SCREEN			what is rate of colon screening
COLON_SCREENCategory		category of previous metric
MAMMOUSE			what is rate of of mammography
MAMMOUSECategory		category of previous metric
COREM				what is rate of preventative measures among men
COREMCategory			category of previous metric
COREW				what is rate of preventative measures among women
COREWCategory			category of previous metric
BPMED				what is rate of blood pressure medication takers
BPMEDCategory			category of previous metric
DENTAL				what is rate of dental access
DENTALCategory			category of previous metric
CHECKUP				what is rate of people accessing checkup
CHECKUPCategory			category of previous metric
Urb_Index			What is urban index
Income				what is median household income
LE_list				what is life expectancy
Area				what is area
Population			what is population
Dth_Rate			what is death rate


**Dataset File Hash(es):** 
c7079fe0a4e64901c060a95745a0db9e
5038f317c20706f0a853413792ec73e3
aba2bfbd6479f4824b88356b6c4dda2c
b456c6fbf18226749bbe7690b5620329
c7079fe0a4e64901c060a95745a0db9e
f579e86c0ea1bfc00fc1688042e823e6
b04b4eff0f9a59a46f1cea5ee1b40c24
3e1021e5a8636a9c380adb4d65536117
2c0c6bcc192c660e78987c5ef301d0e1

## Interpretable Records
### Record 1
Population Density maps to Health Metric
{01023, AL, Choctaw County, AL, 9, 10, 0, 6226, 5815, 411, 6.6, 5907, 5481, 426, 7.2, 5749, 5239, 510, 8.9, 5672, 5107, 565, 10.0, 5465, 5002, 463, 8.5, 5285, 4940, 345, 6.5, 5335, 5038, 297, 5.6, 5197, 4882, 315, 6.1, 5076, 4638, 438, 8.6, 5106, 4474, 632, 12.4, 4857, 4225, 632, 13.0, 4760, 4140, 620, 13.0, 4798, 4292, 506, 10.5, 4701, 4261, 440, 9.4, 4501, 4098, 403, 9.0, 4369, 3969, 400, 9.2, 4292, 3926, 366, 8.5, 4460, 4172, 288, 6.5, 4800, 4539, 261, 5.4, 4722, 4490, 232, 4.9, 4699, 4351, 348, 7.4, 4591, 4391, 200, 4.4, 41649, 77.2}

Explanation:** A lot of problems with health rely heavily on access to health services. Health services are often more difficult to access in areas with low population density due to long travel distances and low funding to build new clinics. In Choctaw County, AL, which is incredibly rural, health metrics may be low. 

### Record 2
Median Household Income maps to Health Metric
example:
{01005, AL, Barbour County, AL, 6, 6, 0, 11449, 10812, 637, 5.6, 11324, 10468, 856, 7.6, 11006, 10154, 852, 7.7, 11019, 10241, 778, 7.1, 10639, 9884, 755, 7.1, 10730, 10114, 616, 5.7, 10713, 10110, 603, 5.6, 10363, 9698, 665, 6.4, 10175, 9249, 926, 9.1, 9944, 8635, 1309, 13.2, 10219, 8978, 1241, 12.1, 9843, 8716, 1127, 11.4, 9377, 8273, 1104, 11.8, 9096, 8152, 944, 10.4, 8859, 7930, 929, 10.5, 8590, 7823, 767, 8.9, 8334, 7638, 696, 8.4, 8415, 7914, 501, 6.0, 8505, 8071, 434, 5.1, 8637, 8292, 345, 4.0, 8680, 8004, 676, 7.8, 8197, 7728, 469, 5.7, 38866, 72.0}

Prediction Explanation:** In America income is heavily associated with health, especially with health metrics that can be skewed by attention to predictive care. Lower median household income might be associated with worse health metrics overall. In Barbour County's case, their health metrics are consistently low. 

## Visualization
### Visual 1: Life_Expectancy, across the US. 
Could not attach file, look under \visuals\USA
**Analysis:** 
A similar percentage of the population of both groups live to the lower seventies, differences start emerging in the data. A lower percentage of rural people only live until eighty, and a higher percentage of them live until eighty five or ninety. Overall, average rural life expectancy is higher; admittedly not by much (in my national average it was only about a month) but higher nonetheless.