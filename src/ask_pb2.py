# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ask.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\task.proto\x12\x04\x64\x65mo\"H\n\nAskRequest\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x13\n\x0b\x63ompanyCode\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\"+\n\x08\x41skReply\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x02 \x01(\t2\xa3\x01\n\x05\x41sker\x12)\n\x03\x41sk\x12\x10.demo.AskRequest\x1a\x0e.demo.AskReply\"\x00\x12\x36\n\x0e\x41skStreamReply\x12\x10.demo.AskRequest\x1a\x0e.demo.AskReply\"\x00\x30\x01\x12\x37\n\rAskBidiStream\x12\x10.demo.AskRequest\x1a\x0e.demo.AskReply\"\x00(\x01\x30\x01\x42&\n\x10io.grpc.demo.askB\nAskerProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ask_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020io.grpc.demo.askB\nAskerProtoP\001\242\002\003HLW'
  _globals['_ASKREQUEST']._serialized_start=19
  _globals['_ASKREQUEST']._serialized_end=91
  _globals['_ASKREPLY']._serialized_start=93
  _globals['_ASKREPLY']._serialized_end=136
  _globals['_ASKER']._serialized_start=139
  _globals['_ASKER']._serialized_end=302
# @@protoc_insertion_point(module_scope)
