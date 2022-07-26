# Scalable_data_lifecycle_COVID-19_case_study
Excess- A directory containing a variety of tools (some not fully implemented) that are not in the workflow.  

parse.py- The first program to run, it inputs the path to a .csv file and outputs many .csv files, which are renamed to <place>.csv except one named parsed.csv.
This program preprocesses the data and split the data into seperate files based on location.

heat_pair.py- Runs after parse.py, it inputs the path to a .csv file and outputs a .png plot.
This program creates the heatmap and pairplot biplot.

standardize.py- Runs after parse.py, it inputs the path to a .csv file and outputs a .csv file named standardized_<filename>.
This program standardizes the data for use for pca_graph.py.

pca_graph.py- Runs after standardize.py, it inputs the path to a .csv file and outputs a .png.plot.
This program creates the PCA plot and with the weight vectors plotted atop.
