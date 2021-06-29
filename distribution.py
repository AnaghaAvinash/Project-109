#Importing necessary modules.
import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

#Reading and converting the data to a list.
df   = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

#Finding the mean, median, mode and standard deviation of the given data.
mean   = sum(data) / len(data)
median = st.median(data)
mode   = st.mode(data)
dev    = st.stdev(data)

#Printing the mean median, mode and standard deviation of the given data.
print("Mean of the given data is "+str(mean))
print("Median of the given data is "+str(median))
print("Mode of the given data is "+str(mode))
print("Standard deviation of the given data is "+str(dev))

#Finding start and end values of standard deviations.
firstDeviationStart , firstDeviationEnd   = mean - dev    , mean + dev
secondDeviationStart, secondDeviationEnd  = mean - (2*dev), mean + (2*dev)
thirdDeviationStart , thirdDeviationEnd   = mean - (3*dev), mean + (3*dev)

#Calculating percentage of the given data.
listOfFirstDeviation  = [result for result in data if result > firstDeviationStart  and result  < firstDeviationEnd]
listOfSecondDeviation = [result for result in data if result > secondDeviationStart and result  < secondDeviationEnd]
listOfThirdDeviation  = [result for result in data if result > thirdDeviationStart  and result  < thirdDeviationEnd]

#Printing the result 
print("{}% of the data lies within 1 standard deviation" .format(len(listOfFirstDeviation) * 100.0 / len(data)))
print("{}% of the data lies within 2 standard deviations".format(len(listOfSecondDeviation)* 100.0 / len(data)))
print("{}% of the data lies within 3 standard deviations".format(len(listOfThirdDeviation) * 100.0 / len(data)))

#Plotting a graph
fig = ff.create_distplot([data], ["reading scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
fig.add_trace(go.Scatter(x = [firstDeviationStart , firstDeviationStart] , y = [0, 0.17], mode = "lines", name = "Standard deviation - 1"))
fig.add_trace(go.Scatter(x = [firstDeviationEnd   , firstDeviationEnd]   , y = [0, 0.17], mode = "lines", name = "Standard deviation - 1"))
fig.add_trace(go.Scatter(x = [secondDeviationStart, secondDeviationStart], y = [0, 0.17], mode = "lines", name = "Standard deviation - 2"))
fig.add_trace(go.Scatter(x = [secondDeviationEnd  , secondDeviationEnd]  , y = [0, 0.17], mode = "lines", name = "Standard deviation - 2"))
fig.show()