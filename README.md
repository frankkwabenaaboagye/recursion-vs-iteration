# Recursion vs Iteration (Python)

Small practice project for converting recursive algorithms into iterative
ones and vice versa.

The idea is:

- We have a bunch of small algorithmic problems in the `problems/` package
  (one `.py` file per problem).
- For some problems, the **recursive** solution is provided and you must
  write the **iterative** version.
- For others, the **iterative** solution is provided and you must
  write the **recursive** version.
- For at least one problem, you implement **both** from scratch.
- Tests in `test_exercises.py` automatically detect which problems are
  implemented and only run tests for those.

This makes it easy to raise a PR that focuses on just one problem.

---

## How it works

All exercises live in the `problems/` package. Each problem has its own
module and defines two functions:

- `<name>_recursive`
- `<name>_iterative`

The problems are (one module per problem):

The problems are (one module per problem):

1. [x] `problems/factorial.py` – `factorial_recursive` / `factorial_iterative`
2. [x] `problems/sum_digits.py` – `sum_digits_recursive` / `sum_digits_iterative`
3. [x] `problems/reverse_string.py` – `reverse_string_recursive` / `reverse_string_iterative`
4. [x] `problems/fibonacci.py` – `fib_recursive` / `fib_iterative`
5. [x] `problems/power.py` – `power_recursive` / `power_iterative`
6. [x] `problems/flatten.py` – `flatten_recursive` / `flatten_iterative`
7. [x] `problems/binary_search.py` – `binary_search_recursive` / `binary_search_iterative`
8. [x] `problems/gcd.py` – `gcd_recursive` / `gcd_iterative`
9. [x] `problems/count_occurrences.py` – `count_occurrences_recursive` / `count_occurrences_iterative`
10. [x] `problems/palindrome.py` – `is_palindrome_recursive` / `is_palindrome_iterative`



There is also a fully-solved **example** problem you can use as a
reference:

- `problems/example_sum_list.py` – `sum_list_recursive` / `sum_list_iterative`

Some of these already have a recursive implementation, some already
have an iterative implementation, and some have neither.

The tests in `test_exercises.py` work like this:

- For each pair, if **either** function still raises `NotImplementedError`,
  the tests for that pair are **skipped**.
- As soon as you implement **both** functions for a pair, the tests for
  that pair become active and must pass.

This means you can send a PR that solves just one problem by implementing
both the recursive and iterative versions for that problem.

---

## How to contribute (raise a PR)

1. **Fork** this repository on GitHub.
2. **Clone** your fork locally and create a new branch, e.g.

   ```bash
   git checkout -b solve-factorial
   ```

3. Open the appropriate file under `problems/` and pick **one problem** from
   the list above.

   - If the recursive version is implemented and the iterative one raises
     `NotImplementedError`, your job is to **translate the recursion into
     iteration**.
   - If the iterative version is implemented and the recursive one raises
     `NotImplementedError`, your job is to **translate the iteration into
     recursion**.
   - For the palindrome problem, you can implement **both** versions from
     scratch.

4. Implement **both** versions for that problem:

   - Keep the existing function names and parameters.
   - Do **not** change the tests.
   - For the "recursive" versions, prefer clear base-case + smaller-subproblem
     style. Avoid loops unless they are trivial.
   - For the "iterative" versions, prefer loops (and, where relevant, an
     explicit stack) and avoid recursion.

5. (Optional but recommended) Create small extra tests or print statements
   locally while developing, but do **not** commit them if they change the
   public API or the main test suite.

6. Install dependencies and run the tests locally:

   ```bash
   pip install pytest
   pytest
   ```

   - Only the problems where you have implemented **both** versions will
     actually run tests; others will show as `skipped`.

7. Commit your changes and push your branch:

   ```bash
   git add problems/
   git commit -m "Implement factorial iterative version"  # example
   git push origin solve-factorial
   ```

8. Open a **Pull Request** on GitHub from your branch to the main
   repository. In the PR description, mention which problem(s) you solved
   and briefly describe your approach (especially how you converted
   recursion ↔ iteration).

---

## For maintainers / presentation use

- This repo is designed for a workshop or talk about recursion vs
  iteration in Python.
- Participants each grab one problem and submit a PR.
- CI should run `pytest` on every PR. A PR is "done" when all tests
  for the problems they touched are passing.

Feel free to add more modules under `problems/` and extend
`test_exercises.py` with more problems, but keep the same structure so
the contribution process stays simple.
