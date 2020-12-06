# HD-Datascience-Flask
Heart Disease Prediction using ML

Libraries Used 
pandas
matplotlib.pyplot
numpy 
sklearn
pickle

![](imgs/capture.png)

OLS REGRESSION RESULTS
Dep. Variable:	y	R-squared:	0.383
Model:	OLS	Adj. R-squared:	0.368
Method:	Least Squares	F-statistic:	26.11
Date:	Sun, 06 Dec 2020	Prob (F-statistic):	9.95e-28
Time:	16:38:03	Log-Likelihood:	-145.67
No. Observations:	303	AIC:	307.3
Df Residuals:	295	BIC:	337.0
Df Model:	7		
Covariance Type:	nonrobust		
coef	std err	t	P>|t|	[0.025	0.975]
const	0.5748	0.309	1.859	0.064	-0.034	1.183
age	-0.0035	0.003	-1.172	0.242	-0.009	0.002
sex	-0.3016	0.050	-5.987	0.000	-0.401	-0.202
cp	0.1617	0.023	6.896	0.000	0.116	0.208
trestbps	-0.0038	0.001	-2.765	0.006	-0.007	-0.001
chol	-0.0008	0.000	-1.714	0.088	-0.002	0.000
fbs	-0.0169	0.066	-0.257	0.798	-0.146	0.113
thalach	0.0061	0.001	5.285	0.000	0.004	0.008
Omnibus:	8.894	Durbin-Watson:	0.753
Prob(Omnibus):	0.012	Jarque-Bera (JB):	5.074
Skew:	-0.111	Prob(JB):	0.0791
Kurtosis:	2.406	Cond. No.	4.41e+03
