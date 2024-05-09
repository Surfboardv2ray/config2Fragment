const fs = require('fs');
const path = require('path');

function apply() {
    // Get all the JSON files in the "configs" directory
    const configsDir = './configs';
    const resultsDir = './results';
    const files = fs.readdirSync(configsDir).filter(file => path.extname(file) === '.json');

    files.forEach(file => {
        // Skip the "combined.json" file
        if (file === 'combined.json') {
            return;
        }

        let sourceText = fs.readFileSync(path.join(configsDir, file), 'utf8');
        let sourceObject = {};

        if(!sourceText.trim()){
            console.error("Source config is empty!");
            return;
        }

        try {
            sourceObject = JSON.parse(sourceText);
        } catch (error) {
            console.error(error);
            return;
        }

        let proxyOutbound = sourceObject.outbounds.find(r => r.tag == "proxy");
        if (!proxyOutbound) {
            console.error("Can not find the outbound with proxy tag.");
            return;
        }

        proxyOutbound={...proxyOutbound};

        let destObject = { ...sourceObject };

        if (!proxyOutbound.streamSettings.sockopt) {
            proxyOutbound.streamSettings.sockopt = {};
        }

        proxyOutbound.streamSettings.sockopt = {
            ...proxyOutbound.streamSettings.sockopt,
            dialerProxy: "fragment",
            tcpKeepAliveIdle: 100,
            tcpNoDelay: true
        };

        destObject.outbounds = destObject.outbounds.filter(r => r.tag != "fragment" && r.tag != "proxy")

        destObject.outbounds.unshift(
            {
                "tag": "fragment",
                "protocol": "freedom",
                "settings": {
                    "domainStrategy": "AsIs",
                    "fragment": {
                        "packets": "1-5",
                        "length": "1-5",
                        "interval": "1-5"
                    }
                },
                "streamSettings": {
                    "sockopt": {
                        "tcpKeepAliveIdle": 100,
                        "tcpNoDelay": true
                    }
                }
            }
        );

        destObject.outbounds.unshift(proxyOutbound);

        fs.writeFileSync(path.join(resultsDir, file), JSON.stringify(destObject, null, 4));
    });
}

apply();
