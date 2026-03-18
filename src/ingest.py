"""
Ingestion module for fetching raw data from external APIs.

This module handles:
- calling the source API
- basic error handling
- saving the raw JSON response to disk

The output of this module is stored in data/raw/.
"""

import json
from pathlib import Path
from typing import Dict, Any

import requests


# Establish directories for data
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)


def fetch_pokemon(limit: int = 20) -> Dict[str, Any]:
    """
    Fetch a list of Pokémon from the public PokéAPI.

    Args:
        limit (int): Number of Pokémon records to request.

    Returns:
        Dict[str, Any]: Parsed JSON response containing Pokémon metadata.

    Raises:
        requests.HTTPError: If the API request fails.
    """
    url = "https://pokeapi.co/api/v2/pokemon"
    params = {"limit": limit}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()
