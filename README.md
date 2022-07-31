# Star Luminosity Analysis
Final Project for University of California - Berkeley's 2022 Summer Sessions Astronomy 9 Class - Group 5


**Group Members:**

**Ma, Yichen**

**Shah, Manthan**

**Su, Aaron**

**Sun, Chengze**

**Wang, Xinyao**

**Yang, Emily**

**Ye, Jeremy**


**1 Abstract**
Luminosity curves are used to show how the brightness of
different stellar objects, especially stars, changes over time. They offer information about
any astronomical processes happening, especially if they cause a sudden change in an object’s
brightness (for example, a supernova causes a sudden increase in brightness). [Research
question] Can there be different factors, such as a star’s mass and radius, that affect a star’s
luminosity curve data? If there are stellar factors that influence the luminosity curve, what
are they?  For this study, we will analyze and compare luminosity
curve data from different types of stars to understand what affects a star’s brightness and
luminosity. Overall, the data findings should support the idea that a star’s
luminosity curve can be influenced by different stellar properties.


**2 Background**
Luminosity Scales are one of the foundations of modern day Astronomy.
Research on luminosity has been conducted as far back as the 1930s. Fortunately, we made
massive improvements to our technology over the last 100 years, which means that we have
tools such as computers and Python to have a better understanding of the relationship of
how factors eventually impact luminosity scales. More recent articles also have demonstrated
an renewed interest in luminosity scales. One area that our group is significantly interested
in is determining which variables can affect the luminosity scale of stars observed by humans
on earth.


**3 Research Question**
Our inspiration for this project originates from several papers studying how luminosity curves
are calculated, as well as the launch of the James Webb Telescope. Through papers such
as ”A re-calibration of the luminosities of early-type stars: its effect on the Cepheid lumi-
nosity scale,” and ”The luminosity evolution of nova shells,” we realized the complexity of
determining a star’s luminosity curve, particularly factors such as its mass, radius, and stage
of life– factors that also play into its stellar classification (Balona and Shobbrook, Tappert
et al.). Through our research, we hope to determine if a star’s luminosity correlates with
its physical features, and if so, which factors most strongly determine its brightness and
luminosity. We anticipate our data analysis will be able to group stars with similar lumi-
nosities and compare within-group and between-group data to determine the factors which
most strongly correspond with stellar luminosity.


**4 Methods**
To determine the correlation between luminosity and other factors (time, mass,
radius, and stage of life, among others), we will first collect the data of stars from public,
usable sources, including the NASA (National Aeronautics and Space Administration) web-
2
site and LightKurve (A python package that is used to find data of different astronomical
objects). For our analysis, we will utilize Python and some add-on python packages (namely
Pandas, NUMPY, MatPlotlib, and LightKurve). These tools will allow us to calculate the
luminosity of different stellar objects and construct their luminosity curves, then group the
stellar objects by their luminosities. We will then study these groups using statistical analysis
to determine within-group as well as between-group similarities and differences to determine
the factors that are most likely to be involved in determining a star’s luminosity.


**References**
Balona, L.A., Shobbrook, R.R. A re-calibration of the luminosities of early-type stars: its
effect on the Cepheid luminosity scale. Monthly Notices of the Royal Astronomical Society
211, 2, 375–390 (1984). https://doi.org/10.1093/mnras/211.2.375
Melnik, A.M., Dambis, A.K. Distance scale for high-luminosity stars in OB associations and
in field with Gaia DR2. Spurious systematic motions. Astrophys Space Sci 365, 112 (2020).
https://doi.org/10.1007/s10509-020-03827-0
Tappert, C., Vogt, N., Ederoclite, A., Schmidtobreick, L., Vuˇckovi ́c, M., Becegato, L.L. The
luminosity evolution of nova shells. Astronomy Astrophysics 641, A122 (2020).
https://doi.org/10.1051/0004-6361/202037913
