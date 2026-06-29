def select_category():
    """
    Select one of the two categories: "Macro" or "Indicators"
    """
    while True:
        category = input("Select one category (Macro or Indicator)").strip().lower()

        if category in ["macro","indicator"]:
            return category
        else:
            print("Invalid category; please re-enter.")