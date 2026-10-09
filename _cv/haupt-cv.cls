% haupt-cv.cls -- CV and resume class matching andyhaupt.com
%
% Typography and colour follow assets/css/main.css on the website:
%   body text   Lato                         (\usepackage{lato})
%   headings    Palatino / URW Palladio      (\fontfamily{ppl})
%   accent      Stanford cardinal #8C1515    (links, buttons, tag pills)
% The Vita entries borrow the website's timeline: a grey rule with a
% cardinal dot per entry and the institution set in a light "flag".
%
% Options:  nophoto   suppress the round headshot in the header
%           compact   tighter spacing (used for the one-page resume)
% Compiles with pdflatex, lualatex or xelatex (e.g. on Overleaf).
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{haupt-cv}[2026/10/09 CV class matching andyhaupt.com]

\newif\if@cvphoto  \@cvphototrue
\newif\if@cvcompact \@cvcompactfalse
\DeclareOption{nophoto}{\@cvphotofalse}
\DeclareOption{compact}{\@cvcompacttrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[10pt,letterpaper]{article}

% ---------------------------------------------------------------- packages
\RequirePackage{iftex}
\ifPDFTeX
  \RequirePackage[T1]{fontenc}
  \RequirePackage[utf8]{inputenc}
\fi
\RequirePackage[default]{lato}
\RequirePackage[letterpaper,
  top=\if@cvcompact .55in\else .7in\fi,
  bottom=\if@cvcompact .5in\else .7in\fi,
  left=.75in,right=.75in]{geometry}
\RequirePackage{microtype}
\RequirePackage{xcolor}
\RequirePackage{tikz}
\RequirePackage{graphicx}
\RequirePackage{etoolbox}
\RequirePackage{enumitem}
\RequirePackage{fontawesome5}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{needspace}
\RequirePackage{hyperref}

% ------------------------------------------------------------------ colours
\definecolor{cardinal}{HTML}{8C1515}   % a{color}, .button, .tag-btn
\definecolor{ink}{HTML}{222222}        % body{color}
\definecolor{muted}{HTML}{666666}
\definecolor{tagbg}{HTML}{F0E6E6}      % .paper-tag background
\definecolor{typebg}{HTML}{E6E6E6}     % .paper-type background
\definecolor{flagbg}{HTML}{F4F4F4}     % timeline .flag background
\definecolor{timeline}{HTML}{505050}   % timeline rule

\hypersetup{colorlinks=true,linkcolor=cardinal,urlcolor=cardinal,
  citecolor=cardinal,pdfborder={0 0 0}}
\color{ink}

% -------------------------------------------------------------------- fonts
\newcommand\headingfont{\fontfamily{ppl}\selectfont}

% ------------------------------------------------------------------ layout
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\linespread{1.08}
\setlist{nosep,leftmargin=1.1em,label={\color{cardinal}\scriptsize\textbullet}}
\raggedbottom

% Header data
\newcommand\cvname[1]{\def\@cvname{#1}}
\newcommand\cvphoto[1]{\def\@cvphoto{#1}}
\newcommand\cvdoctype[1]{\def\@cvdoctype{#1}}
\def\@cvpositions{}
\newcommand\cvposition[1]{\appto\@cvpositions{#1\par}}
\def\@cvcontacts{}
\newcommand\cvcontact[3]{% icon, url, label
  \appto\@cvcontacts{\mbox{\href{#2}{#1\,#3}}\hspace{.75em}\allowbreak}}
\newlength\cvphotoradius
\setlength\cvphotoradius{\if@cvcompact .43in\else .53in\fi}
\cvname{}\cvphoto{}\cvdoctype{Curriculum Vit\ae}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[L]{\scriptsize\color{muted}\@cvname\ \textperiodcentered\ \@cvdoctype}
\fancyfoot[R]{\scriptsize\color{muted}\thepage/\pageref*{LastPage}}
\fancypagestyle{plain}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}}

% Header in the style of the website's .header-flex: round photo with a
% 2px black border, name in Palatino, one line per current position.
\newcommand\makecvheader{%
  \thispagestyle{plain}%
  \begingroup
  \if@cvphoto\ifx\@cvphoto\@empty\else
    \begin{minipage}[c]{\if@cvcompact .95in\else 1.15in\fi}
      \begin{tikzpicture}
        \begin{scope}
          \clip (0,0) circle (\cvphotoradius);
          \node at (0,0) {\includegraphics[width=2.05\cvphotoradius]{\@cvphoto}};
        \end{scope}
        \draw[black,line width=1.3pt] (0,0) circle (\cvphotoradius);
      \end{tikzpicture}
    \end{minipage}\hspace{.9em}%
  \fi\fi
  \begin{minipage}[c]{.78\linewidth}
    {\headingfont\fontsize{\if@cvcompact 22\else 25\fi}{28}\selectfont\@cvname\par}
    \vspace{.35ex}
    {\small\linespread{1.15}\selectfont\@cvpositions}
    \vspace{.6ex}
    {\small\@cvcontacts}
  \end{minipage}
  \par\endgroup
  \vspace{\if@cvcompact .6ex\else 1.2ex\fi}}

% Section headings: Palatino, regular weight, as h2 on the website.
\renewcommand\section[1]{%
  \par\needspace{\if@cvcompact 3\else 5\fi\baselineskip}%
  \addvspace{\if@cvcompact .8ex\else 2.2ex\fi}%
  {\headingfont\fontsize{\if@cvcompact 13.5\else 15.5\fi}{18}\selectfont #1\par}%
  \nobreak\vspace{\if@cvcompact .35ex\else .8ex\fi}\nobreak}
% \cvsubsection: a lighter heading inside a section (e.g. preprints after
% publications) that never forces a page break.
\newcommand\cvsubsection[1]{%
  \par\addvspace{1.2ex}%
  {\headingfont\large #1\par}\nobreak\vspace{.6ex}\nobreak}
\let\subsection\cvsubsection

% --------------------------------------------------------- pills and buttons
% .paper-tag: tinted pill; .paper-type: grey pill; .button: filled cardinal.
\tikzset{cvpill/.style={rounded corners=3.2pt,inner xsep=3.2pt,
  inner ysep=1.3pt,font=\fontsize{7}{8}\selectfont,anchor=base}}
\newcommand\cvtag[1]{\tikz[baseline]\node[cvpill,fill=tagbg,text=cardinal]{\strut #1};}
\newcommand\cvtype[1]{\tikz[baseline]\node[cvpill,fill=typebg,text=black]{\strut #1};}
\newcommand\cvbutton[2]{\href{#2}{\tikz[baseline]\node[cvpill,fill=cardinal,text=white]{\strut #1};}}

% Author markup used by the generated publication lists.
\newcommand\me[1]{\textbf{#1}}
\newcommand\eq{\textsuperscript{\ensuremath{\ddagger}}}

% ------------------------------------------------------------ timeline vita
% \cventry{dates}{institution}{url}{role}{details}
% A grey rule runs down the left of consecutive entries, as on the site.
\newlength\cvdatewidth \setlength\cvdatewidth{\if@cvcompact .82in\else .95in\fi}
\newlength\cvgutter    \setlength\cvgutter{1.1em}
\newcommand\cvflag[2]{%
  \ifblank{#2}{\def\@flagtext{#1}}{\def\@flagtext{\href{#2}{#1}}}%
  \tikz[baseline]\node[anchor=base,fill=flagbg,rounded corners=2.5pt,
    inner xsep=4pt,inner ysep=1.6pt,font=\bfseries\small]{\strut\@flagtext};}
\newcommand\@cvdot{%
  \makebox[0pt]{\raisebox{.42ex}{\tikz\fill[cardinal](0,0)circle(2.1pt);}}}
\newcommand\cventry[5]{%
  \par\noindent
  \makebox[\cvdatewidth][r]{\raisebox{0pt}[0pt][0pt]{\small\color{muted}#1}}%
  \hspace{.8em}%
  {\color{timeline!45}\vrule width 1.2pt}%
  \@cvdot\hspace{\cvgutter}%
  \parbox[t]{\dimexpr\linewidth-\cvdatewidth-.8em-1.2pt-\cvgutter\relax}{%
    \raggedright
    \ifblank{#2}{}{\cvflag{#2}{#3}\ }\textbf{#4}%
    \ifblank{#5}{}{\par\vspace{.2ex}{\small #5}}%
    \par\vspace{\if@cvcompact .35ex\else 1.1ex\fi}}%
  \par}

% \cvitem{left label}{text}: plain two-column row (honours, talks, ...)
\newcommand\cvitem[2]{%
  \par\noindent
  \makebox[\cvdatewidth][r]{\small\color{muted}#1}%
  \hspace{.8em}{\color{timeline!45}\vrule width 1.2pt}\hspace{\cvgutter}%
  \parbox[t]{\dimexpr\linewidth-\cvdatewidth-.8em-1.2pt-\cvgutter\relax}{%
    \raggedright #2\par\vspace{\if@cvcompact .15ex\else .6ex\fi}}%
  \par}

% --------------------------------------------------------------- publications
% \cvpub{title}{authors}{venue}{type}{tags}{buttons}
% Mirrors the website's .paper block: bold title, authors, italic venue,
% then the type pill, subject pills and link buttons on one line.
\newif\ifcvshowtags \cvshowtagstrue
\newcommand\cvpub[6]{%
  \par\noindent\begin{minipage}[t]{\linewidth}
    \textbf{#1}\par
    {\small #2}\par
    {\small\itshape #3}%
    \ifcvshowtags\def\@pills{#5\,#6}\else\def\@pills{#6}\fi
    \ifblank{#5#6}{}{%
      % right-align the pills; move them to the next line only if needed
      \unskip\nobreak\hfil\penalty50\hskip1em\hbox{}\nobreak\hfill
      \mbox{\@pills}\parfillskip=0pt}%
    \par
  \end{minipage}\par\vspace{1.05ex}}

% \cvpubline{year}{title}{venue}{with}{url}: one-line entry for the resume;
% the year is printed only when it changes.
\def\@lastpubyear{}
\newcommand\cvpubline[5]{%
  \def\@thispubyear{#1}%
  \ifx\@thispubyear\@lastpubyear\def\@shownyear{}\else\def\@shownyear{#1}\fi
  \global\let\@lastpubyear\@thispubyear
  \cvitem{\@shownyear}{\ifblank{#5}{\textbf{#2}}{\href{#5}{\color{ink}\textbf{#2}}},
    \textit{#3}\ifblank{#4}{}{ {\color{muted}(#4)}}}}

% \selectedpub[short title]{key}: a publication from generated/pubdefs.tex
\newcommand\selectedpub[2][]{%
  \ifcsname pub@#2\endcsname\csname pub@#2\endcsname{#1}%
  \else\PackageWarning{haupt-cv}{Unknown publication key #2}\fi}

% ----------------------------------------------------------------- references
\newcommand\cvreference[4]{% name, title, institution, email
  \begin{minipage}[t]{.32\linewidth}\raggedright
    \textbf{#1}\par{\small #2\par #3\par
    \href{mailto:#4}{\faEnvelope[regular]\,#4}}
  \end{minipage}}

\endinput
