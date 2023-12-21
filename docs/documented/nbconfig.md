# NotiBlocks Configuration Class

The `NBConfig` class is designed to store configuration details for the NotiBlock handler. It manages various attributes related to colors, signs, brackets, and styles used in different scenarios.

## Attributes

- `warn_color`: Color of the warning sign exterior *(Default: yellow)*
- `fail_color`: Color of the failure sign exterior *(Default: red)*
- `success_color`: Color of the success sign exterior *(Default: green)*
- `time_color`: Color of the time stamp sign exterior *(Default: blue)*
- `warn_bracket_color`: Color of the brackets around the warning sign *(Default: yellow)*
- `fail_bracket_color`: Color of the brackets around the failure sign *(Default: red)*
- `success_bracket_color`: Color of the brackets around the success sign *(Default: green)*
- `time_bracket_color`: Color of the brackets around the time sign *(Default: blue)*
- `warn_bracket_sign`: Bracket style for the warning sign *(Default: None)*
- `fail_bracket_sign`: Bracket style for the failure sign *(Default: None)*
- `success_bracket_sign`: Bracket style for the success sign *(Default: None)*
- `time_bracket_sign`: Bracket style for a log's time stamp *(Default: None)*
- `warn_sign_color`: Color of the warning sign *(Default: white)*
- `fail_sign_color`: Color of the failure sign *(Default: yellow)*
- `success_sign_color`: Color of the success sign *(Default: blue)*
- `time_sign_color`: Color of the time stamp sign *(Default: gray)*
- `warn_sign`: The sign between the warn braces *(Default: "!")*
- `fail_sign`: The sign between the fail braces *(Default: "-")*
- `success_sign`: The sign between the success braces *(Default: "+")*
- `time_sign_stamp`: Time stamp instead of sign between the braces *(Default: ss:mm:hh)*
- `warn_background_color`: Background behind the warning sign *(Default: None)*
- `fail_background_color`: Background behind the failure sign *(Default: None)*
- `success_background_color`: Background behind the success sign *(Default: None)*
- `time_background_color`: Background behind the time sign *(Default: None)*
- `is_underlined`: Is the sign underlined? *(Default: False)*
- `bracket_style`: Type of brackets around the sign *(Default: None)*

Supported colors include:
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white *(bright gray)*
- gray *(bright black)*
- bright_red
- bright_green
- bright_yellow
- bright_blue
- bright_magenta
- bright_cyan
- bright_white *(actual white)*

Note that the color values are **case insensitive**.

## Methods

The class includes both getters and setters for each attribute to retrieve and modify the configuration details.

For example:
- `get_warn_color()` retrieves the warning sign's color.
- `set_warn_color(value)` sets the color of the warning sign.

## Usage

Depending on the approach, users can either set attributes directly through the constructor or utilize the defined getters and setters.

## Note

- Users can create their own bracket styles by following the provided pattern.
- Bracket types include `SQUARE`, `CURLY`, `ANGLE`, `ROUND`.

## Example

```python
from .constants import *

# Creating an instance of NBConfig with custom configurations
config = NBConfig(
    warn_color='yellow',
    fail_color='red',
    # Add other custom configurations here
)

# Getting and setting attributes
warn_color = config.warn_color
config.success_color = 'green'
```