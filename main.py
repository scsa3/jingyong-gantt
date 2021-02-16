import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

data = [
    dict(Task="書劍恩仇錄", Start='1955-02-08', Finish='1956-09-05', Resource='新晚報', Order=1),
    dict(Task="碧血劍", Start='1956-01-01', Finish='1956-12-31', Resource='香港商報', Order=2),
    dict(Task="射雕英雄傳", Start='1957-01-01', Finish='1959-05-09', Resource='香港商報', Order=3),
    dict(Task="雪山飛狐", Start='1959-02-09', Finish='1959-06-18', Resource='新晚報', Order=4),
    dict(Task="神鵰俠侶", Start='1959-05-20', Finish='1961-07-08', Resource='明報', Order=5),

    dict(Task="飛狐外傳", Start='1960-01-11', Finish='1962-04-06', Resource='武俠與歷史', Order=6),
    dict(Task="鴛鴦刀", Start='1961-05-01', Finish='1961-05-28', Resource='明報', Order=7),
    dict(Task="倚天屠龍記", Start='1961-07-06', Finish='1963-09-02', Resource='明報', Order=8),
    dict(Task="白馬嘯西風", Start='1961-10-14', Finish='1962-01-15', Resource='明報', Order=9),
    dict(Task="天龍八部", Start='1963-09-03', Finish='1966-05-27', Resource='明報', Order=10),

    dict(Task="連城訣", Start='1964-01-12', Finish='1965-03-07', Resource='東南亞洲刊', Order=11),
    dict(Task="俠客行", Start='1966-06-11', Finish='1967-04-19', Resource='明報', Order=12),
    dict(Task="笑傲江湖", Start='1967-04-20', Finish='1969-10-12', Resource='明報', Order=13),
    dict(Task="鹿鼎記", Start='1969-10-24', Finish='1972-09-23', Resource='明報', Order=14),
    dict(Task="越女劍", Start='1969-12-01', Finish='1969-12-31', Resource='明報晚報', Order=15),
]


def new_style():
    df = pd.DataFrame(data)

    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Task",
        color='Resource',
        # color='Order',
    )
    fig.update_yaxes(autorange="reversed")  # otherwise tasks are listed from the bottom up
    return fig


def old_style():
    fig = ff.create_gantt(data)
    return fig


if __name__ == '__main__':
    figure = new_style()
    # figure = old_style()

    # figure.show()
    # figure.write_html('docs/order.html')
    figure.write_html('docs/source.html')
