
import altair as alt
# Create Graph for x and y


def chart(df, x, y, target):
    graph = alt.Chart(df, title=f"{x} by {y} and {target}").mark_point().encode(
        y=y,
        x=x,
        color=alt.Color(target, scale=alt.Scale(scheme='lightgreyred'))
    ).properties(
        width=800,
        height=650,
        background="#252525",
    ).configure(
        axis={
            "titlePadding": 10,
            "labelPadding": 5,
            "gridColor": "Black",
            "tickColor": "Black",
            "titleColor": "#AAAAAA",
            "labelColor": "#AAAAAA",
            "domainColor": "Black",
            },
        legend={
            "titleColor": "#AAAAAA",
            "labelColor": "#AAAAAA",
            },
        title={
            "color": "#AAAAAA",
            "fontSize": 25,
            },
        )
    return graph


