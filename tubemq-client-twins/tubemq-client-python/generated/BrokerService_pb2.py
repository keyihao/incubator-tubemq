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
# source: BrokerService.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BrokerService.proto',
  package='',
  serialized_pb='\n\x13\x42rokerService.proto\"[\n\x11TransferedMessage\x12\x11\n\tmessageId\x18\x01 \x02(\x03\x12\x10\n\x08\x63heckSum\x18\x02 \x02(\x05\x12\x13\n\x0bpayLoadData\x18\x03 \x02(\x0c\x12\x0c\n\x04\x66lag\x18\x04 \x02(\x05\"K\n\x0e\x41uthorizedInfo\x12\x1c\n\x14visitAuthorizedToken\x18\x01 \x02(\x03\x12\x1b\n\x13\x61uthAuthorizedToken\x18\x02 \x01(\t\"\xd6\x01\n\x15SendMessageRequestP2B\x12\x10\n\x08\x63lientId\x18\x01 \x02(\t\x12\x11\n\ttopicName\x18\x02 \x02(\t\x12\x13\n\x0bpartitionId\x18\x03 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x02(\x0c\x12\x0c\n\x04\x66lag\x18\x05 \x02(\x05\x12\x10\n\x08\x63heckSum\x18\x06 \x02(\x05\x12\x10\n\x08sentAddr\x18\x07 \x02(\x05\x12\x0f\n\x07msgType\x18\x08 \x01(\t\x12\x0f\n\x07msgTime\x18\t \x01(\t\x12!\n\x08\x61uthInfo\x18\n \x01(\x0b\x32\x0f.AuthorizedInfo\"_\n\x16SendMessageResponseB2P\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rrCode\x18\x02 \x02(\x05\x12\x0e\n\x06\x65rrMsg\x18\x03 \x02(\t\x12\x13\n\x0brequireAuth\x18\x04 \x01(\x08\"\xa7\x02\n\x12RegisterRequestC2B\x12\x0e\n\x06opType\x18\x01 \x02(\x05\x12\x10\n\x08\x63lientId\x18\x02 \x02(\t\x12\x11\n\tgroupName\x18\x03 \x02(\t\x12\x11\n\ttopicName\x18\x04 \x02(\t\x12\x13\n\x0bpartitionId\x18\x05 \x02(\x05\x12\x12\n\nreadStatus\x18\x06 \x02(\x05\x12\x15\n\rfilterCondStr\x18\x07 \x03(\t\x12\x12\n\ncurrOffset\x18\x08 \x01(\x03\x12\x12\n\nsessionKey\x18\t \x01(\t\x12\x13\n\x0bsessionTime\x18\n \x01(\x03\x12\x12\n\nssdStoreId\x18\x0b \x01(\x03\x12\x15\n\rqryPriorityId\x18\x0c \x01(\x05\x12!\n\x08\x61uthInfo\x18\r \x01(\x0b\x32\x0f.AuthorizedInfo\"[\n\x13RegisterResponseB2C\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rrCode\x18\x02 \x02(\x05\x12\x0e\n\x06\x65rrMsg\x18\x03 \x02(\t\x12\x12\n\ncurrOffset\x18\x04 \x01(\x03\"\xb3\x01\n\x13HeartBeatRequestC2B\x12\x10\n\x08\x63lientId\x18\x01 \x02(\t\x12\x11\n\tgroupName\x18\x02 \x02(\t\x12\x12\n\nreadStatus\x18\x03 \x02(\x05\x12\x15\n\rpartitionInfo\x18\x04 \x03(\t\x12\x12\n\nssdStoreId\x18\x05 \x01(\x03\x12\x15\n\rqryPriorityId\x18\x06 \x01(\x05\x12!\n\x08\x61uthInfo\x18\x07 \x01(\x0b\x32\x0f.AuthorizedInfo\"\x8a\x01\n\x14HeartBeatResponseB2C\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rrCode\x18\x02 \x02(\x05\x12\x0e\n\x06\x65rrMsg\x18\x03 \x02(\t\x12\x16\n\x0ehasPartFailure\x18\x04 \x01(\x08\x12\x13\n\x0b\x66\x61ilureInfo\x18\x05 \x03(\t\x12\x13\n\x0brequireAuth\x18\x06 \x01(\x08\"\xae\x01\n\x14GetMessageRequestC2B\x12\x10\n\x08\x63lientId\x18\x01 \x02(\t\x12\x13\n\x0bpartitionId\x18\x02 \x02(\x05\x12\x11\n\tgroupName\x18\x03 \x02(\t\x12\x11\n\ttopicName\x18\x04 \x02(\t\x12\x18\n\x10lastPackConsumed\x18\x05 \x01(\x08\x12\x1a\n\x12manualCommitOffset\x18\x06 \x01(\x08\x12\x13\n\x0b\x65scFlowCtrl\x18\x07 \x01(\x08\"\xd8\x01\n\x15GetMessageResponseB2C\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rrCode\x18\x02 \x02(\x05\x12\x0e\n\x06\x65rrMsg\x18\x03 \x01(\t\x12$\n\x08messages\x18\x04 \x03(\x0b\x32\x12.TransferedMessage\x12\x12\n\ncurrOffset\x18\x05 \x01(\x03\x12\x14\n\x0cminLimitTime\x18\x06 \x01(\x05\x12\x13\n\x0b\x65scFlowCtrl\x18\x07 \x01(\x08\x12\x13\n\x0b\x63urrDataDlt\x18\x08 \x01(\x03\x12\x13\n\x0brequireSlow\x18\t \x01(\x08\"\x7f\n\x16\x43ommitOffsetRequestC2B\x12\x10\n\x08\x63lientId\x18\x01 \x02(\t\x12\x11\n\ttopicName\x18\x02 \x02(\t\x12\x13\n\x0bpartitionId\x18\x03 \x02(\x05\x12\x11\n\tgroupName\x18\x04 \x02(\t\x12\x18\n\x10lastPackConsumed\x18\x05 \x01(\x08\"_\n\x17\x43ommitOffsetResponseB2C\x12\x0f\n\x07success\x18\x01 \x02(\x08\x12\x0f\n\x07\x65rrCode\x18\x02 \x02(\x05\x12\x0e\n\x06\x65rrMsg\x18\x03 \x02(\t\x12\x12\n\ncurrOffset\x18\x04 \x01(\x03\x42\x45\n-org.apache.tubemq.corebase.protobuf.generatedB\x0c\x43lientBrokerH\x01\x88\x01\x01\xa0\x01\x01')




