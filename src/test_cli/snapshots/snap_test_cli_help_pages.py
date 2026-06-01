# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_algos_help_pages[aid] aid'] = '''A modern algorithm for discovery of exact functional
dependencies. Unlike all other algorithms, it is approximate, i.e. it can
miss some dependencies or produce non-valid ones. In exchange,
it is significantly faster (10x-100x). For more information, refer to the
“Approximate Discovery of Functional Dependencies for Large Datasets” paper
by T.Bleifus et al.

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_algos_help_pages[apriori] apriori'] = '''An algorithm for frequent item set mining and association 
rule discovery. For more information, refer to the "Fast Algorithms for 
Mining Association Rules" paper by Agrawal and Srikant from 1994.

--has_tid=BOOLEAN
\tindicates that the first column contains the transaction IDs

--input_format=STRING
\tformat of the input dataset for AR mining
[singular|tabular]

--item_column_index=INTEGER
\tindex of the column where an item name is stored

--minconf=FLOAT
\tminimum confidence value (between 0 and 1)

--minsup=FLOAT
\tminimum support value (between 0 and 1)

--tid_column_index=INTEGER
\tindex of the column where a TID is stored

'''

snapshots['test_algos_help_pages[cords] cords'] = '''An algorithm for discovery of correlations and soft
functional dependencies. For more information, refer to 
"CORDS: Automatic Discovery of Correlations and Soft Functional Dependencies" 
paper by Ihab F. Ilyas et al.

--delta=FLOAT
\tadditional constant for computation of sample size. Value lies in (0, 1) and must be greater than minimum_cardinality_.

--fixed_sample=BOOLEAN
\tIndicates that instead of random generated sample CORDS uses sample consisting of n first rows of the given table. Intended for tests only.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_amount_of_categories=INTEGER
\tMax amount of categories for the chi-squared test in case the data is not skewed

--max_different_values_proportion=FLOAT
\tthe maximum proportion that the numberof different values in the concatenation of sample columns from the number of rows in the sample for the test for SFD to be meaningful. Value lies in (0, 1)

--max_false_positive_probability=FLOAT
\t(1 - max_false_positive_probability) is the maximum acceptable probability of a false-positive correlation test result. Value lies in (0, 0.39).

--max_lhs=INTEGER
\tmax considered LHS size

--min_cardinality=FLOAT
\t (1 - min_cardinality) * |R| (where |R| is amount of rows in table R) denotes minimum cardinality of a column to be considered a soft key. Value lies in (0, 1)

--min_sfd_strength=FLOAT
\t(1 - min_sfd_strength) denotes minimum threshold of strength measure of a SFD. Value lies in (0, 1)

--min_skew_threshold=FLOAT
\t(1 - min_skew_threshold) * |R| (where |R| is amount of rows in table R) is the minimum sum of the frequencies of occurrence of the most frequentvalues of the column in the table R, indicating that the distribution of values in the column is skewed. Value lies in (0, 1).

--min_structural_zeroes_amount=FLOAT
\tmin_structural_zeroes_amount*d1*d2 is the minimum number of structural zeros in the contingency table indicating that the columns are correlated. d1, d2 - the number of different values in columns C1, C2, respectively. Value lies in (0, 1).

--only_sfd=BOOLEAN
\tDon't mine correlations

'''

snapshots['test_algos_help_pages[dep_miner] dep_miner'] = '''A classic algorithm for discovery of exact functional
dependencies. For more information refer to “Efficient Discovery of
Functional Dependencies and Armstrong Relations” paper by S. Lopes et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_algos_help_pages[dfd] dfd'] = '''A modern algorithm for discovery of exact functional
dependencies. For more information, refer to the “DFD: Efficient Functional
Dependency Discovery” paper by Z. Abedjan et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[egfd_verifier] egfd_verifier'] = '''Algorithm for verifying whether a given
graph functional dependency holds. For more information about the primitive
refer to “Functional Dependencies for Graphs” by Wenfei Fan et al.

--gfd=STRING
\tPath to file with GFD
\tFor multiple values, specify multiple times 
\t(e.g., --gfd=1 --gfd=2)

--graph=STRING
\tPath to dot-file with graph

