# write a function def solution(A, D) that given an array A of N integers representing transaction amounts and an array D of strings N representing transaction dates, returns the financial balance of the account at the end of the year 2020. Transaction number K (for k within the range [0..N..1]) was executed on the date representing D[k] for amount A[k]




def solution(A, D):
    balance = 0
    transactions = []

    if len(A) == len(D):
        for i in range(len(A)):
            transactions.append((A[i], D[i]))

    for transaction in transactions:
        amount, date = transaction
        year = date.split('-')[0]
        if year == '2020':
            balance += amount

    print(balance)


solution(A=[1, -1, 0, -105], D=[
         "2020-12-31", "2020-04-04", "2020-04-14", "2020-07-12"])
