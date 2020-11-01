# I'm Not Lying

![Forensics](https://img.shields.io/badge/Forensics--8700ff?style=for-the-badge) ![Points - 450](https://img.shields.io/badge/Points-450-9cf?style=for-the-badge)

```txt
Our field agents had captured someone who we had suspected to have information about a flag. The recording of their conversation is attached below.

- YoshiBoi#2008
```

---

When listening to the .mp3, we can notice some Morse Code beeping at around 12 seconds.

Opening it in Audacity and switching to Spectrogram View revealed some Morse Code:

![spectrogram](./spectrogram.jpg)

![reveal](./reveal.jpg)

So where is the rest of it? - Navigate to "Effects->Change Pitch" => set `-12` for semitones

![semitones](./semitones.jpg)

Now there is a more or less clearly visible Morse Code pattern:

![morse](./morse.jpg)

`-.-. -.-- -.-. - ..-. - .-. ..- --... .... ..--.- .... .---- -.. -.. ...-- -. ..--.- ..- -. -.. ...-- .-. ..--.- .-.. -.-.-- . ...-..-`

Using [CyberChef](https://gchq.github.io/CyberChef/) => cyctftru7h_h1dd3n_und3r_l!e$



`cyctf{tru7h_h1dd3n_und3r_l!e$}`

