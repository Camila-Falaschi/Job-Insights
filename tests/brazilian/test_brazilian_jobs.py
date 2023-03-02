from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    dict_jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert dict_jobs[1] == {
        "title": "Motorista",
        "salary": "3000",
        "type": "full time",
    }
