import sys
import numpy as np
from itertools import izip, count
import sqlalchemy
import pyodbc
from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.lines as lines
from scipy.interpolate import pchip
from pylab import rcParams

def handle_close(evt):
    #print('Closed Figure!')
    sys.exit()

if __name__ == "__main__":
         
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 9}
    
    matplotlib.rc('font', **font)
    rcParams['figure.figsize'] = 15, 6
    #plt.ion() #Tell matplotlib you want interactive mode to plot live data

    # Connect to Microsoft SQL and get graph configuration row 
    # Table design
    # x1name, y1name, y2name, y3name, y4name, y5name, y6name, y7name, y8name, xscale, title, numplots, dataid
    engine = sqlalchemy.create_engine("mssql+pyodbc://sa:nimda@Logging")
    connection2 = engine.connect()
    resoverall = connection2.execute("SELECT * FROM datalogcfg where dataid = 1")
    config_df = DataFrame(resoverall.fetchall())

    # Get the columns and store into somthing understandable
    x1name = config_df.loc[0,0]
    y1name = config_df.loc[0,1]
    y2name = config_df.loc[0,2]
    y3name = config_df.loc[0,3]
    y4name = config_df.loc[0,4]
    y5name = config_df.loc[0,5]
    y6name = config_df.loc[0,6]
    y7name = config_df.loc[0,7]
    y8name = config_df.loc[0,8]
    xscale = config_df.loc[0,9]
    title = config_df.loc[0,10]
    numplots = config_df.loc[0,11]

    # Append the in comming data from database to lists for streaming.
    xaxis1 = []
    yaxis1 = []
    yaxis2 = []
    yaxis3 = []
    yaxis4 = []
    yaxis5 = []
    yaxis6 = []
    yaxis7 = []
    yaxis8 = []

    # Database index for SQL Select statement
    i=1

    # Configure the number of axes with the number of graphs in database
    if numplots == 1:
        fig, ax1 = plt.subplots()
        fig.tight_layout()		
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1]	
        ax1.set_title(title) 
        axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 	
    if numplots == 2:
        fig, ax1 = plt.subplots()
        fig.tight_layout()	
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        ax1.set_title(title)  	
        axes1 = [ax1, ax1.twinx()]
        axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue')
    if numplots == 3:
        fig, ax1 = plt.subplots()
        fig.tight_layout()	
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1, ax1.twinx(), ax1.twinx() ]
        ax1.set_title(title) 	
        axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 		
    if numplots == 4:
        fig, ax1 = plt.subplots()
        fig.tight_layout()		
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1, ax1.twinx(), ax1.twinx(), ax1.twinx() ]
        ax1.set_title(title)  	
        axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 		
    if numplots == 5:
        fig, (ax1 ,ax2) = plt.subplots(2, sharex=True)
        fig.tight_layout()		
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1, ax1.twinx(), ax1.twinx(), ax1.twinx()]
        axes2 = [ax2]
        ax1.set_title(title)		
        #axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 	
        axes2[0].set_xlabel(x1name, color='blue')
        axes2[0].tick_params(axis='y', colors='blue')
        axes2[0].spines['bottom'].set_color('blue') 		
    if numplots == 6:
        fig, (ax1 ,ax2) = plt.subplots(2, sharex=True)
        fig.tight_layout()		
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1, ax1.twinx(), ax1.twinx(), ax1.twinx()]
        axes2 = [ax2, ax2.twinx()]
        ax1.set_title(title)		
        #axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 	
        axes2[0].set_xlabel(x1name, color='blue')
        axes2[0].tick_params(axis='y', colors='blue')
        axes2[0].spines['bottom'].set_color('blue') 
    if numplots == 7:
        fig, (ax1 ,ax2) = plt.subplots(2, sharex=True)
        fig.tight_layout()		
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1, ax1.twinx(), ax1.twinx(), ax1.twinx()]
        axes2 = [ax2, ax2.twinx(), ax2.twinx()]
        ax1.set_title(title)		
        #axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 	
        axes2[0].set_xlabel(x1name, color='blue')
        axes2[0].tick_params(axis='y', colors='blue')
        axes2[0].spines['bottom'].set_color('blue') 
    if numplots == 8:
        fig, (ax1 ,ax2) = plt.subplots(2, sharex=True)
        fig.tight_layout()		
        fig.subplots_adjust(bottom=0.09)
        fig.subplots_adjust(left=0.05)
        fig.subplots_adjust(right=0.8)
        fig.canvas.set_window_title('Matplotlib Interpolate')		
        axes1 = [ax1, ax1.twinx(), ax1.twinx(), ax1.twinx()]
        axes2 = [ax2, ax2.twinx(), ax2.twinx(), ax2.twinx()]
        ax1.set_title(title)		
        #axes1[0].set_xlabel(x1name, color='blue')
        axes1[0].tick_params(axis='y', colors='blue')
        axes1[0].spines['bottom'].set_color('blue') 	
        axes2[0].set_xlabel(x1name, color='blue')
        axes2[0].tick_params(axis='y', colors='blue')
        axes2[0].spines['bottom'].set_color('blue')
    fig.canvas.mpl_connect('close_event', handle_close)	
    # To make the border of the right-most axis visible, we need to turn the frame
    # on. This hides the other plots, however, so we need to turn its fill off.
    ax1.set_frame_on(True)
    ax1.patch.set_visible(False)
    # And finally we set up all graphs...
    colors = ('Green', 'Red', 'Yellow','Cyan')
    labels = (y1name, y2name, y3name, y4name)
    spines = (0, 1.0, 1.10, 1.20)
    for ax, color, labels, spines in izip(axes1, colors, labels, spines):
        ax.set_ylabel(labels, color=color)
        ax.tick_params(axis='y', colors=color)
        ax.spines['right'].set_color(color)
        ax.spines['right'].set_position(('axes', spines))
    colors = ('Magenta','Azure','Darksalmon', 'Darkolivegreen')
    labels = (y5name,y6name,y7name, y8name)
    spines = (0, 1.0, 1.10, 1.20)
    if numplots > 4:
        for ax, color, labels, spines in izip(axes2, colors, labels, spines):
            ax.set_ylabel(labels, color=color)
            ax.tick_params(axis='y', colors=color)
            ax.spines['right'].set_color(color)
            ax.spines['right'].set_position(('axes', spines))
    # Plot data that is stored in database 
    # Connect to Microsoft SQL and get row count
    resoverall = connection2.execute("SELECT Total_Rows= SUM(st.row_count) FROM sys.dm_db_partition_stats st WHERE \
    object_name(object_id) = 'datalog' AND (index_id < 2)")
    rowcount = DataFrame(resoverall.fetchall())	
    # Plot data that is stored in database 
    #print rowcount
    # stream data from server as long as there are rows to stream	
    # Connect to Microsoft SQL and get graph data rows
    # Table design
    # x1, y1, y2, y3, y4, y5, y6, y7, y8, datastamp, dataid
    resoverall = connection2.execute("SELECT * FROM datalog order by dataid asc")
    df = DataFrame(resoverall.fetchall())	
    #print(df)
    # Plot all the graphs indicated by database		
    # interpolation
    # Create the interpolator.
    # Dense x for the smooth curve.
    if rowcount[0].values > 10:
        interp = pchip(df[0], df[1])
        xx = np.linspace(0, rowcount[0].values, 101)
        axes1[0].plot(xx, interp(xx), marker='None', linestyle='-', color='Green')		
        if numplots >= 2:
            interp1 = pchip(df[0], df[2])
            axes1[1].plot(xx, interp1(xx), marker='None', linestyle='-', color='Red')	
        if numplots >= 3:
            interp2 = pchip(df[0], df[3])
            axes1[2].plot(xx, interp2(xx), marker='None', linestyle='-', color='Yellow')	
        if numplots >= 4:
            interp3 = pchip(df[0], df[4])
            axes1[3].plot(xx, interp3(xx), marker='None', linestyle='-', color='Cyan')	  			
        if numplots >= 5:
            interp4 = pchip(df[0], df[5])
            axes2[0].plot(xx, interp4(xx), marker='None', linestyle='-', color='Magenta')				
        if numplots >= 6:
            interp5 = pchip(df[0], df[6])
            axes2[1].plot(xx, interp5(xx), marker='None', linestyle='-', color='Azure')				
        if numplots >= 7:
            interp6 = pchip(df[0], df[7])	
            axes2[2].plot(xx, interp6(xx), marker='None', linestyle='-', color='Darksalmon')				
        if numplots >= 8:
            interp7 = pchip(df[0], df[8])		
            axes2[3].plot(xx, interp7(xx), marker='None', linestyle='-', color='Darkolivegreen')			
        plt.draw()
        plt.show()