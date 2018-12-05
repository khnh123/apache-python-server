import plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd


def get_data(n):
    # pull your data here based on your input parameters
    df = pd.DataFrame(np.random.randint(-1000, 1000, size=(n, 2)), columns=['x', 'y'])
    return df


# test function above by uncommenting this line, and running the python file:
# print(get_data(1000))

def get_plotly_html(df, title):
    trace = go.Scatter(
        x=df['x'],
        y=df['y'],
        mode='markers',
    )
    layout = dict(
        width=1000,
        height=700,
        autosize=False,
        title=title,
    )
    fig = dict(data=[trace], layout=layout)

    # test chart in html file with the line below
    # py.offline.plot(fig, filename='test.html')

    return py.offline.plot(fig, output_type='div')

# test function above by uncommenting this line, and running the python file:
# getPlotlyHTML(get_data(1000), 'asd')
