# def toh(N, fromm, to, aux):
#     if N==1:
#         print(f"move disk from {fromm} to {to}")
#         return

#     toh(N-1, fromm, aux, to)
#     print(f"move disk from {fromm} to {to}")
#     toh(N-1, to, fromm, aux)


# toh(4,'A','C','B')


# def toh(N, fromm, to, aux):
#     count = 0;
#     def helper(N, fromm, to, aux):
#         nonlocal count
#         if N==1:
#             print(f"move disk {N} from rod {fromm} to {to}")
#             count+=1
#             return
#         helper(N-1, fromm, aux, to)
#         print(f"move disk {N} from rod {fromm} to {to}")
#         count+=1
#         helper(N-1, aux, fromm, to)
#     helper(N, fromm, to, aux)
#     return count
# toh(4,'A','C','B')

def toh(N, fromm, to, aux):
    if N == 1:
        print(f"Move disk 1 from {fromm} to {to}")
        return

    toh(N - 1, fromm, aux, to)
    print(f"Move disk {N} from {fromm} to {to}")
    toh(N - 1, aux, to, fromm)

# Example usage
N = 3
toh(N, 'A', 'C', 'B')
print("Total moves:", 2**N - 1)
