# School_District_Analysis
The purpose of this analysis was to examine the reading and math test scores for a set of high schools. 

- How is the district summary affected?

By altering the students and test scores of the select subset of students - Thomas High School 9th graders - it slightly lowered both the reading and math scores as well as slightly lowered the the percent of students passing each subject.

- How is the school summary affected?

The average scores as well as % passing will have been altered in this dataframe.

- How does replacing the ninth graders’ math and reading scores affect Thomas High

By removing their math and reading scores you are changing the equation in which the averages and % passing are calculated on. The average goes down which implies you are removing scores higher than the average and the % passing also goes down which mean we not removing them from that equation. 

- School’s performance relative to the other schools?

It did cause Thomas High School to drop in the ranks in many of the categories including but not limited to Average Math Score and Average Reading Score although doesn't affect their raking in % overall passing.

- How does replacing the ninth-grade scores affect the following:

    - Math and reading scores by grade

    The only field that would be affected by this change would be Thomas High Schools 9th grade reading and math scores which are being coded as not available. 

    - Scores by school spending

    While no change appears to have occurred on the surface I would suspect if you went out enough decimal places the things that would be affected are the the average score and % columns because scores were removed there was no change for Thomas High School. However, due to the number of students being averaged out in this calculation we are not seeing any change in the current view.  As far as spending per student so it did not move to a different bucket.

    - Scores by school size

    While no change appears to have occurred on the surface I would suspect if you went out enough decimal places the things that would be affected are the the average score and % columns because scores were removed there was no change for Thomas High School. However, due to the number of students being averaged out in this calculation we are not seeing any change in the current view.  As far as spending per student so it did not move to a different bucket.  

    - Scores by school type

    We see no change in this analysis.

# Thomas High School Summary: 
Thomas High School has suspected its 9th graders of cheating so their scores have been removed from the analysis to see how the final values would change. Overall this did not seem to have a large impact due to the small number of THS 9th graders relative to total students who took the tests. Thomas High School didn't change ranking in over all passing percentage for reading and math. It also did not have any impact on total score averages. We did see a slight lowering of both the reading and math scores as well as slightly lowered the the percent of students passing each subject. We also saw an obvious whole when looking at schools by grade because we removed all of THS 9th graders not just a subset of them. 

version: Python 3.7