'''

snapshots['test_algos_help_pages[eulerfd] eulerfd'] = '''A modern algorithm for discovery of exact functional
dependencies. Like AID, it is approximate, i.e. it can miss some
dependencies or produce non-valid ones, but is significantly faster than
exact algorithms. For more information, refer to the “EulerFD: An Efficient
Double-Cycle Approximation of Functional Dependencies” paper by Qiongqiong Lin,
Yunfan Gu, Jingyan Sa et al.

--custom_random_seed=INTEGER
\tseed for the custom random generator. Used for consistency of results across platforms.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_algos_help_pages[faida] faida'] = '''Both unary and n-ary inclusion dependency mining algorithm.
Unlike all other algorithms, it is approximate, i.e. it can
miss some dependencies or produce non-valid ones. In exchange,
it is significantly faster. For more information, refer to "Fast approximate
discovery of inclusion dependencies" by S. Kruse et al.

--hll_accuracy=FLOAT
\tHyperLogLog approximation accuracy. Must be positive
Closer to 0 - higher accuracy, more memory needed and slower the algorithm.


--ignore_constant_cols=BOOLEAN
\tIgnore INDs which contain columns filled with only one value. May increase performance but impacts the result. [true|false]

--ignore_null_cols=BOOLEAN
\tIgnore INDs which contain columns filled only with NULLs. May increase performance but impacts the result. [true|false]

--max_arity=INTEGER
\tmax considered arity

--sample_size=INTEGER
\tSize of a table sample. Greater value - more correct answers, but higher memory consumption.
 Applies to all tables

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[fastfds] fastfds'] = '''A classic algorithm for discovery of exact functional
dependencies. For more information, refer to “FastFDs: A Heuristic-Driven,
Depth-First Algorithm for Mining Functional Dependencies from Relation
Instances Extended Abstract” paper by C. Wyss et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[fastod] fastod'] = '''A modern algorithm for discovery of canonical order 
dependencies. For more information, refer to the “Effective and complete 
discovery of order dependencies via set-based axiomatization” paper by 
J. Szlichta et al.

--time_limit=INTEGER
\tmax running time of the algorithm. Pass 0 to remove limit

'''

snapshots['test_algos_help_pages[fd_first] fd_first'] = '''FD-First algorithm belongs to the family of algorithms
for discovering approximate conditional functional dependencies. For more
information, refer to the “Revisiting Conditional Functional Dependency
Discovery: Splitting the “C” from the “FD”” paper by J. Rammelaere 
and F. Geerts.

--cfd_max_lhs=INTEGER
\tcfd max considered LHS size

--cfd_minconf=FLOAT
\tcfd minimum confidence value (between 0 and 1)

--cfd_minsup=INTEGER
\tminimum support value (integer number between 1 and number of tuples in dataset)

--cfd_substrategy=STRING
\tCFD lattice traversal strategy to use
[dfs|bfs]

--columns_number=INTEGER
\tNumber of columns in the part of the dataset if you want to use algo not on the full dataset, but on its part

--tuples_number=INTEGER
\tNumber of tuples in the part of the dataset if you want to use algo not on the full dataset, but on its part

'''

snapshots['test_algos_help_pages[fd_mine] fd_mine'] = '''A classic algorithm for discovery of exact functional
dependencies. Has issues with the minimality of answer. For more
information, refer to the “FD_Mine: discovering functional dependencies in a
database using equivalences paper” by H. Yao et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_algos_help_pages[fdep] fdep'] = '''A classic algorithm for discovery of exact functional
dependencies. For more information, refer to the “Database Dependency
Discovery: A Machine Learning Approach” paper by Peter A. Flach and
Iztok Savnik.

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_algos_help_pages[fun] fun'] = '''A classic algorithm for discovery of exact functional
dependencies. For more information,  refer to the “FUN: An efficient
algorithm for mining functional and embedded dependencies” paper by
N. Novelli and R. Cicchetti.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_algos_help_pages[gfd_verifier] gfd_verifier'] = '''Algorithm for verifying whether a given
graph functional dependency holds. For more information about the primitive
refer to “Functional Dependencies for Graphs” by Wenfei Fan et al.

