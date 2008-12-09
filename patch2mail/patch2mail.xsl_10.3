<?xml version="1.0" encoding="ISO-8859-15"?>
<!--

Copyright (c) 2007 Christian Boltz - www.cboltz.de

Thanks to Thomas Schraitle for helping with some xslt details.


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License (http://www.gnu.org/copyleft/gpl.html)
for more details.

-->

<xsl:stylesheet version="1.1"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!-- <xsl:output method="text" encoding="ISO-8859-15" media-type="text/plain" /> -->

<xsl:strip-space elements="*"/>


<xsl:template match="/"><xsl:apply-templates /></xsl:template>

<xsl:template match="update-status">
<xsl:document href="-" method="text" ><xsl:apply-templates />
</xsl:document></xsl:template>


<!-- errors -->

<xsl:template match="errors"><xsl:apply-templates /></xsl:template>

<xsl:template match="errors/error">
  <xsl:text>*** ERROR ***&#10;</xsl:text>
    <xsl:apply-templates />
  <xsl:text>&#10;&#10;</xsl:text>
</xsl:template>


<!-- update sources -->

<xsl:template match="update-sources">
  <xsl:text>Update sources:&#10;</xsl:text>
  <xsl:apply-templates />
  <xsl:text>&#10;</xsl:text>
</xsl:template>

<xsl:template match="update-sources/source">
  <xsl:text>- </xsl:text>
  <xsl:value-of select="@alias" /> (<xsl:value-of select="@url" />)
</xsl:template>


<!-- updates -->

<xsl:template match="update-list">
  <xsl:apply-templates />
</xsl:template>

<xsl:template match="update-list/update">
<xsl:if test="@kind = 'patch'">
  <xsl:text>&#10;=== </xsl:text> 
  <xsl:value-of select="@name" /> 
  <xsl:text> - Patch </xsl:text>
  <xsl:value-of select="@edition" /> 
  <xsl:text> (</xsl:text>
  <xsl:value-of select="@category" />
  <xsl:text>) ===&#10;&#10;</xsl:text>
  <xsl:apply-templates />
  <xsl:text>&#10;</xsl:text>
</xsl:if>
</xsl:template>

<xsl:template match="update-list/update/summary">
   <xsl:apply-templates />
</xsl:template>

<xsl:template match="update-list/update/description">
  <xsl:text>&#10;&#10;</xsl:text>
  <xsl:apply-templates />
</xsl:template>

<!-- update source of this specific update isn't that interesting ;-) -->
<!--
<xsl:template match="update-list/update/source">Update source: <xsl:value-of select="@alias" /> (<xsl:value-of select="@url" />)</xsl:template>
-->


<!-- summary -->

<xsl:template match="update-summary">
  <xsl:text>--------------------------------------------------------&#10;&#10;</xsl:text>
  <xsl:text>    Total: </xsl:text>
  <xsl:value-of select="@total" />
  <xsl:text> updates (</xsl:text>
  <xsl:value-of select="@security" /> 
  <xsl:text> security)&#10;__TOTAL__</xsl:text>
  <xsl:value-of select="@total" /><xsl:value-of select="@security" />
  <xsl:text>__&#10;</xsl:text>
</xsl:template>


<!-- end -->

</xsl:stylesheet>
