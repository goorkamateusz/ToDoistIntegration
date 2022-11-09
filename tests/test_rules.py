from src.LanguageProcessor.Processor import *


def test_adding_task():
    processor = LanguageProcessor()
    processor.add_rule("add", "dodaj zadanie [treść]")

    results = processor.process("Dodaj zadanie kup mleko")
    assert len(results) == 1

    result = results[0]
    assert result.command == "add"
    assert result.dict["treść"] == "kup mleko"


def test_adding_task_with_label():
    processor = LanguageProcessor()
    processor.add_rule("add", "dodaj zadanie [treść] z etykietą [etykieta]")

    results = processor.process("Dodaj zadanie kup mleko z etykietą zakupy")
    assert len(results) == 1

    result = results[0]
    assert result.command == "add"
    assert result.dict["treść"] == "kup mleko"
    assert result.dict["etykieta"] == "zakupy"


def test_multiple_tasks_to_add():
    processor = LanguageProcessor()
    processor.add_rule("add", "dodaj zadanie [treść] z etykietą [etykieta]")

    results = processor.process("""
Dodaj zadanie kup mleko z etykietą zakupy
dodaj zadanie posprzątaj z etykietą dom""")
    assert len(results) == 2

    result = results[0]
    assert result.command == "add"
    assert result.dict["treść"] == "kup mleko"
    assert result.dict["etykieta"] == "zakupy"

    result = results[1]
    assert result.command == "add"
    assert result.dict["treść"] == "posprzątaj"
    assert result.dict["etykieta"] == "dom"
