import numpy as np


def invertibility(x):
    try:
        np.linalg.inv(x)
    except np.linalg.LinAlgError:
        print("Matriz no invertible")
    else:
        print("Matriz invertible")


if __name__ == "__main__":
    I = np.eye(32, dtype=int)

    M1 = np.random.permutation(I)
    M2 = np.random.permutation(I)

    print("\nInvertibilidad M1:")
    invertibility(M1)
    print("\nInvertibilidad M2:")
    invertibility(M2)

    P = (M1 + M2) % 2
    print("\nInvertibilidad P:")
    invertibility(P)

    print("\nMatriz Clave")
    with np.printoptions(threshold=np.inf):
        print(P)

    with open('key32.npy', 'wb') as file:
        np.save(file, P)
        print("\nKey saved!")
