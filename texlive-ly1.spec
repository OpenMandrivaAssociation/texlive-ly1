# revision 21086
# category Package
# catalog-ctan /fonts/psfonts/ly1
# catalog-date 2010-06-15 10:37:47 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-ly1
Version:	20100615
Release:	2
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
%{_texmfdistdir}/fonts/enc/dvips/ly1/texnansi.enc
%{_texmfdistdir}/fonts/map/dvips/ly1/pag8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pbk8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pcr8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/phv8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pnc8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/ppl8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/ptm8y.map
%{_texmfdistdir}/fonts/map/dvips/ly1/pzc8y.map
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagd8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagdo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagk8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pagko8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkd8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkdi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkdo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkl8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbkli8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pbklo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pcrro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvb8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvbo8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvr8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/phvro8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncbi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncri8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pncro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplbi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplbu8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplr8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplri8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplrr8ye.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pplru8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmb8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmbc8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmbi8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmbo8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmr8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmr8yn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmrc8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmri8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmro8y.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/ptmrr8ye.tfm
%{_texmfdistdir}/fonts/tfm/adobe/ly1/pzcmi8y.tfm
%{_texmfdistdir}/fonts/vf/adobe/ly1/ptmbc8y.vf
%{_texmfdistdir}/fonts/vf/adobe/ly1/ptmrc8y.vf
%{_texmfdistdir}/tex/latex/ly1/ly1enc.def
%{_texmfdistdir}/tex/latex/ly1/ly1pag.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pbk.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pcr.fd
%{_texmfdistdir}/tex/latex/ly1/ly1phv.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pnc.fd
%{_texmfdistdir}/tex/latex/ly1/ly1ppl.fd
%{_texmfdistdir}/tex/latex/ly1/ly1ptm.fd
%{_texmfdistdir}/tex/latex/ly1/ly1pzc.fd
%{_texmfdistdir}/tex/latex/ly1/texnansi.sty
%{_texmfdistdir}/tex/plain/ly1/texnansi.tex
%doc %{_texmfdistdir}/doc/fonts/ly1/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100615-2
+ Revision: 753672
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100615-1
+ Revision: 718934
- texlive-ly1
- texlive-ly1
- texlive-ly1
- texlive-ly1

