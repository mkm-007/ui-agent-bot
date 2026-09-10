import pytest
from ui_agent.agent import run_agent


def test_button_properties():
    result = run_agent('Add a secondary button labeled Submit')
    assert result['props'] == {'label': 'Submit', 'variant': 'secondary'}
    assert '@Input() label: string' in result['stub']
    assert 'standalone: true' in result['stub']


def test_table_columns():
    result = run_agent('Add a table with name and department columns')
    assert result['props']['columns'] == ['name', 'department']
    assert 'scope="col"' in result['stub']

@pytest.mark.parametrize('prompt', ['', 'Add calendar', 'Add button and card', 'x'*1001, 'unstable layout'])
def test_refusal(prompt):
    with pytest.raises(ValueError): run_agent(prompt)


def test_no_request_source_injection():
    result = run_agent('Add a button labeled `; alert(1); //')
    assert 'alert(1)' not in result['stub']
    assert 'alert(1)' in result['props']['label']


def test_catalog_is_not_mutated():
    first = run_agent('Add a card')
    first['component']['inputs'].append('injected')
    assert 'injected' not in run_agent('Add a card')['component']['inputs']


def test_quoted_component_name_is_label():
    assert run_agent('Add a button labeled "card"')['component']['name'] == 'AppButton'
