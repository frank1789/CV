\ProvidesClass{friggeri-cv}[2012/04/30 CV class]
\NeedsTeXFormat{LaTeX2e}

\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}%
}
\ProcessOptions\relax
\LoadClass{article}
\usepackage[utf8]{inputenc}
\usepackage{csquotes}
\usepackage{multicol}
\usepackage{tabularx}


%%%%%%%%%%
% Colors %
%%%%%%%%%%

\RequirePackage{fontawesome5}
\RequirePackage{xcolor}

% Defines the colors used for the template scheme and for assigning color to
% FontAwesome characters
\definecolor{airforceblue}{rgb}{0.36, 0.54, 0.66}
\definecolor{bananayellow}{rgb}{1.0, 0.88, 0.21}
\definecolor{blue}{HTML}{6CE0F1}
\definecolor{darkgray}{HTML}{333333}
\definecolor{gray}{HTML}{4D4D4D}
\definecolor{green}{HTML}{C2E15F}
\definecolor{lightgray}{HTML}{999999}
\definecolor{linkedin}{HTML}{1683BB}
\definecolor{orange}{HTML}{FDA333}
\definecolor{phonegreen}{HTML}{006B3C}
\definecolor{purple}{HTML}{D3A4F9}
\definecolor{red}{HTML}{FB4485}
\definecolor{skypeblue}{RGB}{0,175,240}
\definecolor{white}{RGB}{255,255,255}
\definecolor{cyan-vimeo}{RGB}{77,170,233}

% Function that defines the color cycle for the first three letters of the
% section
\ifdefined\@cv@print
  \colorlet{green}{gray}
  \colorlet{orange}{gray}
  \colorlet{purple}{gray}
  \colorlet{brown}{gray}
  \colorlet{red}{gray}
  \colorlet{blue}{gray}
  \colorlet{fillheader}{white}
  \colorlet{header}{gray}
\else
  \colorlet{fillheader}{gray}
  \colorlet{header}{white}
\fi
\colorlet{textcolor}{gray}
\colorlet{headercolor}{gray}

%%%%%%%%%
% Fonts %
%%%%%%%%%

\RequirePackage{fontspec}
\RequirePackage{unicode-math}
\RequirePackage{calc}
\RequirePackage{stackengine}

% set-up fonts 
\newfontfamily\bodyfont[]{Roboto}
\newfontfamily\thinfont[]{Roboto Light}
\newfontfamily\headingfont[]{Roboto Bold}
\defaultfontfeatures{Mapping=tex-text}
\setmainfont[Mapping=tex-text, Color=textcolor]{Roboto Light}

%%%%%%%%%%
% Header %
%%%%%%%%%%

\RequirePackage{tikz}

\newcommand{\rolefont}{%
  \fontsize{14pt}{24pt}\selectfont%
  \thinfont%
  \color{white}%
}

\newcommand{\header}[3]{%
  \begin{tikzpicture}[remember picture,overlay]
    \node [rectangle, fill=fillheader, anchor=north, minimum width=\paperwidth, minimum height=4cm] (box) at (current page.north){};
    \node [anchor=center] (name) at (box) {%
      \fontsize{40pt}{72pt}\color{header}%
      {\thinfont #1}{\bodyfont  #2}
    };
    \node [anchor=north] at (name.south) {%
      \fontsize{14pt}{24pt}\color{header}%
      \thinfont #3%
    };
  \end{tikzpicture}
  \vspace{2.5cm}
  \vspace{-2\parskip}
}


%%%%%%%%%%%%%
% Structure %
%%%%%%%%%%%%%

\RequirePackage{parskip}

\newcounter{colorCounter}
\def\@sectioncolor#1#2#3{%
  {%
    \color{%
      \ifcase\value{colorCounter}%
        blue\or%
        red\or%
        orange\or%
        green\or%
        purple\or%
        brown\or%
        airforceblue\or%
        bananayellow\else%
        headercolor\fi%
    } #1#2#3%
  }%
  \stepcounter{colorCounter}%
}

