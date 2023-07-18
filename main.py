def IMAGE_SMOTE(df , sample):
    n = df.shape[0]
    for i in range(sample):
        j = np.random.randint(0, n, 1)
        k = np.random.randint(0, n, 1)
        x = df.iloc[j,:].values
        y = df.iloc[k,:].values
        x_hat = ((x - y ) * np.random.sample(1)) + x
        x_hat = np.array([0 if i<=150 else 1 for i in       np.ravel(x_hat)])
        plt.matshow(x_hat.reshape(28,28))
    plt.show()
