import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px


# Load data
df = pd.read_csv("data/processed_data.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")


app = Dash(__name__)


app.layout = html.Div(
    className="container",
    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Visualiser",
            className="title"
        ),

        html.Div(
            [
                html.Label(
                    "Select Region:",
                    className="label"
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    className="radio"
                ),
            ],
            className="filter-box"
        ),


        dcc.Graph(
            id="sales-chart",
            className="chart"
        )
    ]
)



@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(region):

    if region == "all":
        filtered = df
    else:
        filtered = df[
            df["region"].str.lower() == region
        ]


    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )


    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        annotation_text="Price Increase"
    )


    return fig



if __name__ == "__main__":
    app.run(debug=True)