Name:		texlive-de-macro
Version:	61719
Release:	2
Summary:	Expand private macros in a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/de-macro
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/de-macro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/de-macro.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/de-macro/de-macro de-macro
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
