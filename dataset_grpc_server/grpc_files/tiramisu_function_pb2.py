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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17tiramisu_function.proto\x12\x12tiramisudataserver\"$\n\x14TiramisuFunctionName\x12\x0c\n\x04name\x18\x01 \x01(\t\"O\n\x10TiramisuFunction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0b\n\x03\x63pp\x18\x03 \x01(\t\x12\x0f\n\x07wrapper\x18\x04 \x01(\x0c\"\x1b\n\x0b\x44\x61tasetSize\x12\x0c\n\x04size\x18\x01 \x01(\x03\"\x07\n\x05\x45mpty\"(\n\x17TiramisuListOfFunctions\x12\r\n\x05names\x18\x01 \x03(\t2\x97\x03\n\x12TiramisuDataServer\x12g\n\x13GetTiramisuFunction\x12(.tiramisudataserver.TiramisuFunctionName\x1a$.tiramisudataserver.TiramisuFunction\"\x00\x12h\n\x14SaveTiramisuFunction\x12$.tiramisudataserver.TiramisuFunction\x1a(.tiramisudataserver.TiramisuFunctionName\"\x00\x12N\n\x0eGetDatasetSize\x12\x19.tiramisudataserver.Empty\x1a\x1f.tiramisudataserver.DatasetSize\"\x00\x12^\n\x12GetListOfFunctions\x12\x19.tiramisudataserver.Empty\x1a+.tiramisudataserver.TiramisuListOfFunctions\"\x00\x42\x06\xa2\x02\x03TDSb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tiramisu_function_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\242\002\003TDS'
  _globals['_TIRAMISUFUNCTIONNAME']._serialized_start=47
  _globals['_TIRAMISUFUNCTIONNAME']._serialized_end=83
  _globals['_TIRAMISUFUNCTION']._serialized_start=85
  _globals['_TIRAMISUFUNCTION']._serialized_end=164
  _globals['_DATASETSIZE']._serialized_start=166
  _globals['_DATASETSIZE']._serialized_end=193
  _globals['_EMPTY']._serialized_start=195
  _globals['_EMPTY']._serialized_end=202
  _globals['_TIRAMISULISTOFFUNCTIONS']._serialized_start=204
  _globals['_TIRAMISULISTOFFUNCTIONS']._serialized_end=244
  _globals['_TIRAMISUDATASERVER']._serialized_start=247
  _globals['_TIRAMISUDATASERVER']._serialized_end=654
# @@protoc_insertion_point(module_scope)
