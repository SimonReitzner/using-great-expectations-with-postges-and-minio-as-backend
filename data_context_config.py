from great_expectations.data_context.types.base import DataContextConfig

data_context_config = DataContextConfig(
        config_version=2,
        datasources=None,
        expectations_store_name="expectations_store",
        validations_store_name="validations_store",
        evaluation_parameter_store_name="evaluation_parameter_store",
        checkpoint_store_name="checkpoint_store",
        profiler_store_name="profiler_store",
        plugins_directory=None,
        validation_operators={
            "action_list_operator": {
                "class_name": "ActionListValidationOperator",
                "action_list": [
                    {
                        "name": "store_validation_result",
                        "action": {"class_name": "StoreValidationResultAction"},
                    },
                    {
                        "name": "store_evaluation_params",
                        "action": {"class_name": "StoreEvaluationParametersAction"},
                    },
                    {
                        "name": "update_data_docs",
                        "action": {"class_name": "UpdateDataDocsAction"},
                    },
                ],
            }
        },
        stores={
            "expectations_store": {
                "class_name": "ExpectationsStore",
                "store_backend": {
                    "class_name": "DatabaseStoreBackend",
                    "credentials": {
                        "drivername": "postgresql+psycopg2",
                        "host": "localhost",
                        "port": "${POSTRES_PORT}",
                        "username": "${POSTRES_USER}",
                        "password": "${POSTGRES_PASSWORD}",
                        "database": "${POSTGRES_DB}",
                    },
                },
            },
            "validations_store": {
                "class_name": "ValidationsStore",
                "store_backend": {
                    "class_name": "TupleS3StoreBackend",
                    "bucket": "${MINIO_BUCKET_NAME}",
                    "prefix": "validationsstore",
                    "boto3_options": {
                        "endpoint_url": "http://localhost:${MINIO_API_PORT}",
                        "aws_access_key_id": "${MINIO_ROOT_USER}",
                        "aws_secret_access_key": "${MINIO_ROOT_PASSWORD}"
                    },
                },
            },
            "evaluation_parameter_store" : {
                "class_name": "EvaluationParameterStore"
            },
            "metric_store": {
                "class_name": "MetricStore",
                "store_backend": {
                    "class_name": "TupleS3StoreBackend",
                    "bucket": "${MINIO_BUCKET_NAME}",
                    "prefix": "metricstore",
                    "boto3_options": {
                        "endpoint_url": "http://localhost:${MINIO_API_PORT}",
                        "aws_access_key_id": "${MINIO_ROOT_USER}",
                        "aws_secret_access_key": "${MINIO_ROOT_PASSWORD}"
                    },
                },
            },
            "checkpoint_store": {
                "class_name": "CheckpointStore",
                "store_backend": {
                    "class_name": "TupleS3StoreBackend",
                    "bucket": "${MINIO_BUCKET_NAME}",
                    "prefix": "checkpointstore",
                    "boto3_options": {
                        "endpoint_url": "http://localhost:${MINIO_API_PORT}",
                        "aws_access_key_id": "${MINIO_ROOT_USER}",
                        "aws_secret_access_key": "${MINIO_ROOT_PASSWORD}"
                    },
                },
            },
            "profiler_store": {
                "class_name": "ProfilerStore",
                "store_backend": {
                    "class_name": "TupleS3StoreBackend",
                    "bucket": "${MINIO_BUCKET_NAME}",
                    "prefix": "profilerstore",
                    "boto3_options": {
                        "endpoint_url": "http://localhost:${MINIO_API_PORT}",
                        "aws_access_key_id": "${MINIO_ROOT_USER}",
                        "aws_secret_access_key": "${MINIO_ROOT_PASSWORD}"
                    },
                },
            },
        },
        data_docs_sites={
            "s3_site": {
                "class_name": "SiteBuilder",
                "store_backend": {
                    "class_name": "TupleS3StoreBackend",
                    "bucket": "${MINIO_BUCKET_NAME}",
                    "prefix": "datadocs",
                    "boto3_options": {
                        "endpoint_url": "http://localhost:${MINIO_API_PORT}",
                        "aws_access_key_id": "${MINIO_ROOT_USER}",
                        "aws_secret_access_key": "${MINIO_ROOT_PASSWORD}"
                    },
                },
                "site_index_builder": {
                    "class_name": "DefaultSiteIndexBuilder",
                    "show_cta_footer": False,
                },
                "show_how_to_buttons" : False
            }
        },
        notebooks=None,
        config_variables_file_path=None,
        anonymous_usage_statistics={"enabled": False},
        store_backend_defaults=None,
        commented_map=None,
        concurrency=None,
        progress_bars=None,
)
