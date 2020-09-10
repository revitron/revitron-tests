![](https://raw.githubusercontent.com/revitron/revitron/master/svg/revitron-readme.svg)

# Revitron Unit Tests

A [Revitron](https://github.com/revitron/revitron) unit test extension for pyRevit.

![GitHub](https://img.shields.io/github/license/revitron/revitron-tests?color=222222)
![GitHub top language](https://img.shields.io/github/languages/top/revitron/revitron-tests?color=222222)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/revitron/revitron-tests?color=222222)

Revitron unit tests need their own pyRevit UI to run. Since they are only needed to develop the library extension and would only bother normal users, all unit tests are located separately in this repository and can be installed as an independent UI extension if required as follows:

	cd C:[\path\to\pyrevit]\extensions
	git clone https://github.com/revitron/revitron-tests.git revitron-tests.extension

---

&copy; 2020 Marc Anton Dahmen &mdash; MIT license