#!/usr/bin/env python3
"""Update Andrew6rant-style profile SVG stats."""

from __future__ import annotations

import datetime
import os
from pathlib import Path

import requests
from dateutil import relativedelta
from lxml import etree

USER_NAME = os.environ.get("USER_NAME", "Navneethd8")
TOKEN = os.environ.get("ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")
HEADERS = {"authorization": f"token {TOKEN}"}


def graphql(query: str, variables: dict | None = None) -> dict:
    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables or {}},
        headers=HEADERS,
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]


def fetch_stats() -> dict[str, str]:
    data = graphql(
        """
        query($login: String!) {
          user(login: $login) {
            createdAt
            followers { totalCount }
            ownedRepositories: repositories(ownerAffiliations: OWNER) { totalCount }
            repositoriesContributedTo(contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) {
              totalCount
            }
            starredRepositories: repositories(first: 100, ownerAffiliations: OWNER) {
              nodes { stargazerCount }
            }
            contributionsCollection {
              contributionCalendar { totalContributions }
            }
          }
        }
        """,
        {"login": USER_NAME},
    )["user"]

    created = datetime.datetime.fromisoformat(data["createdAt"].replace("Z", "+00:00"))
    age = relativedelta.relativedelta(datetime.datetime.now(datetime.UTC), created)
    age_text = f"{age.years} years, {age.months} months, {age.days} days"

    stars = sum(node["stargazerCount"] for node in data["starredRepositories"]["nodes"])
    return {
        "repo_data": f"{data['ownedRepositories']['totalCount']:,}",
        "contrib_data": f"{data['repositoriesContributedTo']['totalCount']:,}",
        "star_data": f"{stars:,}",
        "commit_data": f"{data['contributionsCollection']['contributionCalendar']['totalContributions']:,}",
        "follower_data": f"{data['followers']['totalCount']:,}",
        "age_data": age_text,
    }


def justify_format(root, element_id: str, text: str, width: int = 0) -> None:
    element = root.find(f".//*[@id='{element_id}']")
    if element is not None:
        element.text = text
    if width:
        dots = root.find(f".//*[@id='{element_id}_dots']")
        if dots is not None:
            padding = max(0, width - len(text))
            dots.text = " " if padding <= 1 else " " + ("." * padding) + " "


def update_svg(path: Path, stats: dict[str, str]) -> None:
    root = etree.parse(str(path)).getroot()
    justify_format(root, "repo_data", stats["repo_data"], 4)
    justify_format(root, "contrib_data", stats["contrib_data"])
    justify_format(root, "star_data", stats["star_data"], 11)
    justify_format(root, "commit_data", stats["commit_data"], 17)
    justify_format(root, "follower_data", stats["follower_data"], 7)
    justify_format(root, "age_data", stats["age_data"], 20)
    path.write_bytes(etree.tostring(root, encoding="utf-8", xml_declaration=True))


def main() -> None:
    stats = fetch_stats()
    root = Path(__file__).resolve().parent
    for name in (
        "trim_light.svg",
        "trim_dark.svg",
        "clean_light.svg",
        "clean_dark.svg",
        "style_light.svg",
        "style_dark.svg",
        "hair_light.svg",
        "hair_dark.svg",
        "face_light.svg",
        "face_dark.svg",
        "light_mode.svg",
        "dark_mode.svg",
        "header_light.svg",
        "header_dark.svg",
        "navneeth_light.svg",
        "navneeth_dark.svg",
        "bust_light.svg",
        "bust_dark.svg",
        "me_light.svg",
        "me_dark.svg",
        "stats_light.svg",
        "stats_dark.svg",
    ):
        path = root / name
        if path.exists():
            update_svg(path, stats)
    print("Updated profile SVG stats.")


if __name__ == "__main__":
    main()
