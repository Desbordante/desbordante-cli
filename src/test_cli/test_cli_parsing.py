from collections import namedtuple
from click.testing import CliRunner
import pytest
import desbordante

from src.cli import desbordante_cli, ALGOS

# There is a problem with get_opts() method for this algos
UNFIXED_ALGOS = [
    'tane',
    'pfdtane',
    'cords',
    'spider',
    'faida',
    'fd_first',
    'split',
    'naive_gfd_verifier',
    'gfd_verifier',
    'egfd_verifier',
    'apriori',
    'naive_pfd_verifier',
    'eulerfd', # https://github.com/Desbordante/desbordante-core/issues/774
]

DATA_OPTS = ['table', 'tables', 'difference_table']
SKIPPED_OPTS = ['tables_list', 'tables_directory']

OptionInfo = namedtuple('OptionInfo', ['str', 'value'])

OPTION_VALUES = {
    (int,): OptionInfo('4', 4),
    (float,): OptionInfo('0.1', 0.1),
    (bool,): OptionInfo('True', True)
}

ALGORITHM_SPECIFIC_OPTS = {
    'table': OptionInfo("src/test_cli/test.csv , False", ''),
    'tables': OptionInfo("src/test_cli/test.csv , False", ''),
    'difference_table': OptionInfo("src/test_cli/test.csv , False", ''),
    'lhs_indices': OptionInfo('0 --lhs_indices=2', [0, 2]),
    'rhs_indices': OptionInfo('0', [0]),
    'metric': OptionInfo('cosine', 'cosine'),
    'metric_algorithm': OptionInfo('brute', 'brute'),
    'ucc_indices': OptionInfo('0', [0]),
    'error_measure': OptionInfo('per_tuple', 'per_tuple'),
    'mem_limit': OptionInfo('16', 16),
    'cfd_substrategy': OptionInfo('dfs', 'dfs'),
    'afd_error_measure': OptionInfo('g1', 'g1'),
    'pfd_error_measure': OptionInfo('per_tuple', 'per_tuple'),
    'input_format': OptionInfo('tabular', 'tabular')
}


def get_expected_options(algo):
    algo_opts = algo.get_possible_options()
    expected_options = dict()
    for opt in algo_opts:
        if opt not in ALGORITHM_SPECIFIC_OPTS.keys():
            opt_type = algo.get_option_type(opt)
            expected_options.update({opt: OPTION_VALUES[opt_type].value})
        elif opt not in DATA_OPTS:
            expected_options.update({opt: ALGORITHM_SPECIFIC_OPTS[opt].value})
    return expected_options


def get_invoke_str(algo_name):
    invoke_str = f'--algo={algo_name}'
    algo = ALGOS[algo_name]()
    algo_opts = [opt for opt in algo.get_possible_options() if opt not in SKIPPED_OPTS]
    for opt in algo_opts:
        if opt not in ALGORITHM_SPECIFIC_OPTS.keys():
            opt_type = algo.get_option_type(opt)
            value_as_str = OPTION_VALUES[opt_type].str
        else:
            value_as_str = ALGORITHM_SPECIFIC_OPTS[opt].str
        invoke_str = f'{invoke_str} --{opt}={value_as_str}'
    return invoke_str


def get_algo_options(self, **kwargs):
    return self.get_opts()


def compare_parsing_result(algo, algo_name, provided_options):
    expected_result = get_expected_options(algo)
    cli_parsing_result = algo.execute()
    return 'success' if cli_parsing_result == expected_result else 'fail'


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture(autouse=True)
def patch_cli(monkeypatch):
    monkeypatch.setattr(desbordante.Algorithm, 'execute', get_algo_options)
    monkeypatch.setattr('src.cli.get_algo_result', compare_parsing_result)


@pytest.mark.parametrize('algo_name', [name for name in ALGOS.keys() if name not in UNFIXED_ALGOS])
def test_algo_parsing(runner, algo_name):
    invoke_str = get_invoke_str(algo_name)
    result = runner.invoke(desbordante_cli, invoke_str)
    assert result.output == 'success\n', f'Failed on {algo_name}'