_TRANSFEREDMESSAGE = _descriptor.Descriptor(
  name='TransferedMessage',
  full_name='TransferedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageId', full_name='TransferedMessage.messageId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkSum', full_name='TransferedMessage.checkSum', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payLoadData', full_name='TransferedMessage.payLoadData', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='TransferedMessage.flag', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=23,
  serialized_end=114,
)


_AUTHORIZEDINFO = _descriptor.Descriptor(
  name='AuthorizedInfo',
  full_name='AuthorizedInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='visitAuthorizedToken', full_name='AuthorizedInfo.visitAuthorizedToken', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authAuthorizedToken', full_name='AuthorizedInfo.authAuthorizedToken', index=1,
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
  serialized_start=116,
  serialized_end=191,
)


_SENDMESSAGEREQUESTP2B = _descriptor.Descriptor(
  name='SendMessageRequestP2B',
  full_name='SendMessageRequestP2B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='SendMessageRequestP2B.clientId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topicName', full_name='SendMessageRequestP2B.topicName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partitionId', full_name='SendMessageRequestP2B.partitionId', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='SendMessageRequestP2B.data', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='SendMessageRequestP2B.flag', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checkSum', full_name='SendMessageRequestP2B.checkSum', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sentAddr', full_name='SendMessageRequestP2B.sentAddr', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msgType', full_name='SendMessageRequestP2B.msgType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msgTime', full_name='SendMessageRequestP2B.msgTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authInfo', full_name='SendMessageRequestP2B.authInfo', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=194,
  serialized_end=408,
)


_SENDMESSAGERESPONSEB2P = _descriptor.Descriptor(
  name='SendMessageResponseB2P',
  full_name='SendMessageResponseB2P',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='SendMessageResponseB2P.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='SendMessageResponseB2P.errCode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errMsg', full_name='SendMessageResponseB2P.errMsg', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requireAuth', full_name='SendMessageResponseB2P.requireAuth', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=410,
  serialized_end=505,
)


