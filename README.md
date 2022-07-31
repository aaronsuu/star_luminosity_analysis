# star_luminosity_analysis
Final Project for University of California - Berkeley's 2022 Summer Sessions Astronomy 9 Class - Group 5



\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[letterpaper, portrait, margin=1in]{geometry}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{float} 
\usepackage{parskip}
\usepackage{color}

\begin{document}
% % % COVER PAGE % % % % % % % % % % % % % % % % % %
\thispagestyle{empty}
\begin{center}


    \vspace*{3.5cm}
    \LARGE\textbf{Luminosity Scales} 
    \\\bigskip\textbf{Project Proposal Version 1.0}
    
    \vspace*{2.5cm}\LARGE Final Project Proposal
    
    \vspace*{1cm}\large ASTRO 9 - Introduction to Python, Summer 2022
    \\\medskip Astronomy Division - University of California, Berkeley

    \vspace*{0.75cm}
    {07/21/2022} % If you are using Overleaf, their server might be located in a different time zone. You can alternatively manually enter the date.

    
\end{center}

% % % PAGE TWO: AUTHORS % % % % % % % % % % % % % % % %
\newpage
\setcounter{page}{1}
\vspace*{3cm}
\begin{center}
    
    \vspace{2cm}
    \LARGE\textbf{Group Members:}
    
    
    \large Ma, Yichen
    
    \large Shah, Manthan
    
    \large Su, Aaron
    
    \large Sun, Chengze
    
    \large Wang, Xinyao
    
    \large Yang, Emily
    
    \large Ye, Jeremy
    
\end{center}

% % % BEGIN PROPOSAL % % % % % % % % % % % % % % % %
\newpage

\section{Abstract}

\textbf{Abstract}:
\textbf{[Problem domain]} Luminosity curves are used to show how the brightness of different stellar objects, especially stars, changes over time. They offer information about any astronomical processes happening, especially if they cause a sudden change in an object's brightness (for example, a supernova causes a sudden increase in brightness). \textbf{[Research question]} Can there be different factors, such as a star's mass and radius, that affect a star's luminosity curve data? If there are stellar factors that influence the luminosity curve, what are they? \textbf{[Methods and results]} For this study, we will analyze and compare luminosity curve data from different types of stars to understand what affects a star's brightness and luminosity. \textbf{[Conclusions]} Overall, the data findings should support the idea that a star's luminosity curve can be influenced by different stellar properties.

\section{Background}
\textbf{Background}: Luminosity Scales are one of the foundations of modern day Astronomy. Research on luminosity has been conducted as far back as the 1930s. Fortunately, we made massive improvements to our technology over the last 100 years, which means that we have tools such as computers and Python to have a better understanding of the relationship of how factors eventually impact luminosity scales. More recent articles also have demonstrated an renewed interest in luminosity scales. One area that our group is significantly interested in is determining which variables can affect the luminosity scale of stars observed by humans on earth.


\section{Research Question}
Our inspiration for this project originates from several papers studying how luminosity curves are calculated, as well as the launch of the James Webb Telescope. Through papers such as "A re-calibration of the luminosities of early-type stars: its effect on the Cepheid luminosity scale," and "The luminosity evolution of nova shells," we realized the complexity of determining a star's luminosity curve, particularly factors such as its mass, radius, and stage of life-- factors that also play into its stellar classification (Balona and Shobbrook, Tappert et al.). Through our research, we hope to determine if a star's luminosity correlates with its physical features, and if so, which factors most strongly determine its brightness and luminosity. We anticipate our data analysis will be able to group stars with similar luminosities and compare within-group and between-group data to determine the factors which most strongly correspond with stellar luminosity.

\section{Methods}

\textbf{Methods}: To determine the correlation between luminosity and other factors (time, mass, radius, and stage of life, among others), we will first collect the data of stars from public, usable sources, including the NASA (National Aeronautics and Space Administration) website and LightKurve (A python package that is used to find data of different astronomical objects). For our analysis, we will utilize Python and some add-on python packages (namely Pandas, NUMPY, MatPlotlib, and LightKurve). These tools will allow us to calculate the luminosity of different stellar objects and construct their luminosity curves, then group the stellar objects by their luminosities. We will then study these groups using statistical analysis to determine within-group as well as between-group similarities and differences to determine the factors that are most likely to be involved in determining a star's luminosity.


\section*{References}

Balona, L.A., Shobbrook, R.R. A re-calibration of the luminosities of early-type stars: its effect on the Cepheid luminosity scale. Monthly Notices of the Royal Astronomical Society 211, 2, 375–390 (1984). https://doi.org/10.1093/mnras/211.2.375

Melnik, A.M., Dambis, A.K. Distance scale for high-luminosity stars in OB associations and in field with Gaia DR2. Spurious systematic motions. Astrophys Space Sci 365, 112 (2020). https://doi.org/10.1007/s10509-020-03827-0

Tappert, C., Vogt, N., Ederoclite, A., Schmidtobreick, L., Vučković, M., Becegato, L.L. The luminosity evolution of nova shells. Astronomy & Astrophysics 641, A122 (2020). 
\linebreak
https://doi.org/10.1051/0004-6361/202037913

\end{document}
