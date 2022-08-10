W = []
for i in range(10):
    W.append(int(input()))
K = []
for i in range(10):
    K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)

W_total = W[0] + W[1] + W[2]
K_total = K[0] + K[1] + K[2]

print(W_total, K_total)