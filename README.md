# Manfred by Lord Byron

<p align="center">!<img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fvictorian-era.org%2Fimages%2Fdb210f0dd5240945f1289550a6b4b5a4.jpg&f=1&nofb=1"></p>

# Overview
This project aims to extract textual data from Project Gutenberg (txt format), encode it in XML using regex and output it as a final HTML file, through the usage of XSLT stylesheets.

# Project timeline
<ol>
    <li> Retrieving text in .txt format and save it.
    <li> Clean up and re-format the text as necessary.
    <li> Use regex to select the different structures within the text and transform it into an XML file.
    <li> Through the use of XSLT, render the file in HTML.
</ol>

As it stands, the file `extract.py` is responsible for retrieving the text and doing the necessary clean up. `buildxml.py` creates `output.xml` and applies `stylesheet.xslt` in order to finally render `manfred.html`.

# Libraries and dependencies
The project makes exclusive use of native Python Modules, specifically [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) for the XML and XSLT handling.

# Post-mortem
The realization of this project has allowed us to learn a lot about regex, document handling as well as software development in general. The main obstacles were not only the length of the text (regex matching over thousands of lines can become problematic) but also its complex structure (multiple acts, irregular number of scenes per act, etc). The document chosen also presented other challenges, given that it was uploaded to Project Gutenberg after undergoing OCR and as such, presented various odd characters and inconsistencies. Character indications were highly variable, as were stage directions and even scene/act numbering schemes. Overall, while the result is not perfect, we have acquired functional skills working with regex, XML and XSLT as well as general software development methodology.

# Authors

Project developed by [Philipa Payne](https://github.com/P-C-R-P) and [Fábio Cabral](https://github.com/ftorresc/) for the "Ingénierie Documentaire" class by Michael Piotrowksi and Moritz Feichtinger at Université de Lausanne during the Winter semester of 2021.
