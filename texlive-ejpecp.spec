Name:		texlive-ejpecp
Version:	60950
Release:	2
Summary:	Class for EJP and ECP
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ejpecp
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ejpecp.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/ejpecp
%doc %{_texmfdistdir}/doc/latex/ejpecp
#- source
%doc %{_texmfdistdir}/source/latex/ejpecp

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
