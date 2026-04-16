"""
Base85 encoder and decoder
"""

from __future__ import annotations
import base64
from beartype import beartype


@beartype
def encode(b: bytes):
    """
    Base85 encoder
    """
    # TODO: IMPLEMENT !
    return base64.b85encode(b, pad=False)


@beartype
def decode(b: bytes):
    """
    Base85 decoder
    """
    # TODO: IMPLEMENT !
    return base64.b85decode(b)
