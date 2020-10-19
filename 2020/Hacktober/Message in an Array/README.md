# Message in an Array

![Programming](https://img.shields.io/badge/Programming--ff8f00?style=for-the-badge) ![Points - 10](https://img.shields.io/badge/Points-10-9cf?style=for-the-badge)

```txt
Deadface has left a message in the code. Can you read the code and figure out what it says? You may also copy and paste the code in an emulator. Enter the answer as flag{Word Word Word Word}.
```

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GhostTown
{
    class Program
    {
        static void Main(string[] args)
        {
           string[] str = new string[4] {"DEADFACE","Nothing", "Stop", "Will"};

           Console.WriteLine("{1} {3} {2} {0}", str);
         }
    }
}
```

---

_... not too much "writing-up" to do here..._

Ok! Simply by looking at the source code provided above, you should be able to tell that it's the `C#` programming language.

Sadly, we didn't have a fitting compiler when we were solving the challenge and we were a bit to lazy to search for an emulator online... So... since the source code isn't too hard to understand - we just read through it and recovered the flag this way.

Really, all you want to look at are the two lines in the `static void Main` function. The first defines a string array with four elements and the second prints those elements in the order: 1, 3, 2, 0.

Therefore, we can easily reconstruct the flag: `flag{Nothing Will Stop DEADFACE}`