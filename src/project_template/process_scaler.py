from sklearn.preprocessing import StandardScaler




class Process_scaler():

    def __init__(self) -> None:
        self.scaler = StandardScaler()

    def process(self, data):
        """ """
        data = self.scaler.fit_transform(data)
        return data

    def apply(self, data):
        data = self.scaler.transform(data)
        return data