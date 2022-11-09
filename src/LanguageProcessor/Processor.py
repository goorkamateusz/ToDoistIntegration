from dataclasses import dataclass
from typing import Dict, List
import re


@dataclass
class Result:
    command: str
    text: str
    dict: Dict[str, str]

    def __len__(self) -> int:
        return len(self.dict)

    def __lt__(self, other):
        return len(self) > len(other)

    def __str__(self):
        return f"{self.command} / {self.dict} / {len(self)}"


class Rule:
    def __init__(self, command: str, rule: str) -> None:
        self.command: str = command

        r = re.sub(r"\[([a-zA-Ząęśćżźłó0-9]*)\]",
                   r"(?P<\g<1>>.*)",
                   rule)
        self.reg = re.compile(r)

    def process(self, text: str):
        text = text.lower()
        s = self.reg.finditer(text)
        return [Result(self.command, i.group(), i.groupdict()) for i in s]


class LanguageProcessor:
    def __init__(self) -> None:
        self.rules: List[Rule] = []

    def add_rule(self, command: str, rule: str):
        self.rules.append(Rule(command, rule))

    def process(self, text: str) -> List[Result]:
        results: Dict[str, List[Result]] = {}
        out = []

        for rule in self.rules:
            for r in rule.process(text):
                if r.text in results:
                    results[r.text].append(r)
                else:
                    results[r.text] = [r]

        for key, match in results.items():
            match = sorted(match)
            out.append(match[0])

        return out
