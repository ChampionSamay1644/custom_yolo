# numa_ultralytics 🚀 AGPL-3.0 License - https://numa_ultralytics.com/license

from .predict import OBBPredictor
from .train import OBBTrainer
from .val import OBBValidator

__all__ = "OBBPredictor", "OBBTrainer", "OBBValidator"
