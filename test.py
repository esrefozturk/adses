from time import time

import plotly
import plotly.graph_objs as go

from election import Election


def running_time_comparison():
    times = []
    for i in range(10, 200):
        print(i)
        s = time()
        Election(voter_count=i)
        e = time()
        times.append(e - s)

    trace = go.Scatter(
        x=list(range(10, 200)),
        y=times,
        mode="lines",
    )

    plotly.offline.plot([trace], filename='times.html')


def main():
    running_time_comparison()


if __name__ == '__main__':
    main()
