from wf_dataprocessing import processor
from wf_ml_evaluation import split_data, eval_predictions
from wf_ml_prediction import test_model
from wf_ml_training import trn_model
from wf_visualization import create_visualization

if __name__ == '__main__':
    filename = "data_processed/USA/_allData.csv"
    process_path = "data_processed/_datasets/"
    model_path = "models/"
    predictions_path = "data_processed/_predictions/"
    eval_file = "evaluation/"

    #processor()
    print("Initial data processed.")

    #split_data(filename, process_path, .8)
    print("Data split.")

    #create_visualization()
    print("Data visualized and graphs created.")

    trn_model(process_path + "trn/", model_path)
    print("Models trained.")

    test_model(process_path + "tst/", predictions_path)
    print("Predictions made.")

    eval_predictions(predictions_path, eval_file)
    print("Models Evaluated")

    # the experiment: generating data to evaluate models
    # experiment_path = "data_processed/_datasets/experiment/"
    # experiment_out = "evaluation/experiment/"
    # experiment_predictions_path = "data_processed/_predictions/experiment"
    # # for i in range(20):
    #     if False:
    #         # generateExperiment(experiment_path)
    #
    #         vary = ['income/', 'pop_density/', 'both/', 'inverse/']
    #         for var in vary:
    #             trn_model(process_path + "trn/", model_path)
    #             trn_model(experiment_path + var, model_path)
    #
    #             print("Models trained.")
    #
    #             test_model(process_path + "tst/", model_path, experiment_predictions_path + var)
    #             print("Predictions made.")
    #
    #             eval_predictions(experiment_predictions_path + var, eval_file + "experiment/" + var)
    #             print("Models Evaluated")
