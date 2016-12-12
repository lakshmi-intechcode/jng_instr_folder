# Pandas

---

### Learning Objectives
***Students will be able to...***

* Import the `pandas` library
* Import a text file
* Make a DataFrame
* Filter through a DataFrame

---
### Context 

* Pandas is a widely used library for filtering through large data sets

---
### Lessons

##### Part 1 - What is Pandas

* Today you'll get some time to dive into the `pandas` library
* This is an open source library that is used to import files and run data analysis
* Their documentation is here: [http://pandas.pydata.org/](http://pandas.pydata.org/)
* Check out the section titled "10 Minutes to Pandas" Here
	* [http://pandas.pydata.org/pandas-docs/stable/10min.html](http://pandas.pydata.org/pandas-docs/stable/10min.html)

##### Part 2- Series and DataFrames

* `DataFrame` - A two dimensional labeled data structure. 
* `.read_csv()` - The pandas way of importing the contents of a file and returning a data frame

```
import pandas as pd

df = pd.read_csv('cpuo.csv')

print(df)
```
* `Series` - A one-dimensional labeled array
	* A column inside of a Pandas DataFrame is an example of a `Series`	
##### Part 3 - Some Pandas Functions

* `head` - returns first n rows

```
df.head(n=5) 
```
* `tail` - returns last n rows

```
df.tail(n=5)
```
* Target by specific column label to return a `Series`

```
print(df['Ranking'])
print(df['Complaints Count'])
print(df['Year'])
```
* Get the mean of a column

```
# print(df["Year"].mean())
```