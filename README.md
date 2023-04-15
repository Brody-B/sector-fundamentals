# Sector-Fundamentals

This is a simple application I use in the course of my investment research to make comparative analysis of stocks within industries fast and easy. It is a useful tool that has saved me lots of time. 

The app scrapes fundamental data for each stock in the selected industry from FinViz, and compiles into a pandas DataFrame, then I apply a heatmap background gradient to the table to visualize the best and worst stocks across each fundamental metric.

I containerize this application using Docker. To run, first build the Docker Image and then run the image once built. 
