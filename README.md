# APA Final Data Analysis Project: Crime, Weather & Unemployment in Chicago, Illinois
### Summary
This project will engage in exploratory data analysis in mirroring a classic social science analysis with regards to crime and weather, with the addition of unemployment, but with a more recent dataset. This project will excercise the integration of pandas for reading .CSV files, responding to missing variables, grouping keys and merging datasets. 

## Input Data

The input data is comprised of three .csv files entitled **unemployment.csv**, **Crimes_-_2001_to_present.csv** and **weather.csv**. The weather file consists of relevant weather metrics, including 'Max Temperature', 'Mean Temperature', 'Max Humidity', 'Max Sea Level' and Precipitation from 2001 to 2020. The Crimes dataset contains a variety of law enforcement metrics, the measures that will be utilized in the data are as follows: Date', 'Primary Type','Description','Location Description' and 'Arrest,' again from 2001-2020.The Crime dataset holds a record of crimes committed via block, while offering a description as to they type of location the crime occured in and the nature of the crime committed Lastly, the Unemployment dataset covers employment, unemployment and the unemployment rate for the city labor force from 2000 to 2019.All three datasets include a 'Date' key, which is helpful for first steps into merging datasets. Similiar to the task of identifying trends in electon data, here we want to utilize the complete 'Date' timeline to get a 'big picture' perspective on the impact of weather and unemployment on crime. 


### Deliverables
Five scripts will be generated on Spyder: 1. crime.py will review the data in the large .csv file and develop a datframe of select keys that will be utilized in the merge portion of the project. The script will also produce a .csv file entitled **df_final.csv**, which will include the selected keys for df conconated with another dataframe for the counts and percentages of the'Primary Type' (of crime) key 2. The 'graph.py' script covers basic data visualization for the dataFrame within 'crime.py'-"Primary Type" key through a Bar and Pie chart 3. The script 'weather.py' imports the **weather.csv** datafile and utilizes a groupby function to select relevant key 4&5. The 'unemployment.py' script imports the datafile into Spyder and 'crime_project_merge.py' merges the dataFrames into a final .csv file, **analysis_dataset.csv**.  

### Analysis
The merged datafile will provide the opportunity to integrate the .groupby() function to explore initial relationships for keys across columns, including Primary Crime, Crime Frequency, Dates, Unemployment Rate and Max/Min temperatures to discern any trends that occur by grouping the data. 

### Instructions
Script: crime.py

