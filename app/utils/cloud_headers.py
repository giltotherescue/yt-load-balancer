import google.auth.transport.requests
import google.oauth2.id_token


def get_cloud_run_auth_header(audience: str) -> dict:
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)
    return {"Authorization": f"Bearer {id_token}"}
