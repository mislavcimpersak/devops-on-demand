import math
from typing import Dict, List, Union


# type aliases
DataCenters = List[Dict[str, Union[str, int]]]


def single_center_de_needs(servers: int, DE_capacity: int) -> int:
    """Calculate how many DevOps Engineers are required for given amount of servers."""

    return math.ceil(servers / DE_capacity)


def other_center_de_needs(
    current_center_location: str, DE_capacity: int, data_centers: DataCenters
) -> int:
    """Calculate how many DevOps Engineers are required in all data centers except the current one."""

    other_center_engineers = 0
    for data_center in data_centers:
        if current_center_location != data_center["name"]:
            other_center_engineers += single_center_de_needs(data_center["servers"], DE_capacity)
    return other_center_engineers


def optimal_devops_coverage(
    DM_capacity: int, DE_capacity: int, data_centers: DataCenters
) -> Dict[str, Union[str, int]]:
    """Calculate optimal DevOps Manager and DevOps Engineer server coverage."""

    solutions = {}

    for data_center in data_centers:
        current_center_location = data_center["name"]

        # taking out servers that DM will manage
        leftover_servers = data_center["servers"] - DM_capacity
        current_center_engineers = single_center_de_needs(leftover_servers, DE_capacity)

        other_center_engineers = other_center_de_needs(
            current_center_location, DE_capacity, data_centers
        )

        solutions[current_center_location] = current_center_engineers + other_center_engineers
    optimal_center = min(solutions, key=solutions.get)
    return {"DE": solutions[optimal_center], "DM_data_center": optimal_center}
