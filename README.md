# lektor-disqus-comments

This plugin adds support for Disqus comments to Lektor.  Once the plugin is
enabled a `render_disqus_comments` function which can render a disqus comment
box.

## Enabling the Plugin

To enable the plugin add this to your project file:

```ini
[packages]
lektor-disqus-comments = 0.1
```

## Configuring the Plugin

The plugin has a config file that is needed to inform it about your
website.  Just create a file named `disqus-comments.ini` into your
`configs/` folder and configure the `shortname` key with the name of
your disqus community:

```ini
shortname = YOUR_SHORTNAME
```

## In Templates

Now you can add a discussion box to any of your templates by just using
the `render_disqus_comments` function.  Just calling it is enough to
get the comment box:

```html
<div class="comments">{{ render_disqus_comments() }}</div>
```

Optionally the function accepts two arguemnts: `identifier` and
`url` to override the defaults.  For more information have a look at
the disqus widget documentation.
