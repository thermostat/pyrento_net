
# Pyrento dot net

SSG for [Pyrento.net](http://pyrento.net).

## Building

Current building flow is:

    cd pyrento_site
    make html
    # <manually copy output html to site>

On windows without make, manually running pelican is straightforward:

    pelican . -o output -s pelicanconf.py


    
