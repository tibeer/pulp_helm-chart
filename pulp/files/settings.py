SECRET_KEY = "aabbcccd"
CONTENT_ORIGIN = "http://1.2.3.4.nip.io"
DATABASES = {
    "default": {
        "HOST": "pulp-postgres",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pulp",
        "USER": "pulp",
        "PASSWORD": "password",
        "PORT": "5432",
        "CONN_MAX_AGE": 0,
        "OPTIONS": {
            "sslmode": "prefer"
        }
    }
}
# CACHE_ENABLED is a tech preview
# https://docs.pulpproject.org/pulpcore/configuration/settings.html#cache-enabled
CACHE_ENABLED = True
REDIS_HOST = "pulp-redis"
REDIS_PORT = 6379
REDIS_PASSWORD = ""
ANSIBLE_API_HOSTNAME = "http://localhost:24817"
TOKEN_SERVER = "localhost:24817/token/"
TOKEN_AUTH_DISABLED = False
TOKEN_SIGNATURE_ALGORITHM = "ES256"
PUBLIC_KEY_PATH = "/etc/pulp/keys/container_auth_public_key.pem"
PRIVATE_KEY_PATH = "/etc/pulp/keys/container_auth_private_key.pem"
