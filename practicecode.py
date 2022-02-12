#4.3.4
# A dictionary of high schools and the type of school.
hs_types = [{"High School": "Griffin", "Type":"District"},
            {"High School": "Figueroa", "Type": "District"},
            {"High School": "Wilson", "Type": "Charter"},
            {"High School": "Wright", "Type": "Charter"}]

print(f'{hs_types["High School"]}, {hs_types["Type"]}')


TypeError                                 Traceback (most recent call last)
C:\Users\ETHOMA~1\AppData\Local\Temp/ipykernel_16504/2926504258.py in <module>
      5                     {"High School": "Wright", "Type": "Charter"}]
      6 
----> 7 print(f'{hs_types["High School"]}, {hs_types["Type"]}')

TypeError: list indices must be integers or slices, not str


#4.3.5

#add pandas dependency. 
import pandas as pd

# A dictionary of high schools
high_school_dicts = [{"School ID": 0, "school_name": "Huang High    School", "type": "District"},
                   {"School ID": 1, "school_name": "Figueroa High School", "type": "District"},
                    {"School ID": 2, "school_name":"Shelton High School", "type": "Charter"},
                    {"School ID": 3, "school_name":"Hernandez High School", "type": "District"},
                    {"School ID": 4, "school_name":"Griffin High School", "type": "Charter"}]

# Create a Pandas Series from a list 
school_df = pd.DataFrame(high_school_dicts)
school_df


#______________________________________
#add pandas dependency. 
import pandas as pd
# Three separate lists of information on high schools
school_id = [0, 1, 2, 3, 4]

school_name = ["Huang High School", "Figueroa High School",
"Shelton High School", "Hernandez High School","Griffin High School"]

type_of_school = ["District", "District", "Charter", "District","Charter"]

#initilize data frame 
schools_df = pd.DataFrame()

schools_df["School ID"] = school_id
schools_df["School Name"] = school_name
schools_df["Type"] = type_of_school


#print the data frame
schools_df


#_________________________________________________
#4.4.3
# Add the dependencies.
import pandas as pd
import os

# Files to load
school_data_to_load = os.path.join("Resources", "schools_complete.csv")
student_data_to_load = os.path.join("Resources", "students_complete.csv")

##OR##
# Add the Pandas dependency.
import pandas as pd
# Files to load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# look at the first or last X rows
school_data_df.head(3)
school_data_df.tail(3)


#_____________________________________________
#4.5.1 
import pandas as pd

# Files to load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# read schools data in data frame
school_data_df = pd.read_csv(school_data_to_load)
school_data_df

#Read the student data file and store in dataframe.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()

# Determine if there are any missing values in the school data.
school_data_df.count()

# Determine if there are any missing values in the student data.
student_data_df.count()

# determine if there are missing values in the school data 
school_data_df.isnull()

# determine if there are missing values in the student data
student_data_df.isnull().sum()