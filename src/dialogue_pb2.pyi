from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Content(_message.Message):
    __slots__ = ["id", "content", "time"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    time: str
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., time: _Optional[str] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["id", "text", "type", "time"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    text: str
    type: str
    time: str
    def __init__(self, id: _Optional[str] = ..., text: _Optional[str] = ..., type: _Optional[str] = ..., time: _Optional[str] = ...) -> None: ...

class Conversation(_message.Message):
    __slots__ = ["id", "message", "content", "messageHistory"]
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGEHISTORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    message: Message
    content: _containers.RepeatedCompositeFieldContainer[Content]
    messageHistory: _containers.RepeatedCompositeFieldContainer[Message]
    def __init__(self, id: _Optional[str] = ..., message: _Optional[_Union[Message, _Mapping]] = ..., content: _Optional[_Iterable[_Union[Content, _Mapping]]] = ..., messageHistory: _Optional[_Iterable[_Union[Message, _Mapping]]] = ...) -> None: ...
