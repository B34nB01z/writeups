# Bashing My Head

![Misc](https://img.shields.io/badge/Misc--ff0049?style=for-the-badge) ![Points - 450](https://img.shields.io/badge/Points-450-9cf?style=for-the-badge)

```txt
This program won't let me get in! It says im not a bot, but I believe I am! I think so, because I can't solve captchas. Are you bot level brain?

nc cyberyoddha.baycyber.net 10006

- YoshiBoi#2008
```

---

Ok... this essentially was a scripting challenge ^^.

Once you actually connected via `netcat` you could see that you had to complete some sort of quiz in order to retrieve the flag.

You can find our final python script that solves the quiz [here](./solve.py), but here's a short explanation of how you can solve the individual questions:

* **Quick, decrypt this: _some_base64_!**

Ok this one wasn't to complicated ... You simply had to decode the base64 string and return the result.

* **Supa ez.  Is it possible for p to equal _some_number_? [y/n]**

All you had to do on this one was to check, whether or not the provided _some_number_ is prime. If it is, return `y` otherwise `n`.

* **Quick give me the p and q (where p < q) values for when n is _some_number_!**

Calculate and return _some_number_'s prime factors. Be mindful that you have to return them individually.

* **Now tell me if it is possible for n to equal _some_number_! [y/n]**

Simply check, whether or not the given _some_number_ has exactly two primefactors.

* **Tell me ϕ whe n is _some_number_!**

Calculate the given _some_number_'s prime factors (p and q) and then use those two to calculate phi with: `ϕ = (p-1) * (q-1)`.

* **Is it possible for ϕ to be _some_number_ when e is _some_other_number_? [y/n]**

Check, whether or not _some_number_ and _some_other_number_ are co-prime, i.e. their greatest common divisor is 1.

_Answering this question was a bit buggy sometimes, so... you might have to try more than once ... ^^_

If you implemented all the questions and answers above, nothing could stop you from getting the flag (assuming that you ran the script often enough ... ^^): `CYCTF{tru3_1337_b4$h!ng_t@13nt_r1ght_h3r3}`