1. Import the following modules for each script: 
from os import listdir
import matplotlib.pyplot as plt (##For graphs and charts in Spyder)
import pandas as pd ((##Ideal module for data analysis, especially for taking datafile (.csv) and creating dataframes).
from numpy.linalg import * ##(all numpy functions loaded into local script space)
from numpy import linalg as la ##(Important as a general array processing tool, includes critical linear algebra capabilities as well. Typically imported as 'np' to streamline calls to its functions)
import numpy as np
import scipy.linalg as SL ##(scipy is the carrier for models/files for a number of  imported packages, including pandas, MatPlotlib and NumPy). 
import numpy
import statsmodels.formula.api as smf
from scipy.stats.stats import pearsonr
import statsmodels.api as sm
from scipy import stats
import csv ##(module imports tools for reading and writing data in CSV format). 


1. use pd.read_csv("filename", low memory= False) to import the crime statistic    
   datafile into variable 'crime_data.'Due to the size of the datafile, integrate low        
   memory= False to ensure more efficient system output (or data parsing) through  
   less memory usage. As the variable 'crime_data' will be utilized to create a  
   dataframe, we wil opt to use the 'pd.read_csv' call. 
   
   
1. Review the columns in the datafile by attaching the .columns attribute to the end    of  
   the variable 'crime_data.' Print this attribute and label the action "Crime  
    Dataset Columns."
   
1. Integrate the .info attribute to the end of 'crime_data' to generate a summary of 
   the datafile. This is useful as a quality assurance measure to ensure all of your    
   information was succesfully imported. Print this action and the label "Crime 
   Dataset Summary"
   
1. To view the dataset with actual values, print the following attribute: 
         print(crime_data.head(5))
         
  This will generate an output of the first five rows of the datafile, complete with   
   corresponding values for each of the columns. 
   
1. To manage colummns with NaN (missing values), employ the following call: 
       print(crime_data.columns[crime_data.isnull().any()].tolist())
    
   This command will create a list of columns with empy values. 
   
1. After the list is generated, we can use the following function to eliminate  
   missing values from the dataframe:
               crime_data = crime_data.dropna()
            

1. We can now select the final columns from the dataframe for further exploratory  
   analysis. Create a variable called 'df' that is equal to the following columns in 
   crime_data:
        [[Date', 'Primary Type','Description', 'Location Description','Arrest']]
   
   1. To conduct an in-depth analysis of one of the columns, set variable crime_type 
      equal to a new dataframe for 'Primary Type', which pertains to the most  
      prolific crimes within the dataset by count and percentage. Utilize the  
      following function to extract the 'Primary Type' key from variable 'df' and  
      build a new dataframe specifically for 'Primary Type'and corresponding values:
      
      crime_type = pd.DataFrame(df['Primary  Type'].value_counts()).reset_index()            
      As crime_type is a new index that will only include the values for 'Primary  
      Type' and not the other columns stored in 'df', reseting the index will remove 
      one or more levels of the dataframe. 
     
   1. To build the 'crime_type' dataframe, we are going to take the values within   
      'Primary Type' (the different types of crimes) and order them by their count 
       and percentage. To accomplish this task we can first include the attribute  
      .columns at the end of crime_type and set the dataframe equal to the column          
      list 'Crime Type' and 'Count.'
         
   
   1. Now that we understand what our columns and values look like in the terminal,  
      let's add a function to crime_type that will allow us to organize the data in  
      descending order, so the first element will be the most frequently occuring. As      
      we are reordering the dataframe, let's drop the previous index through  
      .reset_index()). The command will be as follows: 
      
      crime_type_value_counts = pd.DataFrame(df['Primary Type'].value_counts().reset_index()) 
   
   1. Review the columns for the new dataframe by including the attribute .columns at the end 
       of crime_type_value_counts and       set it equal to column keys 'Crime Type' and 
       'Count.'
   
  
   1. To generate a percentage of each crime type as a fraction of the total amount of   
       frequently occuring crimes, set crime_type_value_counts['Percentage'] equal to the   
       the count key in the dataframe, crime_type_value_counts['Count'], divided by the sum 
       of values in the         
       'Counts' column and multiply by 100. The command should look as follows:
       
   crime_type_value_counts['Percentage'] =
   (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum())* 100   
   
1. Print the first ten elements of crime_type_value_counts by adding the attribute .head(10)) 
    at the end of the dataframe 
   
1. Create a variable named 'df_final' and set it equal to a merged dataframe for df and  
   crime_type_value_counts. Use the function pd.concat[()] to join the two dataframes. Print the final iteration of the merged  
   dataframes (df_final).
  
1. Input the following command to write df_final to a .csv file entitled "df_final.csv."

   df_final.to_csv("df_final.csv", index = False, header = True, sep = ',', encoding = 'utf-8')   

## Script 2: Weather.py

2. Import pandas as pd, numpy as np, import csv
2. Print "Weather Dataset"
2. Create variable 'weather' and set it equal to the pd.read_csv("weather.csv") 
2. For review, print the following attributes:
     weather.columns
     weather.head(5))
     weather.info())
     
2. Create a variable named 'grouped_weather' and set it equal to the following: 

     weather.groupby(['Date']).mean().reset_index()

   The  groupby function will enable us to split the data into  
   groups based on the 'Date' key, apply the 'group' function to each element  
   and combine the results into a dataframe ('grouped_weather')
   
2. Include the following column keys to the grouped_weather dataframe:        
   'Date','Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF','Max 
    Humidity', ' Mean Humidity', ' Min Humidity', 'PrecipitationIn']]
    
## Script 3: Unemployment.py

3. import modules: pandas as pd, numpy as  np, import csv
3. import the .csv file for unemployment data in Chicago by creating a variable, 
    'unemployment' and setting it equal to the function 
     pd.read_csv("unemployment3.csv"
    
3. To review the complete result in the terminal, utilize the function 
   pd.set_option('display.max_columns', None).
   
3. Print the first rows unemployment by adding the attribute .head(5))

Script#4: crime_project_merge.py

4. import modules: pandas as pd, numpy as  np, import csv
4. Utilize the pd.read_csv function to import the new .csv file, df_final.csv  
   and the original datafiles for weather and unemployment. 
   
   df_final = pd.read_csv("df_final.csv")
   weather = pd.read_csv("weather.csv")
   unemployment = pd.read_csv("unemployment3.csv") 
   
 4. Create a variable named 'analysis_dataset' and set it equal to the pd.merge     function. Within this function, we will merge df_final and weather on the  
    'Date' key. The command will be as follows: 
    
    analysis_dataset = pd.merge(df_final, weather, on=['Date'])
    
 4. Use the same dataframe and set it equal to pd.merge() for analysis_dataset 
      and unemployment on the 'Date' key. 
      
 4. Print "Analysis Dataset Information" and then print the first five rows of      the dataframe. 
  
 4. Write the dataframe into a .csv file titled "crime_info1.csv")
   
