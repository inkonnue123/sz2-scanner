import requests

class AuthChecker:
    def __init__(self, base_url):
        self.base_url = base_url

    def check_broken_auth(self, endpoint, credentials):
        # Try to authenticate using provided credentials
        response = requests.get(f"{self.base_url}{endpoint}", auth=credentials)
        if response.status_code == 401:
            return "Broken authentication - Unauthorized access."
        elif response.status_code == 200:
            return "Authentication successful."
        return "Unexpected response: {response.status_code}"

    def check_weak_credentials(self, credentials_list):
        weak_credentials = []
        for credentials in credentials_list:
            response = self.check_broken_auth(
                '/protected', 
                credentials
            )
            if response == "Broken authentication - Unauthorized access.":
                weak_credentials.append(credentials)
        return weak_credentials

# Example usage:
# checker = AuthChecker('http://example.com')
# result = checker.check_broken_auth('/login', ('user', 'pass'))

