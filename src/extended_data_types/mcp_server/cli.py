import argparse

from .server import ExtendedDataTypesMCP

def main():
    """CLI entry point for the MCP server."""
    parser = argparse.ArgumentParser(description="Extended Data Types MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="The transport protocol to use.",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Host for HTTP server.")
    parser.add_argument("--port", type=int, default=8080, help="Port for HTTP server.")
    args = parser.parse_args()

    server = ExtendedDataTypesMCP()
    server.run(transport=args.transport, host=args.host, port=args.port)

if __name__ == "__main__":
    main()
