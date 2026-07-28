from ui_agent.agent import run_agent


def test_button_agent():
    result = run_agent("Add a primary button labeled Submit")
    assert result["component"]["name"] == "AppButton"
    assert "emit_angular_stub" in result["plan"]
    assert "AppButton" in result["stub"]


def test_table_agent():
    result = run_agent("Add a data table for employees")
    assert result["component"]["name"] == "AppDataTable"
    assert "configure_columns" in result["plan"]
