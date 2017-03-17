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
* Pandas allows us to deal with data in a way that us humans can understand it
* We are provided labeled columns and indexes. 
* It allows us to effortlessly import data from files such as CSVs, quickly apply complex transformations and filters to our data and much more. 
* Along with Numpy and Matplotlib, it helps create a really strong base for data exploration and analysis in Python. 
* Their documentation is here: [http://pandas.pydata.org/](http://pandas.pydata.org/)
* Check out the section titled "10 Minutes to Pandas" Here
	* [http://pandas.pydata.org/pandas-docs/stable/10min.html](http://pandas.pydata.org/pandas-docs/stable/10min.html)

``` python
import pandas as pd 
from pandas import Series, DataFrame
```

##### Part 2 - Series

* A Series is a one-dimensional array-like object containing an array of data (of any NumPy data type) and an associated array of data labels, called its index. 
* The simplest Series is formed from only an array of data:

``` python
obj = Series([4, 7, -5, 3])
```

Often it will be desirable to create a Series with an index identifying each data point:

``` python
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
```

You can also take a dictionary and convert it to a Series:
``` python
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
```

##### Part 3 - DataFrames

* A DataFrame represents a tabular, spreadsheet-like data structure containing an ordered collection of columns, each of which can be a different value type (numeric, string, boolean, etc.).
* There are numerous ways to construct a DataFrame, though one of the most common is from a dict of equal-length lists or NumPy arrays:

``` python
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002], 'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
```

Then we take this and convert it to a DataFrame:

``` python
frame = DataFrame(data)
```

This gets us:

```
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
```
You can also specify the sequence of columns by:

``` python
DataFrame(data, columns=['year', 'state', 'pop'])
```

##### Part 4 - Apply

Lets's generate a random dictionary:

``` python
frame = DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
```

With this, we can apply a function on a DataFrame:
``` python
np.abs(frame)
```

We can also apply functions with the `apply()` method:

``` python
f = lambda x: x.max() - x.min()
frame.apply(f)
```

##### Part 5 - Sorting

To sort lexicographically by row or column index, use the sort_index method, which returns a new, sorted object:

``` python
frame.sort_index()
```

Naive Bayes works on Bayes Theorem of probability to predict the class of a given data point. Naive Bayes is extremely fast compared to other classification algorithms and works with an assumption of independence among predictors. 

The Naive Bayes model is easy to build and particularly useful for very large data sets. Along with simplicity, Naive Bayes is known to outperform even highly sophisticated classification methods.


### 2.3 Challenge

Recall Bayes Theorem, which provides a way of calculating the posterior probability. Its formula is as follows:

![alt text](https://github.com/ByteAcademyCo/stats-programmers/blob/master/bayes.png?raw=true "Logo Title Text 1")

Let's go through an example of how the Naive Bayes Algorithm works using `pandas`. We'll go through a classification problem that determines whether a sports team will play or not based on the weather. 

Let's load the module data:

``` python
import pandas as pd
f1 = pd.read_csv("./weather.csv")
```

#### 2.3.1 Frequency Table

The first actual step of this process is converting the dataset into a frequency table. Using the `groupby()` function, we get the frequencies:

``` python
df = f1.groupby(['Weather','Play']).size()
```

Now let's split the frequencies by weather and yes/no. Let's start with the three weather frequencies:

``` python
df2 = f1.groupby('Weather').count()
```

Now let's get the frequencies of yes and no:

``` python
df1 = f1.groupby('Play').count()
```

#### 2.3.2 Likelihood Table


Next, you would create a likelihood table by finding the probabilites of each weather condition and yes/no. This will require that we add a new column that takes the play frequency and divides it by the total data occurances. 


``` python
df1['Likelihood'] = df1['Weather']/len(f1)
df2['Likelihood'] = df2['Play']/len(f1)
```

This gets us a dataframe that looks like:

```
          Play  Likelihood
Weather                   
Overcast     4    0.285714
Rainy        5    0.357143
Sunny        5    0.357143
```

Now, we're able to use the Naive Bayesian equation to calculate the posterior probability for each class. The highest posterior probability is the outcome of prediction.

#### 2.3.1 Calculation

So now we need a question. Let's propose the following: "Players will play if the weather is sunny. Is this true?"

From this question, we can construct Bayes Theorem. So what's our P(A|B)? P(Yes|Sunny), which gives us:

P(Yes|Sunny) = (P(Sunny|Yes)*P(Yes))/P(Sunny)

Based off the likelihood tables we created, we just grab P(Sunny) and P(Yes). 

``` python
ps = df2['Likelihood']['Sunny']
py = df1['Likelihood']['Yes']
```

That leaves us with P(Sunny|Yes). This is the probability that the weather is sunny given that the players played that day. In `df`, we see that the total number of `yes` days under `sunny` is 3. We take this number and divide it by the total number of `yes` days, which we can get from `df`. 

``` python
psy = df['Sunny']['Yes']/df1['Weather']['Yes']
```

Now, we just have to plug these variables into bayes theorem: 

``` python
p = (psy*py)/ps
```

And we get:

```
0.59999999999999998
```

That means the answer to our original question is yes!
