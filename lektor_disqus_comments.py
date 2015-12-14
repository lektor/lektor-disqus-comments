# -*- coding: utf-8 -*-
from markupsafe import Markup

from lektor.pluginsystem import Plugin
from lektor.context import get_ctx, url_to
from lektor.utils import htmlsafe_json_dump


SCRIPT = '''
<div id="disqus_thread"></div>
<script>
  var disqus_config = function() { %(config)s };
  (function() {
    var d = document, s = d.createElement('script');
    s.src = '//%(shortname)s.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
  })();
</script>
<noscript>
  Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript"
    rel="nofollow">comments powered by Disqus.</a>
</noscript>
'''


class DisqusCommentsPlugin(Plugin):
    name = u'Disqus Comments'
    description = u'Adds disqus comments to a website.'

    def get_disqus_config(self, identifier=None, url=None):
        configs = []
        ctx = get_ctx()
        if identifier is None:
            if ctx.source is not None and ctx.source.path is not None:
                identifier = ctx.source.path
        if identifier is not None:
            configs.append('this.page.identifier = %s;' %
                           htmlsafe_json_dump(identifier))

        if url is None and ctx.source is not None:
            try:
                url = url_to(ctx.source, external=True)
            except RuntimeError:
                url = None
        if url is not None:
            configs.append('this.page.url = %s;' % htmlsafe_json_dump(url))
        return ' '.join(configs)

    def on_setup_env(self, **extra):
        shortname = self.get_config().get('shortname')
        if shortname is None:
            raise RuntimeError('Disqus shortname not configured')

        def disqus(identifier=None, url=None):
            config = self.get_disqus_config(identifier, url)
            return Markup(SCRIPT % {
                'config': config,
                'shortname': shortname,
            })

        self.env.jinja_env.globals['render_disqus_comments'] = disqus
