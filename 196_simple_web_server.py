"""196 Local static web server; binds only to localhost for safety."""
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
def main():
 try: port=int(input("Port [8000]: ").strip() or "8000")
 except ValueError: print("Port must be a number."); return
 if not 1024<=port<=65535: print("Choose port 1024-65535."); return
 print(f"Serving {Path.cwd()} at http://127.0.0.1:{port} (local computer only). Ctrl+C stops.")
 try:
  with ThreadingHTTPServer(("127.0.0.1",port),SimpleHTTPRequestHandler) as server: server.serve_forever()
 except OSError as e: print("Could not start server:",e)
 except KeyboardInterrupt: print("\nServer stopped.")
if __name__=="__main__": main()
