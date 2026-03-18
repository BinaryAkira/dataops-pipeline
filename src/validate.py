"""
Validation module for enforcing schema checks on processed Pokémon data.
"""

from pathlib import Path

import pandas as pd
import pandera as pa
from pandera import Check, Column, DataFrameSchema

PROCESSED_PATH = Path("data/processed/pokemon_processed.csv")


# Modern Pandera schema (works on all new versions)
pokemon_schema = DataFrameSchema(
    {
        "name": Column(pa.String, nullable=False),
        "url": Column(pa.String, nullable=False),
    },
    strict=True,
)


def load_processed(path: Path = PROCESSED_PATH) -> pd.DataFrame:
    """Load processed CSV data."""
    return pd.read_csv(path)


def validate(df: pd.DataFrame) -> pd.DataFrame:
    """Validate the processed DataFrame using the schema."""
    return pokemon_schema.validate(df)


def main() -> None:
    """Execute the validation step."""
    df = load_processed()
    validate(df)
    print("Validation successful — processed data is valid.")


if __name__ == "__main__":
    main()
