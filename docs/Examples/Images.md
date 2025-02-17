## Working with images in Markdown

## Adding images

![Image title](accommodation status.png)

### Adding images from the web

```md
![Image title](https://picsum.photos/800/600)
```

![Image title](https://picsum.photos/800/600)

### Adding captions to images

This configuration adds the ability to align images, add captions to images (rendering them as figures), and mark large images for lazy-loading. Add the following lines to `mkdocs.yml`:

```yaml
markdown_extensions:
  - attr_list
  - md_in_html
```

**Example:**

```md
<figure markdown>
  ![Image title](https://picsum.photos/800/600){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>
```

<figure markdown>
  ![Image title](https://picsum.photos/800/600)
  <figcaption>Image caption</figcaption>
</figure>


### Aligning images


## Hosting images for your documentation

It's easy to add images to your documentation. But there are few ways to host images for your documentation.

1. hosting the images on your own server
2. hosting the images on Github
3. hosting the images on [Imgur](https://imgur.com/)
4. hosting the images on [Imgbb](https://imgbb.com/)

I would recommend hosting the images on Github or Imgur.

### Embedding images in Markdown


### Hosting images on Github


#### Hosting images on Imgur

### Taking screenshots and uploading to Imgur

=== "Mac"
    - Open the image in the browser
    - Right click on the image
    - Select `Copy Image Address`
    - Paste the image address in the markdown file
    - Add `?raw=true` to the end of the image address
    - The image address should look like this
  
        ```md
        ![2023-05-15_22-10-53.png](https://i.imgur.com/mp4S3jD.png)
        ```

    - The image should be displayed in the preview window
    
    Use plugsins

    - Markdown Image
    - Markdown Image Extended

=== "Windows"

    There are different tools you can use to take screenshots and upload them to Imgur. I would recommend using [ShareX](https://getsharex.com/) or [Greenshot](https://getgreenshot.org/).

    #### Using ShareX
    - configure ShareX to upload to Imgur
    - take a screenshot
    - edit the image if necessary
    - click on the 'Upload' button
    - ShareX will upload the image to Imgur and copy the image address to the clipboard
    - Paste the image address in the markdown file

    **Example**
    !!! example
        Here are some example images hosted on Imgur

        - ![2023-05-15_22-10-53.png](https://i.imgur.com/mp4S3jD.png "trying to add some captions")
        - ![2023-05-15_22-24-48.png](https://i.imgur.com/5r8tFZi.png)

    #### Using Greenshot







