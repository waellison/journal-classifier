#!/usr/bin/env python3

import re
import untangle
import slugify

with open("wordpress.wxr", "r") as fh:
  document = untangle.parse(fh)

posts = [post for post in document.rss.channel.item]

for post in posts:
  content = post.content_encoded.cdata
  cleaner = re.compile(r"<.*?>")
  title_text = post.title.cdata
  title_text_parts = [part.strip() for part in title_text.split(":", 2)]
  date = post.wp_post_date.cdata.split(" ")[0]
  content = post.content_encoded.cdata
  clean_content = re.sub(cleaner, "", content)

  if len(title_text_parts) > 1:
    title_text = title_text_parts[1]

  title = slugify.slugify(title_text)

  fn = f"{date}-{title}.md"
  with open(fn, "w") as outfile:
    outfile.write(content)


