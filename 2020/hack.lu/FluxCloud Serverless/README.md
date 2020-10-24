# FluxCloud Serverless

![Web](https://img.shields.io/badge/Web--blue?style=for-the-badge) 

```txt
To host stuff like our website, we developed our own cloud because we do not trust the big evil corporations! Of course we use cutting edge technologies, like serverless. Since we know what we are doing, it is totally unhackable. If you want to try, you can check out the demo and if you can access the secret, you will even get a reward :)

Note: This version of the challenge contains a bypass that has been fixed in FluxCloud Serverless 2.0.

https://serverless.cloud.flu.xxx
```

---

We started looking at the Source Code

In <a href="./public/app/serverless/functions/waf.js">waf.js</a> you will see the Firewall's checks and notice, that it checks for `flag` in the URL, which it then redirects to the `/blocked` content.

In <a href="./public/app/serverless/functions/app.js">app.js</a> you can see a `/flag` Route, which should display the `FLAG` but since the Firewall checks for that, we are not coming that far.

However, since the Firewall only checks for lowercase `flag` we can simply use another variation of the word and for example the route `/fLag` or `/Flag` etc.

<p  align="center"><b>flag{ca$h_ov3rfl0w}</b></p>