import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from app import app


def test_header_present():

    layout = app.layout

    header = layout.children[0]

    assert header.children == "Soul Foods Pink Morsel Sales Visualiser"



def test_visualisation_present():

    layout = app.layout

    graph = layout.children[2]

    assert graph.id == "sales-chart"



def test_region_picker_present():

    layout = app.layout

    radio = layout.children[1].children[1]

    assert radio.id == "region-filter"