# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cworker.proto\x12\x06worker\"\xb5\x01\n\x04Task\x12(\n\ttask_type\x18\x01 \x01(\x0e\x32\x15.worker.Task.TaskType\x12\x12\n\ninput_path\x18\x02 \x01(\t\x12\x13\n\x0boutput_path\x18\x03 \x01(\t\x12\x15\n\rfunction_name\x18\x04 \x01(\t\x12\x15\n\rfunction_code\x18\x05 \x01(\t\",\n\x08TaskType\x12\x07\n\x03MAP\x10\x00\x12\x0b\n\x07SHUFFLE\x10\x01\x12\n\n\x06REDUCE\x10\x02\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"Y\n\x06Status\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.worker.Status.WorkerStatus\"\"\n\x0cWorkerStatus\x12\x08\n\x04IDLE\x10\x00\x12\x08\n\x04\x42USY\x10\x01\"\x07\n\x05\x45mpty2e\n\x06Worker\x12-\n\nAssignTask\x12\x0c.worker.Task\x1a\x0f.worker.Message\"\x00\x12,\n\tGetStatus\x12\r.worker.Empty\x1a\x0e.worker.Status\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'worker_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TASK']._serialized_start=25
  _globals['_TASK']._serialized_end=206
  _globals['_TASK_TASKTYPE']._serialized_start=162
  _globals['_TASK_TASKTYPE']._serialized_end=206
  _globals['_MESSAGE']._serialized_start=208
  _globals['_MESSAGE']._serialized_end=234
  _globals['_STATUS']._serialized_start=236
  _globals['_STATUS']._serialized_end=325
  _globals['_STATUS_WORKERSTATUS']._serialized_start=291
  _globals['_STATUS_WORKERSTATUS']._serialized_end=325
  _globals['_EMPTY']._serialized_start=327
  _globals['_EMPTY']._serialized_end=334
  _globals['_WORKER']._serialized_start=336
  _globals['_WORKER']._serialized_end=437
# @@protoc_insertion_point(module_scope)
