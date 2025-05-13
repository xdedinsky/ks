import os
import importlib.util
import pytest

VSTUPY_OCAKAVANIA = [
    (-0.001, 0), (-5, 0),
    (0, 6), (30, 6), (55.999, 6),
    (56, 5), (60, 5), (64.999, 5),
    (65, 4), (70, 4), (73.999, 4),
    (74, 3), (80, 3), (82.999, 3),
    (83, 2), (85, 2), (91.999, 2),
    (92, 1), (95, 1), (100, 1),
    (100.001, 0), (152, 0),
]

def nacitaj_funkciu_grade(subor):
    spec = importlib.util.spec_from_file_location("student_modul", subor)
    modul = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(modul)
        return getattr(modul, "grade", None)
    except Exception:
        return None

@pytest.mark.parametrize("subor_meno", sorted(os.listdir("students")))
def testuj_grade_studentov(subor_meno):
    if not subor_meno.endswith("_grade.py"):
        pytest.skip(f"Preskakujem: {subor_meno} nie je relevantný súbor.")
    cesta = os.path.join("students", subor_meno)
    funkcia = nacitaj_funkciu_grade(cesta)
    assert funkcia is not None, f"{subor_meno} neobsahuje funkciu 'grade'"

    for vstup, ocakavany_vystup in VSTUPY_OCAKAVANIA:
        try:
            vysledok = funkcia(vstup)
            assert vysledok == ocakavany_vystup, (
                f"{subor_meno} zlyhal pri vstupe {vstup}: "
                f"očakával sa {ocakavany_vystup}, ale bol {vysledok}"
            )
        except Exception as chyba:
            pytest.fail(f"{subor_meno} vyhodil výnimku pre vstup {vstup}: {chyba}")
