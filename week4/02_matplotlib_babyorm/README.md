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
