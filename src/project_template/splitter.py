from sklearn.model_selection import train_test_split

class Splitter:

    def __init__(self) -> None:
        pass

    def split(self, data):
        """ """
        X = data.drop(['target'], axis = 1)
        y = data['target'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        return X_train, X_test, y_train, y_test