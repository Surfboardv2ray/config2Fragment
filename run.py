from v2tj import convert_uri_json

uri = "vless://149400e4-6910-4a3f-8c4a-c5c175929b87@crackthecode.ftp.sh:443?encryption=none&security=tls&sni=vcp3.dehel15354.wOrkeRS.dEv&alpn=h3%2Ch2%2Chttp%2F1.1&fp=ios&type=ws&host=vcp3.dehel15354.wOrkeRS.dEv&path=%2Fromb.minusober.com%3A443%2Fromb#13%2B%F0%9F%8C%A8%F0%9F%87%A8%F0%9F%87%A6%2B%40Surfboardv2ray"
file = convert_uri_json(uri=uri)
