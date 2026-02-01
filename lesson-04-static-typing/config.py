from pydantic import BaseModel, Field


class MainConfig(BaseModel):
    """Configuration of data processing."""

    data_path: str = Field(..., description="Path to the input data file")
    target_column: str = Field(..., description="Target column")
    features: list[str] = Field(..., description="List of feature names")
    output_path: str = Field(..., description="Where to store model")


class ModelConfig(BaseModel):
    """Configuration of model training."""

    n_estimators: int = Field(
        ..., gt=0, description="Number of trees in the forest"
    )
    max_depth: int = Field(..., gt=0, description="Maximum depth of the trees")
    random_state: int = Field(
        42, description="Random state for reproducibility"
    )
