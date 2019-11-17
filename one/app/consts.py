from enum import Enum


class MsgType(Enum):
    info = "info"
    warning = "warning"
    error = "error"
    danger = "danger"


MsgType.info.label = "信息"
MsgType.warning.label = "警告"
MsgType.error.label = "错误"
MsgType.danger.label = "危险"


MsgType.info.color = "green"
MsgType.warning.color = "orange"
MsgType.error.color = "grey"
MsgType.danger.color = "red"


SensitiveWord = ["天气", "坏人", "不开心"]

