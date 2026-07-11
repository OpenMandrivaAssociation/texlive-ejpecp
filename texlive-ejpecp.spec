%global tl_name ejpecp
%global tl_revision 60950

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.11.3
Release:	%{tl_revision}.1
Summary:	Class for EJP and ECP
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ejpecp
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class is designed for typesetting articles for the mathematical
research periodicals Electronic Journal of Probability (EJP) and
Electronic Communications in Probability (ECP). It depends on amsmath,
amsfonts, amsthm, bera, dsfont, geometry, graphicx, hyperref, lastpage,
latexsym, mathtools, microtype, and afterpackage.

