---
title: Bash Shell
summary: Learn how to use a shell, write shell scripts, and configure your shell environment.
competencies:
- "Software Engineering"
---

## What is Bash?

Bash is a shell - a shell is a program that uses text commands to run computer programs.  

### Resources

A few resources to use in addition to this lesson:

- [Survival guide for Unix newbies](https://matt.might.net/articles/basic-unix/) - A short guide on Unix.
- [Effective Shell](https://effective-shell.com/) - A book of essentials on how to use the shell.
- [BashGuide](https://mywiki.wooledge.org/BashGuide) - A guide on Bash and Bash scripting.

### Notation

`$` indicates a command is run interactively in a Bash shell -- you don't need to write this leading `$` when you are typing in the shell.

For example, in the code below, to run this on your own machine, you need to type `ls`, then `Enter` to run the command in the REPL:

```shell-session
$ ls
```

## Why Learn Bash?

Bash is a popular shell, that is readily available in the cloud.  

A lot of computing in the cloud is done on machines running some form of Linux, where the Bash shell is often installed with the operating system.  Cloud CI/CD tools like GitHub Actions or Azure Devops usually use run Bash to run pipeline components by default.

Learning how to use a shell will allow you to:

- **Create CI/CD Pipelines** - Most pipelines are sequences of shell commands.
- **Use Docker** - Dockerfiles are sequences of shell commands.
- **Repeat and Automate Tasks** - automating text commands is easier than automating pointing and clicking. 
- **Unlock Powerful Tools** - many development tasks are best done with shell tools.

<svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1085.8865699623695 941.4159980186889" width="600" height="600"><!-- svg-source:excalidraw --><metadata></metadata><defs><style class="style-fonts">
      @font-face { font-family: Excalifont; src: url(data:font/woff2;base64,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); }</style></defs><rect x="0" y="0" width="1085.8865699623695" height="941.4159980186889" fill="#ffffff"></rect><g stroke-linecap="round" transform="translate(9.999999999999773 310.92487796564023) rotate(0 184.41635220460762 178.4244851654687)"><path d="M80.04 30.96 C91.8 19.4, 107.19 13.46, 123.51 8.41 C139.84 3.35, 160.41 1.35, 178 0.65 C195.59 -0.05, 212.25 0.39, 229.05 4.22 C245.86 8.05, 263.63 15.23, 278.86 23.62 C294.08 32.01, 308.6 42.29, 320.39 54.57 C332.18 66.85, 341.76 81.73, 349.59 97.28 C357.42 112.84, 364.35 131.46, 367.38 147.91 C370.4 164.35, 369.69 179.3, 367.71 195.94 C365.73 212.59, 361.71 232.41, 355.5 247.78 C349.28 263.16, 341.55 275.51, 330.41 288.2 C319.26 300.88, 303.28 313.76, 288.62 323.88 C273.96 334, 258.9 343.52, 242.45 348.9 C226 354.27, 207.29 355.84, 189.92 356.11 C172.55 356.39, 155.01 354.46, 138.24 350.53 C121.48 346.6, 103.83 341.11, 89.32 332.53 C74.81 323.95, 62.82 311.36, 51.19 299.03 C39.57 286.71, 27.88 273.03, 19.56 258.56 C11.25 244.09, 4.55 228.53, 1.31 212.2 C-1.94 195.86, -1.71 177.15, 0.09 160.53 C1.89 143.92, 5.48 127.89, 12.11 112.52 C18.73 97.15, 26.15 83.17, 39.83 68.32 C53.51 53.47, 82.62 31.27, 94.2 23.44 C105.77 15.6, 107.97 18.57, 109.27 21.3 M300.52 42.14 C315.03 50.73, 328.86 66.2, 338.74 79.42 C348.62 92.64, 354.54 105.61, 359.79 121.46 C365.04 137.31, 369.73 157.11, 370.24 174.53 C370.74 191.94, 366.98 210.34, 362.83 225.96 C358.68 241.57, 354.76 254.55, 345.35 268.22 C335.93 281.89, 319.27 296.67, 306.35 307.98 C293.42 319.29, 283.08 328.32, 267.8 336.08 C252.52 343.85, 231.74 350.83, 214.66 354.59 C197.59 358.34, 182.27 360.18, 165.37 358.62 C148.47 357.06, 129.66 351.81, 113.28 345.23 C96.91 338.64, 80.27 330.44, 67.14 319.1 C54.01 307.77, 44.32 291.67, 34.5 277.21 C24.67 262.75, 14.29 247.61, 8.2 232.33 C2.11 217.06, -1.5 202.33, -2.04 185.55 C-2.57 168.77, 0.7 148.33, 4.97 131.66 C9.25 115, 14.73 99.9, 23.62 85.57 C32.52 71.23, 45.36 56.55, 58.33 45.66 C71.3 34.77, 86.12 27.35, 101.44 20.24 C116.76 13.12, 133.32 6.44, 150.25 2.96 C167.19 -0.51, 185.06 -2.55, 203.06 -0.61 C221.07 1.33, 242.36 8.19, 258.28 14.6 C274.19 21.02, 291.58 33, 298.54 37.88 C305.5 42.76, 301.89 41.6, 300.01 43.9" stroke="none" stroke-width="0" fill="#b2f2bb"></path><path d="M134.46 5.85 C149.25 -1.51, 169.12 -0.73, 186.47 -0.46 C203.83 -0.19, 221.92 2.71, 238.58 7.47 C255.24 12.24, 271.72 19.05, 286.43 28.11 C301.14 37.17, 315.92 48.81, 326.83 61.83 C337.74 74.85, 344.85 90.94, 351.9 106.23 C358.95 121.52, 366.55 136.91, 369.12 153.57 C371.68 170.23, 370.07 189.45, 367.32 206.2 C364.57 222.96, 360.14 238.75, 352.62 254.12 C345.1 269.5, 333.63 285.98, 322.2 298.45 C310.78 310.92, 298.66 320.11, 284.05 328.96 C269.44 337.81, 251.55 346.77, 234.54 351.55 C217.54 356.33, 199.07 358.31, 182.03 357.63 C165 356.94, 148.64 352.49, 132.32 347.44 C116.01 342.38, 99.1 336.41, 84.16 327.3 C69.21 318.18, 54.21 305.7, 42.67 292.74 C31.13 279.78, 21.45 264.88, 14.9 249.54 C8.35 234.2, 5.57 217.07, 3.35 200.71 C1.14 184.34, -0.51 167.54, 1.61 151.36 C3.73 135.18, 8.71 118.61, 16.06 103.62 C23.42 88.63, 33.71 74.46, 45.73 61.45 C57.74 48.43, 64.22 35.84, 88.15 25.52 C112.09 15.2, 163.62 2.01, 189.36 -0.5 C215.1 -3, 242.53 7.69, 242.58 10.49 M296.54 40.01 C311.5 47.92, 323.37 62.86, 333.39 76.71 C343.41 90.57, 351.06 107.62, 356.64 123.13 C362.22 138.64, 365.37 153.9, 366.89 169.79 C368.41 185.68, 369.78 201.73, 365.74 218.48 C361.69 235.23, 351.48 254.93, 342.62 270.29 C333.75 285.65, 325.19 299.13, 312.56 310.64 C299.92 322.15, 282.83 331.86, 266.82 339.36 C250.8 346.85, 233.12 352.53, 216.47 355.6 C199.82 358.68, 184.11 359.33, 166.92 357.81 C149.72 356.3, 129.62 353.14, 113.29 346.53 C96.96 339.91, 81.68 329.3, 68.95 318.11 C56.22 306.92, 47.01 293.2, 36.9 279.39 C26.78 265.57, 14.44 250.96, 8.27 235.23 C2.09 219.49, 0.44 201.86, -0.14 184.98 C-0.72 168.1, 0.74 149.82, 4.8 133.93 C8.85 118.04, 14.99 103.74, 24.2 89.66 C33.4 75.58, 47.56 60.95, 60.01 49.46 C72.47 37.97, 84.38 28.57, 98.95 20.73 C113.52 12.89, 129.98 5.95, 147.44 2.44 C164.9 -1.08, 186.47 -1.81, 203.71 -0.37 C220.95 1.07, 234.65 4.7, 250.9 11.08 C267.14 17.47, 293.58 32.53, 301.17 37.94 C308.75 43.36, 299.1 41.15, 296.39 43.57" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(170.0476318237495 476.6841997408874) rotate(0 24.46666717529297 12.5)"><text x="24.46666717529297" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" fill="#1e1e1e" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic">Bash</text></g><g stroke-linecap="round" transform="translate(691.0755534487855 574.5670276877515) rotate(0 184.41635220460762 178.4244851654687)"><path d="M315.38 51.59 C328.73 60.57, 337.74 77.68, 346.05 92.47 C354.36 107.25, 361.5 123.74, 365.25 140.31 C368.99 156.88, 369.74 175.26, 368.51 191.88 C367.28 208.51, 363.78 224.37, 357.86 240.06 C351.93 255.75, 343.22 272.47, 332.95 286.01 C322.69 299.55, 310.41 311.64, 296.26 321.32 C282.11 330.99, 264.87 338.14, 248.04 344.08 C231.22 350.02, 212.2 355.78, 195.32 356.97 C178.43 358.16, 163.05 354.63, 146.73 351.21 C130.41 347.78, 113.23 344.22, 97.41 336.43 C81.6 328.64, 64.63 316.69, 51.83 304.47 C39.03 292.26, 28.68 277.92, 20.64 263.11 C12.6 248.3, 7.27 231.74, 3.59 215.61 C-0.09 199.48, -2.94 182.9, -1.46 166.33 C0.03 149.75, 5.79 131.87, 12.49 116.16 C19.2 100.44, 28.81 85.66, 38.77 72.06 C48.73 58.45, 58.92 44.68, 72.27 34.52 C85.61 24.36, 102.43 16.85, 118.82 11.08 C135.21 5.31, 153.14 1.18, 170.63 -0.09 C188.11 -1.36, 206.58 0.08, 223.74 3.46 C240.9 6.84, 255.19 9.07, 273.58 20.2 C291.97 31.33, 322.58 57.74, 334.08 70.24 C345.59 82.74, 345.03 93.23, 342.61 95.2 M162.85 1.92 C178.72 -2.74, 197.11 -0.47, 213.69 2.07 C230.26 4.62, 246.75 9.79, 262.31 17.18 C277.87 24.57, 293.59 35.29, 307.03 46.4 C320.47 57.51, 333.79 69.48, 342.95 83.83 C352.1 98.18, 357.83 115.58, 361.95 132.52 C366.07 149.45, 368.44 168.59, 367.66 185.45 C366.89 202.3, 362.5 218.34, 357.29 233.66 C352.08 248.98, 345.85 263.63, 336.39 277.36 C326.93 291.09, 313.94 305.34, 300.51 316.02 C287.08 326.7, 271.47 334.48, 255.78 341.46 C240.1 348.44, 223.86 355.33, 206.4 357.89 C188.94 360.45, 167.72 360.31, 151.03 356.84 C134.33 353.36, 121.26 344.98, 106.22 337.05 C91.17 329.11, 73.61 319.78, 60.75 309.22 C47.89 298.67, 38.24 287.74, 29.06 273.74 C19.87 259.73, 10.38 242.16, 5.63 225.2 C0.87 208.24, 0.47 189.07, 0.53 171.99 C0.58 154.92, 0.72 138.78, 5.96 122.75 C11.21 106.72, 21.77 89.32, 31.98 75.8 C42.2 62.28, 53.43 51.86, 67.24 41.62 C81.05 31.37, 98.49 21.22, 114.85 14.31 C131.2 7.4, 157.38 1.96, 165.37 0.16 C173.35 -1.64, 162.43 0.04, 162.75 3.51" stroke="none" stroke-width="0" fill="#b2f2bb"></path><path d="M307.64 46.1 C321.62 54.78, 334.86 70.51, 343.93 85.13 C353 99.75, 357.72 117.01, 362.07 133.83 C366.42 150.64, 370.35 169.03, 370.01 186 C369.67 202.98, 365.71 219.81, 360.03 235.69 C354.35 251.56, 345.57 267.94, 335.94 281.25 C326.31 294.56, 315.71 305.42, 302.24 315.57 C288.77 325.71, 271.59 335.21, 255.13 342.12 C238.67 349.04, 220.71 355.22, 203.48 357.06 C186.24 358.9, 168.85 356.38, 151.71 353.17 C134.58 349.95, 116.21 345.21, 100.66 337.79 C85.11 330.36, 71 319.68, 58.42 308.61 C45.84 297.54, 34.22 285.56, 25.18 271.37 C16.13 257.18, 8.59 240.12, 4.15 223.49 C-0.28 206.87, -2.52 188.34, -1.45 171.62 C-0.37 154.9, 5.25 139.14, 10.62 123.15 C15.99 107.16, 21.07 89.45, 30.79 75.69 C40.51 61.92, 55.45 51.12, 68.94 40.55 C82.43 29.97, 96.21 18.99, 111.71 12.25 C127.22 5.51, 144.55 1.85, 161.97 0.12 C179.39 -1.61, 198.52 -1.34, 216.23 1.88 C233.95 5.11, 247.55 5.9, 268.25 19.45 C288.94 32.99, 325.95 65.69, 340.41 83.14 C354.88 100.58, 357.57 122.82, 355.05 124.12 M98.48 22.5 C111.78 12.62, 130.44 5.89, 147.51 2.22 C164.58 -1.46, 183.62 -0.95, 200.87 0.46 C218.13 1.86, 234.69 4.75, 251.06 10.66 C267.42 16.57, 285.83 25.55, 299.08 35.92 C312.34 46.28, 320.3 59.41, 330.6 72.84 C340.89 86.27, 354.5 100.56, 360.84 116.48 C367.19 132.4, 367.91 151.52, 368.66 168.38 C369.41 185.23, 369.04 201.18, 365.34 217.6 C361.63 234.02, 355.25 251.86, 346.43 266.88 C337.6 281.9, 325.42 296.46, 312.4 307.73 C299.37 319, 283.66 326.55, 268.27 334.51 C252.89 342.47, 236.74 351.44, 220.1 355.49 C203.46 359.54, 185.67 360.17, 168.43 358.83 C151.19 357.49, 132.99 353.45, 116.66 347.46 C100.34 341.47, 84.23 333.48, 70.48 322.89 C56.73 312.31, 44.23 297.7, 34.17 283.94 C24.11 270.17, 15.6 256.43, 10.1 240.3 C4.6 224.17, 2.12 204.43, 1.15 187.13 C0.19 169.84, 0.29 152.39, 4.31 136.52 C8.33 120.66, 16.95 106.42, 25.27 91.95 C33.6 77.49, 42 61.47, 54.25 49.73 C66.5 37.99, 91.15 25.44, 98.77 21.49 C106.39 17.54, 98.97 23.91, 99.95 26.01" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(759.5648509219493 740.3263494629987) rotate(0 116.0250015258789 12.5)"><text x="116.0250015258789" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" fill="#1e1e1e" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic">Source Control with Git</text></g><g stroke-linecap="round" transform="translate(707.0538655531548 10) rotate(0 184.41635220460762 178.4244851654687)"><path d="M185.64 0.19 C202.4 -2.53, 220.75 3.42, 236.95 7.9 C253.14 12.38, 268.28 18.33, 282.83 27.08 C297.39 35.83, 312.8 47.64, 324.28 60.39 C335.75 73.14, 344.24 87.83, 351.68 103.59 C359.12 119.35, 366.3 138.43, 368.92 154.95 C371.53 171.47, 369.88 186.11, 367.35 202.73 C364.82 219.35, 360.96 239.54, 353.74 254.67 C346.51 269.8, 335.8 280.87, 324.03 293.51 C312.25 306.15, 298.04 321.28, 283.1 330.51 C268.16 339.74, 251 344.44, 234.37 348.91 C217.75 353.38, 200.56 357.3, 183.36 357.34 C166.16 357.38, 147.41 354.09, 131.18 349.13 C114.95 344.17, 100.44 336.26, 86 327.58 C71.56 318.89, 56.28 309.63, 44.54 297.04 C32.8 284.45, 22.75 267.51, 15.55 252.03 C8.36 236.55, 3.7 220.99, 1.37 204.15 C-0.96 187.32, -1.31 167.87, 1.56 151.03 C4.44 134.2, 11.25 118.21, 18.62 103.16 C25.98 88.12, 34.72 73.18, 45.77 60.77 C56.81 48.36, 70.1 37.94, 84.91 28.68 C99.71 19.43, 116.82 9.78, 134.58 5.24 C152.34 0.69, 180.56 1.29, 191.47 1.4 C202.38 1.5, 200.13 2.93, 200.04 5.88 M336.01 71.53 C347.88 82.53, 352.25 102.11, 357.39 118.07 C362.53 134.03, 365.68 150.74, 366.86 167.28 C368.05 183.82, 368.3 200.4, 364.49 217.31 C360.68 234.22, 352.65 254.34, 343.98 268.75 C335.31 283.15, 324.61 292.87, 312.46 303.74 C300.31 314.61, 286.06 325.31, 271.1 333.96 C256.15 342.61, 239.53 352.06, 222.72 355.65 C205.91 359.23, 187.66 357.51, 170.24 355.47 C152.82 353.43, 134.72 348.91, 118.21 343.39 C101.69 337.88, 85.01 332.11, 71.17 322.39 C57.32 312.68, 45.32 299.27, 35.15 285.1 C24.98 270.94, 16.39 253.44, 10.13 237.39 C3.88 221.34, -1.57 205.03, -2.4 188.8 C-3.24 172.56, 0.7 156.27, 5.13 140 C9.56 123.73, 15.22 106.6, 24.15 91.17 C33.08 75.74, 46.51 59.08, 58.73 47.4 C70.95 35.71, 82.5 28.74, 97.46 21.06 C112.43 13.38, 131.49 5.06, 148.51 1.31 C165.54 -2.43, 182.17 -3.57, 199.62 -1.42 C217.08 0.72, 236.74 7.77, 253.25 14.18 C269.76 20.59, 285.03 27.16, 298.68 37.04 C312.33 46.92, 330.18 66.77, 335.15 73.45 C340.13 80.13, 330.78 75.17, 328.53 77.12" stroke="none" stroke-width="0" fill="#b2f2bb"></path><path d="M320.44 56.84 C333.71 67.11, 343.71 85.96, 351.25 101.19 C358.79 116.42, 362.89 132.25, 365.68 148.24 C368.46 164.23, 370.17 180.72, 367.97 197.15 C365.78 213.58, 359.24 231.45, 352.49 246.84 C345.75 262.23, 338.1 276.29, 327.48 289.51 C316.87 302.72, 302.79 316.39, 288.8 326.15 C274.82 335.9, 259.76 343.03, 243.58 348.01 C227.4 353, 209.41 355.68, 191.74 356.05 C174.07 356.41, 154.33 354.09, 137.55 350.19 C120.77 346.3, 106.05 340.85, 91.05 332.67 C76.05 324.48, 59.87 313.94, 47.55 301.08 C35.23 288.23, 24.36 271.12, 17.12 255.53 C9.89 239.93, 6.84 223.62, 4.13 207.52 C1.42 191.42, -0.98 175.05, 0.87 158.95 C2.73 142.85, 8.63 126.31, 15.26 110.93 C21.88 95.54, 29.89 79.75, 40.63 66.64 C51.36 53.52, 65.37 42.05, 79.66 32.22 C93.95 22.39, 109.95 13.07, 126.35 7.66 C142.74 2.25, 160.83 0.18, 178.05 -0.24 C195.27 -0.66, 213.06 0.53, 229.67 5.15 C246.28 9.76, 261.79 17.65, 277.72 27.45 C293.65 37.26, 316.75 56.35, 325.26 63.96 C333.77 71.57, 330.95 71.17, 328.79 73.14 M106.6 17.96 C120.19 8.27, 139.14 2.53, 157.22 0.19 C175.3 -2.15, 197.29 0.7, 215.08 3.9 C232.88 7.11, 248.65 12.63, 264 19.41 C279.36 26.19, 294.64 34.21, 307.23 44.59 C319.82 54.97, 330.02 67.25, 339.55 81.7 C349.08 96.15, 359.02 115.38, 364.4 131.3 C369.78 147.21, 372.31 160.99, 371.81 177.19 C371.31 193.39, 367 212.24, 361.38 228.47 C355.76 244.7, 347.48 260.1, 338.07 274.57 C328.66 289.05, 318.16 304.42, 304.95 315.3 C291.74 326.18, 275.18 332.93, 258.82 339.85 C242.45 346.77, 223.96 354.29, 206.77 356.82 C189.58 359.34, 172.7 357.93, 155.69 355.03 C138.67 352.13, 119.87 346.97, 104.68 339.41 C89.48 331.85, 77.61 320.91, 64.51 309.67 C51.41 298.42, 35.18 285.33, 26.07 271.93 C16.97 258.53, 14.46 245.39, 9.88 229.26 C5.3 213.13, -1.54 192.38, -1.4 175.15 C-1.26 157.93, 5.95 142.1, 10.73 125.92 C15.51 109.75, 18.12 92.28, 27.29 78.1 C36.45 63.91, 52.46 50.96, 65.69 40.82 C78.92 30.67, 98.74 21.02, 106.66 17.24 C114.59 13.46, 111.13 16.09, 113.24 18.14" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(815.2181660780764 175.75932177524714) rotate(0 76.3499984741211 12.5)"><text x="76.3499984741211" y="17.619999999999997" font-family="Excalifont, Xiaolai, Segoe UI Emoji" font-size="20px" fill="#1e1e1e" text-anchor="middle" style="white-space: pre;" direction="ltr" dominant-baseline="alphabetic">CI/CD Pipelines</text></g><g stroke-linecap="round"><g transform="translate(338.88692414828915 349.5391322178689) rotate(0 175.76143314807382 -91.20953159578062)"><path d="M-2.15 -2.17 C56.43 -32.74, 293.15 -154.45, 351.89 -184.23 M1.88 2.82 C60.09 -27.35, 292.2 -150.19, 349.85 -181.58" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(338.88692414828915 349.5391322178689) rotate(0 175.76143314807382 -91.20953159578062)"><path d="M331.63 -162.69 C337.17 -169.55, 344.8 -174.26, 350.34 -181.74 M332.73 -163.53 C338.78 -170.1, 345.96 -177.34, 349.02 -181.32" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(338.88692414828915 349.5391322178689) rotate(0 175.76143314807382 -91.20953159578062)"><path d="M323.55 -177.77 C331.58 -179.84, 341.75 -179.82, 350.34 -181.74 M324.66 -178.61 C333.53 -179.64, 343.67 -181.35, 349.02 -181.32" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g></g><mask></mask><g stroke-linecap="round"><g transform="translate(352.20218423526444 606.5236518964921) rotate(0 165.77498808284236 63.24748541313238)"><path d="M-2.35 -1.3 C52.76 19.86, 276.15 105.48, 332.15 126.42 M1.57 4.17 C56.23 25.86, 275.01 109.66, 330.24 130.02" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(352.20218423526444 606.5236518964921) rotate(0 165.77498808284236 63.24748541313238)"><path d="M304.31 130.16 C314.03 131.53, 321.39 130.27, 331.47 129.27 M305.84 129.07 C311.53 129.21, 316.04 129.06, 330.03 130.48" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g><g transform="translate(352.20218423526444 606.5236518964921) rotate(0 165.77498808284236 63.24748541313238)"><path d="M310.35 114.16 C317.9 121.14, 323.13 125.53, 331.47 129.27 M311.88 113.07 C316.26 116.62, 319.46 119.93, 330.03 130.48" stroke="#1e1e1e" stroke-width="2" fill="none"></path></g></g><mask></mask></svg>


Bash is an enabling skill - it enables workflows that have huge benefits for development, such as source control, automated tests (CI) and automated deployments (CD).

## Terminal, Command-Line, Shell

### The Terminal

The terminal, command line and shell are often used interchangeably. They are however different tools - all three are used when using a computer via text commands.

**The terminal (also called a console) is an interface that controls user input & output**.

![The DEC VT100 Terminal](/images/bash-shell/terminal.png "The DEC VT100 Terminal")

**Historically a terminal was hardware**. The terminal originates in the mainframe era of computing.  Terminals could connect to other computers - you could run programs on a central computer from your terminal.

**Today terminals are often software** - using terminal emulator programs on a computer.  These software terminals can also be used to connect to other computers.

Popular terminal emulators include:
- **MacOS** - iTerm2,
- **Windows** - Windows Terminal,
- **Ubuntu** - Gnome Terminal.

### Command-Line

The command-line is the space or interface in the terminal where you can type and execute text commands. 

When you launch your terminal, you are in a command-line interface.  The command-line below shows a Bash shell, with the `echo` command:

```shell-session
$ echo "this is the command line"
"this is the command line"
```

### The Shell

**A shell is a computer program that executes text commands**. Shells are used in two ways:

1. **as a REPL** (Read-Eval-Print Loop) that runs interactively,
2. **as a programming language** that runs via scripts.

A shell is automatically started in a new terminal. When you write text in the command-line of a terminal, it is executed in a shell, the output displayed, and then a new command line prompt is shown, ready for the next user input.

The shell we shall use in this lesson is the Bash shell. This is because it's common and readily available in the cloud.

## Tooling

**Different developers use different tools for using a Bash shell**.

Some developers run terminals inside an IDE like VS Code - one terminal can be used with different shells.  Others will use a separate program like Windows Terminal to run different shells.

What shells you have available depends on your operating system - my suggestion is:

- **Windows** - for a shell, either Windows Subsystem for Linux or Git Bash.  For a terminal, Windows terminal is great.
- **MacOS** - for a shell, either Bash or Zsh are fine. For a terminal, iTerm2 is popular.
- **Linux** - Zsh or Bash are fine. For a terminal, use the Gnome Terminal if available, or try Kitty.

### Shells

There are many different shells available -- commonly used shells are:

- **sh** - the Bourne Shell, the original Unix shell. It introduced features like redirection (`>`, `>>`, `<`) and piping (`|`).
- **Bash** - the Bourne Again Shell, an improved version of Bourne Shell, is the default shell for many Unix and Linux systems. 
- **zsh** - the default shell on MacOS, which improves on Bash,
- **PowerShell** - a shell developed by Microsoft for Windows.

You can combine different shells with a given terminal emulator.  For example, you could use Bash with the Windows Terminal, or Zsh with iTerm2.

The best shells to know are the ones that are most easily available in the cloud. 

**Bash is the most common shell on Linux systems, which is the most common compute environment available in the cloud**.

### Text Editors 

VS Code is a good choice for most!  You'll want a text editor to write things like shell scripts or configuration files (YAML, JSON etc).

## Common Bash Programs

A shell has its own syntax and set of commands, along with a collection of programs available.  

Common Bash shell programs include:

- `ls` - list files & directories,
- `pwd` - print working directory,
- `cd` - change directory,
- `cat` - print file contents.

The programs that are available in your shell are programs that are in the shell's `$PATH` environment variable - more on the `$PATH` and environment variables later.

## Ways to use Bash

### Bash as a REPL

We can use the shell as a REPL to list the current directory files & directories using the `ls` program:

```shell-session
$ ls
```

### Bash as a Programming Language

We can use the shell as a programming language via shell scripting - an example shell script that lists the current directory using `ls`:

```bash { title = "script.sh" }
#!/usr/bin/env bash
ls
```

We can then execute this script in a shell REPL:

```shell-session
$ bash script.sh
```

Shell scripts can take input from command-line arguments or from environment variables.

## Whitespace

Bash use the space character to separate commands & arguments. This makes working at the shell natural, but requires some care.

**The shell will expand spaces by default into separate commands** - this means that spaces in the wrong places can cause shell scripts to break.

Space expansion is one reason why you should never put spaces in file names - use `-` or `_` as a separator in file names:

```bash
# don't do this
/folder name/file name.txt

# do this instead
/folder-name/file_name.txt
```

If you do use spaces, you may end up seeing (or having to write!) your paths by escaping the spaces with the escape character `\`:

```bash
# this is harder to work with
/folder\ name/file\ name.txt
```

## Navigation

### Where Am I?

`pwd` shows us where we are in the file system - this is our current directory:

```shell-session
$ pwd
/Users/adamgreen/data-science-south-projects/bash-shell
```

We can remove output from the terminal with `clear`:

```shell-session
$ clear
```

### What is in the Current Directory?

`ls` lists our current directory - showing us the files and folders:

```shell-session
$ ls
```

We can configure how `ls` works using **flags** - these are options that the `ls` program exposes.

Two common flags for `ls` are showing hidden files with `-a` in a long format with `-l`:

```shell-session
$ ls -al
```

### Changing Directories

We can change our current directory using `cd`, which will move down into a directory:

```shell-session
$ mkdir practice-dir
$ cd practice-dir
```

We can move back up a directory with `cd ..`, which moves into the parent directory:

```shell-session
$ cd ..
```

Another useful `cd` command is `cd -`, which moves to the directory we were previously in:

```shell-session
$ cd -
```

A special directory on Unix system is the home folder, which is the highest level folder for a user.  

We can get to the home folder in a few different ways:

```shell-session
$ cd ~
$ cd $HOME
$ cd
```

`~` is a special syntax that refers to the home folder. `$HOME` is an environment variable that is the path to your home folder.

The highest level of a file system on MacOS contains folders like `/etc` and `/Users` - we can move to these directories using `cd`:

```shell-session
$ cd /etc
```

Important top level directories include:

- `/etc` - configuration files,
- `/bin` - programs,
- `/Users` - user home directories (MacOS),
- `/home` - user home directories (Linux).

## Files & Directories

### Making & Editing Files

We can make an empty file using `touch`:

```shell-session
$ touch myfile.txt
```

We can edit the contents of this file using a text editor.  

It's important to know how to use at least one of the text editors that are included with an operating system, for example `nano`:

```shell-session
$ nano myfile.txt
```

### Making Directories

You can make a directory with `mkdir`:

```shell-session
$ mkdir practice
```

We can recursively create directories by passing the `-p` flag to `mkdir`:

```shell-session
$ mkdir -p practice/subfolder
```

### Moving Stuff

We can move a file or folder from one place to another with `mv`:

```shell-session
$ mv myfile.txt practice-dir/myfile.txt
```

Be careful with `mv` - it will overwrite the file!

We can copy a file or directory using `cp`:

```shell-session
$ cp myfile.txt practice-dir/myfile-copy.txt
```

### Removing Stuff

We can delete files with `rm`:

```shell-session
$ rm file
```

Be careful with `rm` - there is no trash can for `rm`!

We can also delete a folder using `rm`.  Two useful flags are `-r` which will recursively delete a folder and `-f` which will force deletion:

```shell-session
$ rm -rf directory
```

`-f` is needed as by default, `rm` will not delete a directory that has things in it.

### Viewing Files

`cat` is a program that prints the contents of a file to the terminal:

```shell-session
$ cat README.md
```

One common use of `cat` is at the start of a shell pipeline.  

For example, we can pipe the contents of a file into another program `grep`:

```shell-session
$ cat README.md | grep "data"
```

`head` will print the first `n` lines of a file:

```shell-session
$ head -n 3 readme.md
```

`tail` will print the last `n` lines of a file:

```shell-session
$ tail -n 3 readme.md
```

A file pager is a program that will keep a file open and allows you to move through that file.  

A most common pager is `less`:

```shell-session
$ less readme.md
```

## Searching 

We don't always know exactly where files or directories are, or what the contents of files are.

### Finding Directories

We can find directories using the `find` program:

```shell-session
$ find /path/to/search -type d -name "directory-name"
```

### Finding Files

To find a file by it's name, we can use the `find` program:

```shell-session
$ find /path/to/search -type f -name "file-name"
```

We can use the wildcard character `*` to match any characters.

For example, to find all Python scripts:

```shell-session
$ find /path/to/search -type f -name "*.py"
```

### Finding Text in Files

To find a specific string in files, we can use `grep`:

```shell-session
$ grep "search-string" filename.txt
```

### Finding Programs

To find where a program lives, we can use `which`:

```shell-session
$ which ls
```

This will show the location of the `ls` program, which is a binary file.

## Redirection 

**Shells can redirect input and output between commands**.  

Redirection allows a program to accept text input and output text to another program.

This enables the composition of programs, with programs generating text for each other.

### Standard Input, Output & Error

The shell establishes three text streams:

- **standard input** (STDIN) - the input stream (commonly a keyboard),
- **standard output** (STDOUT) - the output stream (commonly a terminal console),
- **standard error** (STDERR) - the error output stream (also usually goes to terminal console).

It's possible to direct these text streams to different places - for example to redirect STDOUT to a file, rather than the terminal console.

![](/static/mermaid/redirection1.svg)

### Redirecting Input

The `<` operator is used to redirect input. It reads input from a file instead of the keyboard. For example:

```shell-session
$ sort < unsorted.txt
```

![](/static/mermaid/redirection2.svg)

### Redirecting Output

The `>` operator is used to redirect output from a command to a file, overwriting the file if it exists.

The following redirects the output of `ls -l` to a file named `files.txt`.

```shell-session
$ ls -l > files.txt
```

![](/static/mermaid/redirection3.svg)

### Appending Output

The `>` command will overwrite - if you want to append the output to an existing file rather than overwriting it, you can use the >> operator.

```shell-session
$ ls -l >> files.txt
```

This will sort the lines in the `unsorted.txt` file.

### Pipes

**The pipe operator `|` allows you to chain commands together by passing the output of one command as input to another**. This enables composition of commands without using temporary files.

A pipe connects the standard output of the first command to the standard input of the second command.

```shell-session
$ ls | wc -l
```

Multiple pipes can be chained together to create more complex operations:

```shell-session
$ ls -l | grep ".txt" | sort | head -n 5
```

## Shell Configuration

### Environment Variables

The shell is a stateful system - a shell stores data in between execution of programs.  This data is stored in environment variables.

Environment variables can set and accessed in the shell, and then used as part of shell commands.

Programming languages like Python can access environment variables - in Python we can use `os.ENVIRON` to access the environment variables of the shell process the Python program is running in.

#### Setting an Environment Variable

We can set an environment variable using `NAME=VALUE` - note the lack of space around the `=`:

```shell-session
$ stage=production
```

#### Accessing an Environment Variable

We can view the value of this environment variable with `echo`, using the `$NAME` syntax:

```shell-session
$ echo $stage
production
```

#### Exporting Environment Variables to Sub-Processes

Our shell is run in a process - there are hundreds of processes running on your computer now.

Many actions we take in a shell create a new process - this new process is called a sub-process.  For example, when we run a Python script in a shell, a new Python process is created.

Environment variables are not inherited by sub processes.

We can however make environment variables accessible to sub processes using `export`:

```shell-session
$ export stage=production
```
You will often see `export` used in the shell config scripts like `.bashrc`.  This is because these scripts are run during shell startup, and the environment variables defined in these scripts are supposed to be available to all sub processes.

#### Viewing All Environment Variables

You can see all the environment variables currently defined in your shell with the `env` command:

```shell-session
$ env
```

You can access an environment variable using the `$NAME` syntax.  

You can use `echo` to view the value of an environment variable - below we look at the `$HOME` environment variable.

```shell-session
$ echo $HOME
```

### `$PATH`

The `$PATH` environment variable is a list of directories, separated by a `:`.

The `$PATH` environment variable is a list of directories that the shell will search when you type a command.  Appending a directory to `$PATH` makes that program accessible via a shell from any directory.

The `$PATH` variable will be quite long - a useful tip is to pipe the variable into `tr`, which can replace the `:` used to separate the paths with a new line `\n`:

```shell-session
$ echo $PATH | tr ":" "\n"
```

It's common to see the `PATH` variable modified in scripts by appending a new path onto the existing path:

```shell-session
$ export PATH=$PATH:$SPARK_HOME/bin
```

A common pattern you will see in install scripts is to copy this path update command into our shell configuration script:

`$ echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc`

This will append `export PATH=$PATH:$SPARK_HOME/bin` to the user's `~/.bashrc`.  On next shell startup, the `$SPARK_HOME/bin` directory will be available in the user's `PATH`.

Any binary programs that exist in `$SPARK_HOME/bin` will now be available to run from the shell.

### Sourcing

Sourcing a file executes the commands in the file in the current shell.  

This is different from running a file, which will execute the commands in a new shell in a sub-process.

One common use of `source` is to load environment variables into the current shell:

```bash { title = "myfile" }
NAME=value
```

```shell-session
$ source myfile
$ echo $NAME
value
```

### RC Files

Your shell is configured using text files.  These text files are `source`'d during shell startup, before you see your first command line prompt.  Often these files are `.rc` files, which stands for "run command".

Which shell configuration file depends on both your shell and your operating system:

- `~/.bashrc` on Linux with Bash,
- `~/.zshrc` on Linux with Zsh,
- `~/.bashrc` & `~/.bash_profile` on MacOS with Bash,
- `~/.bashrc` & `~/.zshenv` on MacOS with Zsh.

### Login vs. Non-Login Shells

A final complexity here is the difference between a login versus non-login shell.  

When you log into a system and start a shell, that's called a login shell. Login shells read certain configuration files, and the settings in those files persist for the session.

When you start a new terminal window or a new shell in an existing session, those are non-login shells. They read a different set of configuration files, and settings last only for the life of the shell.

This distinction depends on your operating system - for the shell and OS you are using, make sure you understand the intricacies of which configuration files are `source`'d.

## Aliases

A shell alias is a shortcut for a command or set of commands.  Aliases are commonly defined in your shell configuration files.

Here are some example aliases you can use for inspiration:

```bash
alias ls='ls -aGl'
alias c='clear'
alias cls='clear && ls'
alias bashrc='vim ~/git/dotfiles/.bashrc'
```

You can use `"command"` to run a command without alias expansion:

```shell-session
$ "ls"
```

## Shell Scripting

### Why Use Shell Scripts?  

Shell scripts allow code reuse and automation.

Bash is frequently used for scripting as it's the default shell on common Linux distributions like Ubuntu.

Even you are using Zsh as an interactive REPL via a terminal, you can still run scripts using the Bash program - below would work in both Zsh and Bash:

```shell-session
$ bash script.sh
```

### What is a Script?

A script is a text file containing lines of commands. Any command that can be executed in the terminal REPL with the Bash shell can also be put into a Bash script.

Below prints when we are using Bash as a REPL:

```shell-session
$ echo "this is printing in the Bash repl"
this is printing in the Bash repl
```

Below is a script that prints some text:

```bash { title = "script.sh" }
echo "this is printing in a Bash script"
```

We can run this script in the shell to see what it prints:

```shell-session
$ bash script.sh
this is printing in a Bash script
```

### The Shebang

The first line of a bash script usually begins with a 'shebang' (`#!`) followed by the path to the Bash program:

```bash
#!/usr/bin/env bash
```

This line tells the system that the file is a bash script and to use the Bash shell to interpret the script. 

A shebang is not necessary - even without a shebang, we can execute a script by specifying the `bash` program directly:

```shell-session
$ bash script.sh
```

A shebang allows us to execute a script like a standalone executable - without using Bash as part of our command:

```shell-session
$ ./script.sh
```

Common shebangs include:

- **Python** - `#!/usr/bin/env python`,
- **Bash** - `#!/usr/bin/env bash`,
- **sh** - `#!/usr/bin/env sh`.

We use `/bin/env` as this will find the program wherever it occurs in the `$PATH` shell environment variable.

### File Permissions and Execution

Before you can run your script using the `./` syntax, it must have execute permissions.

You can add execute permissions with the `chmod` command:

```shell-session
$ chmod +x script.sh
```

After setting this permission, we can execute our script like a standalone executable:

```shell-session
$ ./script.sh
```

You can also specify the program to run the script as part of the command - this works with and without a shebang in `script.sh`:

```shell-session
$ bash script.sh
```

## Writing a Bash Script

### Hello World

Let's start with the traditional Hello World program as a Bash script:

```bash { title = "script.sh" }
#!/usr/bin/env bash

# comments in Bash use a #
echo "Hello, World!"
```

`echo` is a shell program that prints its arguments to standard out - commonly to a terminal.

### Adding Variables

We can add a variable for a name:

```bash { title = "script.sh" }
#!/usr/bin/env bash

name="adam"
echo "Hello, $name!"
```

We use the `$name` syntax to refer to the value of the `name` variable within the script.

### Accepting Command Line Arguments

Command line arguments provide a way to customize the behavior of a script each time it's run. They are provided after the script name, separated by spaces.

Inside the script, you can access the arguments using special variables - `$1` refers to the first argument:

```bash { title = "myscript.sh" }
#!/usr/bin/env bash

name=$1
echo "Hello, $name!"
```

Running a Bash script with command line arguments:

```shell-session
$ ./myscript.sh adam
```

## Functions 

We can write a function in a Bash script using the `function` keyword:

```bash
function greet {
    echo "Hello, $1"
}

greet "adam"
```