--gfd=STRING
\tPath to file with GFD
\tFor multiple values, specify multiple times 
\t(e.g., --gfd=1 --gfd=2)

--graph=STRING
\tPath to dot-file with graph

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[hpivalid] hpivalid'] = '''An algorithm to discover unique column combinations based on
hitting set enumeration and validation. For more information, refer
to "Hitting Set Enumeration with Partial Information for Unique Column
Combination Discovery" by J. Birnick et. al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

'''

snapshots['test_algos_help_pages[hyfd] hyfd'] = '''A modern algorithm for discovery of exact functional
dependencies. One of the most high-performance algorithms for this task. For
more information, refer to “A Hybrid Approach to Functional Dependency
Discovery” by T. Papenbrock and F. Naumann.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[hyucc] hyucc'] = '''An algorithm to discover exact unique column combinations.
For more information, refer to "A Hybrid Approach for Efficient Unique Column
Combination Discovery" by T. Papenbrock and F. Naumann

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[icde09_mfd_verifier] icde09_mfd_verifier'] = '''A family of metric functional dependency
verification algorithms. For more information about the primitive and the
algorithms, refer to “Metric Functional Dependencies” by N. Koudas et al.

--dist_from_null_is_infinity=BOOLEAN
\tspecify whether distance from NULL value is infinity (if not, it is 0)

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--lhs_indices=INTEGER
\tLHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --lhs_indices=1 --lhs_indices=2)

--metric=STRING
\tmetric to use
[euclidean|levenshtein|cosine]

--metric_algorithm=STRING
\tMFD algorithm to use
[brute|approx|calipers]

--parameter=FLOAT
\tmetric FD parameter

--q=INTEGER
\tq-gram length for cosine metric

--rhs_indices=INTEGER
\tRHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --rhs_indices=1 --rhs_indices=2)

'''

snapshots['test_algos_help_pages[naive_afd_verifier] naive_afd_verifier'] = '''A straightforward partition-based algorithm for
verifying whether a given approximate dependency holds. For more
information, refer to Section 2 of “TANE : An Efficient Algorithm for
Discovering Functional and Approximate Dependencies” by Y.Huntala et al. We
also recommend looking into “Efficient Discovery of ApproximateDependencies" by
S. Kruse and F. Naumann.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--lhs_indices=INTEGER
\tLHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --lhs_indices=1 --lhs_indices=2)

--rhs_indices=INTEGER
\tRHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --rhs_indices=1 --rhs_indices=2)

'''

snapshots['test_algos_help_pages[naive_aucc_verifier] naive_aucc_verifier'] = '''A straightforward partition-based algorithm for
verifying whether a given approximate unique column combination holds.
For more information on partitions refer to Section 2 of “TANE : An 
Efficient Algorithm for Discovering Functional and Approximate Dependencies”
by Y.Huntala et al. For more information on AUCC, refer to "Efficient Discovery
of Approximate Dependencies" by S. Kruse and F. Naumann.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--ucc_indices=INTEGER
\tcolumn indices for UCC verification
\tFor multiple values, specify multiple times 
\t(e.g., --ucc_indices=1 --ucc_indices=2)

'''

snapshots['test_algos_help_pages[naive_fd_verifier] naive_fd_verifier'] = '''A straightforward partition-based algorithm for
verifying whether a given exact functional dependency holds on the specified
dataset. For more information, refer to Lemma 2.2 from “TANE: An Efficient
Algorithm for Discovering Functional and Approximate Dependencies” by
Y.Huntala et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--lhs_indices=INTEGER
\tLHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --lhs_indices=1 --lhs_indices=2)

--rhs_indices=INTEGER
\tRHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --rhs_indices=1 --rhs_indices=2)

'''

snapshots['test_algos_help_pages[naive_gfd_verifier] naive_gfd_verifier'] = '''Algorithm for verifying whether a given
graph functional dependency holds. For more information about the primitive
refer to “Functional Dependencies for Graphs” by Wenfei Fan et al.

--gfd=STRING
\tPath to file with GFD
\tFor multiple values, specify multiple times 
\t(e.g., --gfd=1 --gfd=2)

--graph=STRING
\tPath to dot-file with graph

