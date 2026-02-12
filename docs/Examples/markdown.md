---
icon: material/language-markdown
---

# Markdown features

## Headers

### HTML rendering

<!-- 
# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header -->

### Markdown syntax

```
# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header
```

---

## Text formatting

| HTML rendering       | Markdown syntax         |
|:---------------------|:------------------------|
|**bold text**         | `**bold text**`         |
|*italic text*         | `*italic text*`         |
|***bold and italic*** | `***bold and italic***` |
|~~strikethrough~~     | `~~strikethrough~~`     |
|`inline code`         | `` `inline code` ``     |

---

## Links

```
[Link text](https://example.com)
[Link with hover title](https://example.com "Hover title")

```

[Link text](https://example.com)

[Link with hover title](https://example.com "Hover title")

---

## Images

```
![Image with title](../assets/logo-plain-dark.svg "Zensical SVG logo"){ width=150 }
![Left-aligned image](assets/logo-plain-dark.svg "Zensical SVG logo"){ align=left width=150 }
![Right-aligned image](../assets/logo-plain-dark.svg "Zensical SVG logo"){ align=right width=150 }
![Centered image](../assets/logo-plain-dark.svg){ width=150 } <!-- Center w/ empty caption -->
```

### Image with title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco ...

![Image with title](../assets/logo-plain-dark.svg "My SVG logo"){ width=150 }

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Left-aligned image with title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

![Left-aligned image](../assets/logo-plain-dark.svg "My SVG logo"){ align=left width=150 }

---
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Right-aligned image with title
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

![Right-aligned image](../assets/logo-plain-dark.svg "My SVG logo"){ align=right width=150 }

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

### Centered image with title & caption
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

![Centered image](../assets/logo-plain-dark.svg "My SVG logo"){ width=150 } <!-- Empty caption to center -->
/// caption
This is the image caption
///

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

---

## Lists

### Unordered list

```
- Item 1
- Item 2
  - Nested item
```

- Item 1
- Item 2
    - Nested item
- Item 3

### Ordered list

```
1. First item
2. Second item
    1. Nested item
3. Third item
```

1. First item
2. Second item
    1. Nested item
3. Third item

### Unordered tickmark list

```
- [x] Item 1
- [x] Item 2
    - [x] Nested item
- [ ] Item 3
```

- [x] Item 1
- [x] Item 2
    - [x] Nested item
- [ ] Item 3

---

## Blockquotes

```
> This is a blockquote
> Multiple lines
>> Nested quote
```

> This is a blockquote

> Multiple lines
>> Nested quote

---

## Code blocks
````
```python
def hello() {
  print("Hello, world!")
}
```
````

```python
def hello() {
  print("Hello, world!")
}
```

---

## Tables
```
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |
```

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |

---

## Horizontal rule
```
--- or *** or ___
```

---

## Escaping characters
```
Use backslash to escape: \* \_ \# \`
```

## Line breaks
```
End a line with two spaces  
to create a line break.

Or use a blank line for a new paragraph.
```

First paragraph.

Second paragraph after blank line.  
Line breaks after two spaces.
