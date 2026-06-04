import typing as tp
from enum import StrEnum, auto
import sys

import click
import desbordante


class BuiltinDomainType(StrEnum):
    ball = auto()
    parallelepiped = auto()


DOMAIN_TYPE_OPT = "domain_type"
LEVELING_COEFFICIENTS_OPT = "leveling_coefficients"
CENTER_OPT = "center"
RADIUS_OPT = "radius"
LOWER_BOUND_OPT = "lower_bound"
UPPER_BOUND_OPT = "upper_bound"


def register_pac_domain_option(func: tp.Callable) -> tp.Callable:
    click.option(
        f"--{DOMAIN_TYPE_OPT}",
        type=click.Choice(BuiltinDomainType, case_sensitive=False),
    )(func)
    click.option(f"--{LEVELING_COEFFICIENTS_OPT}", type=float, multiple=True)(func)

    # Ball options
    click.option(f"--{CENTER_OPT}", type=float, multiple=True)(func)
    click.option(f"--{RADIUS_OPT}", type=float)(func)

    # Parallelepiped options
    click.option(f"--{LOWER_BOUND_OPT}", type=float, multiple=True)(func)
    click.option(f"--{UPPER_BOUND_OPT}", type=float, multiple=True)(func)

    return func


def get_mandatory_opt(opts: dict[str, tp.Any], opt_name: str) -> tp.Any:
    value = opts[opt_name]
    if value is None or value == ():
        print(f'Missing value for option --{opt_name}')
        sys.exit(1)
    return value


def process_pac_domain_options(opts: dict[str, tp.Any]) -> dict[str, tp.Any]:
    opts = opts.copy()

    domain_type = get_mandatory_opt(opts, DOMAIN_TYPE_OPT)
    del opts[DOMAIN_TYPE_OPT]
    leveling_coefficients = list(opts.get(LEVELING_COEFFICIENTS_OPT, []))
    del opts[LEVELING_COEFFICIENTS_OPT]
    match domain_type:
        case BuiltinDomainType.ball:
            center = [str(value) for value in get_mandatory_opt(opts, CENTER_OPT)]
            del opts[CENTER_OPT]
            radius = get_mandatory_opt(opts, RADIUS_OPT)
            del opts[RADIUS_OPT]
            domain = desbordante.pac.domains.Ball(
                center,
                radius,
                leveling_coefficients,
            )
        case BuiltinDomainType.parallelepiped:
            lower_bound = [
                str(value) for value in get_mandatory_opt(opts, LOWER_BOUND_OPT)
            ]
            del opts[LOWER_BOUND_OPT]
            upper_bound = [
                str(value) for value in get_mandatory_opt(opts, UPPER_BOUND_OPT)
            ]
            del upper_bound[UPPER_BOUND_OPT]
            domain = desbordante.pac.domains.Parallelepiped(
                lower_bound=lower_bound, upper_bound=upper_bound
            )
        case _:
            raise ValueError(f"Unknown domain type: {domain_type}")
    opts["domain"] = domain
    return opts
