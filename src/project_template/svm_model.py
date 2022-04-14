from sklearn import svm
from project_template import PATH_CONFIG_FOLDER
from project_template.config_manager import LearningParamConfig

class SVModel:

    def __init__(self, config: LearningParamConfig) -> None:
        self.clf = None
        self.config = config

    def train(self, X_train, y_train):
        """ """
        C = self.config.C  # SVM regularization parameter
        self.clf = svm.LinearSVC(C=C, max_iter=10000)
        self.clf.fit(X_train, y_train)

    def predict(self, data):
        """ """
        pred = self.clf.predict(data)
        return pred