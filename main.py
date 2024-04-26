if __name__ == "__main__":
  # Python block comments

  # increase price by 5%
  price = 100
  price *= 1.05
  print(price)

  # Python inline comments

  salary = 100
  salary*= 1.02 # increase salary by 2%

  # Python docstrings

  """
  Unlike a regular comment, a documentation string can be accessed at run-time using obj.__doc__ attribute when obj is the name of the function.
  """

  # One-line docstrings

  def quicksort():
    """sort the list using quicksort algorithm"""

  print(quicksort.__doc__)
