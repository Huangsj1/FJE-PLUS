import json
from builder import JSONBuilder
from styleFactory import StyleFactory
from iconFamily import PokerFaceIconFamily
from visitor import TreeDisplayVisitor, RectangleDisplayVisitor
from iterator import NodeIterator

def main():
    style = "tree"  # or "rectangle"
    # style = "rectangle"
    icon_family = PokerFaceIconFamily()  # 图标族示例

    # 读取JSON数据
    json_data = '''
    {
        "oranges": {
            "mandarin": {
                "clementine": null,
                "tangerine": "cheap & juicy!"
            }
        },
        "apples": {
            "gala": null,
            "pink lady": null
        }
    }
    '''

    data = json.loads(json_data)

    # 创建风格工厂
    factory = StyleFactory.get_factory(style)
    
    # 使用建造者模式创建节点树
    builder = JSONBuilder(factory)
    root = builder.build(data)

    # 显示节点树
    if style == "tree":
        visitor = TreeDisplayVisitor()
    else:
        visitor = RectangleDisplayVisitor()

    iterator = NodeIterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)

if __name__ == "__main__":
    main()
