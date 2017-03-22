# MatPlotLib

---

### Learning Objectives
***Students will be able to...***

* Import the `matplotlib` library
* Import a text file
* Make a DataFrame
* Filter through a DataFrame

---
### Context 

* The missing limb of pandas

---
### Lessons

##### Part 1 - What is MatPlotLib

* Before we do anything lets install the library

```
pip3 install matplotlib
```
* This is a python 2D plotting library
* It will take your data and create images with that information
* You can start looking at the docs here
	* [MatPlotLib Documentation](http://matplotlib.org/)
	* [Pandas Visualization](http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html)

##### Examples

* import pandas and matplotlib

```
import pandas as pd
import matplotlib.pyplot as plt
```
* `pd.DataFrame` has a [`.plot()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html) method to generate a graph from its data.
* A Plot object has the method `get_figure`, which returns a Figure. 
* A Figure can be saved to a file with the method [`.savefig()`](http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.savefig)
* (`.savefig()` takes the arguments `*args` and `**kwargs`. You don't have to understand them yet, but be sure to notice them because you'll see them again very soon.


##### Basic Plots with matplotlib.pyplot

`matplotlib.pyplot` is a collection of functions that make matplotlib work similar to matlab. Each pyplot function makes some change to a figure. In `matplotlib.pyplot` various states are preserved across function calls, so that it keeps track of things like the current figure and plotting area, and the plotting functions are directed to the current axes. In this section, we'll overview the basic plot types: line plots, scatter plots, and histograms.

##### Line Plots 

Line graphs are plots where a line is drawn to indicate a relationship between a particular set of x and y values.

``` python
import numpy as np
import matplotlib.pyplot as plt
```

To be able to plot anything, we need to provide the data points, so we declare those as follows:

``` python
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
```

Using matplotlib, we can plot a line between plot x and y.
```
plt.plot(x, y)
```

And as always, we use the `show()` method to have the visualizations pop up.
``` python
plt.show()
```

##### Scatter Plots

Alternatively, you might want to plot quantities with 2 positions as data points. To do this, you first have to import the needed libraries, as always. We'll be using the same data from before:

```  python
import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
```

Next, we plot it with the `plt.plot()` method. Note that the `ro` denotes the type of graph we're plotting. 

``` python
plt.plot(x, y, 'o')
```

As always, let's look at what we made:

``` python
plt.show()
```

##### Histograms

Histograms are very often used in science applications and it's highly likely that you will need to plot them at some point. They are very useful to plot distributions. As before, we'll use numpy and matplotlib.

``` python
import numpy as np
import matplotlib.pyplot as plt
```

First, we'll make the data to plot. We're going to make a normal distribution with 1000 points. 

``` python
data = np.random.normal(5.0, 3.0, 1000)
```

Now, we actually make that histogram of the data array and attach a label:

``` python
plt.hist(data)
plt.xlabel("data")
```

Lastly, let's look at what we've made: 

``` python
plt.show()
```

##### Customization

The default customization for matplotlib isn't very appealing or even helpful in data visualization tasks. 


##### Colors

When there are multiple data points or objects, they have to be able to be differentiated between one another. An easy way to do that is by using different marker styles and colors. You can do this by editing the third parameter to include a letter that indicates the color, such as: 

``` python
plt.plot(x, y, "r")
```
This will give you the same line as before, but now it'll be red. 

##### Styles

You can also customize the style of the your lines and markers. With line graphs, you can change the line to be dotted, dashed, etc, for example the following should give you a dashed line now:

``` python
plt.plot(x,y, "--")
```

You can find other linestyles you can use can be found on the [Matplotlib webpage](http://
matplotlib.sourceforge.net/api/pyplot)

``` python
plt.plot(x,y, "b*")
```

With Scatter Plots, you can customize the dots to be squares, pentagons, etc. This will get you the a scatter plot with star markers:

``` python
plt.plot(x,y, "*")
```

##### Labels

We want to always label the axes of plots to tell users what they're looking at. You can do this in matplotlib, very easily:

If we want to attach a label on the x-axis, we can do that with the `xlabel()` function: 
``` python
plt.xlabel("X Axis")
```

With a quick modification, we can also do that for the y-axis:
``` python
plt.ylabel("Y Axis")
```

What good is a visualization without a title to let us know what the visualization is showing? Luckily, matplotlib has a built in function for that:
``` python
plt.title("Title Here")
```

Lastly, we can even customize the range for the x and y axes: 
``` python
plt.xlim(0, 10)
plt.ylim(0, 10)
```
