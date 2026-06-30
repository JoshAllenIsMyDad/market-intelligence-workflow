def select_question():
    """
    Select one of the two categories: "Macro" or "Indicators",
    then select one of the three questions
    """

    while True:
        category = input("Select one category (Macro or Indicator)").strip().lower()

        if category == "macro":
            question = input("""
                  Select the index (1/2/3) of question you are interested in:
                  1. How does FOMC rate decision impact USD, US equities and Treasury Price?
                  2. How does CPI / NFP affect USD, US equities and Treasury Price?
                  3. How does Middle East geopolitical risk affect USD, US equities and Treasury Price?
                  """).strip()
            if question in ["1","2","3"]:
                return category, question
            else:
                print("Invalid question; please re-enter.")
        elif category == "indicator":
            question = input("""
                  Select the index (1/2/3) of question you are interested in:
                  1. Does opening price-volume combination indicate any trends for the rest of the day?
                  2. How does opening volatility affect rest of the day?
                  3. If price deviates from MA / VWAP, how does it affect rest of the day?
                  """).strip()
            if question in ["1","2","3"]:
                return category, question
            else:
                print("Invalid question; please re-enter.")
        else:
            print("Invalid category; please re-enter.")

# test
if __name__ == "__main__":
    print(select_question())