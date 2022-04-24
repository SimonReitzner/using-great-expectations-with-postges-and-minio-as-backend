from great_expectations.data_context import BaseDataContext
from great_expectations.core.expectation_configuration import ExpectationConfiguration
from dotenv import load_dotenv
from sklearn.datasets import load_wine
from datetime import datetime

from data_context_config import data_context_config


def main():

    # Load environment file
    load_dotenv()

    # Setup data context from configuration dictionary
    context = BaseDataContext(project_config=data_context_config)

    # Add a datasource to the data context
    datasource_config = {
        "name": "pandas",
        "class_name": "Datasource",
        "module_name": "great_expectations.datasource",
        "execution_engine": {
            "module_name": "great_expectations.execution_engine",
            "class_name": "PandasExecutionEngine"
        },
        "data_connectors": {
            "default_runtime_data_connector_name": {
                "class_name": "RuntimeDataConnector",
                "batch_identifiers": ["default_identifier_name"]
            }
        }
    }
    context.add_datasource(**datasource_config)

    # Create an expectation suite
    suite = context.create_expectation_suite(
        "my_expectation_suite",
        overwrite_existing=True,
        ge_cloud_id=None
    )

    # Create and save some expectations
    expectation_configurations = []
    expectation_configurations.append(
        ExpectationConfiguration(
            expectation_type="expect_column_values_to_not_be_null",
            kwargs={
                "column": "magnesium",
                "mostly": 0.9,
            }
        )
    )
    expectation_configurations.append(
        ExpectationConfiguration(
            expectation_type="expect_column_values_to_be_between",
            kwargs={
                "column": "proanthocyanins",
                "min_value": 1,
                "max_value": 3
            }
        )
    )

    for expectation_configuration in expectation_configurations:
        suite.add_expectation(
            expectation_configuration=expectation_configuration,
            overwrite_existing=True
        )
    context.save_expectation_suite(suite)

    # Create and save a checkpoint
    checkpoint_config = {
        "name": "pandas_checkpoint",
        "config_version": 1,
        "class_name": "SimpleCheckpoint",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "pandas",
                    "data_connector_name": "default_runtime_data_connector_name",
                    "data_asset_name": "pandas",
                },
                "expectation_suite_name": "my_expectation_suite",
            }
        ],
    }
    context.add_checkpoint(**checkpoint_config)

    # Import data
    df, _ = load_wine(return_X_y=True, as_frame=True)
    
    # Validate data by running the checkpoint
    results = context.run_checkpoint(
        checkpoint_name="pandas_checkpoint",
        batch_request={
            "runtime_parameters": {"batch_data": df},
            "batch_identifiers": {
                "default_identifier_name": f"wine-data_{datetime.today()}"
            },
        },
        run_name="wine-dataset",
        run_time=None
    )

    # Open data docs
    context.open_data_docs(results.list_validation_result_identifiers()[0])


if __name__ == "__main__":
    main()