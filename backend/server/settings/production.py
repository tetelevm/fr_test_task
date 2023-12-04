from ..secrets import get_secret_variable


ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_secret_variable("DB_NAME", ""),
        "USER": get_secret_variable("DB_USER", ""),
        "PASSWORD": get_secret_variable("DB_PASSWORD", ""),
        "HOST": get_secret_variable("DB_HOST", "localhost"),
        "PORT": get_secret_variable("DB_PORT", "5432"),
    }
}
