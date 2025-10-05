from hello import hello_world

def test_hello_world():
    """test hello_world function"""
    
    assert hello_world() == "Hello, World!"