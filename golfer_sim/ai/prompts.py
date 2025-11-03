"""Prompt templates for the agent-coach."""
from __future__ import annotations

from textwrap import dedent

BASIC_WEEKLY_PROMPT = dedent(
    """
    You are an analytical golf agent-coach. Provide a concise weekly plan with
    probabilities for making the cut, expected ranking points, and financial
    outlook. Highlight risks and give a recommendation plus a fallback.
    """
)
