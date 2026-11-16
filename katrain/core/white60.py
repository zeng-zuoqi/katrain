"""Coach for the annotated White 60 study. Navigation uses KaTrain game nodes."""
STEPS = {
    "start": ("白刚提劫。左下还可以怎样走？", "看黑在左下怎么走", "local"),
    "local": ("黑 E4 留在左下，白怎样补劫？", "看白应手", "try"),
    "try": ("白 C4 已经补住。请在棋盘上试一手黑棋。", "", None),
    "compare": ("KataGo 参考走黑 D6。即使白补劫，附近的黑棋仍有后续。", "看右上实战", "threat"),
    "threat": ("黑去右上 Q18 找劫材，白会怎样应？", "看白 62", "reply"),
    "reply": ("白应在 R16，黑现在能回到哪里？", "看黑 63", "capture"),
    "capture": ("黑在 C4 提回一次。请替白走一手，提掉右上 R17。", "", None),
    "cost": ("白 S17 提掉了黑 R17。黑换得一次回提，左下的劫还在。", "回白 60 总结", "start"),
}


def describe(node, summary=False):
    step = node.get_property("KAGSTEP")
    if step == "start" and summary:
        return "为什么先看左下？去右上换来了什么，又付出了什么？", "再摆一次", "local"
    if step in STEPS:
        return STEPS[step]
    parent = node.parent.get_property("KAGSTEP") if node.parent else None
    if parent == "try":
        return "你摆出了自己的走法。现在可以核对引擎变化。", "看黑 D6", "compare"
    if parent == "capture":
        return "黑 R17 还在。再数一下它的气。", "回黑 63 再试", "capture"
    return "从白 60 后的劫争开始。", "定位白 60", "start"


def destination(node):
    target = describe(node)[2]
    if not target:
        return None
    return next((n for n in node.root.nodes_in_tree if n.get_property("KAGSTEP") == target), None)
