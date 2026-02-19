<p align="center">
  <img src="https://github.com/edoardottt/images/blob/main/longtongue/logo.png"><br>
  <b>Generate customized Password/Passphrase wordlist based on target information</b>
  <br>
  <sub>
    Coded with 💙 by edoardottt
  </sub>
  <br>
  <!--Tweet button-->
  <a href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fedoardottt%2Flongtongue%20&text=longtongue%20-%20Customized%20Password/Passphrase%20List%20inputting%20Target%20Info%20%21&hashtags=pentesting%2Clinux%2Cpython%2Cnetwork%2Cpassword%2Cbugbounty%2Cinfosec" target="_blank">Share on Twitter!
  </a>
</p>

Installation ⬇️
----

```console
git clone https://github.com/edoardottt/longtongue.git
cd longtongue
pip install -r requirements.txt
python3 longtongue.py
```

Usage 💻
----

```console
usage: longtongue.py [-h] (-p | -c | -v) [-l | -L] [-y] [-n] [-m MINLENGTH] [-P COMMON_PASSWORD_LIST]

Generate customized Password/Passphrase wordlist based on target information

options:
  -h, --help            show this help message and exit
  -p, --person          The target is a person
  -c, --company         The target is a company
  -v, --version         Show the version of this program
  -l, --leet            Add also complete 1337(leet) passwords
  -L, --leetall         Add also ALL possible le37(leet) passwords
  -y, --years           Add also years to password. See years range inside longtongue.py
  -n, --numbers         Add also numbers to password. See numbers range inside longtongue.py
  -m, --minlength MINLENGTH
                        Set the minimum length for passwords (default 0).
  -P, --common-password-list COMMON_PASSWORD_LIST
                        Set the file which contains common passwords (default included in the source).
```

Examples 📖
-------

- `python longtongue.py -v`

- `python longtongue.py -h`

- `python longtongue.py -p`

- `python longtongue.py -pl`

- `python longtongue.py -pln`

- `python longtongue.py -plny`

- `python longtongue.py -c`

- `python longtongue.py -cl`

- `python longtongue.py -cln`

- `python longtongue.py -clny`

- `python longtongue.py -c -m 10`

- `python longtongue.py -p -m 10`

- `python longtongue.py -c -P ./common-passwords.txt`

- `python longtongue.py -p -P ./common-passwords.txt`

Changelog 📌
-------

Detailed changes for each release are documented in the [release notes](https://github.com/edoardottt/longtongue/releases).

Contributing 🤝
------

If you want to contribute to this project, open an [issue](https://github.com/edoardottt/longtongue/issues) or a [pull request](https://github.com/edoardottt/longtongue/pulls).

License 📝
-------

This repository is under [GNU General Public License v3.0](https://github.com/edoardottt/longtongue/blob/main/LICENSE).  
[edoardottt.com](https://edoardottt.com) to contact me.