## Script 5 graphs.py

##Basic Data Visaulization utilizing Matplotlib to create bar and pie graphs for columns 'crime type' and 'location description' by crime count.

5. import all modules from the 'crime.py' script, with the inclusion of the following: 

import matplotlib.pyplot as plt; plt.rcdefaults()
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px

5. Import the "Crimes_-_2001_to_present.csv" by creating dataframe 'crime_type' and setting 
   it equalto the pd.read_csv("filename")   
   function 
 
 5. Copy the 'crime_type_value_counts' dataframe block from  
   'crime.py' script. 
        crime_type = pd.DataFrame(df['Primary Type'].value_counts()).reset_index() 
        crime_type.columns = ['Crime Type', 'Count']
        crime_type_value_counts = pd.DataFrame(df['Primary Type'].value_counts().reset_index())
        crime_type_value_counts.columns = ['Crime Type', 'Count']
    crime_type_value_counts['Percentage'] = (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum()) * 100
        print(crime_type_value_counts.head(10))
        
  5. The first bar graph will incorporate Crime Count in Chicaco by Type. For the graph, create a variable called 'objects'      and set it equal to the following elements: 'THEFT', 'BATTERY', 'CRIMINAL DAMAGE', 'ASSAULT', 'OTHER', 'DECEPTIVE  
     PRACT','NARCOTICS', 'BURGLARY', 'ROBBERY', 'MOTOR  THEFT'). On a new line, you can dictate font size by setting  
     fontsize equal to 10. 
     
  5. To establish the arrangement of y_pos, set it equal to the following function:
                 np.arange(len(objects))  
                 
    On the next line, integrate the values under the 'Count' column in correspondence with the order of the Crime Type in  
   'Objects.'Refer to the output of  print(crime_type_value_counts.head(10)) for these values. 
   
  5. Implement the following commands to align the graph, plot x and y labels and create the graph title. 
                  plt.bar(y_pos, performance, align='center', alpha=1.0)
                  plt.xticks(y_pos, objects)
                  plt.ylabel('Count')
                  plt.title(' Crime Count in Chicago by Type')
                  plt.show()  
                  
  5. Save bar graph as a .png file. 
  
  ## Pie Chart
  
  5. Create a variable called 'labels' and set it equal to a list of crime types noted in the 'objects' variable for bar  
     graph. Create a variable called sizes and set it equal to a list of  descending values noted in the 'Percentage' column      of crime_type_value_counts.head(10)). On the next line, create a variable called 'colors' and set it equal to a list of
     colors (i.e. ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'pink', 'green', 'black', 'purple', 'orange', 'red']
     which correspond to the crime types in 'labels'.
     
  5. Start plotting the pie chart by integrating the following command lines:
  
  5. Use the following command will establish the text and patches (face & edge color) for the graph. 
                  patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)

  5. To establish similiar parameters for the graph legend, implement the following: 
                  plt.legend(patches, labels, loc="best")

  5. To establish equal spacing for elements on the axis, padding between the figure edge and the edges of subplots  
     and expand a specific slice of the pie chart, integrate the following: 
                  plt.axis('equal')
                  plt.tight_layout()
                  explode = (0.1, 0, 0, 0,0,0,0,0,0,0 ) 
                  
 5. Lastly, utilize the following command to align graph parameters and establish the 'Count' elements as perentages:
 
                     plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                     autopct='%1.1f%%', shadow=True, startangle=140)explode = (0.1, 0, 0, 0,0,0,0,0,0,0 ) 
                     
   Plot the axis and display the graph by excercising the plot.axis('equal') and plt.show() functions. Save the graph as a 
   .png. 
   
 6. The same steps can be applied to Crime Count by Location Description. Please see the code in graph.py for details. 
