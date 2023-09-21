from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AskRequest(_message.Message):
    __slots__ = ["question", "companyCode", "productCode"]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    COMPANYCODE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODE_FIELD_NUMBER: _ClassVar[int]
    question: str
    companyCode: str
    productCode: str
    def __init__(self, question: _Optional[str] = ..., companyCode: _Optional[str] = ..., productCode: _Optional[str] = ...) -> None: ...

class AskReply(_message.Message):
    __slots__ = ["content", "answer"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    content: str
    answer: str
    def __init__(self, content: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...
