import debugpy

debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()