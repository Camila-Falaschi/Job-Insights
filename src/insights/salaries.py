import re
from typing import Dict, List, Union

from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    jobs_salaries = []
    for job in jobs:
        match = re.fullmatch(r"^[0-9]+$", job["max_salary"])
        if match is not None and job["max_salary"] != "":
            jobs_salaries.append(int(job["max_salary"]))

    return max(jobs_salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    jobs_salaries = []
    for job in jobs:
        match = re.fullmatch(r"^[0-9]+$", job["min_salary"])
        if match is not None and job["min_salary"] != "":
            jobs_salaries.append(int(job["min_salary"]))

    return min(jobs_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary_int = int(salary)
        if min_salary < max_salary:
            return min_salary <= salary_int <= max_salary
    except (KeyError, TypeError, ValueError):
        raise ValueError
    else:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs_list.append(job)
        except ValueError:
            pass
    return filtered_jobs_list