_REGISTERREQUESTC2B = _descriptor.Descriptor(
  name='RegisterRequestC2B',
  full_name='RegisterRequestC2B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opType', full_name='RegisterRequestC2B.opType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='RegisterRequestC2B.clientId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groupName', full_name='RegisterRequestC2B.groupName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topicName', full_name='RegisterRequestC2B.topicName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partitionId', full_name='RegisterRequestC2B.partitionId', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readStatus', full_name='RegisterRequestC2B.readStatus', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filterCondStr', full_name='RegisterRequestC2B.filterCondStr', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currOffset', full_name='RegisterRequestC2B.currOffset', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sessionKey', full_name='RegisterRequestC2B.sessionKey', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sessionTime', full_name='RegisterRequestC2B.sessionTime', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssdStoreId', full_name='RegisterRequestC2B.ssdStoreId', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qryPriorityId', full_name='RegisterRequestC2B.qryPriorityId', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authInfo', full_name='RegisterRequestC2B.authInfo', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=508,
  serialized_end=803,
)


_REGISTERRESPONSEB2C = _descriptor.Descriptor(
  name='RegisterResponseB2C',
  full_name='RegisterResponseB2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='RegisterResponseB2C.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='RegisterResponseB2C.errCode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errMsg', full_name='RegisterResponseB2C.errMsg', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currOffset', full_name='RegisterResponseB2C.currOffset', index=3,
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
  serialized_start=805,
  serialized_end=896,
)


_HEARTBEATREQUESTC2B = _descriptor.Descriptor(
  name='HeartBeatRequestC2B',
  full_name='HeartBeatRequestC2B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='HeartBeatRequestC2B.clientId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groupName', full_name='HeartBeatRequestC2B.groupName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readStatus', full_name='HeartBeatRequestC2B.readStatus', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partitionInfo', full_name='HeartBeatRequestC2B.partitionInfo', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssdStoreId', full_name='HeartBeatRequestC2B.ssdStoreId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qryPriorityId', full_name='HeartBeatRequestC2B.qryPriorityId', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authInfo', full_name='HeartBeatRequestC2B.authInfo', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=899,
  serialized_end=1078,
)


_HEARTBEATRESPONSEB2C = _descriptor.Descriptor(
  name='HeartBeatResponseB2C',
  full_name='HeartBeatResponseB2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='HeartBeatResponseB2C.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='HeartBeatResponseB2C.errCode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errMsg', full_name='HeartBeatResponseB2C.errMsg', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasPartFailure', full_name='HeartBeatResponseB2C.hasPartFailure', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failureInfo', full_name='HeartBeatResponseB2C.failureInfo', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requireAuth', full_name='HeartBeatResponseB2C.requireAuth', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1081,
  serialized_end=1219,
)


_GETMESSAGEREQUESTC2B = _descriptor.Descriptor(
  name='GetMessageRequestC2B',
  full_name='GetMessageRequestC2B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='GetMessageRequestC2B.clientId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partitionId', full_name='GetMessageRequestC2B.partitionId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groupName', full_name='GetMessageRequestC2B.groupName', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topicName', full_name='GetMessageRequestC2B.topicName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastPackConsumed', full_name='GetMessageRequestC2B.lastPackConsumed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manualCommitOffset', full_name='GetMessageRequestC2B.manualCommitOffset', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escFlowCtrl', full_name='GetMessageRequestC2B.escFlowCtrl', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1222,
  serialized_end=1396,
)


_GETMESSAGERESPONSEB2C = _descriptor.Descriptor(
  name='GetMessageResponseB2C',
  full_name='GetMessageResponseB2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='GetMessageResponseB2C.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='GetMessageResponseB2C.errCode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errMsg', full_name='GetMessageResponseB2C.errMsg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages', full_name='GetMessageResponseB2C.messages', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currOffset', full_name='GetMessageResponseB2C.currOffset', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minLimitTime', full_name='GetMessageResponseB2C.minLimitTime', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='escFlowCtrl', full_name='GetMessageResponseB2C.escFlowCtrl', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currDataDlt', full_name='GetMessageResponseB2C.currDataDlt', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requireSlow', full_name='GetMessageResponseB2C.requireSlow', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1399,
  serialized_end=1615,
)


_COMMITOFFSETREQUESTC2B = _descriptor.Descriptor(
  name='CommitOffsetRequestC2B',
  full_name='CommitOffsetRequestC2B',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientId', full_name='CommitOffsetRequestC2B.clientId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topicName', full_name='CommitOffsetRequestC2B.topicName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partitionId', full_name='CommitOffsetRequestC2B.partitionId', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groupName', full_name='CommitOffsetRequestC2B.groupName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastPackConsumed', full_name='CommitOffsetRequestC2B.lastPackConsumed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1617,
  serialized_end=1744,
)


