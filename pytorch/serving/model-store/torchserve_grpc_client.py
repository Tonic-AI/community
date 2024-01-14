# Copyright (c) 2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
#
# This file was assembled from multiple pieces, whose use is documented
# throughout. Please refer to the TensorFlow dockerfiles documentation
# for more information.
# based on https://github.com/pytorch/pytorch/blob/master/Dockerfile
#
# NOTE: To build this you will need a docker version >= 19.03 and DOCKER_BUILDKIT=1
#
#       If you do not use buildkit you are not going to have a good time
#
#       For reference:
#           https://docs.docker.com/develop/develop-images/build_enhancements/

import argparse

import grpc
import inference_pb2
import inference_pb2_grpc
import management_pb2
import management_pb2_grpc


def get_inference_stub():
    channel = grpc.insecure_channel("localhost:7070")
    stub = inference_pb2_grpc.InferenceAPIsServiceStub(channel)
    return stub


def get_management_stub():
    channel = grpc.insecure_channel("localhost:7071")
    stub = management_pb2_grpc.ManagementAPIsServiceStub(channel)
    return stub


def infer(stub, model_name, model_input, metadata):
    with open(model_input, "rb") as f:
        data = f.read()

    input_data = {"data": data}
    response = stub.Predictions(
        inference_pb2.PredictionsRequest(model_name=model_name, input=input_data),
        metadata=metadata,
    )

    try:
        prediction = response.prediction.decode("utf-8")
        print(prediction)
    except grpc.RpcError as e:
        exit(1)


def infer_stream(stub, model_name, model_input, metadata):
    with open(model_input, "rb") as f:
        data = f.read()

    input_data = {"data": data}
    responses = stub.StreamPredictions(
        inference_pb2.PredictionsRequest(model_name=model_name, input=input_data),
        metadata=metadata,
    )

    try:
        for resp in responses:
            prediction = resp.prediction.decode("utf-8")
            print(prediction)
    except grpc.RpcError as e:
        exit(1)


def register(stub, model_name, mar_set_str):
    mar_set = set()
    if mar_set_str:
        mar_set = set(mar_set_str.split(","))
    marfile = f"{model_name}.mar"
    print(f"## Check {marfile} in mar_set :", mar_set)
    if marfile not in mar_set:
        marfile = "https://torchserve.s3.amazonaws.com/mar_files/{}.mar".format(
            model_name
        )

    print(f"## Register marfile: {marfile}\n")
    params = {
        "url": marfile,
        "initial_workers": 1,
        "synchronous": True,
        "model_name": model_name,
    }
    try:
        response = stub.RegisterModel(management_pb2.RegisterModelRequest(**params))
        print(f"Model {model_name} registered successfully")
    except grpc.RpcError as e:
        print(f"Failed to register model {model_name}.")
        print(str(e.details()))
        exit(1)


def unregister(stub, model_name):
    try:
        response = stub.UnregisterModel(
            management_pb2.UnregisterModelRequest(model_name=model_name)
        )
        print(f"Model {model_name} unregistered successfully")
    except grpc.RpcError as e:
        print(f"Failed to unregister model {model_name}.")
        print(str(e.details()))
        exit(1)


if __name__ == "__main__":
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "model_name",
        type=str,
        default=None,
        help="Name of the model used.",
    )

    parser = argparse.ArgumentParser(
        description="TorchServe gRPC client",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(help="Action", dest="action")

    infer_action_parser = subparsers.add_parser(
        "infer", parents=[parent_parser], add_help=False
    )
    infer_stream_action_parser = subparsers.add_parser(
        "infer_stream", parents=[parent_parser], add_help=False
    )
    register_action_parser = subparsers.add_parser(
        "register", parents=[parent_parser], add_help=False
    )
    unregister_action_parser = subparsers.add_parser(
        "unregister", parents=[parent_parser], add_help=False
    )

    infer_action_parser.add_argument(
        "model_input", type=str, default=None, help="Input for model for inferencing."
    )

    infer_stream_action_parser.add_argument(
        "model_input",
        type=str,
        default=None,
        help="Input for model for stream inferencing.",
    )

    register_action_parser.add_argument(
        "mar_set",
        type=str,
        default=None,
        nargs="?",
        help="Comma separated list of mar models to be loaded using [model_name=]model_location format.",
    )

    args = parser.parse_args()

    metadata = (("protocol", "gRPC"), ("session_id", "12345"))

    if args.action == "infer":
        infer(get_inference_stub(), args.model_name, args.model_input, metadata)
    elif args.action == "infer_stream":
        infer_stream(get_inference_stub(), args.model_name, args.model_input, metadata)
    elif args.action == "register":
        register(get_management_stub(), args.model_name, args.mar_set)
    elif args.action == "unregister":
        unregister(get_management_stub(), args.model_name)