'''

snapshots['test_algos_help_pages[naive_nd_verifier] naive_nd_verifier'] = '''A straightforward algorithm for verifying whether
a given numerical dependecy holds. For more information refer to "Efficient
derivation of numerical dependencies" by P. Ciaccia et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--lhs_indices=INTEGER
\tLHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --lhs_indices=1 --lhs_indices=2)

--rhs_indices=INTEGER
\tRHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --rhs_indices=1 --rhs_indices=2)

--weight=INTEGER
\tWeight of ND to verify (positive integer)

'''

snapshots['test_algos_help_pages[naive_pfd_verifier] naive_pfd_verifier'] = '''A straightforward algorithm for
verifying whether a given probabilistic functional dependency holds. For 
more information, refer to “Functional Dependency Generation and Applications 
in pay-as-you-go data integration systems” by Daisy Zhe Wang et al.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--lhs_indices=INTEGER
\tLHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --lhs_indices=1 --lhs_indices=2)

--pfd_error_measure=STRING
\tPFD error measure to use
[per_tuple|per_value]

--rhs_indices=INTEGER
\tRHS column indices
\tFor multiple values, specify multiple times 
\t(e.g., --rhs_indices=1 --rhs_indices=2)

'''

snapshots['test_algos_help_pages[naive_ucc_verifier] naive_ucc_verifier'] = '''A straightforward partition-based algorithm for
verifying whether a given unique column combination holds.
For more information on partitions refer to Section 2 of “TANE : An 
Efficient Algorithm for Discovering Functional and Approximate Dependencies”
by Y.Huntala et al. For more information on UCC, refer to "Efficient Discovery
of Approximate Dependencies" by S. Kruse and F. Naumann.

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--ucc_indices=INTEGER
\tcolumn indices for UCC verification
\tFor multiple values, specify multiple times 
\t(e.g., --ucc_indices=1 --ucc_indices=2)

'''

snapshots['test_algos_help_pages[order] order'] = '''Algorithm Order efficiently discovers all n-ary lexicographical 
order dependencies under the operator “<”. For more information, refer to the
“Efficient order dependency detection” paper by Philipp Langer and Felix Naumann.

'''

snapshots['test_algos_help_pages[pfdtane] pfdtane'] = '''A TANE-based algorithm for discovery of probabilistic
functional dependencies. For more information, refer to “Functional Dependency
Generation and Applications in pay-as-you-go data integration systems” by
Daisy Zhe Wang et al.

--error=FLOAT
\terror threshold value for Approximate FD algorithms

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

--pfd_error_measure=STRING
\tPFD error measure to use
[per_tuple|per_value]

'''

snapshots['test_algos_help_pages[pyro] pyro'] = '''A modern algorithm for discovery of approximate functional
dependencies. Approximate functional dependencies are defined in the
“Efficient Discovery of Approximate Dependencies” paper by S.Kruse and
F.Naumann. Capable of discovering exact dependencies too.

--error=FLOAT
\terror threshold value for Approximate FD algorithms

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

--seed=INTEGER
\tRNG seed

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[pyroucc] pyroucc'] = '''An algorithm to discover exact and approximate unique
column combinations. For more information, refer to "Efficient Discovery
of Approximate Dependencies" by S. Kruse and F. Naumann.

--error=FLOAT
\terror threshold value for Approximate FD algorithms

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

--seed=INTEGER
\tRNG seed

'''

snapshots['test_algos_help_pages[spider] spider'] = '''A disk-backed unary inclusion dependency mining algorithm.
For more information, refer to "Efficiently detecting inclusion dependencies"
by J. Bauckmann et al.

--error=FLOAT
\terror threshold value for Approximate FD algorithms

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--mem_limit=INTEGER
\tmemory limit im MBs

--threads=INTEGER
\tnumber of threads to use. If 0, then as many threads are used as the hardware can handle concurrently.

'''

snapshots['test_algos_help_pages[split] split'] = '''The original algorithm for discovery of differential dependencies.
For more information, refer to the "Differential Dependencies: Reasoning
and Discovery" paper by S.Song and L.Chen.

The algorithm accepts the following specific option:

--difference_table=TABLE

This option specifies the CSV table that contains difference limits
for each column in the following format:

Col1,Col2,Col3
[0;1],[0;0],[2;3]
[1;3],[0;4],-----
[2;5],-----,-----

