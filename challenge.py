# write a function def solution(A, D) that given an array A of N integers representing transaction amounts and an array D of strings N representing transaction dates, returns the financial balance of the account at the end of the year 2020. Transaction number K (for k within the range [0..N..1]) was executed on the date representing D[k] for amount A[k]


def solution(A, D):
    # Looping through all te integer values of A
    for i in range(len(A)):
        # If checking for the last element of D to be 'D' to get the date
        if D[i][-1] == 'D':
            # Multiplying each value in array A by the date value(-1) grabbed from the date
            A[i] *= -1
            # if checking for the negative values in the array A
            if A[i] < 0:
              # looping over the negative values
                count = 0
                for i in A[i]:
                    i *= -1
                    count += 1
                print(i)

    # calculating the sum of A
    print(sum(A))


solution(A=[1, -1, 0, -105], D=[
         "2020-12-31", "2020-04-04", "2020-04-14", "2020-07-12"])
