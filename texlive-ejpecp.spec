# revision 24846
# category Package
# catalog-ctan /macros/latex/contrib/ejpecp
# catalog-date 2011-12-14 17:10:55 +0100
# catalog-license lppl1.2
# catalog-version 0.577
Name:		texlive-ejpecp
Version:	0.577
Release:	1
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

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ejpecp/ejpecp.cls
%doc %{_texmfdistdir}/doc/latex/ejpecp/LPPL
%doc %{_texmfdistdir}/doc/latex/ejpecp/README
%doc %{_texmfdistdir}/doc/latex/ejpecp/ejpecp.pdf
%doc %{_texmfdistdir}/doc/latex/ejpecp/mgetmref.py
%doc %{_texmfdistdir}/doc/latex/ejpecp/sample.pdf
%doc %{_texmfdistdir}/doc/latex/ejpecp/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/ejpecp/ejpecp.dtx
%doc %{_texmfdistdir}/source/latex/ejpecp/ejpecp.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
