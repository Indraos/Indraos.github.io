#!/bin/bash
PATH=/Library/TeX/Root/bin/x86_64-darwin:$PATH
for LANG in ngerman english french; 
	do for TYPE in resume cv; 
		do JOBNAME="$LANG"_"$TYPE" \
		&& pdflatex --jobname=$JOBNAME "\def\isresume{$TYPE}\PassOptionsToPackage{$LANG}{babel}\input{cv.tex}" \
		&& biber $JOBNAME && pdflatex --jobname=$JOBNAME "\def\isresume{$TYPE}\PassOptionsToPackage{$LANG}{babel}\input{cv.tex}" \
		&& pdflatex --jobname=$JOBNAME "\def\isresume{$TYPE}\PassOptionsToPackage{$LANG}{babel}\input{cv.tex}" \
		&& rm $JOBNAME.aux $JOBNAME.bbl $JOBNAME.bcf $JOBNAME.blg $JOBNAME.log $JOBNAME.out $JOBNAME.run.xml
	done 
done