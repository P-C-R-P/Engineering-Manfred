<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
        <html>
            <head>
                <title>Manfred by George Gordon Byron</title>
            </head>
            <body>
                <h2>Manfred by George Gordon Byron</h2>
                 <xsl:apply-templates/> 
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="act">
    <p style="font-size: 35px; margin-left: 50"><xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="scene">
    <p style="font-size: 25px; margin-left: 50"><xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="speech">
    <p style="margin-left:100"><xsl:apply-templates /></p>
    </xsl:template>

    <xsl:template match="stage">
    <p style="font-style: italic"><xsl:apply-templates /></p>
    </xsl:template>

    <xsl:template match="speaker">
    <p style="font-weight:bold"><xsl:apply-templates /></p>
    </xsl:template>
 
</xsl:stylesheet>