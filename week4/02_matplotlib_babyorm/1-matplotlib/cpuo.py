import pandas as pd
import matplotlib.pyplot as plt

df_cpuo = pd.read_csv('cpuo.csv')

'''
Build and save two graphs.
'''
# These lines do the work.
plot_cpuo_1 = df_cpuo.plot()
plot_cpuo_2 = df_cpuo.plot(title='hello plot', kind='bar')

# These lines save the files.
fig_cpuo_1 = plot_cpuo_1.get_figure()
fig_cpuo_1.savefig('cpuo-default.png')

fig_cpuo_2 = plot_cpuo_2.get_figure()
fig_cpuo_2.savefig('cpuo-bar.png')
