# Categorize

Categorize is a simple, customizable CLI-tool for automation sorting your files by their extensions.

## Installing

From sources. Clone the repo:

```bash
$ git clone https://github.com/kantegory/categorize.git
```

Install package:

```bash
$ make install
```

That's all, you awesome!

Or from pip:
```bash
$ pip install categorize
```

## Usage

Sorting:

```bash
$ categorize --directory /path/to/your/directory
```

Show all categories and extensions:

```bash
$ categorize-config --show
```

Edit pattern name:

```bash
$ categorize-config --edit-name pattern_name new_name
```

Edit extensions for pattern name:

```bash
$ categorize-config --edit-ext pattern_name
```

## Contacts

[Email me](mailto:kantegory.etersoft.ru), or contact me in [telegram](https://t.me/kantegory).
