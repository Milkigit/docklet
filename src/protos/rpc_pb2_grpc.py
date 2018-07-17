# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import rpc_pb2 as protos_dot_rpc__pb2


class MasterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.report = channel.unary_unary(
        '/Master/report',
        request_serializer=protos_dot_rpc__pb2.Task.SerializeToString,
        response_deserializer=protos_dot_rpc__pb2.Reply.FromString,
        )


class MasterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def report(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MasterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'report': grpc.unary_unary_rpc_method_handler(
          servicer.report,
          request_deserializer=protos_dot_rpc__pb2.Task.FromString,
          response_serializer=protos_dot_rpc__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Master', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class WorkerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add_task = channel.unary_unary(
        '/Worker/add_task',
        request_serializer=protos_dot_rpc__pb2.Task.SerializeToString,
        response_deserializer=protos_dot_rpc__pb2.Reply.FromString,
        )


class WorkerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def add_task(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add_task': grpc.unary_unary_rpc_method_handler(
          servicer.add_task,
          request_deserializer=protos_dot_rpc__pb2.Task.FromString,
          response_serializer=protos_dot_rpc__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Worker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
