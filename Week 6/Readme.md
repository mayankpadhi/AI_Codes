# Problem Statements:

* Generate 100 data points coming from the mixture of four Gaussians in R^2 with weightages π=[0.4 0.3 0.2 0.1], means μ=[(0,0) (4,4) (0,3) (4,0)].  The covariance matrices corresponding to the Gaussians are as follows: C_1=[1 0.7; 0.7 1],C_2=[1 0.25; 0.25 0.5],C_(3 )=[0.5 0.1; 1 0.1]and C_4=[0.25 0;0 0.35].
*	Make a version of the K-means algorithm that models the data as a mixture of K arbitrary Gaussians, i.e., Gaussians that are not constrained to be axis-aligned.  Use the developed algorithm to cluster the data points generated in part 1 with K=1,2,3,4,5,6.
