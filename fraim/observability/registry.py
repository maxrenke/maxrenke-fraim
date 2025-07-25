# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Resourcely Inc.

"""
Registry for observability backends.
"""

from typing import Dict, List, Optional

from .base import ObservabilityBackend


class ObservabilityRegistry:
    """Registry to manage available observability backends."""

    _backends: Dict[str, ObservabilityBackend] = {}

    @classmethod
    def register(cls, backend: ObservabilityBackend) -> None:
        """Register an observability backend."""
        cls._backends[backend.get_name()] = backend

    @classmethod
    def get_available_backends(cls) -> List[str]:
        """Get list of available backend names."""
        return list(cls._backends.keys())

    @classmethod
    def get_backend(cls, name: str) -> Optional[ObservabilityBackend]:
        """Get a backend by name."""
        return cls._backends.get(name)

    @classmethod
    def get_backend_descriptions(cls) -> Dict[str, str]:
        """Get descriptions for all backends."""
        return {name: backend.get_description() for name, backend in cls._backends.items()}
