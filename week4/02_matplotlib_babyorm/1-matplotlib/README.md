Using MatPlotLib with Pandas
============================

Pandas with MatPlotLib is like the rest of Pandas: there is
already a library method to do what you want, you just have to
know the method and pass it the proper arguments.

[Getting Started](http://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html)

The sample code builds two basic, but essentially meaningless graphs.
Your job is to create two graphs with meaning.

*Hints*
* `pd.DataFrame` has a [`.plot()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html) method to generate a graph from its data.
* A Plot object has the method `get_figure`, which returns a Figure. 
* A Figure can be saved to a file with the method [`.savefig()`](http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.savefig)

(`.savefig()` takes the arguments `*args` and `**kwargs`. You don't
have to understand them yet, but be sure to notice them because you'll
see them again very soon.

### Exercise 1
Build a bar graph showing the total number of police complaints by
year.

### Exercise 2
Build a bar graph showing the total number of police complaints by
Precinct / Command in 2009.