These distance constraints define the search space. For example,
the DD Col1 [1, 3] ; Col2 [0, 0] -> Col3 [2, 3] will be included in the search space.
For more information about the search space refer to the paper stated above
or to the example (examples/mining_dd.py).

The default value for this option is the following table:

Col1,Col2,Col3
[0;0],[0;0],[0;0]
[0;1],[0;1],[0;1]
[0;2],[0;2],[0;2]
[0;3],[0;3],[0;3]
[0;4],[0;4],[0;4]

--difference_table=TABLE
\tCSV table containing difference limits for each column

--num_columns=INTEGER
\tUse only first N columns of the table

--num_rows=INTEGER
\tUse only first N rows of the table

'''

snapshots['test_algos_help_pages[tane] tane'] = '''A classic algorithm for discovery of exact and approximate
functional dependencies. For more information, refer to “TANE : An Efficient
Algorithm for Discovering Functional and Approximate Dependencies” by
Y. Huntala et al.

Besides mining afd's with error measure g1 as intended in the original paper
we provide a possibility to use measures pdep, tau, mu_plus, rho. For more information on the
meausures refer to "Measuring Approximate Functional Dependencies: A Comparative Study"
by M. Parciak et al.

--afd_error_measure=STRING
\tAFD error measure to use
[g1|pdep|tau|mu_plus|rho]

--error=FLOAT
\terror threshold value for Approximate FD algorithms

--is_null_equal_null=BOOLEAN
\tspecify whether two NULLs should be considered equal

--max_lhs=INTEGER
\tmax considered LHS size

'''

snapshots['test_main_help_page main_help'] = '''The Desbordante data profiler is designed to help users
discover or verify various types of patterns in data. These patterns are
various kinds of data dependencies (functional, metric, inclusion, etc),
constraints (algebraic, denial, etc), many types of association rules and more.

Each pattern type is termed a “primitive”, and a specific occurrence of this
primitive inside a specific dataset is referred to as its “instance”. For
example, a functional dependency is a primitive, and the “company -> email”
functional dependency inside the sales.csv table is its instance.

For each primitive, Desbordante supports two key tasks: discovery and
verification. The discovery task discovers (mines) all relevant* primitive
instances within a given dataset, while verification checks (validates)
whether a given instance holds. The verification task name contains the
“_verification” suffix; for example, the “fd” task returns all minimal and
non-trivial functional dependencies contained in the dataset,
and “fd_verification” checks whether a given functional dependency holds.

* The notion of “relevance” depends on the definition of the primitive. The
relevant set is usually the minimal set of instances from which the rest can
be derived. For actual definitions, consult the related papers.

Each task can be performed by one of the provided algorithms. For some
primitives, several algorithms are available, each of which excel on a
different type of dataset, such as “wide” or “tall” tables. See
--task=TASK --help to view the list of all supported algorithms for TASK.
Additionally, we also provide a default algorithm which is the best one in
many cases.

The algorithms accept two types of parameters: primitive-specific
constraints and implementation-related settings. The first group includes
parameters that define which instances are to discover/verify, e.g. the
constraint on the maximum length of the left-hand side of the functional
dependency. The second group refers to general parameters that impact
algorithm performance, e.g. the number of threads to use, seed, buffer size
for intermediates, etc. Note that not all algorithms, even those designed
for the same task, support multithreading.

Next, several primitives have approximate versions, which allow some records
to deviate from the primitive definition. This is practical for dealing with
real-life data, which may contain all kinds of imperfections. The number of
such imperfect records is usually defined by an error threshold which is
calculated according to a primitive-specific procedure. In this case,
the algorithm can be parameterized by this threshold.

Overall, to use the Desbordante profiler, specify the dataset file, task,
algorithm and its parameters. The results will be written to the specified
output file or to console, if none is specified.

