# Usage
1. Fork this repository or download it. Place your v2ray configs inside `list.txt`, one config per line. Run the github actions workflow `action.yaml`.
2. You can set desired TLS Fragmentaion values over at `java/fragment.js` under "fragment" tag, or just let them be.
3. Your json sub will be at `configs/combined.json` and fragment+json sub at `results/combined.json`.
4. Finally, your exported base64 subscription will be saved to `list64`.

# Supported Porotocls

- VLESS+GRPC
- VLESS+GRPC+TLS
- VLESS+TCP
- VLESS+TCP+HTTP
- VLESS+TCP+TLS
- VLESS+TCP+TLS+HTTP
- VLESS+TCP+REALITY
- VLESS+GRPC+REALITY
- VLESS+WS
- VLESS+WS+TLS
- VLESS+WS+HTTP
- VLESS+WS+HTTP+TLS
- VMESS+GRPC
- VMESS+GRPC+TLS
- VMESS+TCP
- VMESS+TCP+HTTP
- VMESS+TCP+TLS
- VMESS+TCP+TLS+HTTP
- VMESS+WS
- VMESS+WS+TLS
- VMESS+WS+HTTP
- VMESS+WS+HTTP+TLS
- TROJAN+TCP
- TROJAN+TCP+HTTP
- TROJAN+TCP+TLS
- TROJAN+TCP+TLS+HTTP
- TROJAN+TCP+REALITY
- TROJAN+GRPC+REALITY
- TROJAN+GRPC+TLS
- TROJAN+WS
- TROJAN+WS+TLS
- TROJAN+WS+HTTP
- TROJAN+WS+HTTP+TLS

# Acknowledgments

This project is a fork of [v2ray-to-json](https://www.github.com/Am-Delta/v2ray-to-json) by Am-Delta.
The basic function is converting a v2ray proxy to json format, but this modified code converts in batches as well.
This project also uses MiSaturo's [Xray-Fragment-Configurator](https://github.com/MiSaturo/Xray-Fragment-Configurator) to apply fragmentation.
