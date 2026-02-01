import json
import pickle
from typing import Any, Dict, Optional, Tuple

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def load_config() -> Dict[str, Any]:
    with open("config.json") as f:
        return json.load(f)  # type: ignore[no-any-return]


def load_data(path: str) -> Optional[pd.DataFrame]:
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        return None


def preprocess(
    data: Optional[pd.DataFrame], config: dict[str, Any]
) -> Tuple[Optional[pd.DataFrame], Optional[pd.Series]]:
    if data is None:
        return None, None
    data = data.dropna()
    X = data[config["features"]]
    y = data[config["target_column"]]
    return X, y


def train(
    X: Optional[pd.DataFrame], y: Optional[pd.Series], params: dict[str, Any]
) -> Optional[RandomForestRegressor]:
    if X is None or y is None:
        return None
    model = RandomForestRegressor(**params)
    model.fit(X, y)
    return model


def save_model(model: Optional[RandomForestRegressor], path: str) -> None:
    if model is not None:
        with open(path, "wb") as f:
            pickle.dump(model, f)


def main() -> None:
    config = load_config()
    data = load_data(config["data_path"])
    X, y = preprocess(data, config)

    if X is not None and y is not None:
        X_train, _, y_train, _ = train_test_split(
            X, y, random_state=config["model_params"]["random_state"]
        )
        model = train(X_train, y_train, config["model_params"])
        save_model(model, config["output_path"])
        print("Model saved successfully")


if __name__ == "__main__":
    main()
