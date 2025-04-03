import datetime as dt
import csv
import json
import matplotlib.pyplot as plt
import pandas as pd
import sys
import re # added this line

def main(input_file, output_file, graph_file):
    print("--START--")
    # Read the data from JSON file
    eva_data = read_json_to_dataframe(input_file)
    # Convert and export data to CSV file
    write_dataframe_to_csv(eva_data, output_file)
    plot_cumulative_time_in_space(eva_data,graph_file)
    print("--END--")

# https://data.nasa.gov/resource/eva.json (with modifications)


def calculate_crew_size(crew):
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        (int): The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1

def add_crew_size_column(df):
    """
    Add crew_size column to the dataset containing the value of the crew size

    Args:
        df (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy

def read_json_to_dataframe(input_file):
    """ read teh data from a JSON file into pandas dataframe
    Clean the data by removing incomplete rows and sort by date
    
    Args: 
        input_file(str): The path to the JSON file
        
    Returns:
        eva_df (pd.Dataframe): The cleande and sorted data as a dataframe structure
        
    """


    print(f'Reading JSON file {input_file}')
    # Read the data from a JSON file into a Pandas dataframe
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean the data by removing any incomplete rows and sort by date
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df

def write_dataframe_to_csv(df, output_file):
    """_summary_

    Args:
        df (_type_): _description_
        output_file (_type_): _description_
    """
    print(f'Saving to CSV file {output_file}')
    # Save dataframe to CSV file for later analysis
    df.to_csv(output_file, index=False)

def text_to_duration(duration): #converts a text duration to a duration in hours?
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60
    return duration_hours

def add_duration_hours_varabile(df):
    df_copy = df.copy()
    df_copy['duration_hours'] = df_copy['duration'].apply(
        text_to_duration
    )
    return df_copy

def plot_cumulative_time_in_space(df, graph_file):
    df = add_duration_hours_varabile(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()

    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    # Plot cumulative time spent in space over years
    df['duration_hours'] = df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

# Main code

if __name__ =="__main__":
    if len(sys.argv) < 3:
        input_file = open('./data/eva-data.json')
        output_file = open('./eva-data.csv')
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

    graph_file = './results/cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)



'''
fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data=[]


for i in range(374):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet


w=csv.writer(output_file)



time = []
date =[]

j=0
for i in data:
    print(data[j])
    # and this bit
    w.writerow(data[j].values())
    if 'duration' in data[j].keys():
        tt=data[j]['duration']
        if tt == '':
            pass
        else:
            t=dt.datetime.strptime(tt,'%H:%M')
            ttt = dt.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()/(60*60)
            print(t,ttt)
            time.append(ttt)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

t=[0]
for i in time:
    t.append(t[-1]+i)

date,time = zip(*sorted(zip(date, time)))



plt.plot(date,t[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
'''