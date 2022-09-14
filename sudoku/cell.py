from __future__ import annotations
from dataclasses import dataclass, field
import random

@dataclass
class Cell:
    x: int
    y: int
    value: int = 0
    domain: list[int] = field(default_factory=list)
    neighbours: list[Cell] = field(default_factory=list, repr=False)
    
    def __post_init__(self) -> None:
        if self.value:
            self.domain.append(self.value)
            return

        self.domain.extend(range(1, 10))

    def assign_random(self, *, clear_domain=False) -> None:
        if not self.domain: raise RuntimeError('Domain is empty')
        if self.value: raise RuntimeError('Value is already assigned')

        self.value = random.choice(self.domain)

        if clear_domain:
            self.domain.clear()
            self.domain.append(self.value)

    def reset(self) -> None:
        self.value = 0
        self.domain.clear()
        self.domain.extend(range(1, 10))