Currently, the console version of Desbordante supports:
1) Discovery of exact functional dependencies
2) Discovery of approximate functional dependencies
3) Discovery of soft functional dependencies
4) Discovery of probabilistic functional dependencies
5) Discovery of association rules
6) Discovery of exact order dependencies (set-based and list-based axiomatization)
7) Discovery of inclusion dependencies
8) Discovery of differential dependencies
9) Discovery of exact unique column combinations
10) Discovery of approximate unique column combinations
11) Verification of exact functional dependencies
12) Verification of approximate functional dependencies
13) Verification of metric dependencies
14) Verification of exact unique column combinations
15) Verification of approximate unique column combinations
16) Verification of numerical dependencies
17) Verification of probabilistic functional dependencies

If you need other types, you should look into the C++ code, the Python
bindings or the Web version.


--task=TASK
    specify the task to run, e.g., discovery of functional dependencies

--algo=ALGORITHM
    specify the algorithm to run, e.g., PYRO

--table=TABLE
    specify the input file to be processed by the algorithm.
    Algorithms for some tasks (currently, only IND) accept multiple
    input files; see --task=TASK for more information

--filename=FILENAME
    specify the file to write the results to. If none is selected, output is
    written to the console

--verbose
    print detailed information before the result

--help
    display this help or help page of the algorithm and task options
    (--task=TASK --help | --algo=ALGO --help); should be specified after
    --algo|--task

'''

snapshots['test_tasks_help_pages[afd] afd'] = '''Discover minimal non-trivial approximate functional
dependencies. Approximate functional dependencies are defined in the
“Efficient Discovery of Approximate Dependencies” paper by S. Kruse and
F. Naumann.

Algorithms: PYRO, TANE
Default: PYRO

'''

snapshots['test_tasks_help_pages[afd_verification] afd_verification'] = '''Verify whether a given approximate functional
dependency holds on the specified dataset. Approximate functional
dependencies are defined in the “Efficient Discovery of Approximate
Dependencies” paper by S. Kruse and F. Naumann.

Algorithms: NAIVE_AFD_VERIFIER
Default: NAIVE_AFD_VERIFIER

'''

snapshots['test_tasks_help_pages[ar] ar'] = '''Discover association rules. For more information, refer to
"Frequent Pattern Mining" book by Charu C. Aggarwal and Jiawei Han.

Algorithms: Apriori
Default: Apriori

'''

snapshots['test_tasks_help_pages[aucc] aucc'] = '''Discover approximate unique column combinations.
For more information, refer to "Efficient Discovery of Approximate
Dependencies" by S. Kruse and F. Naumann.

Algorithms: PYROUCC
Default: PYROUCC

'''

snapshots['test_tasks_help_pages[aucc_verification] aucc_verification'] = '''Verify whether a given approximate unique column combination
holds on the specified dataset. For more information about the primitive and 
the algorithms, refer to "Efficient Discovery of Approximate Dependencies" by 
S. Kruse and F. Naumann

Algorithms: NAIVE_AUCC_VERIFIER
Default: NAIVE_AUCC_VERIFIER

'''

snapshots['test_tasks_help_pages[cfd] cfd'] = '''Discover approximate conditional functional dependencies. For
more information about the primitive and the algorithm, refer to the “Revisiting
Conditional Functional Dependency Discovery: Splitting the “C” from the “FD””
paper by J. Rammelaere and F. Geerts.

Algorithms: FD_FIRST
Default: FD_FIRST

'''

snapshots['test_tasks_help_pages[dd] dd'] = '''Discover differential dependencies. Differential dependencies
are defined in the "Differential Dependencies: Reasoning and Discovery"
paper by S.Song and L.Chen. A more simple and useful definition can be
found in the "Efficient Discovery of Differential Dependencies Through
Association Rules Mining" paper by S.Kwashie et al.

Algorithms: SPLIT
Default: SPLIT

'''

snapshots['test_tasks_help_pages[fd] fd'] = '''Discover minimal non-trivial exact functional dependencies. For
more information about the primitive and the algorithms, refer to the
“Functional dependency discovery: an experimental evaluation of seven
algorithms” paper by T. Papenbrock et al.

Algorithms: PYRO, TANE, HYFD, FD_MINE, DFD, DEP_MINER, FDEP, FUN, FASTFDS, AID, EULERFD
Default: HYFD

'''

snapshots['test_tasks_help_pages[fd_verification] fd_verification'] = '''Verify whether a given exact functional dependency
holds on the specified dataset. For more information about the primitive and
algorithms, refer to the “Functional dependency discovery: an experimental
evaluation of seven algorithms” paper by T. Papenbrock et al.

