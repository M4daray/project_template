from project_template import PATH_CONFIG_FOLDER, driver
import pandas as pd
from project_template.metrics_model import Metric
from project_template.splitter import Splitter
from project_template.svm_model import SVModel
from typing import TypeVar, Generic, List, Tuple
from project_template import config_manager
from project_template import process_scaler
import os

def main() -> None:
    """ """
    app_config: config_manager.AppConfig = config_manager.load_config(os.path.join(PATH_CONFIG_FOLDER, "config.ini"))

    iris: pd.DataFrame = driver.get_iris()

    my_split = Splitter()
    X_train, X_test, y_train, y_test = my_split.split(iris)

    scaler = process_scaler.Process_scaler()
    X_train = scaler.process(X_train)
    
    model = SVModel(app_config.learning_param)
    model.train(X_train, y_train)

    X_test = scaler.process(X_test)
    y_pred = model.predict(X_test)

    my_metric = Metric({})
    report = my_metric.generate_report(y_test, y_pred)

    print(report)

if __name__ == "__main__" :
    main()
    