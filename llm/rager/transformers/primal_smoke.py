if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from elasticsearch import Elasticsearch


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    print(data)
    index_name = data
    query = "When is the next cohort?"
    connection_string = kwargs.get('connection_string', 'http://elasticsearch:9200')

    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^4", "text"],
                        "type": "best_fields"
                    }
                },
            }
        }
    }
    es_client = Elasticsearch(connection_string)

    search_results = es_client.search(index=index_name, body=search_query)
    print(search_results)

    return search_results


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'