from sklearn import svm
from project_template import PATH_CONFIG_FOLDER
import yaml

class SVModel:

    def __init__(self) -> None:
        self.clf = None
        with open(PATH_CONFIG_FOLDER, 'r') as file:
            self.config = yaml.safe_load(file)

    def train(self, X_train, y_train):
        """ """
        C = self.config['learning_param']['C']  # SVM regularization parameter
        self.clf = svm.LinearSVC(C=C, max_iter=10000)
        self.clf.fit(X_train, y_train)

    def predict(self, data):
        """ """
        pred = self.clf.predict(data)
        return pred