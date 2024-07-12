import unittest

from nodes.html_node import LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        pass
    
        # node1 = ParentNode("p", [
        #     LeafNode("b", "This is a LeafNode").to_html(),
        #     LeafNode("i", "This is also a LeafNode").to_html()
        # ], {"href": "html://google.com"})
        # html1 = node1.to_html()
        # print(html1)
        
        # node2 = ParentNode("p", [
        #     LeafNode("b", "This is a LeafNode").to_html(),
        #     LeafNode(None, "This is a LeafNode with no value").to_html(),
        # ])
        # html2 = node2.to_html()
        # print(html2)
        
        # node3 = ParentNode("p", [
        #     LeafNode(None, "This is a LeafNode with no value").to_html(),
        #     LeafNode(None, "This is also a LeafNode").to_html()
        # ])
        # html3 = node3.to_html()
        # print(html3)


if __name__ == "__main__":
    unittest.main()