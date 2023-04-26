import sys
import os
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


from src.logger import logging
from src.exception import CustomException

from src.utils import evaluate_models
from src.utils import save_object

from dataclasses import dataclass

@dataclass
class ModelTrainingConfig:
    trained_model_file_path =os.path.join("artifacts","model.pkl")
class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config=ModelTrainingConfig()
    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("split training and test")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models ={
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(), 
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }
            model_report:dict=evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)

            best_model_score =max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]

            if best_model_score<.6:
                raise CustomException("No best model Faund")
            logging.info(f"best model faunded from train and test data")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )            

            logging.info(f"best model score : {best_model_name,best_model_score}")
            # print(r2_score)
            return best_model_score
        except Exception as e:
            CustomException(e,sys)
