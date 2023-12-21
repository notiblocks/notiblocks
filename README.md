# Notiblocks

Quick and easy customizable terminal logs for your application.

## Table of Contents

- [`Introduction`](#introduction)
- [`Features`](#features)
- [`Installation`](#installation)
- [`Usage`](#usage)
- [`Contributing`](#contributing)
- [`License`](#license)

## Introduction

Welcome to Notiblocks, a versatile Python library designed to enhance terminal logging with customizable and intuitive features.

### What is Notiblocks?

Notiblocks is more than just a logging library; it's a powerful tool that simplifies and elevates your terminal logging experience. It offers a user-friendly interface for creating custom, eye-catching logs, allowing developers to seamlessly integrate informative and visually appealing messages into their applications.

### Why Notiblocks?

- **Simplicity**: With Notiblocks, logging becomes effortless. Its intuitive design makes it easy to craft customized terminal logs without complex configurations.
  
- **Customization**: Tailor your logs to suit your application's needs. Notiblocks offers a wide range of styling options, allowing you to create logs that stand out.

- **Versatility**: Whether you're working on a small script or a large-scale project, Notiblocks scales to meet your logging requirements.

## Features

- Customizable log styles and colors
- Easy integration into existing projects
- Make your own logging templates and reuse them whenever you want to
- Inline formatting, so you could add anything you want in the logs
- Low resource usage

## Installation

Install notiblocks trough pip

```bash
pip install notiblocks
```

And just import the module into your application

```python
import notiblocks
```

## Usage
Notiblocks uses `NBConfig` and `NBHandler` objects, which let you customize your logs by your needs. You can access them trough the module.

* **`NBConfig`**: Holds the information about how your logs will look. You can override the information trough the constructor, or through the setters. For further explanation check the [`docs`](/docs/documented/nbconfig.md).
* **NBHandler**: Wrapper class for the `NBConfig`, which provides the main functionalities as `success`, `fail`, `warn` and `log`. For further information check the [`docs`](/docs/documented/nbhandler.md).

Example:
```python
from notiblocks import NBConfig, NBHandler
    
nb_conf = NBConfig(
    success_sign_color="blue",
    time_sign_color="GrEEn",
    success_sign="SUCCESS",
    success_bracket_color="cyan",
    time_sign_stamp="DATE",
    bracket_style="round     ",
    warn_bracket_sign="square"
)

nb_handler = NBHandler(nb_conf)

print(nb_handler.success("Notiblocks is cool."))
print(nb_handler.fail("Notiblocks is still not in a finished state..."))
print(nb_handler.warn("You haven't smiled enough today :)"))
print(nb_handler.log("User {} accessed this page", page.user))
```

## Contributing
We welcome contributions from the community to help improve Notiblocks. If you'd like to contribute, please follow these guidelines:

* Fork the repository and clone it to your local machine.
* Create a new branch for your feature or bug fix: `git checkout -b feature/my-feature or git checkout -b bugfix/issue-123`.
* Make your changes and test thoroughly.
* Commit your changes with descriptive commit messages: `git commit -m "Brief description of your changes"`.
* Push to your branch: git push origin feature/my-feature.
* Open a pull request to the main branch and provide a detailed description of your changes.
* We appreciate your contributions, whether they're bug fixes, documentation improvements, or new features!

## License
Notiblocks is licensed under the MIT License, check [`LICENSE`](/LICENSE) for more information.

### Join us on the journey to transform your terminal logging experience with Notiblocks!