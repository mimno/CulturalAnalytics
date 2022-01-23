#!/bin/sh

for PDF in pdf/*.pdf
do
    echo $PDF
    ARTICLE=`basename $PDF .pdf`
    TXT=txt/$ARTICLE.txt

    # if the text version doesn't exist, create it
    if [ ! -f $TXT ]
    then
        pdftotext $PDF txt/$ARTICLE.txt
    fi
done
