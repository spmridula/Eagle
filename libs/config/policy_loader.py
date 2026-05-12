from __future__ import annotations
import os
import yaml
from pathlib import Path


class PolicyLoader:
    def __init__(self):
        self.policy_path = os.getenv("POLICY_PATH", "policies/default.yaml")

    def load_policy(self):
        path = Path(self.policy_path)

        if not path.exists():
            raise FileNotFoundError(f"Policy file not found: {path}")

        try:
            with open(path, "r") as f:
                return yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format: {e}")