_COMMITOFFSETRESPONSEB2C = _descriptor.Descriptor(
  name='CommitOffsetResponseB2C',
  full_name='CommitOffsetResponseB2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='CommitOffsetResponseB2C.success', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='CommitOffsetResponseB2C.errCode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='errMsg', full_name='CommitOffsetResponseB2C.errMsg', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currOffset', full_name='CommitOffsetResponseB2C.currOffset', index=3,
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
  serialized_start=1746,
  serialized_end=1841,
)

_SENDMESSAGEREQUESTP2B.fields_by_name['authInfo'].message_type = _AUTHORIZEDINFO
_REGISTERREQUESTC2B.fields_by_name['authInfo'].message_type = _AUTHORIZEDINFO
_HEARTBEATREQUESTC2B.fields_by_name['authInfo'].message_type = _AUTHORIZEDINFO
_GETMESSAGERESPONSEB2C.fields_by_name['messages'].message_type = _TRANSFEREDMESSAGE
DESCRIPTOR.message_types_by_name['TransferedMessage'] = _TRANSFEREDMESSAGE
DESCRIPTOR.message_types_by_name['AuthorizedInfo'] = _AUTHORIZEDINFO
DESCRIPTOR.message_types_by_name['SendMessageRequestP2B'] = _SENDMESSAGEREQUESTP2B
DESCRIPTOR.message_types_by_name['SendMessageResponseB2P'] = _SENDMESSAGERESPONSEB2P
DESCRIPTOR.message_types_by_name['RegisterRequestC2B'] = _REGISTERREQUESTC2B
DESCRIPTOR.message_types_by_name['RegisterResponseB2C'] = _REGISTERRESPONSEB2C
DESCRIPTOR.message_types_by_name['HeartBeatRequestC2B'] = _HEARTBEATREQUESTC2B
DESCRIPTOR.message_types_by_name['HeartBeatResponseB2C'] = _HEARTBEATRESPONSEB2C
DESCRIPTOR.message_types_by_name['GetMessageRequestC2B'] = _GETMESSAGEREQUESTC2B
DESCRIPTOR.message_types_by_name['GetMessageResponseB2C'] = _GETMESSAGERESPONSEB2C
DESCRIPTOR.message_types_by_name['CommitOffsetRequestC2B'] = _COMMITOFFSETREQUESTC2B
DESCRIPTOR.message_types_by_name['CommitOffsetResponseB2C'] = _COMMITOFFSETRESPONSEB2C

class TransferedMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSFEREDMESSAGE

  # @@protoc_insertion_point(class_scope:TransferedMessage)

class AuthorizedInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUTHORIZEDINFO

  # @@protoc_insertion_point(class_scope:AuthorizedInfo)

class SendMessageRequestP2B(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDMESSAGEREQUESTP2B

  # @@protoc_insertion_point(class_scope:SendMessageRequestP2B)

class SendMessageResponseB2P(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SENDMESSAGERESPONSEB2P

  # @@protoc_insertion_point(class_scope:SendMessageResponseB2P)

class RegisterRequestC2B(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERREQUESTC2B

  # @@protoc_insertion_point(class_scope:RegisterRequestC2B)

class RegisterResponseB2C(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REGISTERRESPONSEB2C

  # @@protoc_insertion_point(class_scope:RegisterResponseB2C)

class HeartBeatRequestC2B(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEARTBEATREQUESTC2B

  # @@protoc_insertion_point(class_scope:HeartBeatRequestC2B)

class HeartBeatResponseB2C(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEARTBEATRESPONSEB2C

  # @@protoc_insertion_point(class_scope:HeartBeatResponseB2C)

class GetMessageRequestC2B(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMESSAGEREQUESTC2B

  # @@protoc_insertion_point(class_scope:GetMessageRequestC2B)

class GetMessageResponseB2C(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETMESSAGERESPONSEB2C

  # @@protoc_insertion_point(class_scope:GetMessageResponseB2C)

class CommitOffsetRequestC2B(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMITOFFSETREQUESTC2B

  # @@protoc_insertion_point(class_scope:CommitOffsetRequestC2B)

class CommitOffsetResponseB2C(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMITOFFSETRESPONSEB2C

  # @@protoc_insertion_point(class_scope:CommitOffsetResponseB2C)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n-org.apache.tubemq.corebase.protobuf.generatedB\014ClientBrokerH\001\210\001\001\240\001\001')
# @@protoc_insertion_point(module_scope)
