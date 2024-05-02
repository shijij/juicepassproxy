CONF_YAML = "juicepassproxy.yaml"
VERSION = "v0.2.0"

LOGFILE = "juicepassproxy.log"
LOG_FORMAT = "%(asctime)-20s %(levelname)-9s [%(name)s] %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Defaults
DEFAULT_ENELX_SERVER = "juicenet-udp-prod3-usa.enelx.com"
DEFAULT_ENELX_PORT = "8047"
DEFAULT_LOCAL_IP = "127.0.0.1"
DEFAULT_ENELX_IP = "54.161.147.91"
DEFAULT_MQTT_HOST = "127.0.0.1"
DEFAULT_MQTT_PORT = "1883"
DEFAULT_MQTT_DISCOVERY_PREFIX = "homeassistant"
DEFAULT_DEVICE_NAME = "JuiceBox"
DEFAULT_TELNET_TIMEOUT = 30

EXTERNAL_DNS = "1.1.1.1"
