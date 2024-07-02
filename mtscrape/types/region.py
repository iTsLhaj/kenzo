from dataclasses import dataclass


@dataclass
class Region:
    region: str
    link: str = None