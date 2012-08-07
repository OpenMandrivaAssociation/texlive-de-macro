# revision 26355
# category Package
# catalog-ctan /support/de-macro
# catalog-date 2010-03-10 11:48:14 +0100
# catalog-license other-free
# catalog-version 1.3
Name:		texlive-de-macro
Version:	1.3
Release:	3
Summary:	Expand private macros in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/de-macro
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/de-macro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/de-macro.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-de-macro.bin = %{EVRD}

%description
De-macro is a Python script that helps authors who like to use
private LaTeX macros (for example, as abbreviations). A
technical editor or a cooperating author may balk at such a
manuscript; you can avoid manuscript rejection misery by
running de-macro on it. De-macro will expand macros defined in
\(re)newcommand or \(re)newenvironment commands, within the
document, or in the document's "private" package file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/de-macro
%{_texmfdistdir}/scripts/de-macro/de-macro
%doc %{_texmfdistdir}/doc/support/de-macro/README
%doc %{_texmfdistdir}/doc/support/de-macro/user-guide.pdf
%doc %{_texmfdistdir}/doc/support/de-macro/user-guide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/de-macro/de-macro de-macro
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
