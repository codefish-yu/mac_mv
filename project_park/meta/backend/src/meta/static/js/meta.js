var meta;
(function (meta) {
    function api(name, params = {}) {
        return new Promise((resolve, reject) => {
            var req = new egret.HttpRequest();
            req.responseType = egret.HttpResponseType.TEXT;
            req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");
            req.open('/api/' + name + '/', 'POST');
            req.send(JSON.stringify(params));
            req.addEventListener(egret.Event.COMPLETE, function (e) {
                var res = JSON.parse(req.response);
                if (res.success) {
                    resolve(res.result);
                }
                else {
                    reject(res.result);
                }
            });
        });
    }
    meta.api = api;
    function wechat(readyFunction) {
        api('get_js_ticket', { 'current_url': window.location.href }).then((result) => {
            wx.config({
                debug: false,
                appId: result.appId,
                timestamp: result.timestamp,
                nonceStr: result.nonceStr,
                signature: result.signature,
                jsApiList: ['scanQRCode']
            });
            wx.error(function (res) {
                console.log(res);
            });
            wx.ready(function () {
                readyFunction();
            });
        }).catch((e) => {
            console.error(e);
        });
    }
    meta.wechat = wechat;
    function scan() {
        return new Promise((resolve, reject) => {
            wx.scanQRCode({
                needResult: 1,
                scanType: ["qrCode"],
                success: (res) => {
                    resolve(res.resultStr);
                }
            });
        });
    }
    meta.scan = scan;
    function buy(product_id) {
        return new Promise((resolve, reject) => {
            var req = new egret.HttpRequest();
            req.responseType = egret.HttpResponseType.TEXT;
            req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");
            req.open('/order/public/account/' + product_id.toString() + '/', 'GET');
            req.send();
            req.addEventListener(egret.Event.COMPLETE, function () {
                var res = JSON.parse(req.response);
                WeixinJSBridge.invoke('getBrandWCPayRequest', res, function (res) {
                    if (res.err_msg == "get_brand_wcpay_request:ok") {
                        resolve();
                    }
                    else {
                        reject();
                    }
                });
            });
        });
    }
    meta.buy = buy;
})(meta || (meta = {}));
