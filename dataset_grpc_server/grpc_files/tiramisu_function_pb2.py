# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tiramisu_function.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17tiramisu_function.proto\x12\x12tiramisudataserver\"$\n\x14TiramisuFunctionName\x12\x0c\n\x04name\x18\x01 \x01(\t\"=\n\x0fTiramisuFuction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0b\n\x03\x63pp\x18\x03 \x01(\t2|\n\x12TiramisuDataServer\x12\x66\n\x13GetTiramisuFunction\x12(.tiramisudataserver.TiramisuFunctionName\x1a#.tiramisudataserver.TiramisuFuction\"\x00\x42\x06\xa2\x02\x03TDSb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tiramisu_function_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\242\002\003TDS'
  _globals['_TIRAMISUFUNCTIONNAME']._serialized_start=47
  _globals['_TIRAMISUFUNCTIONNAME']._serialized_end=83
  _globals['_TIRAMISUFUCTION']._serialized_start=85
  _globals['_TIRAMISUFUCTION']._serialized_end=146
  _globals['_TIRAMISUDATASERVER']._serialized_start=148
  _globals['_TIRAMISUDATASERVER']._serialized_end=272
# @@protoc_insertion_point(module_scope)
