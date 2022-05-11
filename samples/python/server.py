"""The Python implementation of the gRPC Uggly server."""

from concurrent import futures
import logging
from operator import contains
from textwrap import fill

import grpc
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'uggly', 'python'))
import uggly
import uggly_pb2_grpc

def style(fg,bg):
    return uggly.Style(fg=fg,bg=bg,attr="4")

class PageServicer(uggly_pb2_grpc.PageServicer):
    """Provides methods that implement functionality of Page server."""

    def GetPage(self, request: uggly.PageRequest, context) -> uggly.PageResponse:
        presp = uggly.PageResponse()
        presp.div_boxes.boxes.append(uggly.DivBox(
            name="hello-world-div",
            width=20,
            height=10,
            start_x=10,
            start_y=10,
            fill_st=style("blue","darkgrey"),
            fill_char=ord("_"),
        ))
        tb = uggly.TextBlob(
            content="hello world",
            style=style("red","darkgrey"),
        )
        tb.div_names.append("hello-world-div")
        presp.elements.text_blobs.append(tb)
        return presp
        

class FeedServicer(uggly_pb2_grpc.FeedServicer):
    """Provides methods that implement functionality of Feed server."""

    def GetFeed(self, feedRequest: uggly.FeedRequest, context) -> uggly.FeedResponse:
        fresp = uggly.FeedResponse()
        logging.info(feedRequest)
        fresp.pages.append(uggly.PageListing("home"))
        return fresp


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    uggly_pb2_grpc.add_PageServicer_to_server(
        PageServicer(), server)
    uggly_pb2_grpc.add_FeedServicer_to_server(
        FeedServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    serve()
