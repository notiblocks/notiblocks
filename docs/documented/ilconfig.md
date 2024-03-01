# NotiBlocks Inline Configuration Class
The `ILConfig` class is for development use only. It wraps the messages, which have inline formatting. For the moment this class has only one changable attribute.

## Attributes
    * `color` - It lets you set the color of the text you want to format.
    * `message` - The text, that is going to be formated.

## Colors
Supported colors include:
- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white` *(bright gray)*
- `gray` *(bright black)*
- `bright_red`
- `bright_green`
- `bright_yellow`
- `bright_blue`
- `bright_magenta`
- `bright_cyan`
- `bright_white` *(actual white)*

Note that the color values are **case insensitive**.

## Usage

Depending on the approach, users can either set attributes directly through the constructor or utilize the defined getters and setters.

## Example
```python
# You can define a configuration like this
config = ILConfig(
    message="This is my custom message configuration", 
    color="red"
)

# or relatively like this
config = ILConfig("This is my custom message configuration", "red")
```

> Note that this class is for development purposes only, so you could not use it outside the source code of `notiblocks`