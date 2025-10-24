from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

def forward(X, W1, b1, W2, b2):
    Z = 1 / (1 + np.exp(-(X.dot(W1) + b1)))  # sigmoid hidden layer
    A = Z.dot(W2) + b2                       # output layer (before softmax)
    expA = np.exp(A)
    Y = expA / expA.sum(axis=1, keepdims=True)  # softmax
    return Y, Z

def classification_rate(Y, P):
    return np.mean(Y == P)

def derivative_w2(Z, T, Y):
    return Z.T.dot(T - Y)

def derivative_w1(X, Z, T, Y, W2):
    dZ = (T - Y).dot(W2.T) * Z * (1 - Z)
    return X.T.dot(dZ)

def derivative_b2(T, Y):
    return (T - Y).sum(axis=0)

def derivative_b1(T, Y, W2, Z):
    return ((T - Y).dot(W2.T) * Z * (1 - Z)).sum(axis=0)

def cost(T, Y):
    return -np.sum(T * np.log(Y))

def main():
    # Create 3-class synthetic dataset
    Nclass = 500
    D = 2
    M = 3
    K = 3

    X1 = np.random.randn(Nclass, D) + np.array([0, -2])
    X2 = np.random.randn(Nclass, D) + np.array([2, 2])
    X3 = np.random.randn(Nclass, D) + np.array([-2, 2])
    X = np.vstack([X1, X2, X3])
    Y = np.array([0]*Nclass + [1]*Nclass + [2]*Nclass)

    # One-hot encoding
    N = len(Y)
    T = np.zeros((N, K))
    for i in range(N):
        T[i, Y[i]] = 1

    # Visualize data
    plt.scatter(X[:, 0], X[:, 1], c=Y, s=100, alpha=0.5)
    plt.title("Training Data")
    plt.show()

    # Initialize weights
    W1 = np.random.randn(D, M)
    b1 = np.random.randn(M)
    W2 = np.random.randn(M, K)
    b2 = np.random.randn(K)

    learning_rate = 1e-3
    costs = []

    for epoch in range(1000):
        Y_hat, Z = forward(X, W1, b1, W2, b2)
        if epoch % 100 == 0:
            c = cost(T, Y_hat)
            P = np.argmax(Y_hat, axis=1)
            r = classification_rate(Y, P)
            print(f"Epoch {epoch}: cost = {c:.3f}, classification_rate = {r:.3f}")
            costs.append(c)

        # Gradient ascent (use -= for descent)
        gW2 = derivative_w2(Z, T, Y_hat)
        gb2 = derivative_b2(T, Y_hat)
        gW1 = derivative_w1(X, Z, T, Y_hat, W2)
        gb1 = derivative_b1(T, Y_hat, W2, Z)

        W2 += learning_rate * gW2
        b2 += learning_rate * gb2
        W1 += learning_rate * gW1
        b1 += learning_rate * gb1

    plt.plot(costs)
    plt.title("Cost over epochs")
    plt.xlabel("Epochs (x100)")
    plt.ylabel("Cost")
    plt.show()

if __name__ == '__main__':
    main()
