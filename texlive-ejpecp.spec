# revision 28535
# category Package
# catalog-ctan /macros/latex/contrib/ejpecp
# catalog-date 2012-12-13 10:43:21 +0100
# catalog-license lppl1.2
# catalog-version 1.0
Name:		texlive-ejpecp
Version:	1.0
Release:	3
Summary:	Class for EJP and ECP
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ejpecp
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is designed for typesetting articles for the
mathematical research periodicals Electronic Journal of
Probability (EJP) and Electronic Communications in Probability
(ECP).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ejpecp/ejpecp.cls
%doc %{_texmfdistdir}/doc/latex/ejpecp/LPPL
%doc %{_texmfdistdir}/doc/latex/ejpecp/README
%doc %{_texmfdistdir}/doc/latex/ejpecp/mgetmref.py
%doc %{_texmfdistdir}/doc/latex/ejpecp/sample.pdf
%doc %{_texmfdistdir}/doc/latex/ejpecp/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/ejpecp/ejpecp.dtx
%doc %{_texmfdistdir}/source/latex/ejpecp/ejpecp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