\renewcommand{\section}[1]{
  \par\vspace{\parskip}
  {%
    \LARGE\headingfont\color{headercolor}%
    \@sectioncolor #1%
  }
  \par\vspace{\parskip}
}

\renewcommand{\subsection}[1]{
  \par\vspace{.5\parskip}%
  {\Large\headingfont\color{headercolor} #1}
  \par\vspace{.25\parskip}%
}

\renewcommand{\subsubsection}[2]{
  \par\vspace{.5\parskip}%
  {\Large\headingfont\color{headercolor} #2}
  \par\vspace{.25\parskip}%
}

\pagestyle{empty}


%%%%%%%%%%%%%%%%%%%%
% List environment %
%%%%%%%%%%%%%%%%%%%%

\setlength{\tabcolsep}{1pt}
\newenvironment{entrylist}{%
  \begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}ll}
}{%
  \end{tabular*}
}
\renewcommand{\bfseries}{\headingfont\color{headercolor}}

% entrytitle command is useful for entering your academic qualifications
% within the education section. Compared to the original version, this
% function builds a table with the data entered; this allows to obtain a
% better alignment with the entered values.
% Args: 
%    #1 start date
%    #2 end date
%    #3 course title
%    #4 univeristy
%    #5 thesis
%    #6 other
% 
% % example:
%     \entrytitle
%     {2015}
%     {2020}
%     {M. Sc. {\normalfont in Mechatronics Engineering}}
%     {University of Trento}
%     {Thesis "\emph{Enhancing UAV capabilities with machine learning on board}".}
%     {Specialization in Mechanics--Mechatronics}
%
\newcommand{\entrytitle}[6]{%
  \parbox[t]{11.5cm}{%
    \begin{tabular}{l c r p{2mm} l r}
      #1  & -- & #2 & \hfill & \textbf{#3}\hfill & {\footnotesize\addfontfeature{Color=lightgray} #4} \\
          &    &    & \hfill & \multicolumn{2}{p{125mm}}{#5}\\
          &    &    & \hfill & \multicolumn{2}{l}{#6}
    \end{tabular}
  }
  \vspace{2.5mm}\\
}

% entry command to enter the experiences gained.
%
% example:
%   \entry
%     #1 {start date}
%     #2 {end date }
%     #3 {company name}{city, country}
%     #4 {job title}
%     #5 {long descritpion}
%     #6 {aux field}
%     #7 {link}
%     #8 {logo}
% 
\newcommand{\entry}[8]{%
  \parbox[t]{11.5cm}{%
    \begin{tabular}{l c r p{2mm} l r}
      #1  & -- & #2 & \hfill & \textbf{#3}\hfill & {\footnotesize\addfontfeature{Color=lightgray} #4} \\
          &    &    & \hfill & \multicolumn{2}{p{110mm}}{#5}\\
          &    &    & \hfill & \multicolumn{2}{p{110mm}}{#6}\\
          &    &    & \hfill & \multicolumn{1}{p{90mm}}{#7} & \multicolumn{1}{r}{#8}\\
    \end{tabular}
  }
  \vspace{7.5mm}\\
}

% entrycertificate command to enter the certificates gained.
%
% example:
%   \entrycertificate
%     #1 {date}
%     #2 {certification}
%     #3 {company name}
%
\newcommand{\entrycertificate}[3]{%
  \parbox[t]{11.5cm}{%
    \begin{tabularx}{\textwidth}{p{9.25mm} p{110mm} r}
      #1  & \textbf{#2} \\
          & {\footnotesize\addfontfeature{Color=lightgray} #3}
    \end{tabularx}%
  }
  \vspace{1.5mm}\\
}

% entry command to enter the skills gained.
%
% example:
%   \entry
%     #1 {area}
%     #2 {skill list}
%
\newcommand{\entryskills}[2]{%
  \parbox[t]{57.5mm}{%
    \begin{tabular}{r l}
      \textbf{#1} & \hfill\\
                  & \multicolumn{1}{p{50mm}}{#2}\hfill\\
    \end{tabular}%
  }
  \vspace{1.5mm}
  \hspace{15.5mm}
}

%%%%%%%%%%%%%%
% Side block %
%%%%%%%%%%%%%%

\RequirePackage[absolute,overlay]{textpos}
\setlength{\TPHorizModule}{1cm}
\setlength{\TPVertModule}{1cm}
\newenvironment{aside}{%
  \let\oldsection\section
  \renewcommand{\section}[1]{
    \par\vspace{\baselineskip}{\Large\headingfont\color{headercolor} ##1}
  }
  \begin{textblock}{3.6}(1.5, 4.33)
  \begin{flushright}
  \obeycr
}{%
  \restorecr
  \end{flushright}
  \end{textblock}
  \let\section\oldsection
}

%%%%%%%%%%%%%%%%
% Bibliography %
%%%%%%%%%%%%%%%%

\RequirePackage[style=verbose, maxnames=99, sorting=ydnt]{biblatex}

\DeclareFieldFormat[article]{title}{#1\par}
\DeclareFieldFormat[book]{title}{#1\par}
\DeclareFieldFormat[inproceedings]{title}{#1\par}
\DeclareFieldFormat[misc]{title}{#1\par}
\DeclareFieldFormat[report]{title}{#1\par}

\DeclareBibliographyDriver{article}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \usebibmacro{journal+issuetitle}%
    \setunit{\space}%
    \printfield{pages}%
    \newunit%
    \printlist{publisher}%
    \setunit*{\addcomma\space}%
    \printfield{year}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{book}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \printlist{publisher}%
    \setunit*{\addcomma\space}%
    \printfield{note}%
    \setunit*{\addcomma\space}%
    \printfield{year}%
    \setunit{\addcomma\space}%
    \printlist{location}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}


\DeclareBibliographyDriver{inproceedings}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}%
    \printfield{booktitle}%
    \setunit{\addcomma\space}%
    \printfield{year}%
    \setunit{\addcomma\space}%
    \printlist{location}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{misc}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \printfield{booktitle}%
    \setunit*{\addcomma\space}%
    \printfield{note}%
    \setunit*{\addcomma\space}%
    \printfield{year}%
    \setunit{\addcomma\space}%
    \printlist{location}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareBibliographyDriver{report}{%
  \printfield{title}%
  \newblock%
  \printnames{author}%
  \par%
  \newblock%
  {%
    \footnotesize\addfontfeature{Color=lightgray}\itshape%
    \printfield{type}%
    \setunit{\space}%
    \printfield{number}%
    \setunit{\addcomma\space}%
    \printfield{year}%
    \newunit%
  }
  \par\vspace{0.3\baselineskip}
}

\DeclareNameFormat{newformat}{%
  \nameparts{#1}% split the name data, will not be necessary in future versions
  \usebibmacro{name:newformat}%
  \usebibmacro{name:andothers}%
}

\defbibheading{bibheading}[\bibname]{%
   \subsubsection*{#1}
   \markboth{#1}{#1}
}

\newcommand{\printbibsection}[2]{
  \begin{refsection}
    \nocite{*}
    \printbibliography[sorting=chronological, type={#1}, title={#2}, heading=bibheading]
  \end{refsection}
}

\DeclareSortingScheme{chronological}{
  \sort[direction=descending]{\field{year}}
  \sort[direction=descending]{\field{month}}
}



%%%%%%%%%%%%%%%%
% Other tweaks %
%%%%%%%%%%%%%%%%

\RequirePackage[left=6.1cm,top=2cm,right=1.5cm,bottom=2.5cm,nohead,nofoot]{geometry}
\RequirePackage{hyperref}
\hypersetup{
    colorlinks=false,
    linkcolor=red,
    citecolor=red,
    filecolor=red,
    urlcolor = red}

% A fix for \href{}{} colors not working with fontspec
\makeatletter
\def\HyColor@@@@UseColor#1\@nil{\addfontfeatures{Color=#1}}
\makeatother
