from data_structures_and_algorithms.data_structures.graph.graphs import Graph, Node


def test_add_node_to_graph(): 
    
    graph = Graph()
    actual = graph.add_node('welcome').value
    assert actual ==  'welcome' 


       
def test_add_edge_other_case():  
    graph = Graph()
    node1 = graph.add_node('node1')
    node2 = graph.add_node('node2')
    graph.add_edge(node1, node2)



def test_get_nodes():
    graph = Graph()
    node1 = graph.add_node('node1')
    node2 = graph.add_node('node2')
    actual = len(graph.get_nodes())
    assert actual == 2



def test_size():
    graph = Graph()
    graph.add_node('node1')
    expected = 1
    actual = graph.size()
    assert actual == expected




def test_size_empty(): 

    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected