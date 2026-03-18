"""
Transformation module for converting raw Pokémon API data
into a structured pandas DataFrame.

This module:
- loads raw JSON from data/raw/
- extracts relevant fields
- outputs a tidy table to data/processed/
"""

import json
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from logger import get_logger

logger = get_logger(__name__)


RAW_PATH = Path("data/raw/pokemon_raw.json")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def load_raw(path: Path = RAW_PATH) -> Dict[str, Any]:
    """
    Load raw JSON data from disk.

    Args:
        path (Path): Path to the raw JSON file.

    Returns:
        Dict[str, Any]: Parsed JSON dictionary.
    """
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def extract_records(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract a list of Pokémon records from the raw API response.

    Args:
        data (Dict[str, Any]): Raw JSON dictionary.

    Returns:
        List[Dict[str, Any]]: List of simplified Pokémon records.
    """
    results = data.get("results", [])
    return [
        {
            "name": item["name"],
            "url": item["url"],
        }
        for item in results
    ]


def save_processed(df: pd.DataFrame, filename: str = "pokemon_processed.csv") -> Path:
    """
    Save the processed DataFrame to CSV.

    Args:
        df (pd.DataFrame): DataFrame to save.
        filename (str): Output filename.

    Returns:
        Path: Path to the saved CSV file.
    """
    path = PROCESSED_DIR / filename
    df.to_csv(path, index=False)
    return path


def main() -> None:
    """
    Execute the transformation step:
    - load raw JSON
    - extract records
    - convert to DataFrame
    - save to processed/
    """
    logger.info("Starting transformation step")
    raw = load_raw()
    records = extract_records(raw)
    df = pd.DataFrame(records)
    path = save_processed(df)
    logger.info(f"Transformation complete: saved to {path}")


if __name__ == "__main__":
    main()
