<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<?xml-stylesheet type="text/xsl" href="file.xsl"?>
    
%-------------------------------------------%

#change href name; should this be xml instead?
#guessing the above file should be 'text3.xml'
    
%-------------------------------------------%

<xsl:output method="html"/>

<xsl:template match="/">
  <html>
      <head>
      </head>
  <body>
  <h2 style='color:blue; font-style:italics; font-family: Courier, monospace;'>Manfred: A Dramatic Poem</h2>
  <h3 style='color:black; font-family: Courier, monospace;'>Lord Byron</h3>
  <h4 style='color:black; font-style:italics; font-family: Courier, monospace;'>(1816-1817)</h4>
  <xsl:apply-templates/>
</body>
  </html>
</xsl:template>

%-------------------------------------------%
    
#styles above just for the sake of putting an element there, will change later
#also want to align the text in a specific way (note to self)
#unsure if the above template has to be integrated with below
    
%-------------------------------------------%

<xsl:template match='drama'>
    <xsl:template match='header'>
        <xsl:template match='castlist'>
            <p><xsl:value-of='.'/></p>
            
%-------------------------------------------%
            
            #not sure what's wrong here with 'value-of' as I used example in XSLT video
              	
%-------------------------------------------%
            
        </xsl:template>
    </xsl:template>
    <xsl:template match='text'>
        <xsl:template match='act1'>
            <xsl:template match='scene1'>
                <p><xsl:value-of='.'/></p>
            </xsl:template>
            <xsl:template match='scene2'>
                <p><xsl:value-of='.'/></p>
            </xsl:template>
        </xsl:template>
        <xsl:template match='act2'>
            <xsl:template match='scene1'>
                <p><xsl:value-of='.'/></p>
            </xsl:template>
            <xsl:template match='scene2'>
                <p><xsl:value-of='.'/></p>
            </xsl:template>
            <xsl:template match='scene3'>
                <p><xsl:value-of='.'/></p>
            </xsl:template>
            <xsl:template match='scene4'>
                <p><xsl:value-of='.'/></p>
            </xsl:template>
        </xsl:template>
        <xsl:template match='act3'>
            <xsl:template match='scene1'>
                <p><xsl:value-of='.'/></p>    
            </xsl:template>
            <xsl:template match='scene2'>
                <p><xsl:value-of='.'/></p>    
            </xsl:template>
            <xsl:template match='scene3'>
                <p><xsl:value-of='.'/></p>    
            </xsl:template>
            <xsl:template match='scene4'> 
            </xsl:template>
        </xsl:template>
    </xsl:template>
</xsl:template>
    
%-------------------------------------------%

#obviously we can use more regex with the above and conslidate but I just thought I could do a brief outline
#we could also add style elements for each subelement
#need to think about alignment as well
#we can also add titles manually, but not sure how this works exactly with titles already in XML file
    
%-------------------------------------------%

</xsl:template>

</xsl:stylesheet> 
