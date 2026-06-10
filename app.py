from pathlib import Path

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html


DATA_FILE = Path("data") / "processed_data.csv"
PRICE_INCREASE_DATE = "2021-01-15"


def load_sales_data() -> pd.DataFrame:
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=["sales", "date", "region"])

    data = pd.read_csv(DATA_FILE)
    data["date"] = pd.to_datetime(data["date"])
    data["sales"] = pd.to_numeric(data["sales"])
    return data.sort_values("date")


def build_sales_figure(data: pd.DataFrame):
    if data.empty:
        figure = px.line(labels={"date": "Date", "sales": "Sales"})
        figure.add_annotation(
            text=f"Missing dataset: {DATA_FILE}",
            xref="paper",
            yref="paper",
            x=0.5,
            y=0.5,
            showarrow=False,
        )
    else:
        figure = px.line(
            data,
            x="date",
            y="sales",
            labels={"date": "Date", "sales": "Sales"},
            title="Pink Morsel Sales Over Time",
        )

    figure.add_vline(
        x=PRICE_INCREASE_DATE,
        line_dash="dash",
        line_color="#d62728",
        annotation_text="Price Increase",
        annotation_position="top left",
    )
    figure.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        margin={"l": 60, "r": 30, "t": 60, "b": 50},
    )
    return figure


app = Dash(__name__)
sales_data = load_sales_data()

app.layout = html.Main(
    [
        html.H1("Soul Foods Pink Morsel Sales Visualiser"),
        dcc.Graph(id="sales-over-time", figure=build_sales_figure(sales_data)),
    ],
    style={
        "maxWidth": "1100px",
        "margin": "0 auto",
        "padding": "32px 24px",
        "fontFamily": "Arial, sans-serif",
    },
)


if __name__ == "__main__":
    app.run(debug=True)
