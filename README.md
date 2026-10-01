# PLP Python Week 3 Assignment

## Files

- `grade_reporter.py` — Loops through a list of scores, assigns each one a
  letter grade (A, B, C, F), counts how many passed and failed, and prints
  the average score rounded to one decimal place.
- `bug_hunt.py` — A broken program that was supposed to sum 1 through 5,
  fixed by finding and correcting three separate bugs.

## Bug Hunt reflection

The hardest bug to find was the third one, the `count < 5` loop condition,
since it produced no error message at all, the program ran and printed a
clean result that simply looked plausible. I knew something was wrong only
because the instructions stated the correct answer should be 15, and the
program printed 10 instead. The first two bugs (the missing colon and the
string/integer concatenation) were much easier to catch, since Python's
own error messages pointed directly at the problem line and explained
what kind of issue it was.