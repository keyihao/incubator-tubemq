#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RPC.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RPC.proto',
  package='',
  serialized_pb='\n\tRPC.proto\"P\n\rRpcConnHeader\x12\x0c\n\x04\x66lag\x18\x01 \x02(\x05\x12\x0f\n\x07traceId\x18\x02 \x01(\x03\x12\x0e\n\x06spanId\x18\x03 \x01(\x03\x12\x10\n\x08parentId\x18\x04 \x01(\x03\"9\n\rRequestHeader\x12\x13\n\x0bserviceType\x18\x01 \x01(\x05\x12\x13\n\x0bprotocolVer\x18\x02 \x01(\x05\"?\n\x0bRequestBody\x12\x0e\n\x06method\x18\x01 \x02(\x05\x12\x0f\n\x07timeout\x18\x02 \x01(\x03\x12\x0f\n\x07request\x18\x03 \x01(\x0c\"\x8f\x01\n\x0eResponseHeader\x12&\n\x06status\x18\x01 \x02(\x0e\x32\x16.ResponseHeader.Status\x12\x13\n\x0bserviceType\x18\x02 \x01(\x05\x12\x13\n\x0bprotocolVer\x18\x03 \x01(\x05\"+\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\t\n\x05\x46\x41TAL\x10\x02\"=\n\x10RspExceptionBody\x12\x15\n\rexceptionName\x18\x01 \x02(\t\x12\x12\n\nstackTrace\x18\x02 \x01(\t\"/\n\x0fRspResponseBody\x12\x0e\n\x06method\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\x42?\n-org.apache.tubemq.corebase.protobuf.generatedB\tRPCProtosH\x01\xa0\x01\x01')



_RESPONSEHEADER_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ResponseHeader.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=320,
  serialized_end=363,
)


_RPCCONNHEADER = _descriptor.Descriptor(
  name='RpcConnHeader',
  full_name='RpcConnHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag', full_name='RpcConnHeader.flag', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traceId', full_name='RpcConnHeader.traceId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spanId', full_name='RpcConnHeader.spanId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parentId', full_name='RpcConnHeader.parentId', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=13,
  serialized_end=93,
)


_REQUESTHEADER = _descriptor.Descriptor(
  name='RequestHeader',
  full_name='RequestHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serviceType', full_name='RequestHeader.serviceType', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocolVer', full_name='RequestHeader.protocolVer', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=95,
  serialized_end=152,
)


_REQUESTBODY = _descriptor.Descriptor(
  name='RequestBody',
  full_name='RequestBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='RequestBody.method', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='RequestBody.timeout', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='RequestBody.request', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=154,
  serialized_end=217,
)


_RESPONSEHEADER = _descriptor.Descriptor(
  name='ResponseHeader',
  full_name='ResponseHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ResponseHeader.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serviceType', full_name='ResponseHeader.serviceType', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocolVer', full_name='ResponseHeader.protocolVer', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSEHEADER_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=220,
  serialized_end=363,
)


_RSPEXCEPTIONBODY = _descriptor.Descriptor(
  name='RspExceptionBody',
  full_name='RspExceptionBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exceptionName', full_name='RspExceptionBody.exceptionName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stackTrace', full_name='RspExceptionBody.stackTrace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=365,
  serialized_end=426,
)


_RSPRESPONSEBODY = _descriptor.Descriptor(
  name='RspResponseBody',
  full_name='RspResponseBody',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='RspResponseBody.method', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='RspResponseBody.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=428,
  serialized_end=475,
)

_RESPONSEHEADER.fields_by_name['status'].enum_type = _RESPONSEHEADER_STATUS
_RESPONSEHEADER_STATUS.containing_type = _RESPONSEHEADER;
DESCRIPTOR.message_types_by_name['RpcConnHeader'] = _RPCCONNHEADER
DESCRIPTOR.message_types_by_name['RequestHeader'] = _REQUESTHEADER
DESCRIPTOR.message_types_by_name['RequestBody'] = _REQUESTBODY
DESCRIPTOR.message_types_by_name['ResponseHeader'] = _RESPONSEHEADER
DESCRIPTOR.message_types_by_name['RspExceptionBody'] = _RSPEXCEPTIONBODY
DESCRIPTOR.message_types_by_name['RspResponseBody'] = _RSPRESPONSEBODY

class RpcConnHeader(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RPCCONNHEADER

  # @@protoc_insertion_point(class_scope:RpcConnHeader)

class RequestHeader(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTHEADER

  # @@protoc_insertion_point(class_scope:RequestHeader)

class RequestBody(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTBODY

  # @@protoc_insertion_point(class_scope:RequestBody)

class ResponseHeader(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEHEADER

  # @@protoc_insertion_point(class_scope:ResponseHeader)

class RspExceptionBody(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPEXCEPTIONBODY

  # @@protoc_insertion_point(class_scope:RspExceptionBody)

class RspResponseBody(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RSPRESPONSEBODY

  # @@protoc_insertion_point(class_scope:RspResponseBody)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n-org.apache.tubemq.corebase.protobuf.generatedB\tRPCProtosH\001\240\001\001')
# @@protoc_insertion_point(module_scope)
