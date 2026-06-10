# Soul Foods Pink Morsel Sales Analytics Dashboard

## 📌 Project Overview

This project was developed as part of the Quantium Software Engineering
Virtual Experience Program.

The goal of this project is to build an interactive analytics dashboard
that helps Soul Foods analyze Pink Morsel sales performance before and
after the price increase on January 15, 2021.

The application processes raw transaction data, transforms it into
meaningful business metrics, and visualizes insights through an
interactive Dash web application.

------------------------------------------------------------------------

## 🚀 Features

-   Data preprocessing pipeline using Python
-   Combines multiple CSV transaction datasets
-   Filters Pink Morsel product sales data
-   Calculates total sales revenue
-   Interactive sales visualization dashboard
-   Region-based filtering:
    -   North
    -   East
    -   South
    -   West
    -   All regions
-   Price increase comparison marker
-   Custom CSS dashboard styling
-   Automated testing using Pytest
-   Bash script for test automation

------------------------------------------------------------------------

## 🛠️ Tech Stack

### Programming Language

-   Python 3.9

### Libraries & Frameworks

-   Dash
-   Plotly
-   Pandas
-   Pytest

### Development Tools

-   Git
-   GitHub
-   VS Code
-   Bash

------------------------------------------------------------------------

## 📂 Project Structure

    quantium-dashboard/

    ├── app.py
    ├── prepare_data.py
    ├── data/
    │   ├── raw CSV files
    │   └── processed_data.csv
    ├── assets/
    │   └── style.css
    ├── tests/
    │   └── test_app.py
    ├── run_tests.sh
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 📊 Data Processing Workflow

Original dataset fields:

-   Product
-   Quantity
-   Price
-   Date
-   Region

Processing steps:

1.  Combine multiple CSV files
2.  Filter only Pink Morsel products
3.  Calculate sales:

```{=html}
<!-- -->
```
    Sales = Quantity × Price

4.  Create final dataset:

```{=html}
<!-- -->
```
    Sales
    Date
    Region

------------------------------------------------------------------------

## 📈 Dashboard Functionality

The dashboard provides:

-   Sales trend line chart
-   Time-based analysis
-   Interactive region filtering
-   Price increase reference line

Main business question:

**Were Pink Morsel sales higher before or after the price increase?**

------------------------------------------------------------------------

## 🧪 Testing

Automated tests verify:

-   Header is present
-   Visualization is present
-   Region selector is present

Run tests:

``` bash
pytest
```

Run automated test script:

``` bash
bash run_tests.sh
```

------------------------------------------------------------------------

## ▶️ How To Run

Install dependencies:

``` bash
pip install -r requirements.txt
```

Start application:

``` bash
python app.py
```

Open:

    http://127.0.0.1:8050/

------------------------------------------------------------------------

## 📚 Skills Demonstrated

-   Python development
-   Data preprocessing
-   Data analytics
-   Dashboard creation
-   Interactive visualization
-   Software testing
-   Test automation
-   Git workflow

------------------------------------------------------------------------

## Author

Chennuru Rohit Reddy
