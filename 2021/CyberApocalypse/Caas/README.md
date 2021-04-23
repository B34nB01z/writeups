# Caas

![Web](https://img.shields.io/badge/Web--0042ff?style=for-the-badge) ![Points - 300](https://img.shields.io/badge/Points-300-eaeaea?style=for-the-badge)

```txt
cURL As A Service or CAAS is a brand new Alien application, built so that humans can test the status of their websites. However, it seems that the Aliens have not quite got the hang of Human programming and the application is riddled with issues.
This challenge will raise 43 euros for a good cause.
```

---

When opening the webpage, we get a little command prompt like input:

<div align="center">
    <img src="page.png" />
</div>

If we now enter a website link (e.g. https://ctf.hackthebox.eu), then we get the result of a little curl:

```html
<!DOCTYPE html><html><head><title>Hack The Box CTF :: Capture the Flag</title><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><meta name=author content="Hack The Box"><meta property=og:title content="Hack The Box :: CTF"><meta property=og:url content=https://ctf.hackthebox.eu/><meta property=og:image content=https://ctf.hackthebox.eu/static/HTB-favicon/favicon.ico><meta property=og:site_name content="Hack The Box :: CTF"><meta name=keywords content="Hack The Box, Hackthebox, Capture The Flag, Challenges, Training"><meta name=description content="Welcome to the Hack The Box CTF Platform. Looking for hacking challenges that will enable you to,                                             compete with others and take your cybersecurity skills to the next level? You are at the right place.,                                             From Jeopardy-style challenges (web, crypto, pwn, reversing, forensics, blockchain, etc) to Full Pwn Machines,                                             and AD Labs, it’s all here!" property=og:description><link rel="shortcut icon" href=./static/HTB-favicon/favicon.ico><link rel=icon type=image/png sizes=16x16 href=./static/HTB-favicon/favicon-16x16.png><link rel=icon type=image/png sizes=32x32 href=./static/HTB-favicon/favicon-32x32.png><link rel=apple-touch-icon href=./static/HTB-favicon/apple-touch-icon.png><link rel=mask-icon href=./static/HTB-favicon/safari-pinned-tab.svg><link href="https://fonts.googleapis.com/css?family=Lato: 100,300,400,500,700,900|Material+Icons&style=outline" rel=stylesheet><script src=https://unpkg.com/vue-recaptcha@latest/dist/vue-recaptcha.min.js></script><script src="https://www.google.com/recaptcha/api.js?onload=vueRecaptchaApiLoaded&render=explicit" async defer=defer></script><script async src="https://www.googletagmanager.com/gtag/js?id=UA-93577176-4"></script><script>window.dataLayer = window.dataLayer || [];,        function gtag(){dataLayer.push(arguments);},        gtag('js', new Date());,        gtag('config', 'UA-93577176-4');</script><script>!function(){var e=window.analytics=window.analytics||[];if(!e.initialize)if(e.invoked)window.console&&console.error&&console.error("Segment snippet included twice.");else{e.invoked=!0,e.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on","addSourceMiddleware","addIntegrationMiddleware","setAnonymousId","addDestinationMiddleware"],e.factory=function(t){return function(){var a=Array.prototype.slice.call(arguments);return a.unshift(t),e.push(a),e}};for(var t=0;t<e.methods.length;t++){var a=e.methods[t];e[a]=e.factory(a)}e.load=function(t,a){var n=document.createElement("script");n.type="text/javascript",n.async=!0,n.src="https://cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var o=document.getElementsByTagName("script")[0];o.parentNode.insertBefore(n,o),e._loadOptions=a},e.SNIPPET_VERSION="4.1.0","ctf.hackthebox.eu"===window.location.hostname?e.load("o7CCLQ34gdSSo2CYWKkONsZxv5cabLHz"):e.load("WW97YNGmBHUFTzI59OHFlJHFfDpc79XR")}}();</script><link href=/static/css/app.8c316d60ac8805351b4f3f7b545df915.css rel=stylesheet></head><body><div id=app></div><script type=text/javascript src=/static/js/manifest.2ae2e69a05c33dfc65f8.js></script><script type=text/javascript src=/static/js/vendor.e31f867762a38d902c5b.js></script><script type=text/javascript src=/static/js/app.b95c11a6a992f1246da8.js></script></body></html>
```

... so it seems to be a standard curl, so what if we just used `file:///flag`? 

<div align="center">
    <img src="curlf.png" />
</div>

Well, we get the flag 🤷‍♂️: `CHTB{f1le_r3trieval_4s_a_s3rv1ce}`
