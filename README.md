# APA Final Data Analysis Project: Crime, Weather & Unemployment in Chicago, Illinois
### Summary
This project will engage in exploratory data analysis in mirroring a classic social science analysis with regards to crime and weather, with the addition of unemployment, but with a more recent dataset. This project will excercise the integration of pandas for reading .CSV files, responding to missing variables, grouping keys and merging datasets. 

## Input Data

The input data is comprised of three .csv files entitled **unemployment.csv**, **Crimes_-_2001_to_present.csv** and **weather.csv**. The weather file consists of relevant weather metrics, including 'Max Temperature', 'Mean Temperature', 'Max Humidity', 'Max Sea Level' and Precipitation from 2001 to 2020. The Crimes dataset contains a variety of law enforcement metrics, the measures that will be utilized in the data are as follows: Date', 'Primary Type','Description','Location Description' and 'Arrest,' again from 2001-2020.The Crime dataset holds a record of crimes committed via block, while offering a description as to they type of location the crime occured in and the nature of the crime committed Lastly, the Unemployment dataset covers employment, unemployment and the unemployment rate for the city labor force from 2000 to 2019.All three datasets include a 'Date' key, which is helpful for first steps into merging datasets. Similiar to the task of identifying trends in electon data, here we want to utilize the complete 'Date' timeline to get a 'big picture' perspective on the impact of weather and unemployment on crime. 


### Deliverables
Five scripts will be generated on Spyder: 1. crime.py will review the data in the large .csv file and develop a datframe of select keys that will be utilized in the merge portion of the project. The script will also produce a .csv file entitled **df_final.csv**, which will include the selected keys for df conconated with another dataframe for the counts and percentages of the'Primary Type' (of crime) key 2. The 'graph.py' script covers basic data visualization for the dataFrame within 'crime.py'-"Primary Type" key through a Bar and Pie chart 3. The script 'weather.py' imports the **weather.csv** datafile and utilizes a groupby function to select relevant key 4&5. The 'unemployment.py' script imports the datafile into Spyder and 'crime_project_merge.py' merges the dataFrames into a final .csv file, **analysis_dataset.csv**.  

### Graph Deliverables

The graph deliverables produced by the graph.py script will be as follows:

 **Primary_TypePie.png**: Plot output showing the ten highest crime types in Chicagopie chart format. The Teh G pie chart will exhibit crime type by percentage.  
 
**Crime_LocationBar.png** & **Crime_LocationPie.png**: Plot output showing the most common location types that a crime has occured in Chicago using bar and pie chart formats. 

**Crime_Year20.png**: Graph showing periodic trend in Chicago crime from 2001-2020 by year.

**Crime_Rolling.png**: Graph exhibits a rolling sum comparision of crimes by day from the past year to offer a clearer visual for crime trend from 2020 to 2019. The visual provides the opportunity to determine whether the crime rate has decreased from a given year, or stays the same. This graph shows an overall decrease in crimes from 2001-2020, with periodic decreases ear the end of each year (winter months) and increases mid to later-mid portion of the year (Spring/Summer).

**Crime_TypeAll.png**: A .png file showing individual graphs by crime type. This visual enables a comparison between the decreasing trend in **Crime_Rolling.png** and the individual trends by crime type. Essentially, these graphs provide answers to the question of whether the overall trend holds true for all crime types, and if not, which types run in conradiction to the trend?

**Crime_TypeBarH.png**: Horizontal Bar graph for Primary Crime Types, interesting visual representation comparing the highest crime  
 types to the remainder of crime types that barely register on the graph, due in large part to the magnitude of crimes such as Theft,  
 Battery and Narcotics. 


### Analysis
The merged datafile will provide the opportunity to integrate the .groupby() function to explore initial relationships for keys across columns, including Primary Crime, Crime Frequency, Dates, Unemployment Rate and Max/Min temperatures to discern any trends that occur by grouping the data. 

### Instructions
A. Script:'crime.py'
The script should be run first, as its main function is to load the **Crimes_-_2001_to_present.csv** datafile and create a dataframe, entitled 'df' with the following keys from the datafile: 'Year', 'Primary Type','Description', 'Location Description' and 'Arrest.' This dataframe will be used for merging in the 'crime_project_merge.py'. 


1. Import modules. 

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
        
   Copy the dataframe 'df' to a .csv file entitled 'df.csv'. 
   
   1. To conduct an  analysis of one of the columns, set variable crime_type 
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
       of values in the 'Counts' column and multiply by 100. The command should look as follows:
       
           crime_type_value_counts['Percentage'] =
           (crime_type_value_counts['Count']/crime_type_value_counts['Count'].sum())* 100   
   
1. Print the first ten elements of crime_type_value_counts by adding the attribute .head(10)) 
   at the end of the dataframe 
   
  
## Script 2: Weather.py
Slightly more involved, this script will load the **weather.csv** data, split the 'Date' key into 'Months' and 'Year', and create a grouped dataframe for the following keys: Year', 'Max TemperatureF', 'Mean TemperatureF','Min TemperatureF','Max Humidity', ' Mean Humidity', ' Min Humidity' and 'PrecipitationIn.' The dataframe, 'grouped_weather', will be copied to a .csv file called **grouped_weather.csv** which will be used for merging. 

2. Import pandas as pd, numpy as np, import csv
2. Print "Weather Dataset"
2. Create variable 'weather' and set it equal to the  
   pd.read_csv("weather.csv") 

2. As 'Year' will be the key employed to merge the datafiles,    
   convert the date column into a format that is acceptable to  
   pandas. The result will be two additional columns entitled 
   'Month' and 'Year'

2. Create a variable named 'grouped_weather' and set it equal to the following: 

     weather.groupby(['Date']).mean().reset_index()

   
2. Include the following column keys to the grouped_weather dataframe:        
   'Date','Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF','Max 
    Humidity', ' Mean Humidity', ' Min Humidity', 'PrecipitationIn']]
    
## Script 3: Unemployment.py
This script will import the unemployment datafile. 

3. import modules: pandas as pd, numpy as  np, import csv
3. import the .csv file for unemployment data in Chicago by creating a variable, 'unemployment' and setting it equal to the function 
   pd.read_csv("unemployment3.csv"
    
3. To review the complete result in the terminal, utilize the function 
   pd.set_option('display.max_columns', None).
   
3. Print the first rows unemployment by adding the attribute .head(5))

Script 4: crime_project_merge.py
This script will merge all of the dataframes on the 'Year' key and generate a final dataframe called 'analysis_dataset', which will then be copied to a .csv file, "crime_info2.csv." The groupby() function will then generate reference .csv files for exploratory analysis, with the most important grouping incorporating 'Mean TemperatureF', 'Primary Type', 'Year' and 'Max/Min' Temperatures.   
 Observations will be recorded in the Crime Results markdown. 

4. Utilize the pd.read_csv function to import the new .csv file, df_final.csv  
   and the original datafiles for weather and unemployment. 
   
    df_final = pd.read_csv("df.csv")
    weather = pd.read_csv("weather.csv")
    unemployment = pd.read_csv("unemployment3.csv") 
   
 4. Create a variable named 'analysis_dataset' and set it equal to the pd.merge   
     function. Within this function, we will merge df_final and weather on the 
    'Year' key. 
    
 4. Use the same dataframe and set it equal to pd.merge() for analysis_dataset 
      and unemployment on the 'Year' key. 
      
 4. Write the dataframe into a .csv file titled "crime_info2.csv")
   
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
