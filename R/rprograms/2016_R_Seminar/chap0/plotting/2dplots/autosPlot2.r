#!/usr/bin/Rscript

# Bhishan Poudel
# Jan 12, 2016
# ref: http://harding.edu/fmccown/r/
# clear; Rscript autosPlot2.r

# inputs: data/autos.dat
# outputs: figures/autosPlot2.pdf

# set the working directory
setwd("~/Copy/Programming/R/rprograms/plotting/2dplots/")

# Start PDF device driver to save output to figure.pdf
#pdf(file="figures/auotsPlot2.pdf", height=3.5, width=5)

# Read car and truck values from tab-delimited autos.dat
autos_data <- read.table("data/autos.dat", header=T, sep="\t")
			
# Define colors to be used for cars, trucks, suvs
plot_colors <- c(rgb(r=0.0,g=0.0,b=0.9), "red", "forestgreen")

			
# Trim off excess margin space (bottom, left, top, right)
par(mar=c(4.2, 3.8, 0.2, 0.2))
			
# Graph autos using a y axis that uses the full range of value
# in autos_data. Label axes with smaller font and use larger 
# line widths.
plot(autos_data$cars, type="l", col=plot_colors[1], 
   ylim=range(autos_data), axes=F, ann=T, xlab="Days",
   ylab="Total", cex.lab=0.8, lwd=2)

# Make x axis tick marks without labels
axis(1, lab=F)

# Plot x axis labels at default tick marks with labels at 
# 45 degree angle
text(axTicks(1), par("usr")[3] - 2, srt=45, adj=1,
          labels=c("Mon", "Tue", "Wed", "Thu", "Fri"),
          xpd=T, cex=0.8)

# Plot y axis with smaller horizontal labels 
axis(2, las=1, cex.axis=0.8)

# Create box around plot
box()

# Graph trucks with thicker red dashed line
lines(autos_data$trucks, type="l", lty=2, lwd=2, 
  col=plot_colors[2])

# Graph suvs with thicker green dotted line
lines(autos_data$suvs, type="l", lty=3, lwd=2, 
  col=plot_colors[3])

# Create a legend in the top-left corner that is slightly  
# smaller and has no border
legend("topleft", names(autos_data), cex=0.8, col=plot_colors, 
   lty=1:3, lwd=2, bty="n");
  
# Turn off device driver (to flush output to PDF)
#dev.off()

# Restore default margins
par(mar=c(5, 4, 4, 2) + 0.1)
