from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
OUTPUT_FILE = DATA_DIR / "processed_data.csv"
PRODUCT_NAME = "Pink Morsel"
FINAL_COLUMNS = ["sales", "date", "region"]


def load_source_data() -> pd.DataFrame:
    csv_files = sorted(
        path for path in DATA_DIR.glob("*.csv") if path.name != OUTPUT_FILE.name
    )

    if len(csv_files) != 3:
        raise FileNotFoundError(
            f"Expected exactly 3 source CSV files in {DATA_DIR}, found {len(csv_files)}."
        )

    return pd.concat((pd.read_csv(path) for path in csv_files), ignore_index=True)


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    pink_morsels = data.loc[data["product"] == PRODUCT_NAME].copy()
    price = pink_morsels["price"].astype(str).str.replace("$", "", regex=False)
    pink_morsels["sales"] = pink_morsels["quantity"] * pd.to_numeric(price)

    return pink_morsels[FINAL_COLUMNS]


def main() -> None:
    cleaned_data = clean_data(load_source_data())
    DATA_DIR.mkdir(exist_ok=True)
    cleaned_data.to_csv(OUTPUT_FILE, index=False)
    print(f"Created {OUTPUT_FILE} with columns: {','.join(cleaned_data.columns)}")


if __name__ == "__main__":
    main()
