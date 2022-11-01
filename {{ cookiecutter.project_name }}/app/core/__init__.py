from uvicorn.workers import UvicornWorker


class CustomUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "loop": "auto",
        "http": "auto",
        "ws_ping_interval": 300,
        "ws_ping_timeout": 300,
        "timeout_keep_alive": 60,
        "ws_max_size": 4096,
    }
