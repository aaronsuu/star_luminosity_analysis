    Stellar brightness vs. time measurements (light curves) for
    "A Search for Variable Stars in the Globular Cluster M4 with K2"
    by Joshua Wallace, Joel Hartman, Gaspar Bakos, and Waqas Bhatti

These data are associated with the publication with the same title and 
authors as indicated above.  Please cite that publication if you use
these data. At time of submission of these light curves to the data
archive, the paper was not published yet, and the archive rules
prevent me from coming back later to edit these files and include the
full publication information, so search for that publication if you
can.  Once it is published, the metadata field for this data
submission should be edited to contain the Digital Object Identifier
of the publication, so you may start your search there. These data are
also associated with the PhD dissertation of Joshua Wallace, graduated
from Princeton University in 2019. 

The data are light curves derived from images taken of the globular
cluster M4 by the Kepler space telescope during the K2 portion of its
mission, specifically during Campaign 2 of that mission, which
occurred in 2014.  A total of 3856 images were taken over
approximately three months at a cadence of approximately half an
hour. The purpose of these observations was to find stars and other
objects that vary in brightness over time --- variable stars.

                      --------------------------

                               License

These data are copyright 2019 by Joshua Wallace, Joel Hartman, and
Gaspar Bakos.

These data are licensed under a Creative Commons Attribution 4.0
International License.

You should have received a copy of the license along with these data.
If not, see <http://creativecommons.org/licenses/by/4.0/>.

                      --------------------------

                            General notes

The files are in a compressed tarball, wallace_data.tgz, for
convenience of download and storage.  The tarball also contains a copy
of this README.  The table found in object_information.txt is included
both in the tarball and as a separate file, the former because it is
information that belongs with the light curves and the latter because
it is a stand-alone table for Joshua Wallace's dissertation.

This data set contains light curves for 4554 objects, stored in the
comma-separated values (CSV) format.  In this format, rows are
separated in the file by new line characters and columns are separated
by commas.  There can be missing data.  The light curves files are
those files with names of format "*_lc.csv", with the * being a
wildcard.  All the light curve files start with either a "V", "S", or
"W".  The first row of each file is a header with labels for each
column, and the rest of the each file contains data and just data.

This data set also contains an additional table
(object_information.txt) that records some additional information on
each object and its associated light curve, including right ascension,
declination, and magnitude (in Gaia G) of each object.  This table is
published as part of Joshua Wallace's dissertation.  It is a plain
text table, with a large and descriptive header marked by lines
beginning with "#" characters and columns separated by arbitrary
numbers of spaces.  It is also planned that a machine-readable version
of the table will be published with the publication indicated at the
beginning of this document. 

                      --------------------------

                          File descriptions


As mentioned, object_information.txt has its own descriptive header,
which should be referenced for any questions on the formatting of that
file.

For the light curve files (those files ending in "_lc.csv"), included
are data describing the time of observation and the observed
brightnesses (in magnitudes) over seven different photometric
apertures and as calculated at three different stages of our
photometric processing. The portion of the file name preceding
"_lc.csv" is the identifier we gave the object for our work and
corresponds to an equivalent identifier listed in the "ID" column of
the table in object_information.txt. The first line of each file is a
header labeling each column.  The first five columns are described below:

 - KBJD: This is Kepler Barycentric Julian Date, with conversion
   between KBJD and Barycentric Julian Date (BJD) being
   KBJD = BJD - 2454833.0

 - raw_ap_chosen: this is the "raw" photometry directly as output by
   our photometric calculation before any post-processing clean up
   occurred.  The "ap_chosen" portion of the name means that these are
   the results from the photometric aperture chosen as the aperture of
   choice for this object for our subsequent analysis.

 - post_decorr_ap_chosen: this is the photometry after applying a
   decorrelation against the roll to clean up much of the systematic
   effects present in the data from the K2 mission.  This is again for
   the chosen aperture.

 - final_ap_chosen: this is the photometry after both applying the
   roll decorrelation and subsequently using the Trend Filtering
   Algorithm to further clean up the data.  The designation of "final"
   means that these were the data used in our analysis; its processing
   was complete.  This is again for the chosen aperture.

 - err_ap_chosen: this is the photometric error, in magnitudes, as
   determined by our photometric calculation.  Errors were not
   additionally calculated for the subsequent processing steps and so
   the error values are applied to all three of raw_ap_chosen,
   post_decorr_ap_chosen, and final_ap_chosen.  We found that the
   errors determined by our calculation were almost certainly
   underestimated relative to the final scatter of the light curves,
   likely due to still-uncorrected systematics in the data.

The subsequent columns are all repeats of the latter four of the five
columns described above for the seven different apertures.  Those
column headers ending in "0" corresponded to the smallest aperture,
those ending in "1" corresponded to the second-smallest aperture, and
so on up to "6".  The aperture sizes used for our calculations were: 
1.5, 1.75, 2.0, 2.25, 2.5, 2.75, and 3.0 pixels in radius.

Note that the set of "*_ap_chosen" columns are a repeat of a set of
one of the other columns with a specified aperture number.  We
included the "*_ap_chosen" columns as a convenience for those
interested in working with the same versions of the light curves that
we did without needing to determine, object-by-object, which columns
should be referenced.

Note also that for all objects and apertures, there are no data for
any of the "post_decorr_ap_*" or "final_ap_*" columns for the first 49
rows. This is an intentional omission as the data did not allow for
our roll decorrelation procedure to work for these 49 observations.
