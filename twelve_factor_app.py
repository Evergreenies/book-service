try:
    from twelve_factor_app_framework.bootstrap import app
    from twelve_factor_app_framework.configs.config import Config, ConfigStrategy
except ImportError:
    from .twelve_factor_app_framework.bootstrap import app
    from .twelve_factor_app_framework.configs.config import Config, ConfigStrategy


app = app
Config = Config
ConfigStrategy = ConfigStrategy

config = Config.get_instance(ConfigStrategy.ENV_VAR)
config.load_config()
