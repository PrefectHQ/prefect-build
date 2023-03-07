test_yaml = """
flows:
  - flow_name: my_flow
    flow_path: flows/sample_flow/say_hello.py
    deployments:
      - name: default
        parameters: {"name": "prefect"}
        schedule: {"cron": "0 * * * *", "timezone": "Australia/Brisbane"}
        infra_overrides: {"cpu": 256, "memory": 512}
      """
