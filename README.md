# CulturalAnalytics
Articles from CA

Load [https://culturalanalytics.org/articles] in a browser. To get more than the most recent 32 articles you may need to hit the "Load more" button at the bottom of the page a few times first. Open the javascript console. Run this command: 

    Array.from(document.querySelectorAll("a.article-title")).map(d => d.href.replace(/(article\/\d+).*/, "$1.pdf"))

This should produce a copyable JSON list of PDF URLs. Copy the array in `[]`s and paste this string **inside double quotes** as an argument to the `download.py` script:

    python download.py "['https://culturalanalytics.org/article/32036.pdf', 'https://culturalanalytics.org/article/30703.pdf']"

This will download each file to the `pdf` directory.

Now run `to_text.sh`, which will create text versions as needed. You must have the `pdftotext` function installed.

    ./to_text.sh

