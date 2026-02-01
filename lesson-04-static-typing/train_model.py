import json
import pickle
from typing import Tuple, cast

import pandas as pd
from config import MainConfig, ModelConfig
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


def load_config() -> dict[str, str]:
    with open("config.json") as f:
        return cast(dict[str, str], json.load(f))


def load_data(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except FileNotFoundError as ex:
        raise ex


def preprocess(
    data: pd.DataFrame, config: MainConfig
) -> Tuple[pd.DataFrame, pd.Series]:
    if data is None:
        raise ValueError("Input data is None. Cannot preprocess data.")
    data = data.dropna()
    X = data[config.features]
    y = data[config.target_column]
    return X, y


def train(
    X: pd.DataFrame, y: pd.Series, params: ModelConfig
) -> RandomForestRegressor:
    if X is None or y is None:
        raise ValueError("Input data is None. Cannot train model.")
    model = RandomForestRegressor(**params.dict())
    model.fit(X, y)
    return model


def save_model(model: RandomForestRegressor, path: str) -> None:
    if model is not None:
        with open(path, "wb") as f:
            pickle.dump(model, f)


def main() -> None:
    config: dict[str, str] = load_config()

    data_cfg = MainConfig(**config)  # type: ignore
    model_cfg = ModelConfig(**config["model_params"])  # type: ignore
    data = load_data(data_cfg.data_path)
    X, y = preprocess(data, data_cfg)

    X_train, _, y_train, _ = train_test_split(
        X, y, random_state=model_cfg.random_state
    )
    model = train(X_train, y_train, model_cfg)
    save_model(model, data_cfg.output_path)
    print("Model saved successfully")


if __name__ == "__main__":
    main()
