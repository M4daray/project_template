from project_template import driver

from project_template.metrics_model import Metric
from project_template.splitter import Splitter
from project_template.svm_model import SVModel

def main() -> None:
    """ """
    iris = driver.get_iris()

    my_split = Splitter()
    X_train, X_test, y_train, y_test = my_split.split(iris)
    
    model = SVModel()
    model.train(X_train, y_train)
    y_pred = model.predict(X_test)

    my_metric = Metric({})
    report = my_metric.generate_report(y_test, y_pred)

    print(report)

if __name__ == "__main__" :
    main()
    