Algorithms: NAIVE_FD_VERIFIER
Default: NAIVE_FD_VERIFIER

'''

snapshots['test_tasks_help_pages[gfd_verification] gfd_verification'] = '''
Algorithms: NAIVE_GFD_VERIFIER, GFD_VERIFIER, EGFD_VERIFIER

'''

snapshots['test_tasks_help_pages[ind] ind'] = '''Discover inclusion dependecies. For more information about
inclusion dependecies, refer to the "Inclusion Dependency Discovery: An
Experimental Evaluation of Thirteen Algorithms" by Falco Dürsch et al.
Algorithms for this task accept multiple input files. You can use one of the
following options:

--tables=TABLE
    specify input files to be processed by the algorithm.
    For multiple values, specify multiple times
    (e.g., --tables=TABLE_1 --tables=TABLE_2)

--tables_list=FILENAME
    specify file with list of input files (one on a line).
    You can type --tables_list=- to use stdin

--tables_directory=FILENAME, STRING, BOOLEAN
    specify directory with input files.
    separator and has_header are applied to all tables

Algorithms: SPIDER, FAIDA
Default: SPIDER

'''

snapshots['test_tasks_help_pages[mfd_verification] mfd_verification'] = '''Verify whether a given metric functional
dependency holds on the specified dataset. For more information about the
primitive and the algorithms, refer to “Metric Functional Dependencies” by
N. Koudas et al.

Algorithms: ICDE09_MFD_VERIFIER
Default: ICDE09_MFD_VERIFIER

'''

snapshots['test_tasks_help_pages[nd_verification] nd_verification'] = '''Verify whether a given numerical dependecy holds
on the specified dataset. For more information about the primitive and
the algorithms, refer to "Efficient derivation of numerical dependencies" by P. Ciaccia et al.
Algorithms: NAIVE_ND_VERIFIER
Default: NAIVE_ND_VERIFIER

'''

snapshots['test_tasks_help_pages[od] od'] = '''Discover order dependencies. For more information about the 
primitive and algorithms, refer to the “Effective and complete discovery 
of order dependencies via set-based axiomatization” paper by J. Szlichta 
et al.

Algorithms: FASTOD, ORDER
Default: FASTOD

'''

snapshots['test_tasks_help_pages[pfd] pfd'] = '''Discover minimal non-trivial probabilistic functional
dependencies. Probabilitistic functional dependencies are defined in the
“Functional Dependency Generation and Applications in pay-as-you-go 
data integration systems” paper by Daisy Zhe Wang et al.
Algorithms: PFDTANE
Default: PFDTANE

'''

snapshots['test_tasks_help_pages[pfd_verification] pfd_verification'] = '''Verify whether a given probabilistic functional dependency holds
on the specified dataset. For more information, refer to “Functional Dependency 
Generation and Applications in pay-as-you-go data integration systems” by 
Daisy Zhe Wang et al.
Algorithms: NAIVE_PFD_VERIFIER
Default: NAIVE_PFD_VERIFIER

'''

snapshots['test_tasks_help_pages[sfd] sfd'] = '''Discover soft functional dependencies and correlations (if only_sfd option set to False). 
Both are defined in the "CORDS: Automatic Discovery of Correlations and Soft 
Functional Dependencies" paper by Ihab F. Ilyas et al.

Algorithms: CORDS
Default: CORDS

'''

snapshots['test_tasks_help_pages[ucc] ucc'] = '''Discover exact unique column combinations. For more
information, refer to "A Hybrid Approach for Efficient Unique Column
Combination Discovery" by T. Papenbrock and F. Naumann

Algorithms: HPIVALID, PYROUCC, HYUCC
Default: HPIVALID

'''

snapshots['test_tasks_help_pages[ucc_verification] ucc_verification'] = '''Verify whether a given unique column combination
holds on the specified dataset. For more information about the primitive and 
the algorithms, refer to "Efficient Discovery of Approximate Dependencies" by 
S. Kruse and F. Naumann

Algorithms: NAIVE_UCC_VERIFIER
Default: NAIVE_UCC_VERIFIER

'''
