# write a function def solution(A, D) that given an array A of N integers representing transaction amounts and an array D of strings N representing transaction dates, returns the financial balance of the account at the end of the year 2020. Transaction number K (for k within the range [0..N..1]) was executed on the date representing D[k] for amount A[k]


def solution(A, D):
    # starting the balance at an initial value of 0
    financial_balance = 0
    # initializing an empty list for the transactions
    transactions = []

    # if to check if the length of array A and D are equal
    if len(A) == len(D):
      # looping through the arrays
        for i in range(len(A)):
          # appending the arrays to the list of transaction to store the amount and transaction date
            transactions.append((A[i], D[i]))

    # Looping through the list of transactions
    for transaction in transactions:
      # assigning the transactions the date and amount
        amount, date = transaction
        # splitting the date to get the year
        year = date.split('-')[0]
        # checking if there is a year
        if year:
          # adding the amount to the balance
            financial_balance += amount

    print(financial_balance)


solution(A=[100, 100, 100, -10], D=[
         "2020-12-31", "2020-04-04", "2020-04-14", "2020-07-12"])
