Name:		texlive-ly1
Version:	20190228
Release:	1
Summary:	Support for LY1 LaTeX encoding
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/psfonts/ly1
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ly1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ly1.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Y&Y 'texnansi' (TeX and ANSI, for Microsoft interpretations
of ANSI standards) encoding lives on, even after the decease of
the company; it is known in the LaTeX scheme of things as LY1
encoding. This bundle includes metrics and LaTeX macros to use
the basic three (Times, Helvetica and Courier) Adobe Type 1
fonts in LaTeX using LY1 encoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/ly1
%{_texmfdistdir}/fonts/map/dvips/ly1
%{_texmfdistdir}/fonts/tfm/adobe/ly1
%{_texmfdistdir}/fonts/vf/adobe/ly1
%{_texmfdistdir}/tex/latex/ly1
%{_texmfdistdir}/tex/plain/ly1
%doc %{_texmfdistdir}/doc/fonts/ly1

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
