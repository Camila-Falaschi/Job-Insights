from typing import Dict, List

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """

    jobs = read(path)
    jobs_industries = []
    for job in jobs:
        if job["industry"] not in jobs_industries and job["industry"] != "":
            jobs_industries.append(job["industry"])
    return jobs_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_list_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_list_by_industry.append(job)

    return jobs_list_by_industry
