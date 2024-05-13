# PresentLang

PresentLang is a markdown-based language for creating presentations like slides or video presentations. It allows you to define the presentation type, scenes, layouts, and content in a simple and readable format.

## Features

- **Supported Presentation Types**: Currently, PresentLang supports `slides` and `video` presentation types.
- **Scene Definition**: You can define multiple scenes for your presentation, specifying the scene type, layout, title, subtitle, and text content.
- **Flexible Layouts**: PresentLang provides different layout options like `intro` and `default` to structure your presentation scenes.
- **Markdown Support**: The content for each scene can be written using markdown syntax, making it easy to format text, add lists, code snippets, and more.

## Getting Started

To create a new presentation using PresentLang, follow these steps:

1. Set the presentation type at the beginning of your file:

```
presentation type = slides
```

or

```
presentation type = video
```

2. Define your scenes with various properties:

```
scene1:
    scene type = intro
    scene layout = intro
    scene title = "My Presentation"
    scene subtitle = "An Introduction"

scene2:
    scene type = default
    scene layout = default
    scene title = "Key Points"
    scene text = "- Point 1\n- Point 2\n- Point 3"
```

3. Save your file with a `.presentlang` extension (e.g., `my_presentation.presentlang`).

4. Use the PresentLang compiler or interpreter to generate your presentation in the desired format (e.g., PowerPoint, PDF, video).

## Example

Here's an example of a simple PresentLang file for creating a slides presentation:

```
# Set the presentation type
presentation type = slides

# Define scenes
scene1:
    scene type = intro
    scene layout = intro
    scene title = "A Slides Presentation"
    scene subtitle = "Created Using PresentLang"

scene2:
    scene type = default
    scene layout = default
    scene title = "PresentLang Benefits"
    scene text = "PresentLang makes creating presentations similar to html or python, where you can simply type away."

scene3:
    scene type = default
    scene layout = default
    scene title = "Get Started"
    scene text = "Check out the documentation to learn more about PresentLang and start creating your own presentations today!"
```

This example defines three scenes for a slides presentation: an intro scene, a scene highlighting the benefits of PresentLang, and a scene encouraging users to get started with the language.