from typing import Dict, List
from src.LanguageProcessor.Processor import LanguageProcessor, Result
import json


def test_it(results: List[Result], test: Dict[str, any]):
    assert len(results) > 0, "No result"
    best = results[0]
    assert best.command == test["c"], "Commands"
    assert best.dict == test["d"], "Dictionary"


if __name__ == "__main__":
    processor = LanguageProcessor("data/rules/pl-PL.json")

    file = open("data/rules/pl-PL-tests.json", encoding="utf-8")
    tests = json.load(file)

    tests_cnt = 0
    fail_cnt = 0

    print("---")
    for test in tests:
        for t in test['t']:
            try:
                results = processor.process(t)
                test_it(results, test)
                tests_cnt += 1
            except AssertionError as e:
                print(f"{e} || {t} || {results}")
                fail_cnt += 1
    print("---")
    print(f"{fail_cnt} / {tests_cnt} fail")
