
def start_listening_thread():
    """Starts the listening process in a separate thread."""
    listening_thread = threading.Thread(target=start_listening)
    listening_thread.start()