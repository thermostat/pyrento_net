
# Pyrento dot net

SSG for [Pyrento.net](http://pyrento.net).

## Building

Current building flow is:

    cd quarto_site/pyrento
    quarto render
    cd ../..
    python3 scripts/publish_site.py

Notes: Must have a working ssh agent and thermostat.github.io must be
a sibling directory.




    
