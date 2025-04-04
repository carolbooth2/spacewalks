# How to generate a graph from a JSON data file
1. copy the source data into the data directory
    `cp myjson.json <path-to-spacewalks>/data/`
2. call the function
    `python3 eva_data_analysis.py data/eva-data.json output.csv newgraph.png `
3. the output PNG will be saved in the results directory
